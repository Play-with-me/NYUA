using Microsoft.VisualStudio.TestTools.UnitTesting;
using PolicyLab.Core;
using PolicyLab.Scenarios;

namespace PolicyLab.Tests;

[TestClass]
public class ScenarioTests
{
    public static IEnumerable<object[]> Cases => ScenarioCatalog.All.Select(x => new object[] { x.Id });

    [TestMethod]
    [DynamicData(nameof(Cases))]
    public void EachScenarioMatchesIndependentExpectation(string id)
    {
        var scenario = ScenarioCatalog.All.Single(x => x.Id == id);
        var result = ScenarioRunner.Run(scenario);
        Assert.IsTrue(result.Passed, result.Summary);
        Assert.IsFalse(result.DiagnosticText.Contains("FORBIDDEN", StringComparison.Ordinal));
        Assert.IsFalse(result.ReceivedText.Contains("FORBIDDEN", StringComparison.Ordinal));
    }

    [TestMethod]
    public void CatalogContainsEveryGroupAndRequiredVariants()
    {
        var groups = ScenarioCatalog.All.Select(x => x.Id.Split('-')[0]).Distinct().ToArray();
        foreach (var id in Enumerable.Range(1, 16).Select(i => $"A{i:00}")
            .Concat(Enumerable.Range(1, 6).Select(i => $"B{i:00}")))
            CollectionAssert.Contains(groups, id);
        foreach (var id in new[] { "A06-hidden", "A06-minimized", "A06-background",
            "A08-password", "A08-otp", "A08-card", "A10-revoke", "A10-source",
            "A11-off", "A11-hide" })
            Assert.IsTrue(ScenarioCatalog.All.Any(x => x.Id == id), id);
        Assert.AreEqual(ScenarioCatalog.All.Count, ScenarioCatalog.All.Select(x => x.Id).Distinct().Count());
    }
}
