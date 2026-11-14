# Kết quả tích hợp Graphify cục bộ

Ngày 2026-11-14; chỉ tài liệu/công cụ. Không chạy test ứng dụng hay thao tác UI trong đợt này.
Source ứng dụng, canonical backlog/requirements và tasks/todo.md không đổi.

## Phạm vi và bằng chứng

- Graphify0.9.97 đã có trên máy; không cài skill/hook/config toàn máy. Hai file extract.py/cli.py
  so SHA256 với tag chính thức khớp; manifest lưu expected hash và version grammar thực tế.
-20 file C#/Python thực có,255nodes/629edges:586 EXTRACTED và43 INFERRED, giữ nguyên confidence/source anchors.
  Không lỗi/bỏ qua file. Input/output LLM token bằng0; socket/subprocess guard ngăn mạng/helper trong extraction.
-219 task/109 requirement/7module từ registry; quan hệ kế hoạch tách khỏi AST bằng provenance riêng.
  Map module→lab chỉ reference thủ công, không chứng minh production life-state/distribution tồn tại.
-219 pack đều giữ exact task/requirement/acceptance, relevant confirmed/residual decisions, full CONSTRAINTS,
  dependency/bootstrap/whitelist/human gate; one-hop≤12 optional edges. Pack lớn nhất52196bytes dưới hard max160000.
- Controls từ chối unknown task, stale source, stale SRS, sửa measurement và overflow; CLI unknown module/task
  và budget1024 trả exit2 không stdout pack. Chưa có pack vượt budget bị cắt hoặc được coi là thành công.
- Trên bản sao TEMP: sửa file SRS thực và sửa byte measurement thực đều STALE; khôi phục đều FRESH.
  Input thật không đổi. Chứng chỉ measurement riêng tránh vòng selfhash; mọi baseline hash được lưu.
- Chạy build lại: graph/index/report/manifest/metrics/measurement certificate byte giống nhau.
- Dossier validator,9 task negative controls và4 dossier controls vẫn đạt; điều chỉnh copier của dossier controls
  để kèm graph navigation links, không giảm kiểm tra. E02a human acceptance/C3 còn mở.

## Số đo input thực

Baseline14 file tường minh trong MEASUREMENTS.json (không các phase card lặp):858256 Unicode chars,
937865 UTF-8bytes sau bỏ BOM/chuẩn hóa LF. Không phải tổng byte thô trên ổ đĩa.

| Input | Unicode chars | UTF-8 bytes | Ước tính ceil(chars/4), không tokenizer thật |
|---|---:|---:|---:|
| Baseline đầy đủ |858256|937865|214564|
| P01-01 |11875|13012|2969|
| P10-03 |16651|18334|4163|
| P40-05 |25385|28891|6347|

Không khẳng định tiết kiệm token tính phí thực tế hay thời gian suy luận tương ứng. Đây là input được chọn
theo task, không thay cho rà toàn hồ sơ khi nhiệm vụ yêu cầu rà toàn cục. Số đo JSON có hash nguồn/map/algorithm;
chạy check trước khi dùng snapshot này.

## Giới hạn

Không semantic document extraction/LLM, không Leiden/HTML hay chứng minh God Nodes. Không quét XAML trong scope;
AST/resolver không kiểm chứng runtime/dynamic dispatch/reflection hoặc đủ cả compiler semantic C#.
Không cài thêm tool mới; tái tạo cần Python có graphifyy0.9.97 đúng pinned file hashes. ZIP không chứa source C#;
standalone freshness phải từ chối khi thiếu nguồn, không dùng snapshot như authority. Không push/cập nhật PR.


## Rà độc lập

nyua-5: PASS trong phạm vi tài liệu/measurement/freshness, không còn blocker của finding SRS/measurement. Reviewer kiểm hash/luồng kiểm qua đọc mã, không chạy script repository hoặc test sản phẩm. Owner chạy các controls/reproducibility ghi trên. Đây không phải user acceptance hoặc product/publishing approval.
