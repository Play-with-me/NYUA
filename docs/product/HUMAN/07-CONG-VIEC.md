# Công việc và điều kiện bắt đầu

Danh sách dự kiến; chưa được phép xây sản phẩm. Không thay tracker và bằng chứng nghiệm thu E02a. Thứ tự thực hiện theo phụ thuộc từng việc, không theo thứ tự nhóm.

## P00-01 — Rà baseline và giải quyết mâu thuẫn phạm vi

Kết quả cần có: Baseline/review log.

Làm sau: Không việc trước; vẫn cần duyệt phạm vi..

Kiểm tra: Đối chiếu toàn bộ sourceIDs/mode rows với SRS và xác nhận phần hoãn. Ghi user decision hoặc blocker cho mỗi mâu thuẫn; không tự dùng default.

[Thẻ đầy đủ](../../../tasks/phase-p00.md). Chưa chạy/chưa nghiệm thu.

## B00-01 — Bootstrap verified tooling and fixtures: companion

Kết quả cần có: Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho companion; phiên bản/giấy phép và lệnh có bằng chứng.

Làm sau: P00-01.

Kiểm tra: Record exact executable/version, license and bounded build/test invocation for companion; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment. Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

[Thẻ đầy đủ](../../../tasks/phase-b00.md). Chưa chạy/chưa nghiệm thu.

## B00-02 — Bootstrap verified tooling and fixtures: desktop-body

Kết quả cần có: Unity fixture bootstrap cô lập và lệnh batch có timeout; không phụ thuộc project renderer sản phẩm.

Làm sau: P00-01.

Kiểm tra: Project Unity fixture tối thiểu nằm đúng whitelist năm file; editor/package ghim phiên bản có license evidence, scene giả không quyền input/capture/network; không đọc hoặc yêu cầu project P02-01 để tạo fixture. Batch dương chạy đúng scene/build fixture, trả 0; nhánh âm cố ý sai trả khác 0; supervisor dừng sau tối đa 120 giây mỗi lượt. Báo cáo giữ exact executable/arguments/log/version/cleanup và NOT RUN cho đến khi có phép thử thực; không coi đọc file là test.

[Thẻ đầy đủ](../../../tasks/phase-b00.md). Chưa chạy/chưa nghiệm thu.

## B00-03 — Bootstrap verified tooling and fixtures: perception

Kết quả cần có: Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho perception; phiên bản/giấy phép và lệnh có bằng chứng.

Làm sau: P00-01.

Kiểm tra: Record exact executable/version, license and bounded build/test invocation for perception; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment. Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

[Thẻ đầy đủ](../../../tasks/phase-b00.md). Chưa chạy/chưa nghiệm thu.

## B00-04 — Bootstrap verified tooling and fixtures: policy

Kết quả cần có: Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho policy; phiên bản/giấy phép và lệnh có bằng chứng.

Làm sau: P00-01.

Kiểm tra: Record exact executable/version, license and bounded build/test invocation for policy; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment. Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

[Thẻ đầy đủ](../../../tasks/phase-b00.md). Chưa chạy/chưa nghiệm thu.

## B00-05 — Bootstrap verified tooling and fixtures: life-state

Kết quả cần có: Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho life-state; phiên bản/giấy phép và lệnh có bằng chứng.

Làm sau: P00-01.

Kiểm tra: Record exact executable/version, license and bounded build/test invocation for life-state; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment. Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

[Thẻ đầy đủ](../../../tasks/phase-b00.md). Chưa chạy/chưa nghiệm thu.

## B00-06 — Bootstrap verified tooling and fixtures: task-execution

Kết quả cần có: Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho task-execution; phiên bản/giấy phép và lệnh có bằng chứng.

Làm sau: P00-01.

Kiểm tra: Record exact executable/version, license and bounded build/test invocation for task-execution; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment. Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

[Thẻ đầy đủ](../../../tasks/phase-b00.md). Chưa chạy/chưa nghiệm thu.

## B00-07 — Bootstrap verified tooling and fixtures: distribution

Kết quả cần có: Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho distribution; phiên bản/giấy phép và lệnh có bằng chứng.

Làm sau: P00-01.

Kiểm tra: Record exact executable/version, license and bounded build/test invocation for distribution; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment. Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

[Thẻ đầy đủ](../../../tasks/phase-b00.md). Chưa chạy/chưa nghiệm thu.

## R00-02 — Resolve residual evidence: D-02

Kết quả cần có: Đề cương phép thử còn mở D-02.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-02 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-02 — Rà đề cương và phạm vi phép thử D-02

Kết quả cần có: Gate đề cương D-02; không phải nghiệm thu kết quả.

Làm sau: R00-02.

Kiểm tra: Rà đề cương D-02: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## R00-03 — Resolve residual evidence: D-03

Kết quả cần có: Đề cương phép thử còn mở D-03.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-03 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-03 — Rà đề cương và phạm vi phép thử D-03

Kết quả cần có: Gate đề cương D-03; không phải nghiệm thu kết quả.

Làm sau: R00-03.

Kiểm tra: Rà đề cương D-03: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P00-02 — Rà ranh giới và hợp đồng hybrid

Kết quả cần có: Module/contract baseline.

Làm sau: P00-01, A00-02, A00-03.

Kiểm tra: Thống nhất host authority, renderer/model chỉ ý định và dữ liệu đã lọc. DTO/error/generation ownership rõ; không vòng dependency hoặc transport tự chốt. AT-SP09 — D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p00.md). Chưa chạy/chưa nghiệm thu.

## R00-04 — Resolve residual evidence: D-04

Kết quả cần có: Đề cương phép thử còn mở D-04.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-04 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-04 — Rà đề cương và phạm vi phép thử D-04

Kết quả cần có: Gate đề cương D-04; không phải nghiệm thu kết quả.

Làm sau: R00-04.

Kiểm tra: Rà đề cương D-04: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P00-03 — Chốt tiêu chuẩn chất lượng sau đo

Kết quả cần có: Quality budget proposal.

Làm sau: P00-01, A00-04.

Kiểm tra: Phân biệt target user đã chốt với ngưỡng còn phải đo. Mỗi gate có phép đo/command thực tế khi triển khai, không coverage/perf giả.

[Thẻ đầy đủ](../../../tasks/phase-p00.md). Chưa chạy/chưa nghiệm thu.

## R00-13 — Resolve residual evidence: D-13

Kết quả cần có: Đề cương phép thử còn mở D-13.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-13 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-13 — Rà đề cương và phạm vi phép thử D-13

Kết quả cần có: Gate đề cương D-13; không phải nghiệm thu kết quả.

Làm sau: R00-13.

Kiểm tra: Rà đề cương D-13: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P00-04 — Lập danh mục giấy phép và chi phí

Kết quả cần có: License/cost bill.

Làm sau: P00-01, A00-13.

Kiểm tra: Ghi source/terms/redistribution của Unity/plugin/model/art/runtime. Tên NYUA và signing/distribution còn mở được ghi riêng, khoản phí phải hỏi.

[Thẻ đầy đủ](../../../tasks/phase-p00.md). Chưa chạy/chưa nghiệm thu.

## P01-01 — Khép kiểm tra UI còn mở của E02a

Kết quả cần có: E02a technical-closure checklist/evidence, separated from user-obtained demo experience acceptance.

Làm sau: P00-01, B00-04.

Kiểm tra: Kiểm minimumresize có số đo, keyboard activation/focus và phần T05 còn mở trên mẫu hiện có bằng bằng chứng thật; mục chưa kiểm vẫn NOT RUN, không dùng quote trải nghiệm để tự đánh dấu kỹ thuật đạt. Human experience gate E02a đã OBTAINED ngày2026-11-15 theo phản hồi nguyên văn; C3 experience đóng theo người dùng. Hoàn tất kỹ thuật của P01-01 vẫn chờ mọi tiêu chí bắt buộc có evidence; T05 extended checks chưa đủ không được tự đóng.

[Thẻ đầy đủ](../../../tasks/phase-p01.md). Chưa chạy/chưa nghiệm thu.

## R00-01 — Resolve residual evidence: D-01

Kết quả cần có: Đề cương phép thử còn mở D-01.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-01 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-01 — Rà đề cương và phạm vi phép thử D-01

Kết quả cần có: Gate đề cương D-01; không phải nghiệm thu kết quả.

Làm sau: R00-01.

Kiểm tra: Rà đề cương D-01: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P02-01 — Chọn và dựng renderer thử tối thiểu

Kết quả cần có: Pinned Unity probe.

Làm sau: P00-02, P00-04, B00-02, A00-01.

Kiểm tra: Version/platform/renderpipeline và license được ghi; nhân vật chỉ placeholder. Build Windows chạy được, không input/capture/network authority.

[Thẻ đầy đủ](../../../tasks/phase-p02.md). Chưa chạy/chưa nghiệm thu.

## P02-02 — Thử transparent overlay và hit regions

Kết quả cần có: Overlay/hit test report.

Làm sau: P02-01, B00-01, B00-02, A00-01.

Kiểm tra: Avatar/prop nhận chuột đúng vùng; vùng rỗng không chặn app phía dưới. Focus/topmost/fullscreen modes đo và ghi unsupported, không bypass.

[Thẻ đầy đủ](../../../tasks/phase-p02.md). Chưa chạy/chưa nghiệm thu.

## P02-03 — Thử tọa độ qua monitor và DPI

Kết quả cần có: Coordinate contract/tests.

Làm sau: P02-02, B00-01, B00-02, A00-01.

Kiểm tra: Phân biệt physical/DIP/Unity units và bind layoutgeneration. Move/scale/monitorchange làm vô hiệu target cũ.

[Thẻ đầy đủ](../../../tasks/phase-p02.md). Chưa chạy/chưa nghiệm thu.

## P02-04 — Thử kết nối typed host-renderer

Kết quả cần có: IPC probe.

Làm sau: P02-01, P00-02, B00-01, A00-03.

Kiểm tra: Handshake role/version/session và boundedmessage validate. Duplicate/unknown/reordered messages không phát input hoặc đổi grants.

[Thẻ đầy đủ](../../../tasks/phase-p02.md). Chưa chạy/chưa nghiệm thu.

## R00-10 — Resolve residual evidence: D-10

Kết quả cần có: Đề cương phép thử còn mở D-10.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-10 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-10 — Rà đề cương và phạm vi phép thử D-10

Kết quả cần có: Gate đề cương D-10; không phải nghiệm thu kết quả.

Làm sau: R00-10.

Kiểm tra: Rà đề cương D-10: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P02-05 — Thử mất kết nối và khôi phục an toàn

Kết quả cần có: Failure state report.

Làm sau: P02-04, P02-03, B00-01, A00-02, A00-10.

Kiểm tra: Mất renderer/latecallback không cho lệnh click vượt generation. Reconnect queue UX theo quyết định người dùng, không silent replay. AT-SP09 — D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p02.md). Chưa chạy/chưa nghiệm thu.

## P03-01 — Sàng lọc model/runtime local có quyền phân phối

Kết quả cần có: Candidate/license matrix.

Làm sau: P00-04, B00-03, A00-04.

Kiểm tra: So Vietnamese/image/OCR/offline và redistribution terms thực tế. Không chọn model theo quảng cáo hoặc assumption free=redistributable. AT-AI01 — D-16: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p03.md). Chưa chạy/chưa nghiệm thu.

## P03-02 — Dựng benchmark dữ liệu cảnh an toàn

Kết quả cần có: Dataset manifest/runner.

Làm sau: P03-01, P01-01, B00-03, A00-04.

Kiểm tra: Clip có quyền sử dụng, labels/onset/clear-hard cố định trước đo. Input đã biết an toàn, không capture desktop cá nhân hoặc gửi cloud.

[Thẻ đầy đủ](../../../tasks/phase-p03.md). Chưa chạy/chưa nghiệm thu.

## P03-03 — Đo phản ứng toàn luồng dưới tải kết hợp

Kết quả cần có: Latency/quality report.

Làm sau: P03-02, P02-04, B00-03, A00-04.

Kiểm tra: Đo scenevisible→filter/OCR/infer/decision→renderstart với Unity đang chạy. Báo mọi mẫu sai/uncertain/unobserved, không đổi ngưỡng hoặc chọn lại clip.

[Thẻ đầy đủ](../../../tasks/phase-p03.md). Chưa chạy/chưa nghiệm thu.

## P03-04 — Đề xuất hai mức và luồng gói nâng cao

Kết quả cần có: Capability recommendation/pack states.

Làm sau: P03-03, P00-03, B00-01, A00-04.

Kiểm tra: Recommendation theo envelope đo, user override sau warning được. Download/validate/cancel states rõ, no silent downgrade hoặc gói giảready.

[Thẻ đầy đủ](../../../tasks/phase-p03.md). Chưa chạy/chưa nghiệm thu.

## P10-01 — Triển khai grants mặc định tắt và read/control

Kết quả cần có: Production grant evaluator.

Làm sau: P00-02, P01-01, B00-04.

Kiểm tra: App/site read-control riêng; browserANDsite; newsource defaultdeny. Revoke tăng generation và control không tự bật read.

[Thẻ đầy đủ](../../../tasks/phase-p10.md). Chưa chạy/chưa nghiệm thu.

## R00-15 — Resolve residual evidence: D-15

Kết quả cần có: Đề cương phép thử còn mở D-15.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-15 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-15 — Rà đề cương và phạm vi phép thử D-15

Kết quả cần có: Gate đề cương D-15; không phải nghiệm thu kết quả.

Làm sau: R00-15.

Kiểm tra: Rà đề cương D-15: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## R00-16 — Resolve residual evidence: D-16

Kết quả cần có: Đề cương phép thử còn mở D-16.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-16 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-16 — Rà đề cương và phạm vi phép thử D-16

Kết quả cần có: Gate đề cương D-16; không phải nghiệm thu kết quả.

Làm sau: R00-16.

Kiểm tra: Rà đề cương D-16: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P10-02 — Nhận dạng nguồn và vùng đang hiển thị

Kết quả cần có: Visible source adapter.

Làm sau: P10-01, P02-03, B00-03, A00-15, A00-16.

Kiểm tra: Nguồn nền/thu nhỏ/bịche không được truyền nội dung; splitview đúng grants. Không mở mail gây mark-read; unsupportedsource chặn và giải thích. AT-QD04 — D-12: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p10.md). Chưa chạy/chưa nghiệm thu.

## P10-03 — Lọc sensitive/private và retry hold trên nguồn thật

Kết quả cần có: Safe snapshot boundary.

Làm sau: P10-02, B00-04, A00-15.

Kiểm tra: No forbidden sentinel in OCR/model/memory/log; unknownwholewindow hold. Explicit retry validates mới, revoke/change trongpipeline discard. AT-SH01 — D-12: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p10.md). Chưa chạy/chưa nghiệm thu.

## P10-04 — Kiểm chứng clipboard history đúng Win+V scope

Kết quả cần có: Clipboard adapter/proof.

Làm sau: P10-03, B00-03, A00-15.

Kiểm tra: Có evidence bảng open/close đúng trước đọc history; không tự bật setting. Đóng giữa chừng hủy buffer và no memory/log persistence.

[Thẻ đầy đủ](../../../tasks/phase-p10.md). Chưa chạy/chưa nghiệm thu.

## R00-07 — Resolve residual evidence: D-07

Kết quả cần có: Đề cương phép thử còn mở D-07.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-07 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-07 — Rà đề cương và phạm vi phép thử D-07

Kết quả cần có: Gate đề cương D-07; không phải nghiệm thu kết quả.

Làm sau: R00-07.

Kiểm tra: Rà đề cương D-07: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## R00-08 — Resolve residual evidence: D-08

Kết quả cần có: Đề cương phép thử còn mở D-08.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-08 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-08 — Rà đề cương và phạm vi phép thử D-08

Kết quả cần có: Gate đề cương D-08; không phải nghiệm thu kết quả.

Làm sau: R00-08.

Kiểm tra: Rà đề cương D-08: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P50-01 — Chốt storage và transaction/persistence

Kết quả cần có: Versioned local storage.

Làm sau: P00-02, P00-04, B00-07, A00-07, A00-08, A00-10.

Kiểm tra: Logicalentity/provenance ownership và state commit transactional, no hiddenbackup. Corrupt/interruptedwrite handling preservesexisting or reportsfailure; no fake recovery. AT-CD01 — D-10: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p50.md). Chưa chạy/chưa nghiệm thu.

## R00-18 — Resolve residual evidence: D-18

Kết quả cần có: Đề cương phép thử còn mở D-18.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-18 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-18 — Rà đề cương và phạm vi phép thử D-18

Kết quả cần có: Gate đề cương D-18; không phải nghiệm thu kết quả.

Làm sau: R00-18.

Kiểm tra: Rà đề cương D-18: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P10-05 — Luồng AI ngoài có preview và consent mỗi lần

Kết quả cần có: Explicit text-only request.

Làm sau: P10-03, P50-01, B00-04, A00-07, A00-18.

Kiểm tra: Exactsafe text+destination preview; payload/sourcechange invalidatesconsent. Reject/retry/offline no auto fallback or forbidden category send. AT-AI02 — D-18: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p10.md). Chưa chạy/chưa nghiệm thu.

## P10-06 — Bridge trình duyệt và ngoại lệ khung video

Kết quả cần có: Optional extension/frame binding.

Làm sau: P10-03, P00-04, B00-03, A00-03, A00-15.

Kiểm tra: Chrome/Edge web requires extension only whenenabled; no broad grants. Crossoriginplayer identified/confirmed scopedparent; mismatch asksagain.

[Thẻ đầy đủ](../../../tasks/phase-p10.md). Chưa chạy/chưa nghiệm thu.

## R00-05 — Resolve residual evidence: D-05

Kết quả cần có: Đề cương phép thử còn mở D-05.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-05 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-05 — Rà đề cương và phạm vi phép thử D-05

Kết quả cần có: Gate đề cương D-05; không phải nghiệm thu kết quả.

Làm sau: R00-05.

Kiểm tra: Rà đề cương D-05: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## R00-11 — Resolve residual evidence: D-11

Kết quả cần có: Đề cương phép thử còn mở D-11.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-11 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-11 — Rà đề cương và phạm vi phép thử D-11

Kết quả cần có: Gate đề cương D-11; không phải nghiệm thu kết quả.

Làm sau: R00-11.

Kiểm tra: Rà đề cương D-11: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P10-07 — Input arbitration và các nút dừng

Kết quả cần có: Stop/input gate.

Làm sau: P10-01, P02-05, B00-04, A00-05, A00-11.

Kiểm tra: Humaninput vs injected classified withoutkeycontent, idle60s/unlockexception đúng. Emergency/off/hide matrix + generation prevents lateraction; sleepedge resolved. AT-XP08 — D-11: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p10.md). Chưa chạy/chưa nghiệm thu.

## R00-14 — Resolve residual evidence: D-14

Kết quả cần có: Đề cương phép thử còn mở D-14.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-14 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-14 — Rà đề cương và phạm vi phép thử D-14

Kết quả cần có: Gate đề cương D-14; không phải nghiệm thu kết quả.

Làm sau: R00-14.

Kiểm tra: Rà đề cương D-14: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P20-01 — Duyệt model sheet nhân vật gốc

Kết quả cần có: Approved art reference.

Làm sau: P00-04, B00-02, A00-14.

Kiểm tra: Đúng adultchibi/appearance/anatomicalclip và source128. User duyệt sample; provenance/license recorded, no borrowedcharacter. AT-NV01 — D-14: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate. AT-NV02 — D-14: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p20.md). Chưa chạy/chưa nghiệm thu.

## P20-02 — Di chuyển và bề mặt cửa sổ

Kết quả cần có: Locomotion/surface model.

Làm sau: P20-01, P02-03, P02-05, B00-02, A00-01.

Kiểm tra: Followmovingwindow; closesupport→fall→land/stand đúng. Geometryonly inputs và forbiddenwindowtitles không lọt renderer.

[Thẻ đầy đủ](../../../tasks/phase-p20.md). Chưa chạy/chưa nghiệm thu.

## R00-12 — Resolve residual evidence: D-12

Kết quả cần có: Đề cương phép thử còn mở D-12.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-12 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-12 — Rà đề cương và phạm vi phép thử D-12

Kết quả cần có: Gate đề cương D-12; không phải nghiệm thu kết quả.

Làm sau: R00-12.

Kiểm tra: Rà đề cương D-12: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P30-01 — Needs/sleep/rest và elapsed reconciliation

Kết quả cần có: Basic life clock.

Làm sau: P00-02, P50-01, B00-05, A00-05, A00-12.

Kiểm tra: Needs/sleep phản ứng clock/fatigue, reservefood/no heavyabsencepenalty. Appclosed elapsed nofakeevents; inactiveprofilefreeze distinct. AT-SH01 — D-12: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate. AT-QD04 — D-12: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p30.md). Chưa chạy/chưa nghiệm thu.

## P30-02 — Lựa chọn hoạt động, mood và attention limits

Kết quả cần có: Activity selection/state.

Làm sau: P30-01, B00-05, A00-05.

Kiểm tra: Causalchoices from needs/mood/preferences/memory, canchangeintent; noOSpranks. Invitation/tease share2attempts/>=30min, ignore→selfplay.

[Thẻ đầy đủ](../../../tasks/phase-p30.md). Chưa chạy/chưa nghiệm thu.

## P20-03 — Pet/lift/throw và chuyển vị trí an toàn

Kết quả cần có: Gesture recognizer.

Làm sau: P20-02, P30-02, B00-02, A00-05.

Kiểm tra: Phân biệt các gestures bằng ngưỡng đã đo/chốt, no accidentalthrow từ slowmove. Refusallift giữ; modifierreposition neutral, readinessgesture có. AT-NV11 — D-05: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p20.md). Chưa chạy/chưa nghiệm thu.

## P20-04 — Foodtray, đồ vật và animatedcleanup

Kết quả cần có: Food/prop interaction.

Làm sau: P20-02, P30-01, B00-02, A00-14.

Kiểm tra: Đủ6foods; tray/lẻ/refusal behavior; max5left with inuse exemption. Sixthleft waits animatedputaway; usermove/hide always available. AT-SH04 — D-14/H08: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p20.md). Chưa chạy/chưa nghiệm thu.

## P20-05 — Placement nhiều màn hình và fullscreen

Kết quả cần có: Placement/support matrix.

Làm sau: P20-02, P02-02, B00-02, A00-01.

Kiểm tra: Onlychosenmonitors, fullscreenedge withoutmidcenter obstruction. MixedDPI and unsupportedexclusive modes documented; not universalgame promise.

[Thẻ đầy đủ](../../../tasks/phase-p20.md). Chưa chạy/chưa nghiệm thu.

## P30-04 — Memory provenance, pin/fade/edit/delete

Kết quả cần có: Memory lifecycle.

Làm sau: P50-01, P10-01, B00-05, A00-08.

Kiểm tra: Documenttopiconly, no clipboard/secretlasting; pin/fade/provenance guards. Editno relationrecalc; explicitdelete inverseonce vs naturalfade keepscloseness.

[Thẻ đầy đủ](../../../tasks/phase-p30.md). Chưa chạy/chưa nghiệm thu.

## P30-03 — Quan hệ sâu, neglect và làm lành

Kết quả cần có: Relationship state machine.

Làm sau: P30-02, P30-04, B00-05, A00-05.

Kiểm tra: Eligibleactiveclock48–72h directionaltrust/hurt, no absence/basicpenalty. Firstthrow/repeat/refusal/selfhide/invite/gifts gradual multisessionrepair đúng. AT-QH05 — D-05/H03: Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không là buổi mới. Không tự đặt số phút/số buổi hoặc quà lập tức xóa tổn thương. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p30.md). Chưa chạy/chưa nghiệm thu.

## P30-05 — Học gu từ user media evidence

Kết quả cần có: Media preference inference.

Làm sau: P30-04, P10-02, B00-05, A00-16.

Kiểm tra: Movie20min/musicrepeat + usertransitions, selfopen does not prove presence. No browserhistory/backgroundcontent/audioanalysis, preference notcertaintylike.

[Thẻ đầy đủ](../../../tasks/phase-p30.md). Chưa chạy/chưa nghiệm thu.

## P30-06 — Mode preservation, personality và romance opt-in

Kết quả cần có: Advanced state transitions.

Làm sau: P30-03, P03-04, B00-05, A00-05.

Kiểm tra: Downgrade preservesstate and suspendsdeeppenalty/expression, reenablecontinues. Romanceoff keep/delete respectschoice; personalitymatures withoutlosingcorenets.

[Thẻ đầy đủ](../../../tasks/phase-p30.md). Chưa chạy/chưa nghiệm thu.

## P40-01 — Onboarding/tray/settings shell

Kết quả cần có: Native management UI.

Làm sau: P02-04, P50-01, B00-01, A00-14.

Kiểm tra: Firstprofile/name/startupchoice, tray opensfullsettings, no signupgate. Namesize/modes/monitors and stop routes accessible independentofmood.

[Thẻ đầy đủ](../../../tasks/phase-p40.md). Chưa chạy/chưa nghiệm thu.

## P40-02 — UI grants và chosenbrowser

Kết quả cần có: App/site permission UI.

Làm sau: P40-01, P10-01, B00-01.

Kiểm tra: Scannedapps+pastedwebsites separategrants with explanatorylabels, alloff. Chrome/Edge selectedbrowser doesnot grantpermissions; revoke routescorrectly.

[Thẻ đầy đủ](../../../tasks/phase-p40.md). Chưa chạy/chưa nghiệm thu.

## R00-17 — Resolve residual evidence: D-17

Kết quả cần có: Đề cương phép thử còn mở D-17.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-17 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-17 — Rà đề cương và phạm vi phép thử D-17

Kết quả cần có: Gate đề cương D-17; không phải nghiệm thu kết quả.

Làm sau: R00-17.

Kiểm tra: Rà đề cương D-17: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P40-03 — Dạy/review/manage lesson và searchparameters

Kết quả cần có: Lesson definition workflow.

Làm sau: P10-03, P40-01, P50-01, B00-06, A00-17.

Kiểm tra: Explicitrecording sameapp/site, reviewconfirm then saveversion. Manage/reteach, searchparameters and firstresult/exactmeaning clear; illegaltyping denied. AT-BH02 — D-17: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p40.md). Chưa chạy/chưa nghiệm thu.

## P40-04 — Embodied execution và postconditionverify

Kết quả cần có: Verified step runner.

Làm sau: P40-03, P10-07, P20-02, B00-06, A00-03, A00-05.

Kiểm tra: Approach→reobserve→finalpermit→singleaction→postcondition, targetchange stops. Human yield60s/resume/reteach, no forbiddenwrites/forms/payments; directrequestdelayonce.

[Thẻ đầy đủ](../../../tasks/phase-p40.md). Chưa chạy/chưa nghiệm thu.

## P40-05 — Hàng đợi, priority và stop lifecycle

Kết quả cần có: Queue state machine.

Làm sau: P40-04, P30-03, B00-06, A00-02, A00-10, A00-17.

Kiểm tra: Runningcancel/pendingpause/resumeexplicit/exitcancel matches matrix. Jobfailed stopsalone, nextindependent runs; directrequest preemptsdiscovery, no doublejob. AT-SP09 — D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate. AT-BH02 — D-17: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate. AT-BH06 — D-02/D-10/D-17: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate. AT-CD01 — D-10: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p40.md). Chưa chạy/chưa nghiệm thu.

## P40-06 — Xem cùng và phản ứng cảm xúc

Kết quả cần có: Attended media response.

Làm sau: P03-03, P10-03, P30-02, P20-04, B00-01, A00-04, A00-12.

Kiểm tra: Safeobservations drive smoothaffect, silentreactions; hard/uncaptured nofakeunderstanding. Usermovie not interrupted, nextended target rechecked; no subtitleautoavoid requirement.

[Thẻ đầy đủ](../../../tasks/phase-p40.md). Chưa chạy/chưa nghiệm thu.

## R00-06 — Resolve residual evidence: D-06

Kết quả cần có: Đề cương phép thử còn mở D-06.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-06 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-06 — Rà đề cương và phạm vi phép thử D-06

Kết quả cần có: Gate đề cương D-06; không phải nghiệm thu kết quả.

Làm sau: R00-06.

Kiểm tra: Rà đề cương D-06: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P40-07 — Tự tìm/mở nội dung trong quyền

Kết quả cần có: Bounded autonomous media.

Làm sau: P40-05, P40-06, P10-06, B00-06, A00-06, A00-11, A00-16.

Kiểm tra: Advancedidle5m+unlocked+nomedia, owntab/chosenbrowser, preserveusertabs/playback. Skiplogin/pay/verify max3; uncertainadkeep; allowedframe scoped. AT-XP05 — D-16: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate. AT-XP07 — D-06: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate. AT-XP08 — D-11: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate. AT-AI01 — D-16: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p40.md). Chưa chạy/chưa nghiệm thu.

## P50-02 — Profile import/switch/reset semantics

Kết quả cần có: Profile lifecycle.

Làm sau: P50-01, P10-01, B00-07, A00-10.

Kiểm tra: Onlyimportadds, exactlyoneactive, inactiveallfreeze and sharedmachinegrants. Resetcurrent clearsstate/memory/relation/lessons, preserveothers; switch cancelsunfinished.

[Thẻ đầy đủ](../../../tasks/phase-p50.md). Chưa chạy/chưa nghiệm thu.

## R00-09 — Resolve residual evidence: D-09

Kết quả cần có: Đề cương phép thử còn mở D-09.

Làm sau: P00-01.

Kiểm tra: Phân loại câu hỏi còn mở của D-09 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy. Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

[Thẻ đầy đủ](../../../tasks/phase-r00.md). Chưa chạy/chưa nghiệm thu.

## A00-09 — Rà đề cương và phạm vi phép thử D-09

Kết quả cần có: Gate đề cương D-09; không phải nghiệm thu kết quả.

Làm sau: R00-09.

Kiểm tra: Rà đề cương D-09: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra. Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

[Thẻ đầy đủ](../../../tasks/phase-a00.md). Chưa chạy/chưa nghiệm thu.

## P50-03 — Manualexport password/recovery format

Kết quả cần có: Reviewed encrypted archive export.

Làm sau: P50-01, P00-04, B00-07, A00-07, A00-09.

Kiểm tra: Requiredpassword/recovery separate, auditedprimitive and boundedformat. Whitelist excludesgrants/keys/rawsources/queue; no autoarchives. AT-SL01 — D-09: Sao lưu không kèm gói AI nâng cao; máy mới tải lại khi cần, không thêm tùy chọn kèm gói mỗi lần xuất. Giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p50.md). Chưa chạy/chưa nghiệm thu.

## P50-04 — Validate/import archive thành hồ sơ riêng

Kết quả cần có: Transactional import.

Làm sau: P50-03, P50-02, B00-07, A00-07, A00-09.

Kiểm tra: Wrongpassword/code/corrupt/pathtraversal/unknownschema boundedreject. Successnewprofile no merge/foreigngrants, existingdata preserved onfailure.

[Thẻ đầy đủ](../../../tasks/phase-p50.md). Chưa chạy/chưa nghiệm thu.

## P50-05 — Local actionhistory và expiry30days

Kết quả cần có: Sanitized history pipeline.

Làm sau: P50-01, B00-07.

Kiểm tra: Time/source/action/outcome only, no raw/privatepayload/screenshots; no telemetry. Userdelete and30days expiry actual, history separatememory.

[Thẻ đầy đủ](../../../tasks/phase-p50.md). Chưa chạy/chưa nghiệm thu.

## P50-06 — Bộ cài và startup opt-in

Kết quả cần có: Native install package.

Làm sau: P00-04, P40-01, P20-05, B00-07, A00-13.

Kiểm tra: Actualcompatible host/renderer/runtime components pinned and installtested. Startup userchoice, basic works without optionalAIpack/extension/account. AT-CD01 — D-10: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

[Thẻ đầy đủ](../../../tasks/phase-p50.md). Chưa chạy/chưa nghiệm thu.

## P50-07 — Own update check/download/install confirmation

Kết quả cần có: Authenticated update flow.

Làm sau: P50-06, P50-04, B00-07, A00-10, A00-13.

Kiểm tra: Ownupdatesource/download verified, userconfirm before install/restart. Invalidsignature/migration stops, no otherappupdate or auto backup; rollback compatibility explicit.

[Thẻ đầy đủ](../../../tasks/phase-p50.md). Chưa chạy/chưa nghiệm thu.

## P50-08 — Uninstall giữ/xóa và manualexport reminder

Kết quả cần có: Uninstall data workflow.

Làm sau: P50-06, P50-03, B00-07, A00-13.

Kiểm tra: Explicitretain/deleteappdata, remindmanualexport, jobswarncancel. No search/delete manuallyexported archives outsideowneddata.

[Thẻ đầy đủ](../../../tasks/phase-p50.md). Chưa chạy/chưa nghiệm thu.

## P60-01 — Lát tích hợp đầu: hiện→đọc an toàn→phản ứng→dừng

Kết quả cần có: One complete product path.

Làm sau: P40-01, P20-02, P30-02, P10-03, B00-01, A00-01, A00-15.

Kiểm tra: Không dùng cannedlabel thay realperception; life/render/grants cùng chạy. Stop/revoke actualconsumers, E02afakeproof không được promote.

[Thẻ đầy đủ](../../../tasks/phase-p60.md). Chưa chạy/chưa nghiệm thu.

## P60-02 — Hồi quy hai mức và toàn bộ nghiệp vụ

Kết quả cần có: Full RTM evidence.

Làm sau: P60-01, P30-06, P40-07, P50-04, P50-05, B00-01, A00-04.

Kiểm tra: Allscope requirements mapped to test/results, deferredseparate; modefeatures correct. Negativepaths/keyboard/DPI/privacy/state tested, no skippedcriteria.

[Thẻ đầy đủ](../../../tasks/phase-p60.md). Chưa chạy/chưa nghiệm thu.

## P60-03 — Phiên8h/offline và ma trận cấu hình

Kết quả cần có: Real8h soak report.

Làm sau: P60-02, P03-04, B00-01, A00-04.

Kiểm tra: Frozen8h schedule, measuredresource/faults on definedmachines. Offlineworks afterinstall, no unapprovedautodowngrade/cloud; actual8h notsimclock.

[Thẻ đầy đủ](../../../tasks/phase-p60.md). Chưa chạy/chưa nghiệm thu.

## P60-04 — Rà độc lập, thương hiệu và release gate

Kết quả cần có: Release readiness packet.

Làm sau: P60-03, P50-07, P50-08, P00-04, B00-07, A00-13, P03-01, C00-04.

Kiểm tra: Bothmodesstable, security/data/license/name issues resolved or explicitapprovedscope. Actualreviewer/owner recorded; no pretendingAIselfreview independent.

[Thẻ đầy đủ](../../../tasks/phase-p60.md). Chưa chạy/chưa nghiệm thu.

## P60-05 — Chuẩn bị công bố và hỗ trợ có kiểm soát

Kết quả cần có: User-facing release/runbook.

Làm sau: P60-04, B00-07, A00-13.

Kiểm tra: User approves actualpublicartifact/costs/communication, notjustplan. Vietnamesehelp/privacy/AIcosts/localhistory/support/redactedbugtemplate ready.

[Thẻ đầy đủ](../../../tasks/phase-p60.md). Chưa chạy/chưa nghiệm thu.

## V00-001 — Clause acceptance: SP01

Kết quả cần có: Case matrix and evidence for AT-SP01.

Làm sau: P30-02, B00-01.

Kiểm tra: Qua kịch bản chăm sóc, nghỉ và thay đổi chú ý, quyết định hoạt động có nguyên nhân từ trạng thái; không chỉ lặp một playlist hoạt ảnh. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-002 — Clause acceptance: SP02

Kết quả cần có: Case matrix and evidence for AT-SP02.

Làm sau: P60-01, B00-01.

Kiểm tra: Dùng thử một luồng kết hợp sinh hoạt, ghi nhớ, hiểu ngữ cảnh và chuyển động; từng demo riêng không thay nghiệm thu luồng kết hợp. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-003 — Clause acceptance: SP03

Kết quả cần có: Case matrix and evidence for AT-SP03.

Làm sau: P50-06, B00-01.

Kiểm tra: Cài/chạy bản tiếng Việt trên Windows11; checklist phát hành ghi miễn phí bản đầu và không công khai source; chưa suy ra hỗ trợ OS khác. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-004 — Clause acceptance: SP04

Kết quả cần có: Case matrix and evidence for AT-SP04.

Làm sau: P40-01, B00-01.

Kiểm tra: Cài mới dùng được không đăng ký; kiểm data local và dịch vụ AI ngoài chỉ dùng thông tin kết nối người dùng cung cấp. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-005 — Clause acceptance: SP05

Kết quả cần có: Case matrix and evidence for AT-SP05.

Làm sau: P60-03, B00-01.

Kiểm tra: Không đóng cổng phát hành nếu một trong hai mức chưa đạt tiêu chí; bản nội bộ được dán nhãn khác bản công khai. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-006 — Clause acceptance: SP06

Kết quả cần có: Case matrix and evidence for AT-SP06.

Làm sau: P00-04, B00-01.

Kiểm tra: Danh mục công cụ ghi chi phí/giấy phép; khoản phí không được mua hoặc kích hoạt khi chưa có quyết định người dùng. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-007 — Clause acceptance: SP07

Kết quả cần có: Case matrix and evidence for AT-SP07.

Làm sau: P30-06, B00-01.

Kiểm tra: Cùng trải nghiệm qua thời gian tạo cách biểu hiện cân nhắc hơn ở nâng cao; vẫn có tò mò/tinh nghịch/ý muốn riêng, cơ bản không tiến hóa tính cách. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-008 — Clause acceptance: SP08

Kết quả cần có: Case matrix and evidence for AT-SP08.

Làm sau: P30-02, B00-01.

Kiểm tra: Không có nút đánh giá hành vi; bỏ qua lời rủ không thành lời phê bình; learning-demo chỉ ghi khi user bật. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-009 — Clause acceptance: SP09

Kết quả cần có: Case matrix and evidence for AT-SP09.

Làm sau: P00-02, B00-01, P02-05, P40-05.

Kiểm tra: Rà phân công Unity/host/WPF/localAI; không đưa web UI làm nền sản phẩm hoặc coi IPC/model đã chứng minh từ sơ đồ. Kiểm cả nhánh cho phép và từ chối: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-010 — Clause acceptance: NV01

Kết quả cần có: Case matrix and evidence for AT-NV01.

Làm sau: P20-01, B00-02.

Kiểm tra: Duyệt mẫu nữ trưởng thành chibi đầu lớn người nhỏ; cài mới các user có cùng ngoại hình đã duyệt. Kiểm cả nhánh cho phép và từ chối: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-011 — Clause acceptance: NV02

Kết quả cần có: Case matrix and evidence for AT-NV02.

Làm sau: P20-01, B00-02.

Kiểm tra: So mẫu front/side với tóc bạc ngang eo, mái thưa, mắt đỏ hồng và da sáng ấm; ghi sửa nếu lệch. Kiểm cả nhánh cho phép và từ chối: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-012 — Clause acceptance: NV03

Kết quả cần có: Case matrix and evidence for AT-NV03.

Làm sau: P20-01, B00-02.

Kiểm tra: Kiểm áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, không tất/giày ở mọi hướng. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-013 — Clause acceptance: NV04

Kết quả cần có: Case matrix and evidence for AT-NV04.

Làm sau: P20-01, B00-02.

Kiểm tra: Front view kẹp ở trái ảnh, thuộc bên phải nhân vật; sprite lật không làm sai bên giải phẫu; nét thường ngày tươi. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-014 — Clause acceptance: NV05

Kết quả cần có: Case matrix and evidence for AT-NV05.

Làm sau: P20-02, B00-02.

Kiểm tra: Kiểm asset nguồn128x128 và chuyển động ở nhiều tỉ lệ; không kết luận mượt chỉ từ kích thước file. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-015 — Clause acceptance: NV06

Kết quả cần có: Case matrix and evidence for AT-NV06.

Làm sau: P40-01, B00-02.

Kiểm tra: Lần đầu128; kéo64–384; mở lại giữ lựa chọn; đặt tên qua onboarding. Giới hạn ký tự cần quyết định riêng. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-016 — Clause acceptance: NV07

Kết quả cần có: Case matrix and evidence for AT-NV07.

Làm sau: P20-02, B00-02.

Kiểm tra: Di chuyển/thu nhỏ/đóng cửa sổ đang làm bề mặt: theo cửa sổ hoặc rơi đúng bề mặt kế tiếp, không đứng lơ lửng. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-017 — Clause acceptance: NV08

Kết quả cần có: Case matrix and evidence for AT-NV08.

Làm sau: P20-05, B00-02.

Kiểm tra: Chỉ xuất hiện trên monitor cho phép; fullscreen ở mép; ghi rõ trường hợp exclusive không hỗ trợ sau thử, không tự hứa mọi game. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-018 — Clause acceptance: NV09

Kết quả cần có: Case matrix and evidence for AT-NV09.

Làm sau: P20-03, B00-02.

Kiểm tra: Phân biệt click/pet/hold-drag/slow-release/fast-release; quăng có đà và rơi/đứng dậy; ngưỡng đo trước chốt. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-019 — Clause acceptance: NV10

Kết quả cần có: Case matrix and evidence for AT-NV10.

Làm sau: P40-04, B00-02.

Kiểm tra: Input thật chỉ xảy ra sau body approach và revalidate; có dụng cụ ảo khi thiếu bề mặt và bàn phím ảo lúc gõ. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-020 — Clause acceptance: NV11

Kết quả cần có: Case matrix and evidence for AT-NV11.

Làm sau: P20-03, B00-02.

Kiểm tra: Modifier-drag di chuyển ngay cả refusal-lift, không quăng và không giảm relation; phím Shift đã chốt, không thêm tùy chọn phím. Kiểm cả nhánh cho phép và từ chối: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-021 — Clause acceptance: MC01

Kết quả cần có: Case matrix and evidence for AT-MC01.

Làm sau: P03-04, B00-01.

Kiểm tra: Cài mới không tải gói nâng cao ngầm; user chọn mới tải, lỗi tải không báo gói đã sẵn sàng. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-022 — Clause acceptance: MC02

Kết quả cần có: Case matrix and evidence for AT-MC02.

Làm sau: P03-04, B00-01.

Kiểm tra: Máy yếu vẫn có lựa chọn thử sau cảnh báo; simulated overload hỏi giảm/tiếp tục và không đổi mode tự động. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-023 — Clause acceptance: MC03

Kết quả cần có: Case matrix and evidence for AT-MC03.

Làm sau: P30-06, B00-01.

Kiểm tra: Nâng cao→cơ bản→nâng cao bảo toàn memory/relation/personality; cơ bản không tích lũy neglect sâu. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-024 — Clause acceptance: MC04

Kết quả cần có: Case matrix and evidence for AT-MC04.

Làm sau: P03-04, B00-01.

Kiểm tra: Recommendation có dựa measured workload/hardware capability; user override được; không chỉ dựa tên GPU. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-025 — Clause acceptance: SH01

Kết quả cần có: Case matrix and evidence for AT-SH01.

Làm sau: P30-01, B00-05, P10-03.

Kiểm tra: Test logical clock/click khi ngủ: phản ứng tùy fatigue, nhịp có naps; chưa tự đặt sleep schedule cố định. Kiểm cả nhánh cho phép và từ chối: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-026 — Clause acceptance: SH02

Kết quả cần có: Case matrix and evidence for AT-SH02.

Làm sau: P30-01, B00-05.

Kiểm tra: Bận/vắng không disease/progress-loss; khi hoạt động có reserve food; không yêu cầu chăm như nghĩa vụ liên tục. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-027 — Clause acceptance: SH03

Kết quả cần có: Case matrix and evidence for AT-SH03.

Làm sau: P30-01, B00-05.

Kiểm tra: Reopen cập nhật elapsed state nhưng không thêm fake memories/events; inactive profile dùng freeze khác appclose. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-028 — Clause acceptance: SH04

Kết quả cần có: Case matrix and evidence for AT-SH04.

Làm sau: P20-04, B00-05.

Kiểm tra: Đủ6 món miễn phí, chọn ghép bữa, kéo lẻ/cả khay; preference/refusal có trạng thái và không bán bằng tiền. Kiểm cả nhánh cho phép và từ chối: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-029 — Clause acceptance: SH05

Kết quả cần có: Case matrix and evidence for AT-SH05.

Làm sau: P20-03, B00-05.

Kiểm tra: Pet có thể được nhận/né theo mood; không có thoại, tiếng hoặc numeric dashboard; functional error text vẫn rõ. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-030 — Clause acceptance: SH06

Kết quả cần có: Case matrix and evidence for AT-SH06.

Làm sau: P30-02, B00-05.

Kiểm tra: Invitation/tease chung2 attempts và>=30min cooldown; ignore rồi self-play; không drag cursor/window thật. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-031 — Clause acceptance: SH07

Kết quả cần có: Case matrix and evidence for AT-SH07.

Làm sau: P20-04, B00-05.

Kiểm tra: Left props không vượt5; held/in-use không tính; đầy thì cất bằng animation trước thêm; cleanup không instantdelete. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-032 — Clause acceptance: SH08

Kết quả cần có: Case matrix and evidence for AT-SH08.

Làm sau: P20-04, B00-05.

Kiểm tra: Cleanup mood delay không chặn user move/hide; gift dùng food/plush đã có, không thêm economy riêng. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-033 — Clause acceptance: QD01

Kết quả cần có: Case matrix and evidence for AT-QD01.

Làm sau: P10-01, B00-04.

Kiểm tra: Fresh install grants off; read/control độc lập; bật control khi thiếu read bị từ chối không auto grant. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-034 — Clause acceptance: QD02

Kết quả cần có: Case matrix and evidence for AT-QD02.

Làm sau: P40-02, B00-04.

Kiểm tra: List app scan không tự cấp; pasted site được normalize; browser+site grants và subdomain test không substring. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-035 — Clause acceptance: QD03

Kết quả cần có: Case matrix and evidence for AT-QD03.

Làm sau: P50-02, B00-04.

Kiểm tra: New source defaultdeny; switch profile dùng installation grants; archive không apply foreign grants. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-036 — Clause acceptance: QD04

Kết quả cần có: Case matrix and evidence for AT-QD04.

Làm sau: P10-02, B00-04, P30-01.

Kiểm tra: Split-screen chỉ vùng visible+allowed; tab nền/minimized/occluded không cấp nội dung vào consumer. Kiểm cả nhánh cho phép và từ chối: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-037 — Clause acceptance: QD05

Kết quả cần có: Case matrix and evidence for AT-QD05.

Làm sau: P10-03, B00-04.

Kiểm tra: Sentinel vùng cấm/private/secret không vào OCR/model/memory/network; unknown-region chặn nguồn, không chỉ overlay che. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-038 — Clause acceptance: QD06

Kết quả cần có: Case matrix and evidence for AT-QD06.

Làm sau: P10-02, B00-04.

Kiểm tra: Đọc qua UI được phép không account connector; không tự mở thư/tin gây marked-read. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-039 — Clause acceptance: QD07

Kết quả cần có: Case matrix and evidence for AT-QD07.

Làm sau: P00-01, B00-04.

Kiểm tra: Scope kiểm tra không có direct file/folder reader bản đầu; không tạo task parser như chức năng đã duyệt. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-040 — Clause acceptance: QD08

Kết quả cần có: Case matrix and evidence for AT-QD08.

Làm sau: P10-04, B00-04.

Kiểm tra: Fake clipboard history chỉ truy cập khi Win+V open evidence; close mid-flight hủy; không persist/memory. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-041 — Clause acceptance: QD09

Kết quả cần có: Case matrix and evidence for AT-QD09.

Làm sau: P30-04, B00-04.

Kiểm tra: Revocation chặn ngay đường mới; keep/delete memories là quyết định riêng, không chờ quyết định mới revoke. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-042 — Clause acceptance: QD10

Kết quả cần có: Case matrix and evidence for AT-QD10.

Làm sau: P20-02, B00-04.

Kiểm tra: Nguồn chưa read chỉ xuất geometry; consumer sinh hoạt không nhận title/text, không sinh control grant. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-043 — Clause acceptance: QD11

Kết quả cần có: Case matrix and evidence for AT-QD11.

Làm sau: P30-04, B00-04.

Kiểm tra: Document observation chỉ memory name/topic; không detailed summary hoặc raw content trong memory/index. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-044 — Clause acceptance: QD12

Kết quả cần có: Case matrix and evidence for AT-QD12.

Làm sau: P10-06, B00-04.

Kiểm tra: Core life không extension; web enable hướng dẫn install rõ, không tự grant mọi host permissions. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-045 — Clause acceptance: QD13

Kết quả cần có: Case matrix and evidence for AT-QD13.

Làm sau: P10-06, B00-04.

Kiểm tra: Thirdparty player chỉ frame đã cho phép trong parent; ad/frame khác không kế thừa; uncertain phải point+confirm. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-046 — Clause acceptance: QD14

Kết quả cần có: Case matrix and evidence for AT-QD14.

Làm sau: P10-06, B00-04.

Kiểm tra: Frame recognition scoped đúng site; layout/source đổi hỏi lại, không replay tọa độ và không gọi bài học tự động. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-047 — Clause acceptance: QD15

Kết quả cần có: Case matrix and evidence for AT-QD15.

Làm sau: P10-03, B00-04.

Kiểm tra: Unsafe window giữ hold; fix/đổi cửa sổ không tự đọc; explicit retry kiểm mới, unsafe vẫn chặn. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-048 — Clause acceptance: DK01

Kết quả cần có: Case matrix and evidence for AT-DK01.

Làm sau: P10-07, B00-04.

Kiểm tra: Human mouse/key làm yield; injected input không reset idle; sau60s revalidate mới resume. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-049 — Clause acceptance: DK02

Kết quả cần có: Case matrix and evidence for AT-DK02.

Làm sau: P10-07, B00-04.

Kiểm tra: Action allowlist chặn write/delete/send/pay/markread; chỉ search/navigation typing; watchhistory incidental được giữ. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-050 — Clause acceptance: DK03

Kết quả cần có: Case matrix and evidence for AT-DK03.

Làm sau: P10-07, B00-04.

Kiểm tra: Emergency cancels running/pauses pending; observation/body tiếp theo quyền; no60s autoresume; enable+ResumeQueue. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-051 — Clause acceptance: DK04

Kết quả cần có: Case matrix and evidence for AT-DK04.

Làm sau: P10-07, B00-04.

Kiểm tra: ObservationOff/Hide matrix đúng, geometry exception chỉ observationoff; cancelled job không sống lại khi show. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-052 — Clause acceptance: BH01

Kết quả cần có: Case matrix and evidence for AT-BH01.

Làm sau: P40-03, B00-06.

Kiểm tra: Demo bắt đầu do user, cùng app/site; summary đầy đủ và confirm trước lưu; cancel không thành lesson. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-053 — Clause acceptance: BH02

Kết quả cần có: Case matrix and evidence for AT-BH02.

Làm sau: P40-03, B00-06, P40-05.

Kiểm tra: Manage steps/name/enabled/delete/reteach; execution chỉ explicit request ở cả2mode, không auto invoke. Kiểm cả nhánh cho phép và từ chối: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-054 — Clause acceptance: BH03

Kết quả cần có: Case matrix and evidence for AT-BH03.

Làm sau: P40-04, B00-06.

Kiểm tra: Direct request bypass initial60s; mood delay tối đa một lần; secondrequest không bypass grants; pending không bị mất. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-055 — Clause acceptance: BH04

Kết quả cần có: Case matrix and evidence for AT-BH04.

Làm sau: P40-04, B00-06.

Kiểm tra: Human interrupt→60s→reobserve/refocus đúng allowed scope; không replay tọa độ cũ. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-056 — Clause acceptance: BH05

Kết quả cần có: Case matrix and evidence for AT-BH05.

Làm sau: P40-04, B00-06.

Kiểm tra: Missing/mismatched target dừng bước lỗi, nhờ reteach; không blindclick hoặc rerun từ đầu. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-057 — Clause acceptance: BH06

Kết quả cần có: Case matrix and evidence for AT-BH06.

Làm sau: P40-05, B00-06, P02-05, P40-03.

Kiểm tra: Queue nhiều việc có order/cancel; failed job stop riêng; later job chỉ chạy khi đủ prerequisites độc lập. Kiểm cả nhánh cho phép và từ chối: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-058 — Clause acceptance: BH07

Kết quả cần có: Case matrix and evidence for AT-BH07.

Làm sau: P40-05, B00-06.

Kiểm tra: Exit/switch cảnh báo và cancel unfinished; reopen không auto-run; saved lessons vẫn giữ. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-059 — Clause acceptance: BH08

Kết quả cần có: Case matrix and evidence for AT-BH08.

Làm sau: P40-05, B00-06.

Kiểm tra: Re-enable/show chưa resume pending; riêng ResumeQueue mới xét tiếp, cancelled vẫn cancelled. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-060 — Clause acceptance: BH09

Kết quả cần có: Case matrix and evidence for AT-BH09.

Làm sau: P40-05, B00-06.

Kiểm tra: Relationshiphide cùng cancel-running/pause-pending; voluntary return chưa tự chạy. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-061 — Clause acceptance: BH10

Kết quả cần có: Case matrix and evidence for AT-BH10.

Làm sau: P40-05, B00-06.

Kiểm tra: Requested job preempts autonomous discovery nhưng vẫn mood delay1; không tự bỏ quyền để ưu tiên. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-062 — Clause acceptance: BH11

Kết quả cần có: Case matrix and evidence for AT-BH11.

Làm sau: P40-03, B00-06.

Kiểm tra: Search parameter đổi mỗi run, không thay target scope hoặc cho gõ chat/document. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-063 — Clause acceptance: BH12

Kết quả cần có: Case matrix and evidence for AT-BH12.

Làm sau: P40-03, B00-06.

Kiểm tra: Teach review phân biệt first-result và exact-content; selection persists/revalidate, không suy từ x/y. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-064 — Clause acceptance: BH13

Kết quả cần có: Case matrix and evidence for AT-BH13.

Làm sau: P50-05, B00-06.

Kiểm tra: History local cótime/source/action/outcome, no privatepayload/screenshots;30days expiry và userdelete; tách memory. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-065 — Clause acceptance: XP01

Kết quả cần có: Case matrix and evidence for AT-XP01.

Làm sau: P40-06, B00-01.

Kiểm tra: Annotated scene sad/action→biểu cảm phù hợp/intensity có lý do, silent; transition dịu không flicker. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-066 — Clause acceptance: XP02

Kết quả cần có: Case matrix and evidence for AT-XP02.

Làm sau: P03-03, B00-01.

Kiểm tra: Measure display-event→animation-start toàn luồng; report từng mẫu rõ/khó/uncertain và quality, chưa tự đặt pass-rate. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-067 — Clause acceptance: XP03

Kết quả cần có: Case matrix and evidence for AT-XP03.

Làm sau: P30-02, B00-01.

Kiểm tra: Attention chooses safe visible source theo preference/mood, không claim mọi cảnh; wrongscene không cần correctionUI. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-068 — Clause acceptance: XP10

Kết quả cần có: Case matrix and evidence for AT-XP10.

Làm sau: P30-02, B00-01.

Kiểm tra: Capture unavailable không giả hiểu; activity selector cho staywatch hoặc play/eat theo mood. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-069 — Clause acceptance: XP11

Kết quả cần có: Case matrix and evidence for AT-XP11.

Làm sau: P30-05, B00-01.

Kiểm tra: Taste inference chủ yếu theo guuser, only allowed visible evidence; không đọc browserhistory hoặc recordaudio. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-070 — Clause acceptance: XP12

Kết quả cần có: Case matrix and evidence for AT-XP12.

Làm sau: P30-05, B00-01.

Kiểm tra: Self-open content chỉ học gu khi có userreturn/continuedwatch evidence, không tính unattended runtime. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-071 — Clause acceptance: XP13

Kết quả cần có: Case matrix and evidence for AT-XP13.

Làm sau: P30-05, B00-01.

Kiểm tra: Movie>=20min hoặc musicrepeat/similarsongs là tín hiệu, chưa chắc thích; không gom với neglecttimer. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-072 — Clause acceptance: XP14

Kết quả cần có: Case matrix and evidence for AT-XP14.

Làm sau: P30-05, B00-01.

Kiểm tra: User contentchange khác autoplay/agentinput; không thêm nút xác nhận hoặc camera theo dõi hiện diện. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-073 — Clause acceptance: XP15

Kết quả cần có: Case matrix and evidence for AT-XP15.

Làm sau: P40-07, B00-01.

Kiểm tra: Autonomous media dùng own tab, giữ existing user tabs và nội dung của chúng. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-074 — Clause acceptance: XP16

Kết quả cần có: Case matrix and evidence for AT-XP16.

Làm sau: P40-02, B00-01.

Kiểm tra: Chosen browser setting quyết định Chrome/Edge cho automedia; grants vẫn phải đủ. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-075 — Clause acceptance: XP09

Kết quả cần có: Case matrix and evidence for AT-XP09.

Làm sau: P20-04, B00-01.

Kiểm tra: Không tự yêu cầu né subtitles; user move avatar/sofa được, không điều hướng phim để dọn vị trí. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-076 — Clause acceptance: XP04

Kết quả cần có: Case matrix and evidence for AT-XP04.

Làm sau: P40-06, B00-01.

Kiểm tra: Usermedia không tự pause/scroll/refocus; next chỉ khi ended và target chắc; uncertain không click. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-077 — Clause acceptance: XP05

Kết quả cần có: Case matrix and evidence for AT-XP05.

Làm sau: P40-07, B00-01.

Kiểm tra: Advanced idledefault5m+nomedia mới autoopen; userreturn giữ playback/yield control, fullscreen không active evidence. Kiểm cả nhánh cho phép và từ chối: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-078 — Clause acceptance: XP06

Kết quả cần có: Case matrix and evidence for AT-XP06.

Làm sau: P40-07, B00-01.

Kiểm tra: YouTube search free trong grants; other site phải explicit allow, không tự nhớ mọi visitedsite thành grant. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-079 — Clause acceptance: XP07

Kết quả cần có: Case matrix and evidence for AT-XP07.

Làm sau: P40-07, B00-01.

Kiểm tra: Ambiguous adtab giữ/quay về phim; login/pay/verify skip; max3 candidates per session, không click download/install/notify. Kiểm cả nhánh cho phép và từ chối: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-080 — Clause acceptance: XP08

Kết quả cần có: Case matrix and evidence for AT-XP08.

Làm sau: P10-07, B00-01, P40-07.

Kiểm tra: Locked noopen; unlocked có thể tiếp nếu chờ đã đủ; unlock event riêng không reset, desktopinput kế reset. Kiểm cả nhánh cho phép và từ chối: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-081 — Clause acceptance: AI01

Kết quả cần có: Case matrix and evidence for AT-AI01.

Làm sau: P03-01, B00-03, P40-07.

Kiểm tra: Không mic/camera/audio-analysis/dancebeat; playback bình thường không bị gọi là cô ấy nghe hiểu. Kiểm cả nhánh cho phép và từ chối: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-082 — Clause acceptance: AI02

Kết quả cần có: Case matrix and evidence for AT-AI02.

Làm sau: P10-05, B00-03.

Kiểm tra: Explicit request→preview sanitized text→confirm mỗi send; deny vẫn local; không image/audio/file/memory upload. Kiểm cả nhánh cho phép và từ chối: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-083 — Clause acceptance: AI03

Kết quả cần có: Case matrix and evidence for AT-AI03.

Làm sau: P03-02, B00-03.

Kiểm tra: Local inference measured với renderer cùng chạy; nhẹ không đồng nghĩa đã đạt subsecond; no silent cloud fallback. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-084 — Clause acceptance: KN01

Kết quả cần có: Case matrix and evidence for AT-KN01.

Làm sau: P30-04, B00-05.

Kiểm tra: Inspect/edit/delete/pin từngmemory, importance fade theo reinforcement; pinned không tựfade; no forbidden payload. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-085 — Clause acceptance: KN02

Kết quả cần có: Case matrix and evidence for AT-KN02.

Làm sau: P30-04, B00-05.

Kiểm tra: Edit không relationrecalc; naturalfade giữ closeness; explicitdelete contribution adjust đúng một lần. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-086 — Clause acceptance: QH01

Kết quả cần có: Case matrix and evidence for AT-QH01.

Làm sau: P30-03, B00-05.

Kiểm tra: Friends default; optinadvanced romance không instantpartner; behaviors trong ranh giới không sexualfeature. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-087 — Clause acceptance: QH02

Kết quả cần có: Case matrix and evidence for AT-QH02.

Làm sau: P30-06, B00-05.

Kiểm tra: Romanceoff choosekeep/delete; retainedmemory buồntạm không pressure/re-enable. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-088 — Clause acceptance: QH03

Kết quả cần có: Case matrix and evidence for AT-QH03.

Làm sau: P30-03, B00-05.

Kiểm tra: Neglect activeadvancedvisible only, freeze/off/basic/sleep/idle excluded; không calendar3days. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-089 — Clause acceptance: QH04

Kết quả cần có: Case matrix and evidence for AT-QH04.

Làm sau: P30-03, B00-05.

Kiểm tra: Trust→threshold gần72h, hurt gần48h; intentionalclick/pet/feed ngắtstreak nhưng sadness không resetinstant. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-090 — Clause acceptance: QH05

Kết quả cần có: Case matrix and evidence for AT-QH05.

Làm sau: P30-03, B00-05.

Kiểm tra: Sad→withdraw progression; severerepair qua nhiềusessions+care, offlinecooling allowed; gifts không instantfix. Kiểm cả nhánh cho phép và từ chối: Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không là buổi mới. Không tự đặt số phút/số buổi hoặc quà lập tức xóa tổn thương. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-091 — Clause acceptance: QH06

Kết quả cần có: Case matrix and evidence for AT-QH06.

Làm sau: P30-03, B00-05.

Kiểm tra: Firstthrow startle/no lastinghurt; repeatedafterprotest refuse lift nhưng pet/feed; readinesssignal before liftreturn. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-092 — Clause acceptance: QH07

Kết quả cần có: Case matrix and evidence for AT-QH07.

Làm sau: P30-03, B00-05.

Kiểm tra: Selfhide shutsread/control; invite/leavegift accessible withoutavatar, can decline, reset/settings remain reachable. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-093 — Clause acceptance: HS01

Kết quả cần có: Case matrix and evidence for AT-HS01.

Làm sau: P50-02, B00-07.

Kiểm tra: Import thêmprofile khôngmerge/createbutton; activeone; inactive state/clocks frozen until selected. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-094 — Clause acceptance: HS02

Kết quả cần có: Case matrix and evidence for AT-HS02.

Làm sau: P50-02, B00-07.

Kiểm tra: All profiles dùng machinegrants, importedprofile không áp importedpermissions. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-095 — Clause acceptance: HS03

Kết quả cần có: Case matrix and evidence for AT-HS03.

Làm sau: P50-02, B00-07.

Kiểm tra: Reset active memories/relation/state/lessons, preserveotherprofiles và installationgrants. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-096 — Clause acceptance: SL01

Kết quả cần có: Case matrix and evidence for AT-SL01.

Làm sau: P50-03, B00-07.

Kiểm tra: Export only useraction; no autoarchive/recoverybackup; keys excluded; reconnect AI onnewmachine. Kiểm cả nhánh cho phép và từ chối: Sao lưu không kèm gói AI nâng cao; máy mới tải lại khi cần, không thêm tùy chọn kèm gói mỗi lần xuất. Giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-097 — Clause acceptance: SL02

Kết quả cần có: Case matrix and evidence for AT-SL02.

Làm sau: P50-03, B00-07.

Kiểm tra: Passwordrequired perexport + separatelyheldrecoverycode; both correct paths open authenticateddata, bad creds reject. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-098 — Clause acceptance: CD01

Kết quả cần có: Case matrix and evidence for AT-CD01.

Làm sau: P50-06, B00-07, P40-05, P50-01.

Kiểm tra: Firstsetup hỏi startup choice; normalstate persistence works and distinctfrombackup. Kiểm cả nhánh cho phép và từ chối: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-099 — Clause acceptance: CD02

Kết quả cần có: Case matrix and evidence for AT-CD02.

Làm sau: P50-07, B00-07.

Kiểm tra: Check/download ownupdate, confirm beforeinstall/restart; no otherappupdate. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-100 — Clause acceptance: CD03

Kết quả cần có: Case matrix and evidence for AT-CD03.

Làm sau: P50-08, B00-07.

Kiểm tra: Uninstall choosekeep/delete và reminder export; không hunt/delete unrelated exported archives. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-101 — Clause acceptance: MODE01

Kết quả cần có: Case matrix and evidence for AT-MODE01.

Làm sau: P60-02, B00-01.

Kiểm tra: Chạy cùng kịch bản sinh hoạt ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-102 — Clause acceptance: MODE02

Kết quả cần có: Case matrix and evidence for AT-MODE02.

Làm sau: P60-02, B00-01.

Kiểm tra: Chạy cùng kịch bản sở thích bằng hoạt ảnh ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-103 — Clause acceptance: MODE03

Kết quả cần có: Case matrix and evidence for AT-MODE03.

Làm sau: P60-02, B00-01.

Kiểm tra: Chạy cùng kịch bản nội dung sách/tranh/game ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-104 — Clause acceptance: MODE04

Kết quả cần có: Case matrix and evidence for AT-MODE04.

Làm sau: P60-02, B00-01.

Kiểm tra: Chạy cùng kịch bản hiểu màn hình ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-105 — Clause acceptance: MODE05

Kết quả cần có: Case matrix and evidence for AT-MODE05.

Làm sau: P60-02, B00-01.

Kiểm tra: Chạy cùng kịch bản điều khiển ứng dụng ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-106 — Clause acceptance: MODE06

Kết quả cần có: Case matrix and evidence for AT-MODE06.

Làm sau: P60-02, B00-01.

Kiểm tra: Chạy cùng kịch bản tự mở phim/nhạc ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-107 — Clause acceptance: MODE07

Kết quả cần có: Case matrix and evidence for AT-MODE07.

Làm sau: P60-02, B00-01.

Kiểm tra: Chạy cùng kịch bản cảm xúc/quan hệ ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-108 — Clause acceptance: MODE08

Kết quả cần có: Case matrix and evidence for AT-MODE08.

Làm sau: P60-02, B00-01.

Kiểm tra: Chạy cùng kịch bản phát triển tính cách ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## V00-109 — Clause acceptance: MODE09

Kết quả cần có: Case matrix and evidence for AT-MODE09.

Làm sau: P60-02, B00-01.

Kiểm tra: Chạy cùng kịch bản mất internet ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

[Thẻ đầy đủ](../../../tasks/phase-v00.md). Chưa chạy/chưa nghiệm thu.

## N00-01 — Authorization at use time, no forbidden data to consumers

Kết quả cần có: Measured evidence: NFR-01.

Làm sau: P10-03, B00-01.

Kiểm tra: Authorization at use time, no forbidden data to consumers; Mandatory deny invariants; universal detection not proven; use E02 + IT-01/02/03. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result. Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

[Thẻ đầy đủ](../../../tasks/phase-n00.md). Chưa chạy/chưa nghiệm thu.

## N00-02 — Reaction latency measured end-to-end under actual combined load

Kết quả cần có: Measured evidence: NFR-02.

Làm sau: P03-03, B00-01.

Kiểm tra: Reaction latency measured end-to-end under actual combined load; XP02 target<1s clear attended scenes; pass-rate/accuracy open D-04; use E04 + IT-10. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result. Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

[Thẻ đầy đủ](../../../tasks/phase-n00.md). Chưa chạy/chưa nghiệm thu.

## N00-03 — Stability with both modes and daily-use mix

Kết quả cần có: Measured evidence: NFR-03.

Làm sau: P60-03, B00-01.

Kiểm tra: Stability with both modes and daily-use mix; About8h required; CPU/RAM/VRAM budgets open D-04; use E05 + IT-19. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result. Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

[Thẻ đầy đủ](../../../tasks/phase-n00.md). Chưa chạy/chưa nghiệm thu.

## N00-04 — Core/local content offline after packages installed

Kết quả cần có: Measured evidence: NFR-04.

Làm sau: P60-03, B00-01.

Kiểm tra: Core/local content offline after packages installed; No silent network/cloud dependency; use IT-11. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result. Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

[Thẻ đầy đủ](../../../tasks/phase-n00.md). Chưa chạy/chưa nghiệm thu.

## N00-05 — Durable local state and authenticated export/import

Kết quả cần có: Measured evidence: NFR-05.

Làm sau: P50-04, B00-01.

Kiểm tra: Durable local state and authenticated export/import; No corruption/data loss in defined recovery cases; format/crypto open D-07/09; use IT-14/15. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result. Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

[Thẻ đầy đủ](../../../tasks/phase-n00.md). Chưa chạy/chưa nghiệm thu.

## N00-06 — Clear accessible UI and retained input priority

Kết quả cần có: Measured evidence: NFR-06.

Làm sau: P40-01, B00-01.

Kiểm tra: Clear accessible UI and retained input priority; Vietnamese, focus and cancel semantics; native accessibility matrix to measure; use IT-06/20. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result. Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

[Thẻ đầy đủ](../../../tasks/phase-n00.md). Chưa chạy/chưa nghiệm thu.

## N00-07 — Maintainable module boundaries and reproducible builds

Kết quả cần có: Measured evidence: NFR-07.

Làm sau: P00-02, B00-01.

Kiểm tra: Maintainable module boundaries and reproducible builds; Pinned real versions, no suppressions to hide failure; CI not installed; use P00-02/P60-02. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result. Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

[Thẻ đầy đủ](../../../tasks/phase-n00.md). Chưa chạy/chưa nghiệm thu.

## N00-08 — Trustworthy installs/updates and explicit costs

Kết quả cần có: Measured evidence: NFR-08.

Làm sau: P50-07, B00-01.

Kiểm tra: Trustworthy installs/updates and explicit costs; Signature/distribution choice open D-13; user consent before install/restart; use IT-16. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result. Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

[Thẻ đầy đủ](../../../tasks/phase-n00.md). Chưa chạy/chưa nghiệm thu.

## N00-09 — Minimal local diagnostic data

Kết quả cần có: Measured evidence: NFR-09.

Làm sau: P50-05, B00-01.

Kiểm tra: Minimal local diagnostic data; BH13 retention30days, no secrets/raw screen, no auto telemetry; use IT-17. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result. Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

[Thẻ đầy đủ](../../../tasks/phase-n00.md). Chưa chạy/chưa nghiệm thu.

## N00-10 — Correct coordinates and visuals across chosen monitors/DPI

Kết quả cần có: Measured evidence: NFR-10.

Làm sau: P20-05, B00-01.

Kiểm tra: Correct coordinates and visuals across chosen monitors/DPI; No assumed universal fullscreen; support matrix after E-INT; use IT-04/05. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result. Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

[Thẻ đầy đủ](../../../tasks/phase-n00.md). Chưa chạy/chưa nghiệm thu.

## C00-01 — Baseline checkpoint

Kết quả cần có: Baseline evidence checkpoint.

Làm sau: P00-01, P00-02, P00-03, P00-04.

Kiểm tra: Every listed predecessor has actual accepted evidence at its recorded revision; missing, failed or NOT RUN evidence blocks this checkpoint. Record exact local revision, unresolved limitations and required user acceptance separately; this checkpoint grants no publishing or production authorization.

[Thẻ đầy đủ](../../../tasks/phase-c00.md). Chưa chạy/chưa nghiệm thu.

## C00-02 — Probes checkpoint

Kết quả cần có: Probes evidence checkpoint.

Làm sau: P01-01, P02-05, P03-03.

Kiểm tra: Every listed predecessor has actual accepted evidence at its recorded revision; missing, failed or NOT RUN evidence blocks this checkpoint. Record exact local revision, unresolved limitations and required user acceptance separately; this checkpoint grants no publishing or production authorization.

[Thẻ đầy đủ](../../../tasks/phase-c00.md). Chưa chạy/chưa nghiệm thu.

## C00-03 — Integrated slice checkpoint

Kết quả cần có: Integrated slice evidence checkpoint.

Làm sau: P60-01.

Kiểm tra: Every listed predecessor has actual accepted evidence at its recorded revision; missing, failed or NOT RUN evidence blocks this checkpoint. Record exact local revision, unresolved limitations and required user acceptance separately; this checkpoint grants no publishing or production authorization.

[Thẻ đầy đủ](../../../tasks/phase-c00.md). Chưa chạy/chưa nghiệm thu.

## C00-04 — Full acceptance checkpoint

Kết quả cần có: Full acceptance evidence checkpoint.

Làm sau: V00-001, V00-002, V00-003, V00-004, V00-005, V00-006, V00-007, V00-008, V00-009, V00-010, V00-011, V00-012, V00-013, V00-014, V00-015, V00-016, V00-017, V00-018, V00-019, V00-020, V00-021, V00-022, V00-023, V00-024, V00-025, V00-026, V00-027, V00-028, V00-029, V00-030, V00-031, V00-032, V00-033, V00-034, V00-035, V00-036, V00-037, V00-038, V00-039, V00-040, V00-041, V00-042, V00-043, V00-044, V00-045, V00-046, V00-047, V00-048, V00-049, V00-050, V00-051, V00-052, V00-053, V00-054, V00-055, V00-056, V00-057, V00-058, V00-059, V00-060, V00-061, V00-062, V00-063, V00-064, V00-065, V00-066, V00-067, V00-068, V00-069, V00-070, V00-071, V00-072, V00-073, V00-074, V00-075, V00-076, V00-077, V00-078, V00-079, V00-080, V00-081, V00-082, V00-083, V00-084, V00-085, V00-086, V00-087, V00-088, V00-089, V00-090, V00-091, V00-092, V00-093, V00-094, V00-095, V00-096, V00-097, V00-098, V00-099, V00-100, V00-101, V00-102, V00-103, V00-104, V00-105, V00-106, V00-107, V00-108, V00-109, N00-01, N00-02, N00-03, N00-04, N00-05, N00-06, N00-07, N00-08, N00-09, N00-10.

Kiểm tra: Every listed predecessor has actual accepted evidence at its recorded revision; missing, failed or NOT RUN evidence blocks this checkpoint. Record exact local revision, unresolved limitations and required user acceptance separately; this checkpoint grants no publishing or production authorization.

[Thẻ đầy đủ](../../../tasks/phase-c00.md). Chưa chạy/chưa nghiệm thu.

## C00-05 — Release review checkpoint

Kết quả cần có: Release review evidence checkpoint.

Làm sau: C00-04, P60-04, P60-05, C00-01, C00-02, C00-03.

Kiểm tra: Every listed predecessor has actual accepted evidence at its recorded revision; missing, failed or NOT RUN evidence blocks this checkpoint. Record exact local revision, unresolved limitations and required user acceptance separately; this checkpoint grants no publishing or production authorization.

[Thẻ đầy đủ](../../../tasks/phase-c00.md). Chưa chạy/chưa nghiệm thu.
