#requires -Version 5.1
<#
.SYNOPSIS
  Bounded Windows PowerShell 5.1 supervisor for B00-01 (companion) bootstrap verification.
  Executes offline dotnet restore, positive smoke, deliberate negative control, and hang/timeout kill-tree checks.
#>
[CmdletBinding()]
param(
    [string]$RunDir = "",
    [ValidateRange(1, 120)]
    [int]$TimeoutSeconds = 120,
    [ValidateSet("All", "Restore", "Positive", "Negative", "Hang")]
    [string]$Mode = "All",
    [string]$DotnetExe = "C:\Users\phamp\.ao\data\tools\nyua-dotnet\dotnet.exe",
    [string]$NuGetSource = "C:\Users\phamp\.nuget\packages",
    [string]$ProjectPath = "tests\bootstrap\companion\Bootstrap.Tests.csproj"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($RunDir)) {
    $RunDir = Join-Path $env:TEMP ("nyua-b00-01-" + [Guid]::NewGuid().ToString("N").Substring(0, 8))
}

$artDir = Join-Path $RunDir "dotnet-artifacts"
$resDir = Join-Path $RunDir "results"
New-Item -ItemType Directory -Force -Path $artDir, $resDir | Out-Null

function Format-WinArgs {
    param([string[]]$ArgList)
    $quoted = foreach ($a in $ArgList) {
        if ($a -match '[\s"]') {
            '"' + ($a -replace '(\\*)"', '$1$1\"' -replace '(\\+)$', '$1$1') + '"'
        } else {
            $a
        }
    }
    return ($quoted -join ' ')
}

function Invoke-BoundedProcess {
    param(
        [Parameter(Mandatory = $true)][string]$FilePath,
        [Parameter(Mandatory = $true)][string[]]$ArgList,
        [Parameter(Mandatory = $true)][int]$TimeoutSec
    )

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $FilePath
    $psi.Arguments = Format-WinArgs -ArgList $ArgList
    $psi.UseShellExecute = $false

    $p = [System.Diagnostics.Process]::Start($psi)
    if ($null -eq $p) {
        throw "Failed to start process: $FilePath"
    }

    try {
        if (-not $p.WaitForExit($TimeoutSec * 1000)) {
            if (-not $p.HasExited) {
                & taskkill /PID $p.Id /T /F 2>$null | Out-Null
            }
            try { $p.WaitForExit() } catch {}
            return [pscustomobject]@{
                TimedOut = $true
                ExitCode = 124
                Pid      = $p.Id
            }
        }

        return [pscustomobject]@{
            TimedOut = $false
            ExitCode = $p.ExitCode
            Pid      = $p.Id
        }
    }
    finally {
        $p.Dispose()
    }
}

if (-not (Test-Path -LiteralPath $DotnetExe)) {
    Write-Error "Dotnet executable not found: $DotnetExe"
    exit 2
}

if (-not (Test-Path -LiteralPath $ProjectPath)) {
    Write-Error "Project file not found: $ProjectPath"
    exit 2
}

if ($Mode -in @("All", "Restore")) {
    $restoreArgs = @(
        "restore", $ProjectPath,
        "--source", $NuGetSource,
        "--artifacts-path", $artDir
    )
    $r = Invoke-BoundedProcess -FilePath $DotnetExe -ArgList $restoreArgs -TimeoutSec $TimeoutSeconds
    Write-Host ("[B00-01][Restore] TimedOut={0} ExitCode={1}" -f $r.TimedOut, $r.ExitCode)
    if ($r.TimedOut -or $r.ExitCode -ne 0) {
        exit $(if ($r.ExitCode -ne 0) { $r.ExitCode } else { 1 })
    }
}

if ($Mode -in @("All", "Positive")) {
    $posArgs = @(
        "test", $ProjectPath,
        "--configuration", "Release",
        "--no-restore",
        "--artifacts-path", $artDir,
        "--filter", "TestCategory=PositiveSmoke",
        "--logger", "trx;LogFileName=b00-01-pos.trx",
        "--results-directory", $resDir
    )
    $pos = Invoke-BoundedProcess -FilePath $DotnetExe -ArgList $posArgs -TimeoutSec $TimeoutSeconds
    Write-Host ("[B00-01][Positive] TimedOut={0} ExitCode={1}" -f $pos.TimedOut, $pos.ExitCode)
    if ($pos.TimedOut -or $pos.ExitCode -ne 0) {
        exit $(if ($pos.ExitCode -ne 0) { $pos.ExitCode } else { 1 })
    }
}

if ($Mode -in @("All", "Negative")) {
    $negArgs = @(
        "test", $ProjectPath,
        "--configuration", "Release",
        "--no-restore",
        "--artifacts-path", $artDir,
        "--filter", "TestCategory=NegativeControl",
        "--logger", "trx;LogFileName=b00-01-neg.trx",
        "--results-directory", $resDir
    )
    $neg = Invoke-BoundedProcess -FilePath $DotnetExe -ArgList $negArgs -TimeoutSec $TimeoutSeconds
    Write-Host ("[B00-01][Negative] TimedOut={0} ExitCode={1}" -f $neg.TimedOut, $neg.ExitCode)
    if ($neg.TimedOut) {
        Write-Error "NegativeControl timed out."
        exit 124
    }
    if ($neg.ExitCode -eq 0) {
        Write-Error "NegativeControl unexpectedly exited 0."
        exit 2
    }
    if ($Mode -eq "Negative") {
        exit $neg.ExitCode
    }
}

if ($Mode -eq "Hang") {
    $hangArgs = @(
        "test", $ProjectPath,
        "--configuration", "Release",
        "--no-restore",
        "--artifacts-path", $artDir,
        "--filter", "TestCategory=TimeoutHang",
        "--logger", "trx;LogFileName=b00-01-hang.trx",
        "--results-directory", $resDir
    )
    $hang = Invoke-BoundedProcess -FilePath $DotnetExe -ArgList $hangArgs -TimeoutSec $TimeoutSeconds
    Write-Host ("[B00-01][Hang] TimedOut={0} ExitCode={1}" -f $hang.TimedOut, $hang.ExitCode)
    if (-not $hang.TimedOut) {
        Write-Error "TimeoutHang exited before supervisor timeout."
        exit 1
    }
    # Expected non-zero exit (124) proving bounded supervisor terminated hung child tree.
    exit $hang.ExitCode
}

exit 0
