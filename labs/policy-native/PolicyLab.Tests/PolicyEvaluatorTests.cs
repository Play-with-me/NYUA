using Microsoft.VisualStudio.TestTools.UnitTesting;
using PolicyLab.Core;

namespace PolicyLab.Tests;

[TestClass]
public class PolicyEvaluatorTests
{
    internal static SourceDescriptor Source => new("source-a", "window-a", "browser", "site-a",
        SourceKind.Web, 1, Visibility.Visible, Privacy.Normal, new(0, 0, 320, 200),
        [new("safe", RegionKind.Safe), new("secret", RegionKind.Sensitive)]);
    internal static PermissionState Permissions => new(1, true, true,
        new Dictionary<string, Access> { ["browser"] = new(true) },
        new Dictionary<string, Access> { ["site-a"] = new(true) });

    [TestMethod]
    public void AllowedDecisionContainsOnlySafeRegionIds()
    {
        var result = PolicyEvaluator.Evaluate(Source, Permissions);
        Assert.AreEqual(Outcome.Allow, result.Outcome);
        CollectionAssert.AreEqual(new[] { "safe" }, result.AllowedRegionIds.ToArray());
    }

    [TestMethod]
    public void MissingBrowserPermissionCannotBeReplacedBySitePermission()
    {
        var result = PolicyEvaluator.Evaluate(Source, Permissions with { Apps = new Dictionary<string, Access>() });
        Assert.AreEqual(Reason.AppReadDenied, result.Reason);
        Assert.AreEqual(0, result.AllowedRegionIds.Count);
    }

    [TestMethod]
    public void UnknownRegionBlocksWholeWindow()
    {
        var result = PolicyEvaluator.Evaluate(Source with { Regions = [new("unknown", RegionKind.Unknown)] }, Permissions);
        Assert.AreEqual(Reason.SafetyUnknown, result.Reason);
    }

    [TestMethod]
    public void RetryDoesNotOverridePermissions()
    {
        var result = PolicyEvaluator.Evaluate(Source, Permissions with { Sites = new Dictionary<string, Access>() }, true, true);
        Assert.AreEqual(Reason.SiteReadDenied, result.Reason);
    }

    [TestMethod]
    public void AppSourceDoesNotRequireUnrelatedWebsitePermission()
    {
        var result = PolicyEvaluator.Evaluate(Source with { Kind = SourceKind.App, SiteId = null },
            Permissions with { Sites = new Dictionary<string, Access>() });
        Assert.AreEqual(Outcome.Allow, result.Outcome);
    }

    [TestMethod]
    public void MalformedNullRegionListFailsClosed()
    {
        Assert.AreEqual(Reason.InvalidInput,
            PolicyEvaluator.Evaluate(Source with { Regions = null! }, Permissions).Reason);
    }

    [TestMethod]
    public void DuplicatedRegionIdsFailClosed()
    {
        Assert.AreEqual(Reason.InvalidInput, PolicyEvaluator.Evaluate(Source with
        { Regions = [new("safe", RegionKind.Safe), new("safe", RegionKind.Sensitive)] }, Permissions).Reason);
    }

    [TestMethod]
    public void ControlRequiresReadAndDoesNotGrantIt()
    {
        Assert.IsFalse(PolicyEvaluator.CanEnableControl(new(false, true)));
        Assert.IsTrue(PolicyEvaluator.CanEnableControl(new(true)));
    }

    [TestMethod]
    public void RegionOutsideKnownWindowBoundsFailsClosed()
    {
        var source = Source with { Regions = [new("safe", RegionKind.Safe) { Bounds = new(310, 0, 20, 10) }] };
        Assert.AreEqual(Reason.InvalidInput, PolicyEvaluator.Evaluate(source, Permissions).Reason);
    }
}
