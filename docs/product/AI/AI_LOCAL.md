# AI cục bộ và hai mức — research/benchmark specification

AI03/MC04: local nhẹ và nhanh; model/runtime/quantization/hardware threshold chưa chọn. Không gán tên model hoặc dung lượng vào requirement chỉ vì có thể tải miễn phí.

## 1. Tách các phản ứng

**Đề xuất:** direct avatar gestures và simple state transitions xử lý bằng C#/life-state, không chờ model mỗi frame. Local AI nhận safe text/image context và trả nhận định. Godot biểu hiện kết quả sau state arbitration. Đây là thiết kế để giảm latency, không sửa yêu cầu mood/relationship.

Basic: app/text/button/simplecontext; Advanced: deeper visual+Vietnamese subtitle scene affect và hoạt động/quan hệ sâu theo mode table. Basic model(s) hay rule-based phần nào chưa chốt; yêu cầu user localAI không được bị đổi thành “không có AI” mà không rà lại. Hai mức không chỉ khác kích thước model; còn feature gates đã chốt.

## 2. Candidate assessment trước chọn

| Chiều | Evidence cần có |
|---|---|
| Vietnamese subtitles | OCR/understanding trên phụ đề thật có quyền dùng, các font/outline/contrast khác nhau |
| Image/scene comprehension | Sad/action/happy/neutral, anime/liveaction, clear vs ambiguous |
| License | Model weights, tokenizer, runtime, quantized redistribution, closed-source commercial/freeapp use |
| Memory/timing | Cold/warm load, RAM/VRAM peak, CPU/GPU contention với Godot và video |
| Offline behavior | Không tự download/callhome sau cài đủ; thiếupackage báo rõ |
| Safety | Model output schema, uncertain handling, no authority/tools/keys/raw forbidden inputs |
| Packaging | Downloadsize/unpacksize/diskspace/runtime dependencies, cancel/resume/corruptdownload |

Chưa có candidate thắng. CPU-only/integrated/discrete GPU đều cần đo cấu hình đại diện trước công bố mức. Máy phát triển RTX5070/16GiB không đại diện máy người dùng.

## 3. End-to-end latency

```text
scene becomes visible
→ capture eligibility + filtering
→ snapshot / OCR
→ local inference
→ validate result + current generations
→ life-state emotional transition decision
→ animation starts on screen
```

Report từng mốc với monotonic timestamps và sceneID, không chỉ thời gian model API. Event-start/scene-label định trước. Chỉ mẫu đang được chú ý tính latency hiểu cảnh; unobserved/blocked không được đếm như correct silence. Movement đến nút không nằm cùng chỉ tiêu emotionalreaction<1s.

Target XP02: cảnh rõ dưới1s khi đang chú ý; cảnh khó ưu tiên đúng, có thểtrễ. Accuracy, passpercentile, coverage of labels, acceptable falseemotion/uncertain rate chưa chốt D-04. Không tự đặt90% hoặc p95<1s thành mục tiêu đã duyệt.

## 4. Dataset and measures

Tạo manifest sceneId, legal source/permission, duration, Vietnamese subtitle presence, scene class/clear-hard label, event onset, expected possibleemotions/intensity range, annotator/reviewstate. Tránh eval set dùng luôn để hardcode output. Giữ frozen evaluation split, không chỉ giữ các clip model đoán đúng.

Report confusion matrix/class metrics, uncertain/blocked/unattended tách riêng, end-to-end latency distributions, coldstart, sustainedmemory, droppedvideo frames nếu đo được, combined workload. Không claim subsecond khi dùng cloud hoặc precomputedlabels.

## 5. Runtime policy

Attention picks allowed visible sources; bounded work queue và stale frame dropping là đề xuất cần đo. Do not endlessly accumulate screenshots. Priority/downgrade prompts theo MC02, không silentchange mode. Model failure no fictional insight: safe fallback selflife/uncertain.

Hardwarecheck chỉ local capability metadata cần thiết, không appcontent/newpermissions. Recommend mode with reason based measured envelope; user chooses; advancedpack optional. Không tự import user profiles into public benchmark.

## 6. Traceability

AT-AI03/MC01–04/XP01–03/10–14; E04/E05; P03-01..04, P30-05, P40-06. D-04 before release acceptance; D-07/13 for secrets/licenses/packages. ExternalAI optional is a separate explicit-consent usecase, not fallback for failed localperformance.
