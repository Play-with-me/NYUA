using PolicyLab.Core;

namespace PolicyLab.Scenarios;

public sealed record ScenarioResult(string Id, bool Passed, Outcome Outcome, Reason Reason,
    int ReceiverCalls, string ReceivedText, string DiagnosticText, string Summary);

public sealed class ScenarioSession
{
    public Scenario Scenario { get; }
    public ReadCoordinator Coordinator { get; }
    public int ReceiverCalls { get; private set; }
    public bool ChangeApplied { get; private set; }
    private long activeAttempt;

    public ScenarioSession(Scenario scenario)
    {
        Scenario = scenario;
        Coordinator = new(ScenarioCatalog.Source, ScenarioCatalog.Permissions, ScenarioCatalog.Payload, _ =>
        {
            ReceiverCalls++;
            if (scenario.ThrowReceiver) throw new InvalidOperationException("FORBIDDEN-EXCEPTION");
        });
        scenario.Setup?.Invoke(Coordinator);
    }

    public Decision Begin(bool? retry = null)
    {
        if (Scenario.ControlRequest && !PolicyEvaluator.CanEnableControl(
            Coordinator.Permissions.Apps.GetValueOrDefault(Coordinator.Source.AppId, new())))
            return new(Outcome.Block, Reason.ReadRequiredForControl, []);
        var decision = Coordinator.Begin(retry ?? Scenario.Retry);
        activeAttempt = Coordinator.AttemptId;
        return decision;
    }

    public void ApplyChange()
    {
        if (ChangeApplied) return;
        Scenario.Change?.Invoke(Coordinator);
        ChangeApplied = true;
    }

    public ScenarioResult Finish(Decision initial)
    {
        if (Scenario.CancelBeforeComplete) Coordinator.Cancel();
        var actual = Coordinator.IsPending || Scenario.CancelBeforeComplete
            ? Coordinator.Complete(activeAttempt) : initial;
        if (Scenario.RepeatComplete) Coordinator.Complete(activeAttempt);
        var text = string.Join(" | ", Coordinator.Analysis?.SafeRegions.Select(x => x.Text) ?? []);
        var diagnostics = string.Join(Environment.NewLine, Coordinator.Diagnostics);
        var expectedCalls = Scenario.ExpectedOutcome is Outcome.Allow or Outcome.Error ? 1 : 0;
        var passed = actual.Outcome == Scenario.ExpectedOutcome && actual.Reason == Scenario.ExpectedReason &&
            text == Scenario.ExpectedText && ReceiverCalls == expectedCalls && !diagnostics.Contains("FORBIDDEN");
        if (Scenario.VerifyOtherSource)
        {
            var other = ScenarioCatalog.Source with { Id = "source-b", AppId = "app-b" };
            var denied = PolicyEvaluator.Evaluate(other, Coordinator.Permissions);
            passed &= denied.Outcome == Outcome.Block && denied.AllowedRegionIds.Count == 0;
        }
        if (Scenario.VerifyGeometry) passed &= Coordinator.GetGeometry() == ScenarioCatalog.Source.Geometry && Coordinator.Analysis is null;
        return new(Scenario.Id, passed, actual.Outcome, actual.Reason, ReceiverCalls, text, diagnostics,
            $"{Scenario.Id}: expected {Scenario.ExpectedOutcome}/{Scenario.ExpectedReason}; actual {actual.Outcome}/{actual.Reason}; receiver={ReceiverCalls}; {(passed ? "PASS" : "FAIL")}");
    }
}

public static class ScenarioRunner
{
    public static ScenarioResult Run(Scenario scenario)
    {
        var session = new ScenarioSession(scenario);
        var decision = session.Begin();
        session.ApplyChange();
        return session.Finish(decision);
    }
}
