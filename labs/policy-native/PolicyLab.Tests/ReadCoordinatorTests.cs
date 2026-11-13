using Microsoft.VisualStudio.TestTools.UnitTesting;
using PolicyLab.Core;

namespace PolicyLab.Tests;

[TestClass]
public class ReadCoordinatorTests
{
    internal static ReadCoordinator Create(Action<AnalysisInput>? receiver = null) => new(
        PolicyEvaluatorTests.Source, PolicyEvaluatorTests.Permissions,
        new Dictionary<string, string> { ["safe"] = "SAFE-A", ["secret"] = "FORBIDDEN-OTP" }, receiver);

    [TestMethod]
    public void RevocationBetweenCheckAndDeliveryCancelsOldAttempt()
    {
        var calls = 0;
        var lab = Create(_ => calls++);
        lab.Begin();
        lab.UpdatePermissions(lab.Permissions with { ObservationEnabled = false });
        Assert.AreEqual(Reason.StaleAttempt, lab.Complete().Reason);
        Assert.AreEqual(0, calls);
        Assert.IsNull(lab.Analysis);
    }

    [TestMethod]
    public void RetryChecksAgainAndHoldDoesNotClearOnMetadataChange()
    {
        var lab = Create();
        lab.UpdateSource(lab.Source with { Regions = [new("safe", RegionKind.Unknown)] });
        Assert.AreEqual(Reason.SafetyUnknown, lab.Begin().Reason);
        lab.UpdateSource(PolicyEvaluatorTests.Source);
        Assert.AreEqual(Reason.RetryRequired, lab.Begin().Reason);
        Assert.AreEqual(Outcome.Allow, lab.Begin(true).Outcome);
        Assert.AreEqual(Outcome.Allow, lab.Complete().Outcome);
        Assert.AreEqual("SAFE-A", lab.Analysis!.SafeRegions.Single().Text);
    }

    [TestMethod]
    public void CompleteTwiceDoesNotDeliverTwice()
    {
        var calls = 0;
        var lab = Create(_ => calls++);
        lab.Begin(); lab.Complete(); lab.Complete();
        Assert.AreEqual(1, calls);
    }

    [TestMethod]
    public void ReceiverFailureIsErrorWithoutSensitiveExceptionText()
    {
        var lab = Create(_ => throw new InvalidOperationException("FORBIDDEN-OTP"));
        lab.Begin();
        Assert.AreEqual(Outcome.Error, lab.Complete().Outcome);
        Assert.IsNull(lab.Analysis);
        Assert.IsFalse(string.Join("", lab.Diagnostics).Contains("FORBIDDEN"));
    }

    [TestMethod]
    public void CancelPreventsLateCompletion()
    {
        var lab = Create(); lab.Begin(); lab.Cancel();
        Assert.AreEqual(Reason.UserCancelled, lab.Complete().Reason);
        Assert.IsNull(lab.Analysis);
    }

    [TestMethod]
    public void OldCallbackCannotCompleteNewAttempt()
    {
        var lab = Create(); lab.Begin(); var oldId = lab.AttemptId;
        lab.Cancel(); lab.Begin();
        Assert.AreEqual(Reason.StaleAttempt, lab.Complete(oldId).Reason);
        Assert.IsTrue(lab.IsPending);
        Assert.IsNull(lab.Analysis);
    }
}
