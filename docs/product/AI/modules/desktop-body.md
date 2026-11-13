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
