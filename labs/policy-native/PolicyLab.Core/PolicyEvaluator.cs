namespace PolicyLab.Core;

public static class PolicyEvaluator
{
    public static Decision Evaluate(SourceDescriptor source, PermissionState permissions,
        bool safetyHold = false, bool isRetry = false)
    {
        static Decision Block(Reason reason) => new(Outcome.Block, reason, []);
        if (!Valid(source, permissions)) return Block(Reason.InvalidInput);
        if (!permissions.CharacterVisible) return Block(Reason.CharacterHidden);
        if (!permissions.ObservationEnabled) return Block(Reason.ObservationOff);
        if (source.Privacy == Privacy.Private) return Block(Reason.PrivateSource);
        if (source.Privacy == Privacy.Unknown) return Block(Reason.PrivacyUnknown);
        if (source.Visibility != Visibility.Visible) return Block(Reason.SourceNotVisible);
        if (!permissions.Apps.TryGetValue(source.AppId, out var app) || !app.Read)
            return Block(Reason.AppReadDenied);
        if (source.Kind == SourceKind.Web &&
            (!permissions.Sites.TryGetValue(source.SiteId!, out var site) || !site.Read))
            return Block(Reason.SiteReadDenied);
        if (safetyHold && !isRetry) return Block(Reason.RetryRequired);
        if (source.Regions.Any(r => r.Classification == RegionKind.Unknown))
            return Block(Reason.SafetyUnknown);
        var safe = source.Regions.Where(r => r.Classification == RegionKind.Safe).Select(r => r.Id).ToArray();
        return safe.Length == 0 ? Block(Reason.NoSafeRegions) : new(Outcome.Allow, Reason.Allowed, safe);
    }

    public static bool CanEnableControl(Access access) => access.Read;

    private static bool Valid(SourceDescriptor s, PermissionState p)
    {
        if (s is null || p is null || string.IsNullOrWhiteSpace(s.Id) ||
            string.IsNullOrWhiteSpace(s.WindowId) || string.IsNullOrWhiteSpace(s.AppId) ||
            (s.Kind == SourceKind.Web && string.IsNullOrWhiteSpace(s.SiteId)) ||
            !Enum.IsDefined(s.Kind) || !Enum.IsDefined(s.Privacy) || !Enum.IsDefined(s.Visibility) ||
            s.Revision < 0 || p.Revision < 0 || s.Geometry is null || s.Regions is null ||
            p.Apps is null || p.Sites is null) return false;
        var g = s.Geometry;
        if (!double.IsFinite(g.X) || !double.IsFinite(g.Y) || !double.IsFinite(g.Width) ||
            !double.IsFinite(g.Height) || g.Width <= 0 || g.Height <= 0) return false;
        return s.Regions.All(r => r is not null && !string.IsNullOrWhiteSpace(r.Id) &&
            Enum.IsDefined(r.Classification) && ValidRegionBounds(r.Bounds, g)) &&
            s.Regions.Select(r => r.Id).Distinct().Count() == s.Regions.Count &&
            p.Apps.All(x => !string.IsNullOrWhiteSpace(x.Key) && x.Value is not null) &&
            p.Sites.All(x => !string.IsNullOrWhiteSpace(x.Key) && x.Value is not null);
    }

    private static bool ValidRegionBounds(Geometry b, Geometry window) => b is not null &&
        double.IsFinite(b.X) && double.IsFinite(b.Y) && double.IsFinite(b.Width) && double.IsFinite(b.Height) &&
        b.X >= 0 && b.Y >= 0 && b.Width > 0 && b.Height > 0 &&
        b.X + b.Width <= window.Width && b.Y + b.Height <= window.Height;
}
