using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Nyua.Bootstrap.Companion.Tests;

/// <summary>
/// Isolated B00-01 synthetic fixture tests. Zero personal data, zero network/UI/input/capture.
/// </summary>
[TestClass]
public sealed class BootstrapTests
{
    [TestMethod]
    [TestCategory("PositiveSmoke")]
    public void PositiveSmoke_SyntheticSeedInvariant_Passes()
    {
        const int syntheticSeed = 42;
        const int expectedDouble = 84;
        Assert.AreEqual(expectedDouble, syntheticSeed * 2);
    }

    [TestMethod]
    [TestCategory("NegativeControl")]
    public void NegativeControl_DeliberateFailure_ReturnsNonZero()
    {
        Assert.Fail("Deliberate NegativeControl failure for B00-01 runner verification.");
    }

    [TestMethod]
    [TestCategory("TimeoutHang")]
    public void TimeoutHang_DeliberateHang_ExceedsBoundedSupervisor()
    {
        // Exceeds the 120s hard bound when invoked in -Mode Hang so the supervisor kills the tree.
        for (var i = 0; i < 3; i++)
        {
            Thread.Sleep(TimeSpan.FromSeconds(60));
        }
    }
}
