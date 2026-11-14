# desktop-body — Unity nhân vật và không gian desktop

Status: draft; rendering direction agreed, no engine version/plugin/topology accepted yet. Uses NV*, SH04/07/08 và mode matrix; assets ART.md.

## Inputs/outputs

Input RenderState, allowed monitors/surfaces, geometry-only windows, ApproachTarget intent, useravatar interactions. Output body interaction events, Arrival/Interrupted/Unreachable report và pose/prop state. Không output OS input trực tiếp, không screenshot desktop để tự suy.

Unity physics world chỉ là representation của host-provided geometry. Needs converter giữa physical pixels/WPF DIPs/Unity units; mỗi target/pose gắn monitor/layout generation. Window closed/minimized removes supporting surface, triggers fall, not teleport to old point. Windows move carries supported body; overlaps/Zorder need tested surface model.

## Interaction recognition

Click, head-hover strokes, hold-lift, slow release reposition, fast release throw, modifier-reposition là các gesture khác nhau. Thresholds sensitivity/holdtime/velocity chưa chốt; phải kiểm Fitts/accidental actions và accessibility. Modifier-reposition bypass refusal purely administrative, không generate playful interaction/throw/hurt.

Transparent window != click-through. Renderer cần per-region hit-testing cho avatar/props và cho input pass-through ở vùng rỗng. Không cướp focus/phím của user khi tự đi. Fullscreen support phải có matrix windowed/borderless/exclusive và known limitations; không hook/bypass game protections.

## Props và movement

LeftBehind maximum5, held/in-use excluded. Before sixth left, animated put-away oldest/selected eligible prop; cách chọn prop kỹ thuật cần đảm bảo không phá tray đang dùng. User/cô ấy move từng prop. Cleanup có mood delay; no instant disappear as quickcleanup. Food groups/tray drag hỗ trợ lẻ/cảkhay, reject partialmeal UX cần rà D-14.

For real target, body travels with ladder/tools where needed. If route impossible or layout changed, no input trigger. Body acknowledgement not authorization; host rechecks final target. Display source128 and arbitrary64–384 scale requires crisp nearest/pixel strategy thử thực, không claim noninteger scaling đều pixel tuyệt đối.

## Prerequisites/acceptance

E-INT transparent, inputregions, topmost/focus, monitor/DPI, disconnect and load; E01 art/animation review. AT-NV*, AT-SH04/07/08. No 3D scope. Host/renderer process topology and plugin licensing must be recorded first.

<!-- CONFIRMED-2026-11-14 -->
## Quyết định hiện hành 2026-11-14 — ưu tiên hơn wording nháp cũ

Sinh từ registry; chỉ phần sau nhãn quyết định là bổ sung đã xác nhận. Chưa triển khai/chưa nghiệm thu; chi tiết kỹ thuật còn mở trong DECISIONS.

- **NV01:** D-14: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật.
- **NV02:** D-14: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt.
- **NV11:** D-05: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo.
- **SH04:** D-14/H08: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt.
