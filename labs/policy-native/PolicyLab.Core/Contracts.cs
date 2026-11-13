namespace PolicyLab.Core;

public enum SourceKind { App, Web }
public enum Visibility { Visible, Hidden, Minimized, Background }
public enum Privacy { Normal, Private, Unknown }
public enum RegionKind { Safe, Sensitive, Unknown }
public enum Outcome { Allow, Block, Cancel, Error }
public enum Reason
{
    Allowed, InvalidInput, CharacterHidden, ObservationOff, PrivateSource,
    PrivacyUnknown, SourceNotVisible, AppReadDenied, SiteReadDenied,
    RetryRequired, SafetyUnknown, NoSafeRegions, StaleAttempt, UserCancelled,
    ReadRequiredForControl, ReceiverError
}

public sealed record Geometry(double X, double Y, double Width, double Height);
public sealed record Access(bool Read = false, bool Control = false);
public sealed record RegionDescriptor(string Id, RegionKind Classification)
{
    // Fixture coordinates only; this lab never crops pixels or detects real sensitive regions.
    public Geometry Bounds { get; init; } = new(0, 0, 1, 1);
}
public sealed record SourceDescriptor(string Id, string WindowId, string AppId,
    string? SiteId, SourceKind Kind, long Revision, Visibility Visibility,
    Privacy Privacy, Geometry Geometry, IReadOnlyList<RegionDescriptor> Regions);
public sealed record PermissionState(long Revision, bool ObservationEnabled,
    bool CharacterVisible, IReadOnlyDictionary<string, Access> Apps,
    IReadOnlyDictionary<string, Access> Sites);
public sealed record Decision(Outcome Outcome, Reason Reason,
    IReadOnlyList<string> AllowedRegionIds);
public sealed record SafeRegion(string Id, string Text);
public sealed record AnalysisInput(long AttemptId, string SourceId,
    long PermissionRevision, long SourceRevision, IReadOnlyList<SafeRegion> SafeRegions);
public sealed record Diagnostic(long AttemptId, string SourceId, Outcome Outcome, Reason Reason);
