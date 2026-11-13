namespace PolicyLab.Core;

// Used on one serialized owner thread; there is no await between final validation and delivery.
public sealed class ReadCoordinator
{
    private SourceDescriptor source;
    private PermissionState permissions;
    private readonly Dictionary<string, string> payload;
    private readonly Action<AnalysisInput>? receiver;
    private readonly HashSet<string> holds = [];
    private readonly List<Diagnostic> diagnostics = [];
    private long attemptId;
    private long capturedSource;
    private long capturedPermissions;
    private bool pending;
    private bool retry;
    private Decision current = new(Outcome.Cancel, Reason.UserCancelled, []);

    public ReadCoordinator(SourceDescriptor source, PermissionState permissions,
        IReadOnlyDictionary<string, string> payload, Action<AnalysisInput>? receiver = null)
    {
        this.source = Copy(source);
        this.permissions = Copy(permissions);
        this.payload = new(payload);
        this.receiver = receiver;
    }

    public SourceDescriptor Source => Copy(source);
    public PermissionState Permissions => Copy(permissions);
    public AnalysisInput? Analysis { get; private set; }
    public IReadOnlyList<Diagnostic> Diagnostics => diagnostics.ToArray();
    public bool IsPending => pending;
    public long AttemptId => attemptId;
    public Decision Current => current with { AllowedRegionIds = current.AllowedRegionIds.ToArray() };

    public void UpdateSource(SourceDescriptor value)
    {
        source = Copy(value) with { Revision = source.Revision + 1 };
        Analysis = null;
    }

    public void UpdatePermissions(PermissionState value)
    {
        permissions = Copy(value) with { Revision = permissions.Revision + 1 };
        Analysis = null;
    }

    public Decision Begin(bool isRetry = false)
    {
        attemptId++;
        Analysis = null;
        retry = isRetry;
        capturedSource = source.Revision;
        capturedPermissions = permissions.Revision;
        current = Check();
        pending = current.Outcome == Outcome.Allow;
        if (!pending) Record();
        return Current;
    }

    public Decision Complete(long? expectedAttemptId = null)
    {
        if (expectedAttemptId.HasValue && expectedAttemptId.Value != attemptId)
            return new(Outcome.Cancel, Reason.StaleAttempt, []);
        if (!pending) return Current;
        pending = false;
        if (capturedSource != source.Revision || capturedPermissions != permissions.Revision)
            return Finish(new(Outcome.Cancel, Reason.StaleAttempt, []));
        current = Check();
        if (current.Outcome != Outcome.Allow) return Finish(current);
        if (current.AllowedRegionIds.Any(id => !payload.ContainsKey(id)))
            return Finish(new(Outcome.Block, Reason.InvalidInput, []));
        var safe = current.AllowedRegionIds.Select(id => new SafeRegion(id, payload[id])).ToArray();
        var input = new AnalysisInput(attemptId, source.Id, permissions.Revision, source.Revision,
            Array.AsReadOnly(safe));
        try
        {
            receiver?.Invoke(input);
            Analysis = input;
            holds.Remove(source.WindowId);
            return Finish(current);
        }
        catch (Exception)
        {
            // Receiver exceptions may contain source text. Never copy their message into diagnostics.
            Analysis = null;
            return Finish(new(Outcome.Error, Reason.ReceiverError, []));
        }
    }

    public Decision Cancel()
    {
        if (!pending) return Current;
        pending = false;
        Analysis = null;
        return Finish(new(Outcome.Cancel, Reason.UserCancelled, []));
    }

    public Geometry? GetGeometry()
    {
        var g = source.Geometry;
        return permissions.CharacterVisible && g is not null &&
            double.IsFinite(g.X) && double.IsFinite(g.Y) && double.IsFinite(g.Width) &&
            double.IsFinite(g.Height) && g.Width > 0 && g.Height > 0 ? g with { } : null;
    }

    private Decision Check()
    {
        var result = PolicyEvaluator.Evaluate(source, permissions, holds.Contains(source.WindowId), retry);
        if (result.Reason == Reason.SafetyUnknown) holds.Add(source.WindowId);
        return result;
    }

    private Decision Finish(Decision result)
    {
        current = result;
        Record();
        return Current;
    }

    private void Record() => diagnostics.Add(new(attemptId, source.Id, current.Outcome, current.Reason));
    private static SourceDescriptor Copy(SourceDescriptor s) => s with { Regions = s.Regions?.ToArray()! };
    private static PermissionState Copy(PermissionState p) => p with
    {
        Apps = p.Apps is null ? null! : new Dictionary<string, Access>(p.Apps),
        Sites = p.Sites is null ? null! : new Dictionary<string, Access>(p.Sites)
    };
}
