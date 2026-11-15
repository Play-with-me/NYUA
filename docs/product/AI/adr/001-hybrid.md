# ADR-001 — Godot Engine cho nhân vật, C#/WPF cho ứng dụng

Date: 2026-11-15 (chuyển từ Unity sang **Godot Engine**; bản gốc 2026-11-13). **Accepted direction; implementation topology proposed / NOT VERIFIED.** Source SP09 và chỉ đạo người dùng; không đổi thành Godot-only hoặc webUI mà không user decision.

## Context

Nhân vật pixel có nhiều hoạt động/đồ vật cần công cụ animation, đồng thời ứng dụng cần settings/tray/quyền/state/Windowsintegration. Windows11 là target đầu, user là novice cùngAI, ưu tiên miễnphí, chưa có deadlines.

## Decision

Dùng **Godot Engine** (`4.7.2 – .NET` đề xuất, MIT) cho rendering/animation, C# host/WPF cho app management và điều phối; localAI xử lý nội dung được phép. Chưa quyết định dứt điểm backend dựng hình hay chứng minh runtime; topology tách tiến trình đang là ứng viên đề xuất (`NOT VERIFIED`).

## Alternatives

- WPF-only: ít kết nối engine, nativeUI thuận; phải tự xây nhiều công cụ animation/propworkflow, chưa chứng minh đúng gu.
- Godot-only: character workflow nhất quán; Windows authority/settings/data vẫn phải xây, không tự có quản lý quyền từ engine.
- WebUI prototype: dễ làm fixturetool nhưng user đã chọn native cho hướng dự án. Không mang lựa chọn thử nghiệm cũ vào sản phẩm.
- Hybrid ngay với fullsystem: đáp ứng phân công mong muốn nhưng quá nhiều rủi ro chưa đo; chọn smallprobes trước.

## Consequences/evidence

Tăng gánh tích hợp, mapping coordinates, failure ordering, packaging và combined GPU load. E02a chạy WPF không chứng minh renderer. E-INT/P02 cần transparent/hitzones/focus/DPI/disconnect proof (`NOT VERIFIED`); E04 localAI với renderer load. Chưa tuyên bố nhẹ hơn phương án khác.

Revisit topology nếu probe không đạt hoặc overhead phá nhu cầu chạy nền. Không tự thay toàn hướng khi một plugin lỗi; trình evidence và alternatives.

Sources: [WPF overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/overview/), [Godot 4 DisplayServer](https://docs.godotengine.org/en/stable/classes/class_displayserver.html). Tài liệu API không phải kết quả benchmark.
