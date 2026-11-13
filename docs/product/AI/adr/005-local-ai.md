# ADR-005 — LocalAI và hai mức theo cấu hình

Date:2026-11-13. **Accepted direction, model/runtime/algorithms pending measurement.** Source AI03/MC04, featurematrix giữ nguyên.

## Context/decision

User muốn xử lý cảm xúc nhanh, offline với nội dung local, hai mức cho máy khác nhau. Chọn hướng localAI; hardwarecheck recommend nhưng userchọn/override; không silentdowngrade. Cloud chỉ optionalexplicittextrequest perAI02, không rescuebenchmark để báo localtargetđạt.

## Alternatives/tradeoffs

Cloud-first có thể tận dụng model khác nhưng thêm networklatency/cost/privacy và không khớp offline/consent. Rule-only cho mọi nội dung có latencythấp nhưng chưa đủ hiểu cảnhphim usermuốn. Localmodel mỗi gesture tránh rules nhưng thêm delay không cần thiết; đề xuất split gestures/state deterministic và contextualinference cần rà.

Local không tự nghĩa nhẹ/nhanh/chínhxác. Unity và model có thể tranhGPU/VRAM; cần đo combinedload, coldstart và sustainedtime. Basic/advanced khác cả featuregates, không chỉ paramsize.

## Acceptance/revisit

E04 dataset rights+Vietsubs, end-to-endlatency và quality/uncertainty; E05/offline/8h trên configs. D-04 trước commitmentminimumspecs; licenseweights/runtime/quantization redistribution before downloadredistribution. Nếu không đạt, trình evidence và tradeoff; không tự đổi sang gửi ảnhcloud hoặc bỏ tínhnăng userđã chọn.
