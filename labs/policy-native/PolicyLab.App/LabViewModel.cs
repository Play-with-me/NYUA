using System.ComponentModel;
using System.Windows.Input;
using PolicyLab.Core;
using PolicyLab.Scenarios;

namespace PolicyLab.App;

public sealed class LabViewModel : INotifyPropertyChanged
{
    private Scenario selected = ScenarioCatalog.All[0];
    private ScenarioSession session;
    private Decision initial = new(Outcome.Cancel, Reason.UserCancelled, []);
    private bool customized;
    public event PropertyChangedEventHandler? PropertyChanged;
    public IReadOnlyList<Scenario> Cases => ScenarioCatalog.All;
    public string Status { get; private set; } = "Chưa chạy";
    public string Explanation { get; private set; } = "Chọn tình huống và bấm Kiểm tra tình huống.";
    public string Report { get; private set; } = "Chưa có kết quả. Chưa chạy không đồng nghĩa với đạt.";
    public string Expected => "Mong đợi: " + Explain(selected.ExpectedReason);
    public string Received => session.Coordinator.Analysis is { } input
        ? string.Join(Environment.NewLine, input.SafeRegions.Select(r => $"{r.Id}: {r.Text}")) : "Trống — chưa có dữ liệu trong bộ nhận.";
    public string GeometrySummary => session.Coordinator.GetGeometry() is { } g
        ? $"Sinh hoạt chỉ nhận hình học: ({g.X}, {g.Y}), {g.Width} × {g.Height}. Không có tiêu đề/nội dung."
        : "Phần sinh hoạt không nhận hình học khi nhân vật đang ẩn hoặc dữ liệu không hợp lệ.";
    public string SourceSummary => $"Nguồn giả: {session.Coordinator.Source.Id} · {session.Coordinator.Source.Visibility} · {session.Coordinator.Source.Privacy}. Bản sửa đổi: {session.Coordinator.Source.Revision}.";
    public string ObservationLabel => session.Coordinator.Permissions.ObservationEnabled ? "Tắt quan sát (giả)" : "Bật quan sát (giả)";
    public string VisibilityLabel => session.Coordinator.Permissions.CharacterVisible ? "Ẩn nhân vật (giả)" : "Hiện nhân vật (giả)";
    public ICommand StartCommand { get; }
    public ICommand RetryCommand { get; }
    public ICommand CompleteCommand { get; }
    public ICommand ApplyChangeCommand { get; }
    public ICommand CancelCommand { get; }
    public ICommand RepairCommand { get; }
    public ICommand ObservationCommand { get; }
    public ICommand VisibilityCommand { get; }
    public ICommand ResetCommand { get; }
    public ICommand RunAllCommand { get; }

    public LabViewModel()
    {
        session = new(selected);
        StartCommand = new Command(() => Begin(false), () => !session.Coordinator.IsPending);
        RetryCommand = new Command(() => Begin(true), () => !session.Coordinator.IsPending);
        CompleteCommand = new Command(Complete, () => session.Coordinator.IsPending);
        ApplyChangeCommand = new Command(ApplyChange, () => session.Coordinator.IsPending && selected.Change is not null && !session.ChangeApplied);
        CancelCommand = new Command(Cancel, () => session.Coordinator.IsPending);
        RepairCommand = new Command(() =>
        {
            customized = true;
            session.Coordinator.UpdateSource(session.Coordinator.Source with { Regions = ScenarioCatalog.Source.Regions });
            Explanation = "Đã sửa vùng giả. Nếu bị chặn an toàn trước đó, phải bấm Thử đọc lại; chưa tự đọc.";
            Refresh();
        });
        ObservationCommand = new Command(() => ChangeMode(true));
        VisibilityCommand = new Command(() => ChangeMode(false));
        ResetCommand = new Command(Reset);
        RunAllCommand = new Command(RunAll, () => !session.Coordinator.IsPending);
    }

    public Scenario SelectedScenario
    {
        get => selected;
        set { if (value is not null && value != selected) { selected = value; Reset(); } }
    }
    private Access AppAccess => session.Coordinator.Permissions.Apps.GetValueOrDefault(session.Coordinator.Source.AppId, new());
    private Access SiteAccess => session.Coordinator.Permissions.Sites.GetValueOrDefault(session.Coordinator.Source.SiteId ?? "site-a", new());
    public bool AppRead { get => AppAccess.Read; set { if (value != AppRead) SetRead(true, value); } }
    public bool SiteRead { get => SiteAccess.Read; set { if (value != SiteRead) SetRead(false, value); } }
    public bool Control
    {
        get => AppAccess.Control && SiteAccess.Control;
        set
        {
            if (value == Control) return;
            if (value && (!AppRead || !SiteRead))
            {
                Explanation = "Không bật Điều khiển: cần bật Đọc ở cả trình duyệt và website trước. Đây chỉ là quyền giả.";
                Refresh(); return;
            }
            var p = session.Coordinator.Permissions;
            var apps = new Dictionary<string, Access>(p.Apps) { [session.Coordinator.Source.AppId] = AppAccess with { Control = value } };
            var sites = new Dictionary<string, Access>(p.Sites) { [session.Coordinator.Source.SiteId ?? "site-a"] = SiteAccess with { Control = value } };
            customized = true;
            session.Coordinator.UpdatePermissions(p with { Apps = apps, Sites = sites });
            Refresh();
        }
    }

    private void SetRead(bool app, bool value)
    {
        var p = session.Coordinator.Permissions;
        var entries = new Dictionary<string, Access>(app ? p.Apps : p.Sites);
        var key = app ? session.Coordinator.Source.AppId : session.Coordinator.Source.SiteId ?? "site-a";
        entries[key] = new(value, value && entries.GetValueOrDefault(key, new()).Control);
        customized = true;
        session.Coordinator.UpdatePermissions(app ? p with { Apps = entries } : p with { Sites = entries });
        Explanation = "Đã đổi quyền giả. Dữ liệu bộ nhận cũ đã xóa; lượt đang chờ phải kiểm tra lại phiên bản.";
        Refresh();
    }

    private void Begin(bool explicitRetry)
    {
        if (explicitRetry) customized = true;
        initial = session.Begin(explicitRetry ? true : null);
        Status = session.Coordinator.IsPending ? "Đang chờ — chưa giao dữ liệu" : Label(initial);
        Explanation = session.Coordinator.IsPending
            ? "Có thể áp dụng thay đổi mẫu, chỉnh quyền, hủy hoặc bấm Tiếp tục kiểm tra."
            : Explain(initial.Reason);
        if (!session.Coordinator.IsPending) ShowResult(session.Finish(initial));
        Refresh();
    }

    private void ApplyChange()
    {
        session.ApplyChange();
        Explanation = "Đã áp dụng thay đổi giả của kịch bản. Bấm Tiếp tục kiểm tra để xác minh lượt cũ bị hủy.";
        Refresh();
    }

    private void Complete() { ShowResult(session.Finish(initial)); Refresh(); }
    private void Cancel()
    {
        customized = true;
        var result = session.Coordinator.Cancel();
        Status = Label(result); Explanation = Explain(result.Reason);
        Report = string.Join(Environment.NewLine, session.Coordinator.Diagnostics);
        Refresh();
    }
    private void ShowResult(ScenarioResult result)
    {
        Status = Label(new(result.Outcome, result.Reason, []));
        Explanation = Explain(result.Reason);
        Report = customized ? "THỬ TÙY CHỈNH — không chấm theo kỳ vọng kịch bản gốc.\n" :
            result.Passed ? "ĐẠT kiểm chứng kịch bản này.\n" : "CHƯA ĐẠT kỳ vọng kịch bản.\n";
        Report += (customized
            ? $"Thực tế: {result.Outcome}/{result.Reason}; số lần gọi bộ nhận: {result.ReceiverCalls}."
            : result.Summary) + Environment.NewLine + result.DiagnosticText;
    }
    private void ChangeMode(bool observation)
    {
        customized = true;
        var p = session.Coordinator.Permissions;
        session.Coordinator.UpdatePermissions(observation ? p with { ObservationEnabled = !p.ObservationEnabled }
            : p with { CharacterVisible = !p.CharacterVisible });
        Explanation = "Đã đổi chế độ giả và xóa dữ liệu bộ nhận cũ. Không tự bắt đầu lượt mới.";
        Refresh();
    }
    private void Reset()
    {
        session.Coordinator.Cancel();
        session = new(selected); customized = false;
        Status = "Chưa chạy"; Explanation = "Mỗi tình huống bắt đầu từ dữ liệu giả độc lập; không có dữ liệu máy thật.";
        Report = "Chưa có kết quả. Chưa chạy không đồng nghĩa với đạt.";
        Refresh();
    }
    private void RunAll()
    {
        var results = ScenarioCatalog.All.Select(ScenarioRunner.Run).ToArray();
        var passed = results.Count(r => r.Passed);
        Report = $"{passed}/{results.Length} trường hợp kiểm chứng đạt. Dữ liệu giả.\n" +
            "B05 cố ý gây lỗi bộ nhận: kiểm tra đạt khi lỗi được báo ERROR, không coi thao tác đã thành công.\n\n" +
            string.Join(Environment.NewLine, results.Select(r => r.Summary));
        Status = passed == results.Length ? $"{passed}/{results.Length} trường hợp giả đạt kiểm chứng"
            : $"{passed}/{results.Length} đạt — còn trường hợp chưa đạt";
        Explanation = "Kết quả này không chứng minh đọc màn hình thật, Unity hoặc AI. Chọn tình huống để thử thủ công.";
        Refresh();
    }
    private void Refresh()
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(null));
        CommandManager.InvalidateRequerySuggested();
    }
    private static string Label(Decision d) => d.Outcome switch
    { Outcome.Allow => "Đã giao nội dung an toàn", Outcome.Block => "Bị chặn", Outcome.Cancel => "Lượt đã hủy", _ => "Lỗi bộ nhận — không thành công" };
    private static string Explain(Reason r) => r switch
    {
        Reason.Allowed => "Bộ nhận chỉ có các vùng giả được phép đọc; vùng nhạy cảm không được chuyển tới.",
        Reason.SafetyUnknown => "Chưa xác định chắc vùng an toàn. Đã chặn cửa sổ; sửa vùng rồi bấm Thử đọc lại.",
        Reason.RetryRequired => "Cửa sổ đang bị chốt an toàn. Phải bấm Thử đọc lại, vẫn kiểm tra mọi điều kiện.",
        Reason.StaleAttempt => "Quyền, nguồn hoặc chế độ đã thay đổi. Hủy dữ liệu chờ của lượt cũ.",
        Reason.ReadRequiredForControl => "Chưa bật Đọc nên không được bật Điều khiển. Không tự cấp Đọc.",
        Reason.UserCancelled => "Người dùng đã hủy lượt. Callback tới muộn không được giao dữ liệu.",
        Reason.ReceiverError => "Bộ nhận báo lỗi. Không có nội dung được giữ lại; không sao chép thông báo lỗi chứa dữ liệu nguồn.",
        Reason.AppReadDenied => "Ứng dụng giả chưa được cấp Đọc.",
        Reason.SiteReadDenied => "Website giả chưa được cấp Đọc.",
        Reason.ObservationOff => "Quan sát đã tắt: không đọc nội dung; chỉ hình học có thể dùng cho sinh hoạt.",
        Reason.CharacterHidden => "Nhân vật đang ẩn: không quan sát hoặc nhận nội dung.",
        Reason.PrivateSource => "Nguồn riêng tư/ẩn danh bị chặn dù quyền đang bật.",
        Reason.SourceNotVisible => "Nguồn không thực sự hiển thị nên không được đọc.",
        Reason.NoSafeRegions => "Không có vùng an toàn để giao; không gọi bộ nhận bằng nội dung rỗng.",
        _ => $"Không đọc vì dữ liệu hoặc điều kiện chưa hợp lệ: {r}."
    };

    private sealed class Command(Action execute, Func<bool>? canExecute = null) : ICommand
    {
        public bool CanExecute(object? parameter) => canExecute?.Invoke() ?? true;
        public void Execute(object? parameter) => execute();
        public event EventHandler? CanExecuteChanged
        { add => CommandManager.RequerySuggested += value; remove => CommandManager.RequerySuggested -= value; }
    }
}
