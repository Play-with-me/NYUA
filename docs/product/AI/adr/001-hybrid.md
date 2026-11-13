# ADR-001 — Unity cho nhân vật, C#/WPF cho ứng dụng

Date:2026-11-13. **Accepted direction; implementation topology proposed.** Source SP09 và cuộc trò chuyện; không đổi thành Unity-only hoặc webUI mà không userdecision.

## Context

Nhân vật pixel có nhiều hoạt động/đồ vật cần công cụ animation, đồng thời ứng dụng cần settings/tray/quyền/state/Windowsintegration. Windows11 là target đầu, user là novice cùngAI, ưu tiên miễnphí, chưa có deadlines.

## Decision

Dùng Unity cho rendering/animation, C# host/WPF cho appmanagement và điều phối; localAI xử lý nội dung được phép. Chưa quyết định embedrenderer hay separateprocess, transport, plugin, Unityversion hoặc packageformat.

## Alternatives

- WPF-only: ít kết nối engine, nativeUI thuận; phải tự xây nhiều công cụ animation/propworkflow, chưa chứng minh đúng gu.
- Unity-only: characterworkflow nhất quán; Windowsauthority/settings/data vẫn phải xây, không tự có quản lý quyền từ engine.
- WebUI prototype: dễ làm fixturetool nhưng user đã chọn native cho hướng dự án. Không mang lựa chọn thử nghiệm cũ vào sản phẩm.
- Hybrid ngay với fullsystem: đáp ứng phân công mong muốn nhưng quá nhiều rủi ro chưa đo; chọn smallprobes trước.

## Consequences/evidence

Tăng gánh tích hợp, mappingcoordinates, failureordering, packaging và combinedGPUload. Unity C# runtime khác host.NET không mặc định sharebinary. E02a chạyWPF không chứng minh renderer. E-INT/P02 cần transparent/hitzones/focus/DPI/disconnect proof; E04 localAI với rendererload. Chưa tuyên bố nhẹ hơn phương án khác.

Revisit topology nếu probe không đạt hoặc overhead phá nhu cầu chạy nền. Không tự thay toàn hướng khi một plugin lỗi; trình evidence và alternatives.

Sources: [WPF overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/overview/), [Unity native plugins](https://docs.unity.com/en-us/engine/6000.0/manual/programming-environment/plug-ins/for-desktop). Tài liệu API không phải kết quả benchmark.
