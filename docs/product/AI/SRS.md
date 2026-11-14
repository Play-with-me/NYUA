# Software Requirements Specification — toàn sản phẩm

Version0.1 — reconciled 2026-11-14. Baseline để rà, không chứng nhận tiêu chuẩn và không tự phê duyệt implementation.

## 1. Purpose, scope, environment

Windows11, Vietnamese first, free initial public release, local data/no account. Companion combines life, perception and embodied interaction. Unity renderer + C#/WPF host + local AI is directional choice; physical architecture/model pending proof. Non-goals and mode matrix are source requirements, not optional defaults.

## 2. Definitions and precedence

Source IDs retain original meaning; SRS- prefix gives dossier key; AT- is acceptance proposal. Source user decisions win over technical draft. Modules mapped in CAPABILITY_MAP. Content-read, geometry-read, control, memory and external-send are distinct authorities. See BUSINESS_RULES and DECISIONS before resolving conflicts.

## 3. Interfaces and constraints

User interfaces in UX.md; provider contracts INTERFACES.md; data DATA.md; privacy SECURITY.md; timing/quality AI_LOCAL.md and QA.md. Unsupported or uncertain sources must fail closed; no raw-content fallback to cloud.

## 4. Functional and scope requirements

Source text below is preserved. Compound source rules remain grouped for provenance; acceptance tests must split all independently testable clauses before implementation. No clause may be dropped because its source shares an ID.

### SRS-SP01

- Source: SP01 (explicit_id); scope: release1.
- Requirement: Tạo cảm giác một người bạn có cá tính sống trên máy: hoạt bát, tò mò, tinh nghịch, tự chọn hoạt động theo nhu cầu, tâm trạng, sở thích và ký ức; có thể đổi ý có lý do. Không phải cam kết có ý thức thật.
- Owner: `companion`; use case: UC-01; task proposal: P30-02.
- AT-SP01: Qua kịch bản chăm sóc, nghỉ và thay đổi chú ý, quyết định hoạt động có nguyên nhân từ trạng thái; không chỉ lặp một playlist hoạt ảnh.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SP02

- Source: SP02 (explicit_id); scope: release1.
- Requirement: Bản dùng thử có ý nghĩa phải kết hợp sinh hoạt/ghi nhớ, hiểu màn hình và chuyển động/tương tác tự nhiên. Chỉ hoạt ảnh đi lại chưa đủ.
- Owner: `companion`; use case: UC-01; task proposal: P60-01.
- AT-SP02: Dùng thử một luồng kết hợp sinh hoạt, ghi nhớ, hiểu ngữ cảnh và chuyển động; từng demo riêng không thay nghiệm thu luồng kết hợp.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SP03

- Source: SP03 (explicit_id); scope: release1.
- Requirement: Phát hành công khai cho nhiều người trên Windows 11, giao diện tiếng Việt và thị trường Việt Nam trước; quốc tế để sau. Miễn phí bản đầu; chỉ phát hành ứng dụng, chưa công khai mã nguồn.
- Owner: `companion`; use case: UC-18; task proposal: P50-06.
- AT-SP03: Cài/chạy bản tiếng Việt trên Windows11; checklist phát hành ghi miễn phí bản đầu và không công khai source; chưa suy ra hỗ trợ OS khác.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SP04

- Source: SP04 (explicit_id); scope: release1.
- Requirement: Không tài khoản riêng của ứng dụng; dữ liệu trên máy. Người dùng tự kết nối và trả chi phí AI ngoài nếu dùng.
- Owner: `companion`; use case: UC-01; task proposal: P40-01.
- AT-SP04: Cài mới dùng được không đăng ký; kiểm data local và dịch vụ AI ngoài chỉ dùng thông tin kết nối người dùng cung cấp.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SP05

- Source: SP05 (explicit_id); scope: release1.
- Requirement: Không hạn phát hành cố định. Cả cơ bản và nâng cao phải ổn định trước phát hành công khai; có thể kiểm chứng bằng bản thử nội bộ trước.
- Owner: `companion`; use case: UC-18; task proposal: P60-03.
- AT-SP05: Không đóng cổng phát hành nếu một trong hai mức chưa đạt tiêu chí; bản nội bộ được dán nhãn khác bản công khai.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SP06

- Source: SP06 (explicit_id); scope: release1.
- Requirement: Ưu tiên công cụ/dịch vụ miễn phí; mọi khoản chi phát triển phải hỏi trước. Chưa có ngân sách số cụ thể hoặc quyền tự chi.
- Owner: `companion`; use case: UC-18; task proposal: P00-04.
- AT-SP06: Danh mục công cụ ghi chi phí/giấy phép; khoản phí không được mua hoặc kích hoạt khi chưa có quyết định người dùng.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SP07

- Source: SP07 (explicit_id); scope: release1.
- Requirement: Ở nâng cao, tính cách phát triển qua trải nghiệm/cách đối xử: từ làm trước nghĩ sau dần biết cân nhắc. Luôn giữ tò mò, tinh nghịch và ý muốn riêng; thay đổi cách thể hiện, không xóa các nét cốt lõi này. Cơ bản giữ tính cách ban đầu, vẫn đổi tâm trạng. Không phải quyền tự sửa code.
- Owner: `companion`; use case: UC-05; task proposal: P30-06.
- AT-SP07: Cùng trải nghiệm qua thời gian tạo cách biểu hiện cân nhắc hơn ở nâng cao; vẫn có tò mò/tinh nghịch/ý muốn riêng, cơ bản không tiến hóa tính cách.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SP08

- Source: SP08 (explicit_id); scope: release1.
- Requirement: Học cách hành xử qua tương tác và trải nghiệm, không thêm nút đánh giá hành vi. Không tự đánh đồng người dùng bận/không đáp lời rủ với phê bình; chế độ làm mẫu thao tác ứng dụng vẫn là chức năng riêng.
- Owner: `companion`; use case: UC-05; task proposal: P30-02.
- AT-SP08: Không có nút đánh giá hành vi; bỏ qua lời rủ không thành lời phê bình; learning-demo chỉ ghi khi user bật.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SP09

- Source: SP09 (explicit_id); scope: release1.
- Requirement: Hướng đã thống nhất để tiếp tục: Unity phụ trách hiển thị/hoạt ảnh nhân vật; C# + WPF phụ trách phần ứng dụng, điều phối và quản lý; AI local phân tích ngữ cảnh/cảm xúc. Phiên bản, cách kết nối, topology tiến trình, hiệu năng và độ tin cậy còn cần thiết kế/kiểm chứng. Không xây giao diện sản phẩm bằng web theo đề xuất cũ. Quyết định 2026-11-14 D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở.
- Owner: `companion`; use case: UC-01; task proposal: P00-02.
- AT-SP09: Rà phân công Unity/host/WPF/localAI; không đưa web UI làm nền sản phẩm hoặc coi IPC/model đã chứng minh từ sơ đồ. Kiểm cả nhánh cho phép và từ chối: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-NV01

- Source: NV01 (explicit_id); scope: release1.
- Requirement: Nữ trưởng thành kiểu chibi, đầu lớn người nhỏ, phong cách anime đời thường. Một mẫu ngoại hình trong bản đầu cho mọi người dùng. Quyết định 2026-11-14 D-14: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật.
- Owner: `desktop-body`; use case: UC-03; task proposal: P20-01.
- AT-NV01: Duyệt mẫu nữ trưởng thành chibi đầu lớn người nhỏ; cài mới các user có cùng ngoại hình đã duyệt. Kiểm cả nhánh cho phép và từ chối: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-NV02

- Source: NV02 (explicit_id); scope: release1.
- Requirement: Tóc trắng bạc buông ngang eo, mái thưa ngang trán; mắt đỏ hồng; da sáng tông ấm. Quyết định 2026-11-14 D-14: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt.
- Owner: `desktop-body`; use case: UC-03; task proposal: P20-01.
- AT-NV02: So mẫu front/side với tóc bạc ngang eo, mái thưa, mắt đỏ hồng và da sáng ấm; ghi sửa nếu lệch. Kiểm cả nhánh cho phép và từ chối: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-NV03

- Source: NV03 (explicit_id); scope: release1.
- Requirement: Áo len rộng cổ tròn hồng nhạt; chân váy xếp ly xám đậm trên gối; chân trần, không tất/giày.
- Owner: `desktop-body`; use case: UC-03; task proposal: P20-01.
- AT-NV03: Kiểm áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, không tất/giày ở mọi hướng.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-NV04

- Source: NV04 (explicit_id); scope: release1.
- Requirement: Kẹp tóc nhỏ hình trái tim đỏ rượu ở bên phải nhân vật, tức phía trái khi nhìn chính diện. Nét mặt thường ngày cười tươi, nhiều năng lượng.
- Owner: `desktop-body`; use case: UC-03; task proposal: P20-01.
- AT-NV04: Front view kẹp ở trái ảnh, thuộc bên phải nhân vật; sprite lật không làm sai bên giải phẫu; nét thường ngày tươi.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-NV05

- Source: NV05 (explicit_id); scope: release1.
- Requirement: Ảnh gốc pixel 128×128; giữ nét pixel, chuyển động mượt mềm mại. Chưa chốt số khung hình, nguồn ảnh hoặc kỹ thuật tạo hoạt ảnh.
- Owner: `desktop-body`; use case: UC-03; task proposal: P20-02.
- AT-NV05: Kiểm asset nguồn128x128 và chuyển động ở nhiều tỉ lệ; không kết luận mượt chỉ từ kích thước file.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-NV06

- Source: NV06 (explicit_id); scope: release1.
- Requirement: Thanh kéo kích thước tự do 64×64–384×384; ban đầu 128×128, nhớ kích thước người dùng chỉnh. Người dùng tự đặt tên khi mở lần đầu.
- Owner: `desktop-body`; use case: UC-01; task proposal: P40-01.
- AT-NV06: Lần đầu128; kéo64–384; mở lại giữ lựa chọn; đặt tên qua onboarding. Giới hạn ký tự cần quyết định riêng.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-NV07

- Source: NV07 (explicit_id); scope: release1.
- Requirement: Sống tự do trên desktop, đi/leo/ngồi trên cạnh cửa sổ. Theo cửa sổ khi di chuyển; mất chỗ đứng vì cửa sổ đóng/thu nhỏ thì rơi xuống bề mặt bên dưới, đứng dậy.
- Owner: `desktop-body`; use case: UC-03; task proposal: P20-02.
- AT-NV07: Di chuyển/thu nhỏ/đóng cửa sổ đang làm bề mặt: theo cửa sổ hoặc rơi đúng bề mặt kế tiếp, không đứng lơ lửng.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-NV08

- Source: NV08 (explicit_id); scope: release1.
- Requirement: Người dùng chọn các màn hình được xuất hiện; nhân vật tự qua lại trong phạm vi đó. Toàn màn hình vẫn hiện sát mép, tránh vùng giữa.
- Owner: `desktop-body`; use case: UC-03; task proposal: P20-05.
- AT-NV08: Chỉ xuất hiện trên monitor cho phép; fullscreen ở mép; ghi rõ trường hợp exclusive không hỗ trợ sau thử, không tự hứa mọi game.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-NV09

- Source: NV09 (explicit_id); scope: release1.
- Requirement: Bấm trái nhận biểu cảm/cử chỉ; rê qua đầu nhiều lần để vuốt; giữ kéo để nhấc. Kéo nhẹ đổi chỗ; kéo nhanh thả bay theo đà; thả giữa khoảng trống thì rơi.
- Owner: `desktop-body`; use case: UC-03; task proposal: P20-03.
- AT-NV09: Phân biệt click/pet/hold-drag/slow-release/fast-release; quăng có đà và rơi/đứng dậy; ngưỡng đo trước chốt.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-NV10

- Source: NV10 (explicit_id); scope: release1.
- Requirement: Để bấm nút thật phải đến vị trí nút trước, chấp nhận thời gian di chuyển; dùng thang/dụng cụ ảo khi thiếu chỗ tiếp cận. Khi gõ thật có hoạt ảnh bàn phím nhỏ trên tay.
- Owner: `desktop-body`; use case: UC-08; task proposal: P40-04.
- AT-NV10: Input thật chỉ xảy ra sau body approach và revalidate; có dụng cụ ảo khi thiếu bề mặt và bàn phím ảo lúc gõ.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-NV11

- Source: NV11 (explicit_id); scope: release1.
- Requirement: Giữ một phím rồi kéo là chế độ chuyển vị trí, dùng được cả khi cô ấy đang từ chối cho nhấc; không tính chơi/quăng hoặc làm xấu quan hệ. Phím đã chốt là Shift. Quyết định 2026-11-14 D-05: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo.
- Owner: `desktop-body`; use case: UC-03; task proposal: P20-03.
- AT-NV11: Modifier-drag di chuyển ngay cả refusal-lift, không quăng và không giảm relation; phím Shift đã chốt, không thêm tùy chọn phím. Kiểm cả nhánh cho phép và từ chối: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MC01

- Source: MC01 (explicit_id); scope: release1.
- Requirement: cài bản nhẹ trước; chỉ tải gói nâng cao khi người dùng chọn. Dung lượng và yêu cầu máy phải được khảo sát trước khi công bố.
- Owner: `companion`; use case: UC-02; task proposal: P03-04.
- AT-MC01: Cài mới không tải gói nâng cao ngầm; user chọn mới tải, lỗi tải không báo gói đã sẵn sàng.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MC02

- Source: MC02 (explicit_id); scope: release1.
- Requirement: máy chưa đạt cấu hình đã kiểm chứng vẫn được bật thử sau cảnh báo rõ; không tự đổi mức. Khi nâng cao làm máy chậm/nóng thì báo và hỏi giảm mức hay tiếp tục.
- Owner: `companion`; use case: UC-02; task proposal: P03-04.
- AT-MC02: Máy yếu vẫn có lựa chọn thử sau cảnh báo; simulated overload hỏi giảm/tiếp tục và không đổi mode tự động.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MC03

- Source: MC03 (explicit_id); scope: release1.
- Requirement: hạ về cơ bản giữ ký ức/quan hệ và phần tính cách đã phát triển, tạm ngừng biểu hiện nâng cao. Bật lại tiếp nối tính cách đã phát triển, không bắt đầu từ đầu. Tương tác ở cơ bản vẫn duy trì quan hệ; thiếu tương tác ở cơ bản không làm giảm quan hệ sâu.
- Owner: `companion`; use case: UC-02; task proposal: P30-06.
- AT-MC03: Nâng cao→cơ bản→nâng cao bảo toàn memory/relation/personality; cơ bản không tích lũy neglect sâu.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MC04

- Source: MC04 (explicit_id); scope: release1.
- Requirement: kiểm tra cấu hình máy người dùng để đề xuất mức cơ bản/nâng cao phù hợp với AI cục bộ. Cách xếp mức và cấu hình tối thiểu cần dựa vào phép đo; không chỉ tên GPU. Giữ quyền chọn/bật thử sau cảnh báo và không tự đổi mức theo MC02.
- Owner: `companion`; use case: UC-02; task proposal: P03-04.
- AT-MC04: Recommendation có dựa measured workload/hardware capability; user override được; không chỉ dựa tên GPU.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SH01

- Source: SH01 (explicit_id); scope: release1.
- Requirement: ngủ theo giờ trong ngày và mức mệt, có ngủ trưa. Mở máy có thể ngái ngủ, chào rồi ngủ tiếp hoặc thức. Bấm lúc ngủ có thể hé mắt, trở mình hoặc thức tùy mệt. Quyết định 2026-11-14 D-12: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại.
- Owner: `life-state`; use case: UC-05; task proposal: P30-01.
- AT-SH01: Test logical clock/click khi ngủ: phản ứng tùy fatigue, nhịp có naps; chưa tự đặt sleep schedule cố định. Kiểm cả nhánh cho phép và từ chối: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SH02

- Source: SH02 (explicit_id); scope: release1.
- Requirement: người dùng cho ăn/vuốt, cô ấy tự nghỉ. Khi vắng mặt hoặc app đóng, không bệnh/mất tiến độ; có thể hơi đói/nhớ, tự có đồ dự phòng khi hoạt động.
- Owner: `life-state`; use case: UC-04; task proposal: P30-01.
- AT-SH02: Bận/vắng không disease/progress-loss; khi hoạt động có reserve food; không yêu cầu chăm như nghĩa vụ liên tục.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SH03

- Source: SH03 (explicit_id); scope: release1.
- Requirement: đóng app/tắt máy không mô phỏng sự kiện, không tự kể đã làm gì. Mở lại tính thời gian đã qua để cập nhật trạng thái; nguôi giận có tính thời gian app đóng, không tạo tương tác giả.
- Owner: `life-state`; use case: UC-05; task proposal: P30-01.
- AT-SH03: Reopen cập nhật elapsed state nhưng không thêm fake memories/events; inactive profile dùng freeze khác appclose.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SH04

- Source: SH04 (explicit_id); scope: release1.
- Requirement: 6 món miễn phí không giới hạn: cơm nắm, mì; trái cây, bắp ngô; sữa, nước trái cây. Chọn riêng để ghép bữa; kéo từng món hoặc cả khay. Có món thích/không thích, đôi khi từ chối, người dùng khám phá qua phản ứng. Quyết định 2026-11-14 D-14/H08: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt.
- Owner: `life-state`; use case: UC-04; task proposal: P20-04.
- AT-SH04: Đủ6 món miễn phí, chọn ghép bữa, kéo lẻ/cả khay; preference/refusal có trạng thái và không bán bằng tiền. Kiểm cả nhánh cho phép và từ chối: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SH05

- Source: SH05 (explicit_id); scope: release1.
- Requirement: thường thích vuốt nhưng có thể né/ra dấu đủ rồi. Biểu đạt bằng cử chỉ, nét mặt, biểu tượng nhỏ; không lời thoại/chữ sinh hoạt, không tiếng; không bảng chỉ số đói/mệt/thân thiết. Thông báo chức năng vẫn có chữ.
- Owner: `life-state`; use case: UC-03; task proposal: P20-03.
- AT-SH05: Pet có thể được nhận/né theo mood; không có thoại, tiếng hoặc numeric dashboard; functional error text vẫn rõ.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SH06

- Source: SH06 (explicit_id); scope: release1.
- Requirement: rủ chơi/gây chú ý có thể ghé con trỏ, thò đầu hoặc ôm con trỏ bằng hoạt ảnh. Không kéo chuột thật/chuyển cửa sổ để nghịch. Hai lần không đáp thì tự chơi và chờ ít nhất 30 phút; trò nghịch và rủ dùng chung giới hạn. Không thêm chế độ tập trung riêng.
- Owner: `life-state`; use case: UC-05; task proposal: P30-02.
- AT-SH06: Invitation/tease chung2 attempts và>=30min cooldown; ignore rồi self-play; không drag cursor/window thật.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SH07

- Source: SH07 (explicit_id); scope: release1.
- Requirement: tối đa 5 món đồ ảo để lại trên màn hình, không tính đồ cô ấy đang cầm/sử dụng. Khi đủ giới hạn, tự cất bớt đồ cũ bằng hoạt ảnh trước khi để thêm món mới. Đồ đều hiện trên cửa sổ; người dùng/cô ấy kéo từng món được, có lệnh dọn. Nút dọn nhanh và yêu cầu dọn đều gọi hoạt ảnh thu dọn, không biến mất ngay.
- Owner: `life-state`; use case: UC-04; task proposal: P20-04.
- AT-SH07: Left props không vượt5; held/in-use không tính; đầy thì cất bằng animation trước thêm; cleanup không instantdelete.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SH08

- Source: SH08 (explicit_id); scope: release1.
- Requirement: tùy tâm trạng có thể chán, trì hoãn hoặc từ chối dọn; người dùng tự di chuyển hoặc ẩn cả nhân vật/đồ được. Quà dỗ là đồ ăn và thú bông đã có, không hệ thống quà mới.
- Owner: `life-state`; use case: UC-04; task proposal: P20-04.
- AT-SH08: Cleanup mood delay không chặn user move/hide; gift dùng food/plush đã có, không thêm economy riêng.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QD01

- Source: QD01 (explicit_id); scope: release1.
- Requirement: Người mới cài chỉ có sinh hoạt; quyền truy cập mặc định tắt. Mỗi app/website tách Đọc và Điều khiển; phải bật Đọc trước mới bật Điều khiển, không tự cấp Đọc.
- Owner: `policy`; use case: UC-06; task proposal: P10-01.
- AT-QD01: Fresh install grants off; read/control độc lập; bật control khi thiếu read bị từ chối không auto grant.
- Acceptance interpretation: DRAFT; production evidence: E02a_fake_partial.

### SRS-QD02

- Source: QD02 (explicit_id); scope: release1.
- Requirement: Quét app trên máy để hiện danh sách; website do người dùng dán link. Cấp cho website gồm tên miền phụ; website khác cần riêng. Chrome/Edge cần quyền ở cả trình duyệt và website.
- Owner: `policy`; use case: UC-06; task proposal: P40-02.
- AT-QD02: List app scan không tự cấp; pasted site được normalize; browser+site grants và subdomain test không substring.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QD03

- Source: QD03 (explicit_id); scope: release1.
- Requirement: App/website mới không tự kế thừa. Quyền chung cho ứng dụng, dùng chung các hồ sơ trên máy; không nhập quyền từ file sao lưu.
- Owner: `policy`; use case: UC-06; task proposal: P50-02.
- AT-QD03: New source defaultdeny; switch profile dùng installation grants; archive không apply foreign grants.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QD04

- Source: QD04 (explicit_id); scope: release1.
- Requirement: Đọc nội dung các cửa sổ cùng đang nhìn thấy nếu đều được phép; không đọc cửa sổ/tab bị che hoặc thu nhỏ. Đọc toàn bộ không còn được hiểu là đọc nền mọi nơi. Quyết định 2026-11-14 D-12: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại.
- Owner: `policy`; use case: UC-07; task proposal: P10-02.
- AT-QD04: Split-screen chỉ vùng visible+allowed; tab nền/minimized/occluded không cấp nội dung vào consumer. Kiểm cả nhánh cho phép và từ chối: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại.
- Acceptance interpretation: DRAFT; production evidence: E02a_fake_partial.

### SRS-QD05

- Source: QD05 (explicit_id); scope: release1.
- Requirement: Che vùng không được cấp trước phân tích; không đọc/điều khiển cửa sổ ẩn danh, kể cả website có quyền. Mật khẩu/OTP/thẻ thanh toán bị loại khỏi đọc/nhớ/gửi AI. Khả năng che chưa kiểm chứng.
- Owner: `policy`; use case: UC-07; task proposal: P10-03.
- AT-QD05: Sentinel vùng cấm/private/secret không vào OCR/model/memory/network; unknown-region chặn nguồn, không chỉ overlay che.
- Acceptance interpretation: DRAFT; production evidence: E02a_fake_partial.

### SRS-QD06

- Source: QD06 (explicit_id); scope: release1.
- Requirement: Email/tin nhắn/lịch/danh bạ chỉ qua giao diện được phép, không kết nối tài khoản riêng. Không tự mở theo cách đánh dấu tin/email đã đọc.
- Owner: `policy`; use case: UC-06; task proposal: P10-02.
- AT-QD06: Đọc qua UI được phép không account connector; không tự mở thư/tin gây marked-read.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QD07

- Source: QD07 (explicit_id); scope: deferred.
- Requirement: Đọc tập tin/thư mục chọn riêng để bản cập nhật sau, không thuộc bản đầu. Các quyết định cũ về thư mục con và chỉ hiểu tức thời được giữ làm lịch sử, không triển khai hoặc tiếp tục hỏi chi tiết ở giai đoạn hiện tại. Đọc app không tự cho đọc ổ đĩa; không sửa tài liệu cá nhân.
- Owner: `policy`; use case: UC-06; task proposal: DEFERRED.
- AT-QD07: Scope kiểm tra không có direct file/folder reader bản đầu; không tạo task parser như chức năng đã duyệt.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QD08

- Source: QD08 (explicit_id); scope: release1.
- Requirement: Chỉ khi mở Windows + V mới được đọc toàn lịch sử trong bảng, không chỉ mục đang hiện. Chỉ để hiểu lúc đó, không tạo ký ức lâu dài. Quy tắc thông tin nhạy cảm vẫn áp dụng.
- Owner: `policy`; use case: UC-07; task proposal: P10-04.
- AT-QD08: Fake clipboard history chỉ truy cập khi Win+V open evidence; close mid-flight hủy; không persist/memory.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QD09

- Source: QD09 (explicit_id); scope: release1.
- Requirement: Thu hồi quyền dừng truy cập mới ngay, cho chọn giữ/xóa ký ức từ nguồn đó.
- Owner: `policy`; use case: UC-06; task proposal: P30-04.
- AT-QD09: Revocation chặn ngay đường mới; keep/delete memories là quyết định riêng, không chờ quyết định mới revoke.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QD10

- Source: QD10 (explicit_id); scope: release1.
- Requirement: Được biết riêng vị trí/kích thước cửa sổ chưa cấp quyền Đọc để đi/ngồi trên cạnh; không đọc tiêu đề hoặc nội dung. Đây không phải quyền Điều khiển.
- Owner: `policy`; use case: UC-07; task proposal: P20-02.
- AT-QD10: Nguồn chưa read chỉ xuất geometry; consumer sinh hoạt không nhận title/text, không sinh control grant.
- Acceptance interpretation: DRAFT; production evidence: E02a_fake_partial.

### SRS-QD11

- Source: QD11 (explicit_id); scope: release1.
- Requirement: Tài liệu hiện trong ứng dụng (ví dụ Word) chỉ được ghi nhớ tên hoặc chủ đề người dùng đang đọc, không lưu chi tiết nội dung. Quyền ghi nhớ màn hình không vượt giới hạn này; nội dung tập tin đọc trực tiếp vẫn chỉ dùng tức thời theo QD07. Thông tin nhạy cảm bị cấm vẫn phải loại trừ.
- Owner: `policy`; use case: UC-07; task proposal: P30-04.
- AT-QD11: Document observation chỉ memory name/topic; không detailed summary hoặc raw content trong memory/index.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QD12

- Source: QD12 (explicit_id); scope: release1.
- Requirement: Chấp nhận cài tiện ích hỗ trợ trên Chrome/Edge khi bật tương tác website, nếu phương án được kiểm chứng; tiện ích không bắt buộc cho sinh hoạt cơ bản và không tự cấp quyền mọi website. Chưa có tiện ích hoặc phương án kỹ thuật được cài/chọn.
- Owner: `policy`; use case: UC-06; task proposal: P10-06.
- AT-QD12: Core life không extension; web enable hướng dẫn install rõ, không tự grant mọi host permissions.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QD13

- Source: QD13 (explicit_id); scope: release1.
- Requirement: Trong trang phim đã cấp quyền, được dùng riêng khung video nhúng từ website khác theo quyền đọc/điều khiển tương ứng của trang phim. Không cấp quyền mở/khám phá toàn website nguồn; không mở rộng ngoại lệ sang quảng cáo hoặc khung khác. Không chắc khung nào là video thì nhờ người dùng chỉ, chỉ dùng sau xác nhận. Phải kiểm chứng nhận diện đúng khung phát video.
- Owner: `policy`; use case: UC-07; task proposal: P10-06.
- AT-QD13: Thirdparty player chỉ frame đã cho phép trong parent; ad/frame khác không kế thừa; uncertain phải point+confirm.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QD14

- Source: QD14 (explicit_id); scope: release1.
- Requirement: Được nhớ cách nhận diện ô video đã được chỉ trên đúng trang; lần sau kiểm tra lại, nếu giao diện/nguồn không khớp thì hỏi tiếp. Không bấm theo tọa độ cũ; đây không phải tự kích hoạt bài học thao tác đã lưu.
- Owner: `policy`; use case: UC-07; task proposal: P10-06.
- AT-QD14: Frame recognition scoped đúng site; layout/source đổi hỏi lại, không replay tọa độ và không gọi bài học tự động.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QD15

- Source: QD15 (explicit_id); scope: release1.
- Requirement: Chưa xác định chắc đã loại vùng nhạy cảm thì ngừng đọc cửa sổ đó, báo lý do để người dùng xử lý sau; vẫn sinh hoạt bình thường. Không điều khiển cửa sổ khi không thể đọc an toàn, theo quy tắc Đọc trước Điều khiển. Chỉ thử đọc lại khi người dùng bấm Thử đọc lại, vẫn kiểm tra an toàn trước khi tiếp tục; không bỏ qua bộ lọc.
- Owner: `policy`; use case: UC-07; task proposal: P10-03.
- AT-QD15: Unsafe window giữ hold; fix/đổi cửa sổ không tự đọc; explicit retry kiểm mới, unsafe vẫn chặn.
- Acceptance interpretation: DRAFT; production evidence: E02a_fake_partial.

### SRS-DK01

- Source: DK01 (explicit_id); scope: release1.
- Requirement: chuột/phím người dùng ưu tiên; nhân vật nhường khi họ thao tác, sau 60 giây không thao tác mới được tự trở lại; không tính chuột/phím do nhân vật tạo.
- Owner: `policy`; use case: UC-09; task proposal: P10-07.
- AT-DK01: Human mouse/key làm yield; injected input không reset idle; sau60s revalidate mới resume.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-DK02

- Source: DK02 (explicit_id); scope: release1.
- Requirement: không sửa/xóa/di chuyển dữ liệu cá nhân, gửi tin, đăng bài hoặc trả tiền; không dùng quyền nhấp/phím để vượt cấm. Chấp nhận lịch sử xem tự cập nhật; không tự đánh dấu thư/tin đã đọc. Gõ thật chỉ ô tìm kiếm/điều hướng, không tài liệu/chat/biểu mẫu gửi dữ liệu.
- Owner: `policy`; use case: UC-09; task proposal: P10-07.
- AT-DK02: Action allowlist chặn write/delete/send/pay/markread; chỉ search/navigation typing; watchhistory incidental được giữ.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-DK03

- Source: DK03 (explicit_id); scope: release1.
- Requirement: Dừng khẩn cấp qua phím tắt tùy chỉnh/nút chỉ dừng điều khiển, vẫn quan sát/sinh hoạt theo quyền; hủy việc đang chạy, giữ các việc chưa chạy ở trạng thái tạm dừng. Chỉ người dùng bật lại, không tự vượt sau 60 giây.
- Owner: `policy`; use case: UC-09; task proposal: P10-07.
- AT-DK03: Emergency cancels running/pauses pending; observation/body tiếp theo quyền; no60s autoresume; enable+ResumeQueue.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-DK04

- Source: DK04 (explicit_id); scope: release1.
- Requirement: Tắt quan sát dừng đọc nội dung và điều khiển ứng dụng, vẫn sinh hoạt; ngoại lệ đã chốt: được biết vị trí/kích thước cửa sổ để đi/ngồi/bám cạnh, không đọc nội dung bên trong. Chủ động ẩn dừng đọc/điều khiển, ẩn cả nhân vật và đồ đến khi hiện lại. Cả hai thao tác hủy việc đang chạy, giữ việc chưa chạy ở trạng thái tạm dừng. Thoát app là trạng thái riêng.
- Owner: `policy`; use case: UC-09; task proposal: P10-07.
- AT-DK04: ObservationOff/Hide matrix đúng, geometry exception chỉ observationoff; cancelled job không sống lại khi show.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH01

- Source: BH01 (explicit_id); scope: release1.
- Requirement: chủ động bật hướng dẫn rồi làm mẫu chuỗi trong cùng app/website; cô ấy tóm tắt việc, nơi áp dụng và các bước, người dùng xác nhận mới lưu. Không ghi mọi thao tác thường ngày.
- Owner: `task-execution`; use case: UC-08; task proposal: P40-03.
- AT-BH01: Demo bắt đầu do user, cùng app/site; summary đầy đủ và confirm trước lưu; cancel không thành lesson.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH02

- Source: BH02 (explicit_id); scope: release1.
- Requirement: cài đặt xem bước, đổi tên, bật/tắt, xóa, dạy lại; chọn bài và bấm Thực hiện. Không tự gọi bài học ở cả hai mức; tự khám phá là cơ chế khác. Quyết định 2026-11-14 D-17: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong.
- Owner: `task-execution`; use case: UC-08; task proposal: P40-03.
- AT-BH02: Manage steps/name/enabled/delete/reteach; execution chỉ explicit request ở cả2mode, không auto invoke. Kiểm cả nhánh cho phép và từ chối: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH03

- Source: BH03 (explicit_id); scope: release1.
- Requirement: yêu cầu trực tiếp được bắt đầu ngay, không chờ 60 giây, trừ khi cô ấy trì hoãn một lần vì tâm trạng. Nếu không yêu cầu lại, vẫn giữ việc chờ và tự làm sau khi xong hoạt động hiện tại, đã kiểm tra quyền/giao diện/điều kiện. Yêu cầu lần hai thì thực hiện nếu đủ điều kiện; không vượt lỗi/giới hạn vì yêu cầu lần hai.
- Owner: `task-execution`; use case: UC-08; task proposal: P40-04.
- AT-BH03: Direct request bypass initial60s; mood delay tối đa một lần; secondrequest không bypass grants; pending không bị mất.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH04

- Source: BH04 (explicit_id); scope: release1.
- Requirement: người dùng thao tác thì nhường; 60 giây sau được kiểm tra quyền/giao diện và quay về nơi cũ tiếp tục. Không làm tiếp máy móc theo tọa độ đã lưu.
- Owner: `task-execution`; use case: UC-08; task proposal: P40-04.
- AT-BH04: Human interrupt→60s→reobserve/refocus đúng allowed scope; không replay tọa độ cũ.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH05

- Source: BH05 (explicit_id); scope: release1.
- Requirement: sai giao diện/không tìm mục tiêu thì dừng tại bước lỗi, nhờ chỉ lại; không bấm thử hay chạy lại cả chuỗi.
- Owner: `task-execution`; use case: UC-08; task proposal: P40-04.
- AT-BH05: Missing/mismatched target dừng bước lỗi, nhờ reteach; không blindclick hoặc rerun từ đầu.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH06

- Source: BH06 (explicit_id); scope: release1.
- Requirement: có hàng đợi nhiều yêu cầu; người dùng xem thứ tự và hủy từng việc riêng. Khi một việc lỗi thì dừng việc đó, không tự chạy lại hoặc coi đã xong; tiếp tục các việc sau nếu từng việc đủ quyền/điều kiện. Quyết định 2026-11-14 D-02/D-10/D-17: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong.
- Owner: `task-execution`; use case: UC-09; task proposal: P40-05.
- AT-BH06: Queue nhiều việc có order/cancel; failed job stop riêng; later job chỉ chạy khi đủ prerequisites độc lập. Kiểm cả nhánh cho phép và từ chối: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH07

- Source: BH07 (explicit_id); scope: release1.
- Requirement: thoát ứng dụng hoặc đổi hồ sơ phải báo rõ và hủy các việc chưa hoàn thành; mở lại không tự thực hiện hàng đợi cũ, không chuyển việc sang hồ sơ khác. Bài học đã lưu vẫn giữ.
- Owner: `task-execution`; use case: UC-09; task proposal: P40-05.
- AT-BH07: Exit/switch cảnh báo và cancel unfinished; reopen không auto-run; saved lessons vẫn giữ.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH08

- Source: BH08 (explicit_id); scope: release1.
- Requirement: sau Dừng khẩn cấp/Tắt quan sát/Ẩn, bật lại chức năng hoặc hiện nhân vật không tự chạy các việc cũ. Phải bấm Tiếp tục hàng đợi riêng; chỉ việc chưa chạy còn giữ được tiếp tục, không khôi phục việc đã hủy. Mọi điều kiện/quyền vẫn được kiểm tra.
- Owner: `task-execution`; use case: UC-09; task proposal: P40-05.
- AT-BH08: Re-enable/show chưa resume pending; riêng ResumeQueue mới xét tiếp, cancelled vẫn cancelled.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH09

- Source: BH09 (explicit_id); scope: release1.
- Requirement: tự ẩn vì buồn/tổn thương cũng hủy việc đang chạy, giữ việc chưa chạy ở trạng thái tạm dừng. Sau khi cô ấy trở lại, người dùng phải bấm Tiếp tục hàng đợi riêng; không tự khôi phục việc đã hủy.
- Owner: `task-execution`; use case: UC-09; task proposal: P40-05.
- AT-BH09: Relationshiphide cùng cancel-running/pause-pending; voluntary return chưa tự chạy.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH10

- Source: BH10 (explicit_id); scope: release1.
- Requirement: khi người dùng yêu cầu thực hiện bài học trong lúc cô ấy tự tìm phim/khám phá ứng dụng, ưu tiên việc người dùng giao, dừng việc tự khám phá; vẫn áp dụng quyền trì hoãn một lần theo tâm trạng đã chốt.
- Owner: `task-execution`; use case: UC-09; task proposal: P40-05.
- AT-BH10: Requested job preempts autonomous discovery nhưng vẫn mood delay1; không tự bỏ quyền để ưu tiên.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH11

- Source: BH11 (explicit_id); scope: release1.
- Requirement: bài học có bước tìm kiếm cho phép người dùng đổi nội dung tìm kiếm trước mỗi lần bấm Thực hiện; giữ nguyên các bước đã dạy. Không mở rộng quyền gõ ngoài ô tìm kiếm/điều hướng đã cho phép.
- Owner: `task-execution`; use case: UC-08; task proposal: P40-03.
- AT-BH11: Search parameter đổi mỗi run, không thay target scope hoặc cho gõ chat/document.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH12

- Source: BH12 (explicit_id); scope: release1.
- Requirement: khi lưu bài học có bước chọn kết quả tìm kiếm, cho người dùng chọn rõ chọn kết quả đầu tiên hoặc đúng nội dung đã chỉ. Không tự suy ra ý nghĩa từ cú bấm mẫu; lựa chọn không bỏ qua quyền và kiểm tra an toàn của mục tiêu.
- Owner: `task-execution`; use case: UC-08; task proposal: P40-03.
- AT-BH12: Teach review phân biệt first-result và exact-content; selection persists/revalidate, không suy từ x/y.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-BH13

- Source: BH13 (explicit_id); scope: release1.
- Requirement: có lịch sử thao tác trong cài đặt, chỉ lưu trên máy; người dùng xem và xóa được. Ghi ngắn gọn thời điểm, app/website, loại thao tác và kết quả; không lưu ảnh màn hình hoặc nội dung riêng tư. Tách lịch sử này khỏi ký ức nhân vật. Giữ 30 ngày rồi tự xóa; người dùng có thể xóa sớm.
- Owner: `task-execution`; use case: UC-18; task proposal: P50-05.
- AT-BH13: History local cótime/source/action/outcome, no privatepayload/screenshots;30days expiry và userdelete; tách memory.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP01

- Source: XP01 (explicit_id); scope: release1.
- Requirement: xem cùng, buồn theo cảnh buồn, hứng thú tùy độ hấp dẫn cảnh hành động; reo hò bằng hoạt ảnh, không tiếng. Cảm xúc chuyển tự nhiên, không bật tắt mỗi khung hình.
- Owner: `companion`; use case: UC-10; task proposal: P40-06.
- AT-XP01: Annotated scene sad/action→biểu cảm phù hợp/intensity có lý do, silent; transition dịu không flicker.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP02

- Source: XP02 (explicit_id); scope: release1.
- Requirement: khi đang chú ý đến cảnh rõ, mục tiêu bắt đầu phản ứng dưới 1 giây; cảnh khó chờ để hiểu đúng. Chưa đo/đạt. Không giới hạn loại phim; ưu tiên phụ đề tiếng Việt, ngôn ngữ khác sau.
- Owner: `companion`; use case: UC-10; task proposal: P03-03.
- AT-XP02: Measure display-event→animation-start toàn luồng; report từng mẫu rõ/khó/uncertain và quality, chưa tự đặt pass-rate.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP03

- Source: XP03 (explicit_id); scope: release1.
- Requirement: tự chọn điểm chú ý theo tâm trạng/sở thích khi nhiều cửa sổ cùng hiển thị; không bắt buộc thấy mọi cảnh. Hiểu sai thì tiếp tục điều chỉnh theo cảnh sau, không tính năng sửa cảm xúc bằng tay.
- Owner: `companion`; use case: UC-10; task proposal: P30-02.
- AT-XP03: Attention chooses safe visible source theo preference/mood, không claim mọi cảnh; wrongscene không cần correctionUI.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP10

- Source: XP10 (explicit_id); scope: release1.
- Requirement: khi không nhìn được hình ảnh phim, cô ấy tự chọn tiếp tục ngồi xem hoặc chuyển sang chơi, ăn uống hay hoạt động khác tùy tâm trạng; không bắt buộc tiếp tục xem và không coi nội dung không nhìn được là đã hiểu.
- Owner: `companion`; use case: UC-10; task proposal: P30-02.
- AT-XP10: Capture unavailable không giả hiểu; activity selector cho staywatch hoặc play/eat theo mood.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP11

- Source: XP11 (explicit_id); scope: release1.
- Requirement: khi tự chọn phim/nhạc, cô ấy chủ yếu học và chọn theo gu của người dùng từ nội dung người dùng chủ động mở và xem/nghe lâu trong phạm vi được phép quan sát. Không tự đọc lịch sử trình duyệt; việc mở thử chưa đủ để kết luận thích. Không mở rộng sang nghe/phân tích âm thanh đang hoãn.
- Owner: `companion`; use case: UC-12; task proposal: P30-05.
- AT-XP11: Taste inference chủ yếu theo guuser, only allowed visible evidence; không đọc browserhistory hoặc recordaudio.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP12

- Source: XP12 (explicit_id); scope: release1.
- Requirement: nội dung cô ấy tự mở cũng có thể góp phần học gu nếu người dùng quay lại và tiếp tục xem/nghe đủ lâu; không coi thời gian tự phát khi người dùng vắng mặt là dấu hiệu yêu thích. Dựa vào thao tác chọn/chuyển nội dung thật của người dùng theo XP14.
- Owner: `companion`; use case: UC-12; task proposal: P30-05.
- AT-XP12: Self-open content chỉ học gu khi có userreturn/continuedwatch evidence, không tính unattended runtime.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP13

- Source: XP13 (explicit_id); scope: release1.
- Requirement: dấu hiệu đủ lâu để góp phần học gu: phim ít nhất 20 phút; nhạc được nghe lặp lại hoặc nhiều bài cùng kiểu. Đây là tín hiệu, không kết luận chắc thích. Dùng dấu hiệu thao tác theo XP14; không dùng quy tắc 60 giây thiếu quan tâm để tự suy ra hiện diện.
- Owner: `companion`; use case: UC-12; task proposal: P30-05.
- AT-XP13: Movie>=20min hoặc musicrepeat/similarsongs là tín hiệu, chưa chắc thích; không gom với neglecttimer.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP14

- Source: XP14 (explicit_id); scope: release1.
- Requirement: dùng thao tác người dùng chủ động chuyển tập, chuyển kênh/video hoặc chọn nhạc làm dấu hiệu đang xem/nghe để học gu; không thêm nút xác nhận. Phân biệt thao tác người dùng với tự chuyển/phát tiếp của website hoặc nhân vật; việc không thao tác không tự chứng minh còn hiện diện.
- Owner: `companion`; use case: UC-12; task proposal: P30-05.
- AT-XP14: User contentchange khác autoplay/agentinput; không thêm nút xác nhận hoặc camera theo dõi hiện diện.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP15

- Source: XP15 (explicit_id); scope: release1.
- Requirement: khi tự mở phim/nhạc lúc người dùng vắng mặt, mở tab riêng; giữ nguyên các tab người dùng đang mở, không điều hướng thay nội dung của chúng.
- Owner: `companion`; use case: UC-11; task proposal: P40-07.
- AT-XP15: Autonomous media dùng own tab, giữ existing user tabs và nội dung của chúng.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP16

- Source: XP16 (explicit_id); scope: release1.
- Requirement: người dùng chọn Chrome hoặc Edge trong cài đặt làm trình duyệt tự mở phim/nhạc. Lựa chọn này không tự cấp quyền đọc/điều khiển trình duyệt hay website.
- Owner: `companion`; use case: UC-11; task proposal: P40-02.
- AT-XP16: Chosen browser setting quyết định Chrome/Edge cho automedia; grants vẫn phải đủ.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP09

- Source: XP09 (explicit_id); scope: release1.
- Requirement: khi nhân vật hoặc sofa che phụ đề, người dùng tự kéo nhân vật/đồ vật sang chỗ khác; không yêu cầu tự phát hiện và né phụ đề. Quy tắc không gián đoạn phim vẫn áp dụng.
- Owner: `companion`; use case: UC-10; task proposal: P20-04.
- AT-XP09: Không tự yêu cầu né subtitles; user move avatar/sofa được, không điều hướng phim để dọn vị trí.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP04

- Source: XP04 (explicit_id); scope: release1.
- Requirement: phim đang phát không tự ngắt/cuộn/chuyển cửa sổ gây gián đoạn; được chuyển tập khi hết trong quyền cho phép. Không chắc thì ra dấu/gợi ý, không bấm thử.
- Owner: `companion`; use case: UC-10; task proposal: P40-06.
- AT-XP04: Usermedia không tự pause/scroll/refocus; next chỉ khi ended và target chắc; uncertain không click.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP05

- Source: XP05 (explicit_id); scope: release1.
- Requirement: tự mở phim/nhạc chỉ nâng cao, sau mặc định 5 phút không thao tác (chỉnh được); không khi nhạc/video đang phát. Toàn màn hình không tự là dấu hiệu đang bận. Người dùng quay lại chỉ nhường điều khiển, giữ nội dung phát. Quyết định 2026-11-14 D-16: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng.
- Owner: `companion`; use case: UC-11; task proposal: P40-07.
- AT-XP05: Advanced idledefault5m+nomedia mới autoopen; userreturn giữ playback/yield control, fullscreen không active evidence. Kiểm cả nhánh cho phép và từ chối: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP06

- Source: XP06 (explicit_id); scope: release1.
- Requirement: YouTube được tìm nội dung miễn phí trong quyền cấp. Website khác chỉ ghi nhớ/mở lại sau chọn Cho phép cô ấy dùng website này; được tìm phim bất kỳ miễn phí trong trang đó.
- Owner: `companion`; use case: UC-11; task proposal: P40-07.
- AT-XP06: YouTube search free trong grants; other site phải explicit allow, không tự nhớ mọi visitedsite thành grant.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP07

- Source: XP07 (explicit_id); scope: release1.
- Requirement: được đóng quảng cáo; tab mới không chắc quảng cáo thì để nguyên và quay lại tab phim. Không coi tải/cài/cấp quyền/trả tiền là đóng quảng cáo. Đòi đăng nhập/trả tiền/xác minh thì bỏ, tối đa 3 nội dung mỗi lần tìm rồi về sinh hoạt nếu vẫn không được. Quyết định 2026-11-14 D-06: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng.
- Owner: `companion`; use case: UC-11; task proposal: P40-07.
- AT-XP07: Ambiguous adtab giữ/quay về phim; login/pay/verify skip; max3 candidates per session, không click download/install/notify. Kiểm cả nhánh cho phép và từ chối: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-XP08

- Source: XP08 (explicit_id); scope: release1.
- Requirement: máy khóa không tự mở nội dung mới; mở khóa được tiếp tục nếu trước đó đủ chờ. Riêng thao tác mở khóa không đặt lại mốc 60 giây/5 phút; thao tác chuột/phím tiếp theo trong desktop mới đặt lại, người dùng vẫn ưu tiên. Quyết định 2026-11-14 D-11: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ.
- Owner: `companion`; use case: UC-11; task proposal: P10-07.
- AT-XP08: Locked noopen; unlocked có thể tiếp nếu chờ đã đủ; unlock event riêng không reset, desktopinput kế reset. Kiểm cả nhánh cho phép và từ chối: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-AI01

- Source: AI01 (explicit_id); scope: release1.
- Requirement: nghe/phân tích âm thanh, micro/camera và nhảy theo nhịp để sau. Chỉ mở/phát nhạc và dùng trạng thái phát cần thiết; chưa có thu âm thanh cho nhân vật trong phạm vi hiện tại. Quyết định 2026-11-14 D-16: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng.
- Owner: `perception`; use case: UC-10; task proposal: P03-01.
- AT-AI01: Không mic/camera/audio-analysis/dancebeat; playback bình thường không bị gọi là cô ấy nghe hiểu. Kiểm cả nhánh cho phép và từ chối: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-AI02

- Source: AI02 (explicit_id); scope: release1.
- Requirement: AI bên ngoài chỉ khi người dùng chủ động yêu cầu; xem và duyệt chữ gửi mỗi lần, từ chối thì vẫn dùng khả năng cục bộ. Chưa cho gửi ảnh/âm thanh/tập tin/ký ức hoặc tự gửi báo cáo. Nhà cung cấp chưa chọn. Quyết định 2026-11-14 D-18: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền.
- Owner: `perception`; use case: UC-13; task proposal: P10-05.
- AT-AI02: Explicit request→preview sanitized text→confirm mỗi send; deny vẫn local; không image/audio/file/memory upload. Kiểm cả nhánh cho phép và từ chối: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-AI03

- Source: AI03 (explicit_id); scope: release1.
- Requirement: người dùng xác nhận hướng chạy AI local nhẹ để xử lý cảm xúc nhanh; hai mức cần phù hợp khả năng máy. Chưa chọn mô hình/runtime, số mô hình hoặc cơ chế suy luận; không coi nhãn nhẹ/local là bằng chứng đạt độ trễ XP02. Việc kiểm tra cấu hình không mở rộng quyền đọc nội dung riêng tư.
- Owner: `perception`; use case: UC-10; task proposal: P03-02.
- AT-AI03: Local inference measured với renderer cùng chạy; nhẹ không đồng nghĩa đã đạt subsecond; no silent cloud fallback.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-KN01

- Source: KN01 (explicit_id); scope: release1.
- Requirement: ký ức có thể xem/sửa/xóa/ghim. Cô ấy tự đánh giá quan trọng; vụn vặt phai theo độ quan trọng/nhắc lại, không mốc cố định. Ghim không phai; không ghi lại dữ liệu nhạy cảm đã cấm.
- Owner: `life-state`; use case: UC-14; task proposal: P30-04.
- AT-KN01: Inspect/edit/delete/pin từngmemory, importance fade theo reinforcement; pinned không tựfade; no forbidden payload.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-KN02

- Source: KN02 (explicit_id); scope: release1.
- Requirement: quên tự nhiên giữ mức thân thiết đã hình thành. Sửa nội dung ký ức chỉ đổi thông tin, không đổi mức thân thiết. Chủ động xóa ký ức có thể điều chỉnh quan hệ nếu nó từng đóng góp.
- Owner: `life-state`; use case: UC-14; task proposal: P30-04.
- AT-KN02: Edit không relationrecalc; naturalfade giữ closeness; explicitdelete contribution adjust đúng một lần.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QH01

- Source: QH01 (explicit_id); scope: release1.
- Requirement: dần thân thiết, chào/phản ứng riêng; mặc định bạn bè. Nâng cao có lãng mạn chỉ khi chủ động bật, không lập tức thành người yêu; thể hiện ngượng/đỏ mặt/đến gần/cử chỉ trái tim có ranh giới, không bổ sung nội dung tình dục.
- Owner: `life-state`; use case: UC-15; task proposal: P30-03.
- AT-QH01: Friends default; optinadvanced romance không instantpartner; behaviors trong ranh giới không sexualfeature.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QH02

- Source: QH02 (explicit_id); scope: release1.
- Requirement: tắt lãng mạn cho chọn giữ/xóa ký ức lãng mạn; giữ thì có thể buồn tạm, không níu kéo/tự bật lại, tôn trọng chuyển về bạn bè.
- Owner: `life-state`; use case: UC-15; task proposal: P30-06.
- AT-QH02: Romanceoff choosekeep/delete; retainedmemory buồntạm không pressure/re-enable.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QH03

- Source: QH03 (explicit_id); scope: release1.
- Requirement: người dùng vắng/tắt app không giảm quan hệ hay làm tự ẩn. Mốc cũ 3 ngày lịch đã thay: cộng khoảng 48–72 giờ dùng máy khi nhân vật nâng cao hiện diện mà không tương tác; sau 60 giây không thao tác thì ngừng cộng. Không tính sleep, mở chốc lát rồi tắt, hoạt động do nhân vật, mức cơ bản hoặc hồ sơ không hoạt động.
- Owner: `life-state`; use case: UC-15; task proposal: P30-03.
- AT-QH03: Neglect activeadvancedvisible only, freeze/off/basic/sleep/idle excluded; không calendar3days.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QH04

- Source: QH04 (explicit_id); scope: release1.
- Requirement: đang tin tưởng/thân thiết chịu được lâu hơn, gần 72 giờ; đang tổn thương gần 48 giờ. Bấm/vuốt/cho ăn ngắt chuỗi thiếu tương tác, không xóa ngay nỗi buồn đã có.
- Owner: `life-state`; use case: UC-15; task proposal: P30-03.
- AT-QH04: Trust→threshold gần72h, hurt gần48h; intentionalclick/pet/feed ngắtstreak nhưng sadness không resetinstant.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QH05

- Source: QH05 (explicit_id); scope: release1.
- Requirement: vượt ngưỡng thì buồn/ít chủ động trước, tiếp diễn lâu hơn mới tự ẩn. Làm lành mọi mức được, nặng qua vài buổi, cần thời gian/đối xử tốt; không phải một thao tác hoặc nhiều quà lập tức hết buồn. Nguôi giận tính cả app đóng nhưng vẫn cần tương tác thật. Quyết định 2026-11-14 D-05/H03: Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không là buổi mới. Không tự đặt số phút/số buổi hoặc quà lập tức xóa tổn thương.
- Owner: `life-state`; use case: UC-15; task proposal: P30-03.
- AT-QH05: Sad→withdraw progression; severerepair qua nhiềusessions+care, offlinecooling allowed; gifts không instantfix. Kiểm cả nhánh cho phép và từ chối: Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không là buổi mới. Không tự đặt số phút/số buổi hoặc quà lập tức xóa tổn thương.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QH06

- Source: QH06 (explicit_id); scope: release1.
- Requirement: quăng lần đầu giật mình/ra dấu không thích, chưa hại lâu dài. Tiếp tục sau phản đối thì tạm không cho nhấc, vẫn nhận vuốt/ăn; bình tĩnh và có tương tác tốt, ra dấu sẵn sàng mới cho nhấc lại. Giận nhẹ không có thời gian từ chối cố định, tùy tâm trạng và cách được dỗ. Nâng cao có thể tổn thương lâu dài nếu liên tục bất chấp ranh giới.
- Owner: `life-state`; use case: UC-15; task proposal: P30-03.
- AT-QH06: Firstthrow startle/no lastinghurt; repeatedafterprotest refuse lift nhưng pet/feed; readinesssignal before liftreturn.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-QH07

- Source: QH07 (explicit_id); scope: release1.
- Requirement: tự ẩn vì xa cách thì ngừng cả quan sát/điều khiển, giữ trạng thái riêng; có thể chưa đồng ý ra. Mời ra/để đồ ăn hoặc thú bông từ cửa sổ khay hệ thống hoặc biểu tượng nhỏ tại chỗ ẩn. Cô ấy tự quyết định nhận/xuất hiện; cài đặt và reset luôn mở được.
- Owner: `life-state`; use case: UC-15; task proposal: P30-03.
- AT-QH07: Selfhide shutsread/control; invite/leavegift accessible withoutavatar, can decline, reset/settings remain reachable.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-HS01

- Source: HS01 (explicit_id); scope: release1.
- Requirement: nhiều hồ sơ chỉ qua nhập sao lưu, không nút tạo thêm mới. Chỉ một hồ sơ hoạt động; không trộn ký ức. Hồ sơ không chọn đóng băng hoàn toàn, chọn lại tiếp từ trạng thái cũ (khác đóng app).
- Owner: `distribution`; use case: UC-16; task proposal: P50-02.
- AT-HS01: Import thêmprofile khôngmerge/createbutton; activeone; inactive state/clocks frozen until selected.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-HS02

- Source: HS02 (explicit_id); scope: release1.
- Requirement: quyền của ứng dụng trên máy dùng chung hồ sơ; file nhập không đem quyền sang. Máy chưa có quyền thì vẫn mặc định tắt.
- Owner: `distribution`; use case: UC-16; task proposal: P50-02.
- AT-HS02: All profiles dùng machinegrants, importedprofile không áp importedpermissions.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-HS03

- Source: HS03 (explicit_id); scope: release1.
- Requirement: Đặt lại nhân vật xóa ký ức, quan hệ, trạng thái và toàn bộ bài học của hồ sơ đang chọn để bắt đầu lại; giữ các hồ sơ khác và quyền chung.
- Owner: `distribution`; use case: UC-16; task proposal: P50-02.
- AT-HS03: Reset active memories/relation/state/lessons, preserveotherprofiles và installationgrants.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SL01

- Source: SL01 (explicit_id); scope: release1.
- Requirement: chỉ sao lưu khi bấm xuất, không bản phục hồi tự động. Xuất nhân vật/ký ức/thiết lập; không khóa truy cập AI, máy mới kết nối AI lại. Quyết định 2026-11-14 D-09: Sao lưu không kèm gói AI nâng cao; máy mới tải lại khi cần, không thêm tùy chọn kèm gói mỗi lần xuất. Giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả.
- Owner: `distribution`; use case: UC-17; task proposal: P50-03.
- AT-SL01: Export only useraction; no autoarchive/recoverybackup; keys excluded; reconnect AI onnewmachine. Kiểm cả nhánh cho phép và từ chối: Sao lưu không kèm gói AI nâng cao; máy mới tải lại khi cần, không thêm tùy chọn kèm gói mỗi lần xuất. Giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-SL02

- Source: SL02 (explicit_id); scope: release1.
- Requirement: mỗi bản xuất bắt buộc mật khẩu, thêm mã khôi phục người dùng tự giữ riêng. Chưa chọn cơ chế bảo vệ; không lưu mã mở khóa chung trong bản cần bảo vệ.
- Owner: `distribution`; use case: UC-17; task proposal: P50-03.
- AT-SL02: Passwordrequired perexport + separatelyheldrecoverycode; both correct paths open authenticateddata, bad creds reject.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-CD01

- Source: CD01 (explicit_id); scope: release1.
- Requirement: hỏi bật/tắt khởi động cùng Windows trong thiết lập đầu; không tự bật ngầm. Dữ liệu được lưu qua lần đóng/mở app, không phải bản sao lưu tự động. Quyết định 2026-11-14 D-10: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát.
- Owner: `distribution`; use case: UC-18; task proposal: P50-06.
- AT-CD01: Firstsetup hỏi startup choice; normalstate persistence works and distinctfrombackup. Kiểm cả nhánh cho phép và từ chối: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-CD02

- Source: CD02 (explicit_id); scope: release1.
- Requirement: tự kiểm tra/tải cập nhật chính app nhân vật; hỏi trước cài/khởi động lại. Không cập nhật phần mềm khác.
- Owner: `distribution`; use case: UC-18; task proposal: P50-07.
- AT-CD02: Check/download ownupdate, confirm beforeinstall/restart; no otherappupdate.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-CD03

- Source: CD03 (explicit_id); scope: release1.
- Requirement: gỡ app hỏi giữ dữ liệu để cài lại hay xóa tất cả, nhắc xuất sao lưu trước. File xuất ngoài vùng ứng dụng phải được giải thích riêng, không tự quét/xóa.
- Owner: `distribution`; use case: UC-18; task proposal: P50-08.
- AT-CD03: Uninstall choosekeep/delete và reminder export; không hunt/delete unrelated exported archives.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MODE01

- Source: MODE01 (mode_table); scope: release1.
- Requirement: Sinh hoạt: cơ bản — Đi lại, leo/ngồi cửa sổ, ăn uống, ngủ/nghỉ, vuốt ve và nhấc thả; nâng cao — Có cơ bản và thêm hoạt động dưới đây.
- Owner: `companion`; use case: UC-02; task proposal: P60-02.
- AT-MODE01: Chạy cùng kịch bản sinh hoạt ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MODE02

- Source: MODE02 (mode_table); scope: release1.
- Requirement: Sở thích bằng hoạt ảnh: cơ bản — Các hoạt động cơ bản; nâng cao — Đọc sách, vẽ, thú bông, máy game ảo, ca hát không tiếng, khối xếp hình; sofa xem phim.
- Owner: `companion`; use case: UC-02; task proposal: P60-02.
- AT-MODE02: Chạy cùng kịch bản sở thích bằng hoạt ảnh ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MODE03

- Source: MODE03 (mode_table); scope: release1.
- Requirement: Nội dung sách/tranh/game: cơ bản — Không yêu cầu; nâng cao — Chỉ hoạt ảnh; không tạo sách/tranh thật hoặc chơi game thật.
- Owner: `companion`; use case: UC-02; task proposal: P60-02.
- AT-MODE03: Chạy cùng kịch bản nội dung sách/tranh/game ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MODE04

- Source: MODE04 (mode_table); scope: release1.
- Requirement: Hiểu màn hình: cơ bản — App, chữ, nút; ngữ cảnh đơn giản; nâng cao — Hiểu cảnh phim/cảm xúc sâu hơn.
- Owner: `companion`; use case: UC-02; task proposal: P60-02.
- AT-MODE04: Chạy cùng kịch bản hiểu màn hình ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MODE05

- Source: MODE05 (mode_table); scope: release1.
- Requirement: Điều khiển ứng dụng: cơ bản — Chỉ bài học người dùng trực tiếp gọi; nâng cao — Có tự khám phá trong quyền cấp; bài học vẫn chỉ gọi bằng yêu cầu.
- Owner: `companion`; use case: UC-02; task proposal: P60-02.
- AT-MODE05: Chạy cùng kịch bản điều khiển ứng dụng ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MODE06

- Source: MODE06 (mode_table); scope: release1.
- Requirement: Tự mở phim/nhạc: cơ bản — Không; nâng cao — Có, theo điều kiện mục 8.
- Owner: `companion`; use case: UC-02; task proposal: P60-02.
- AT-MODE06: Chạy cùng kịch bản tự mở phim/nhạc ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MODE07

- Source: MODE07 (mode_table); scope: release1.
- Requirement: Cảm xúc/quan hệ: cơ bản — Tâm trạng, thân thiết; phản đối và từ chối nhấc; nâng cao — Quan hệ sâu, tổn thương lâu dài, tự ẩn vì xa cách; lãng mạn tùy chọn.
- Owner: `companion`; use case: UC-02; task proposal: P60-02.
- AT-MODE07: Chạy cùng kịch bản cảm xúc/quan hệ ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MODE08

- Source: MODE08 (mode_table); scope: release1.
- Requirement: Phát triển tính cách: cơ bản — Giữ tính cách ban đầu, vẫn đổi tâm trạng; nâng cao — Tính cách phát triển lâu dài theo SP07.
- Owner: `companion`; use case: UC-02; task proposal: P60-02.
- AT-MODE08: Chạy cùng kịch bản phát triển tính cách ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

### SRS-MODE09

- Source: MODE09 (mode_table); scope: release1.
- Requirement: Mất Internet: cơ bản — Hoạt động với nội dung cục bộ; nâng cao — Sau tải đủ gói vẫn hoạt động với nội dung cục bộ.
- Owner: `companion`; use case: UC-02; task proposal: P60-02.
- AT-MODE09: Chạy cùng kịch bản mất internet ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- Acceptance interpretation: DRAFT; production evidence: not_verified_production.

## 5. Non-functional requirements and verification budgets

| ID | Contract | Threshold/status | Verification |
|---|---|---|---|
| NFR-01 | Authorization at use time, no forbidden data to consumers | Mandatory deny invariants; universal detection not proven | E02 + IT-01/02/03 |
| NFR-02 | Reaction latency measured end-to-end under actual combined load | XP02 target<1s clear attended scenes; pass-rate/accuracy open D-04 | E04 + IT-10 |
| NFR-03 | Stability with both modes and daily-use mix | About8h required; CPU/RAM/VRAM budgets open D-04 | E05 + IT-19 |
| NFR-04 | Core/local content offline after packages installed | No silent network/cloud dependency | IT-11 |
| NFR-05 | Durable local state and authenticated export/import | No corruption/data loss in defined recovery cases; format/crypto open D-07/09 | IT-14/15 |
| NFR-06 | Clear accessible UI and retained input priority | Vietnamese, focus and cancel semantics; native accessibility matrix to measure | IT-06/20 |
| NFR-07 | Maintainable module boundaries and reproducible builds | Pinned real versions, no suppressions to hide failure; CI not installed | P00-02/P60-02 |
| NFR-08 | Trustworthy installs/updates and explicit costs | Signature/distribution choice open D-13; user consent before install/restart | IT-16 |
| NFR-09 | Minimal local diagnostic data | BH13 retention30days, no secrets/raw screen, no auto telemetry | IT-17 |
| NFR-10 | Correct coordinates and visuals across chosen monitors/DPI | No assumed universal fullscreen; support matrix after E-INT | IT-04/05 |

## 6. External dependencies and readiness

MSTest/.NET tools exist only for E02a; all production dependencies require version/license/advisory validation before adoption. No production build/test commands exist. E02a facts are linked in QA and not promoted into production compliance. Open decisions and risk ownership live in DECISIONS.md; detailed change/approval workflow lives in TEAM.md.
