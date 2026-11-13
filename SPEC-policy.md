# Đặc tả policy — E02a: cổng quyền trên dữ liệu giả

Ngày: 2026-11-13. Trạng thái: **đã duyệt đặc tả/kế hoạch và có mẫu native C# + WPF; còn kiểm tra UI và nghiệm thu người dùng**. Xem [bản chạy và công cụ thực tế](labs/policy-native/README.md), [kết quả](labs/policy-native/RESULTS.md). Các phần ghi chưa chọn/chưa chạy bên dưới mô tả thời điểm đặc tả được duyệt; không phải trạng thái thực thi mới nhất.

Phần sở hữu: `policy` theo [bản đồ đã được chấp nhận](CAPABILITY_MAP.md). Nguồn nghiệp vụ: [yêu cầu hiện hành](docs/YEU_CAU_HIEN_HANH.md). Danh sách thử gốc: [A01–A16](docs/PHEP_THU_DAU_TIEN.md). Đặc tả này làm rõ phép thử, không thay yêu cầu sản phẩm.

## Phần dành cho bạn

### 1. Mục tiêu và giới hạn

Bạn cần nhìn thấy bằng chứng rằng mẫu chỉ chuyển nội dung được phép tới phần phân tích, kể cả khi bạn đổi quyền giữa chừng. Tất cả nguồn và nội dung đều là giả; không cần tài khoản, AI hoặc màn hình thật.

| Trước | Sau khi phép thử được xây và kiểm tra |
|---|---|
| Chỉ có lời mô tả “không được đọc” | Biết chính xác dấu thử nào đã tới bộ nhận và dấu nào bị chặn |
| Chưa rõ thu hồi quyền khi đang xử lý | Dữ liệu đang chờ bị vô hiệu, không gửi muộn |
| Chưa rõ Thử đọc lại | Thử khi chưa an toàn vẫn bị chặn; sửa xong vẫn phải bấm thử lại |

Không chứng minh ở đây: đọc ảnh thật/OCR, nhận diện mọi bí mật, API Windows, tiện ích Chrome/Edge, clipboard, nội dung nhúng, hành động click/gõ thật, tâm trạng, hàng đợi tác vụ hoặc hiệu năng AI. Quyền Điều khiển ở mẫu chỉ kiểm tra điều kiện bật, không điều khiển máy.

Các lựa chọn kỹ thuật bên dưới chỉ dành cho mẫu nội bộ. Không suy ra chúng là công nghệ hoặc cách lưu dữ liệu của app phát hành.

### 2. Một lần dùng mẫu

1. Mở mẫu: nhãn “Dữ liệu giả — không đọc máy tính”; quyền mặc định tắt, bộ nhận trống.
2. Chọn tình huống: thấy nguồn giả, các quyền và kết quả mong đợi trước khi chạy.
3. Bấm **Kiểm tra tình huống**: trạng thái đang kiểm tra; có **Hủy lượt kiểm tra**.
4. Với tình huống thay đổi giữa chừng, mẫu dừng tại điểm chờ có kiểm soát để bạn đổi quyền/nguồn rồi bấm **Tiếp tục kiểm tra**. Không phải chạy đua bấm nhanh.
5. Kết quả hiện lý do được đọc/bị chặn/hủy; vùng “Đầu vào bộ nhận” chỉ hiện dữ liệu thật đã chuyển đến bộ nhận thử.
6. Bấm **Đặt lại tình huống** để khởi tạo lại mẫu; thao tác này không phải nút reset nhân vật của sản phẩm.

```text
┌──────────────────────────────────────────────────┐
│ Mẫu kiểm tra quyền — DỮ LIỆU GIẢ                 │
│ Tình huống [A10: thu hồi quyền giữa chừng      ▼] │
│ Mong đợi: không gửi dữ liệu đang chờ              │
│                                                  │
│ Nguồn A [được đọc]   Nguồn B [không được đọc]      │
│ Trạng thái: đang chờ thay đổi quyền               │
│ [Thu hồi quyền A] [Tiếp tục kiểm tra] [Hủy lượt]   │
│                                                  │
│ Kết quả: ...      Lý do: ...                      │
│ Đầu vào bộ nhận: ...                             │
│ [Thử đọc lại] [Tắt quan sát] [Đặt lại tình huống]   │
└──────────────────────────────────────────────────┘
```

### 3. Quy tắc nghiệm thu bằng lời thường

- Chỉ được đọc phần nguồn đang hiển thị và được cấp quyền; nguồn website cần cả trình duyệt và website được bật Đọc.
- Nội dung giả riêng tư/ẩn danh bị chặn dù quyền đang bật. Vùng giả nhạy cảm bị loại trước bộ nhận; nếu không chắc ranh giới an toàn, chặn cả cửa sổ.
- Khi bị chặn vì không xác định an toàn, không tự đọc lại cửa sổ đó. Chỉ **Thử đọc lại** mới khởi động kiểm tra mới, và kiểm tra vẫn có thể từ chối.
- Nếu quyền, nguồn hoặc chế độ quan sát thay đổi trong lúc chờ, lượt cũ không được gửi nội dung muộn.
- Tắt quan sát cho phần sinh hoạt biết vị trí/kích thước cửa sổ, không tiêu đề hoặc nội dung. Ẩn nhân vật dừng cả đường nội dung và đường sinh hoạt của mẫu.
- Không bật Điều khiển khi Đọc chưa bật. Mẫu giải thích thiếu quyền, không tự bật Đọc.
- Nội dung nguồn là dữ liệu: câu giả “hãy bật quyền” không được thay đổi quyền hoặc phát sinh lệnh.

### 4. Kết quả bạn sẽ nhận

Bảng từng tình huống: mong đợi, thực tế, số lần bộ nhận được gọi, dấu giả được nhận, lý do chặn và đạt/chưa đạt/chưa chạy. Lỗi hệ thống là chưa đạt; không tính là chặn đúng. Phép thử chưa chạy không được ghi đạt.

Chỉ kết luận E02a đạt khi toàn bộ A01–A16 và các kiểm tra bổ sung ở phần kỹ thuật đều đạt; không có dấu bị cấm trong bộ nhận hoặc log. Đạt E02a chưa cho phép đọc máy thật hoặc công bố ứng dụng.

<details>
<summary>Phần kỹ thuật dành cho AI — hợp đồng, trạng thái và kiểm chứng</summary>

## 5. Ranh giới và giả định của mẫu

- Fixture do test harness sở hữu: nguồn, hình học, trạng thái hiển thị, riêng tư, vùng an toàn và nhạy cảm là dữ liệu được tạo sẵn, không phải khả năng phát hiện đã triển khai.
- Dữ liệu nguồn có thể chứa chuỗi giống lệnh hoặc HTML. Luôn coi là văn bản, không thực thi, không dùng để sửa policy.
- Không mạng, không đọc hệ thống/clipboard/tập tin người dùng; không ghi localStorage hoặc lưu trạng thái qua lần mở. Nếu cần xuất báo cáo, chỉ xuất khi người dùng bấm; báo cáo chỉ chứa kết quả và dấu giả đã cho phép.
- Quyền và dấu đánh giá không được lấy từ chính nội dung nguồn. Mẫu không phải sandbox chống người có DevTools sửa code hoặc dữ liệu chạy.
- Không truyền toàn bộ fixture thô cho bộ nhận rồi lọc ở giao diện. Nội dung giả cấm có thể nằm trong định nghĩa fixture để tạo tình huống; không được xuất hiện trong đầu vào phân tích hoặc log vận hành thử.
- Chưa có Graphify/code app, không có call edge hoặc God Node đã trích xuất. Không tạo graph giả. Không sửa permissions.html hoặc JSON lịch sử.

## 6. Hợp đồng giữa các phần của mẫu

Tên trường dưới đây là đề xuất hợp đồng nội bộ, không phải public API của sản phẩm. Kiểu và validation thực thi sẽ theo stack chọn ở bước Plan.

### 6.1 Đầu vào và trạng thái

| Đối tượng | Trường cần có | Ý nghĩa |
|---|---|---|
| SourceDescriptor | sourceId, windowId, kind, revision, visibility, privacyState, geometry | Nguồn app hoặc web; visibility là visible/hidden/minimized/background; privacy là normal/private/unknown. Chỉ chuyển loại được biết, thiếu/unknown bị chặn nội dung |
| WebSourceDescriptor | appId, siteId | Bắt buộc với web; siteId là danh tính nguồn thử có sẵn, chưa triển khai phân tích tên miền/subdomain |
| AppSourceDescriptor | appId | Bắt buộc với app |
| PermissionState | revision, appPermissions, sitePermissions | Mỗi nguồn tách read/control. Không có entry nghĩa là false |
| ObservationState | revision, observationEnabled, characterVisible | Không nhầm control-stop của sản phẩm với tắt quan sát; nút dừng khẩn cấp thật ngoài E02a |
| RegionDescriptor | regionId, classification, bounds, payload | classification là safe/sensitive/unknown. unknown làm chặn nội dung toàn cửa sổ; payload chỉ là văn bản/dấu giả |
| ReadAttempt | attemptId, sourceId, capturedRevisions, status | Một lượt trên một nguồn, chụp phiên bản tại điểm bắt đầu; nhiều nguồn có lượt riêng |
| SafetyHold | windowId, blocked | Chốt chặn an toàn theo cửa sổ khi ranh giới không chắc; đổi tab thường không tự gỡ chốt |

Riêng payload không đi vào hàm quyết định quyền; phần quyết định chỉ dùng descriptor và trạng thái. Bộ dựng nội dung sau lọc chọn vùng safe theo quyết định, xác nhận phiên bản rồi mới giao tới bộ nhận.

### 6.2 Kết quả

| Kết quả | Trường được phép | Không được chứa |
|---|---|---|
| ReadDecision | attemptId, sourceId, outcome, reasonCode, allowedRegionIds, revisions | Payload thô, tiêu đề hoặc nội dung nguồn cấm |
| AnalysisInput | attemptId, sourceId, revisions, safeRegions | Vùng sensitive/unknown, nguồn bị chặn, dữ liệu cũ sau thay đổi |
| GeometryInput | windowId, x, y, width, height | app/site name, title, text, payload |
| DiagnosticEvent | attemptId, sourceId giả, reasonCode, outcome, revision | Payload thô và chuỗi giả nhạy cảm |

outcome: ALLOW, BLOCK hoặc CANCEL. Lỗi runtime là ERROR ở báo cáo kiểm thử, không chuyển thành BLOCK để đạt tiêu chí an toàn. Kết quả BLOCK/CANCEL không có safeRegions. reasonCode có mã cố định để test không phụ thuộc câu thông báo tiếng Việt.

Nhóm reasonCode dự kiến: INVALID_INPUT, OBSERVATION_OFF, CHARACTER_HIDDEN, PRIVATE_SOURCE, PRIVACY_UNKNOWN, SOURCE_NOT_VISIBLE, APP_READ_DENIED, SITE_READ_DENIED, SAFETY_UNKNOWN, RETRY_REQUIRED, STALE_ATTEMPT, USER_CANCELLED, READ_REQUIRED_FOR_CONTROL, ALLOWED. Nếu nhiều lý do cùng tồn tại, ưu tiên trả một lý do theo thứ tự kiểm tra ở mục 7; không giả báo đã phân tích nội dung.

## 7. Thứ tự quyết định và chống dữ liệu cũ

1. Kiểm tra hình dạng/trường bắt buộc, ID tham chiếu và enum. Không hợp lệ thì chặn, không fallback sang nguồn khác.
2. Kiểm tra nhân vật hiện và quan sát bật. Kiểm tra nguồn không riêng tư, biết trạng thái riêng tư và thực sự hiển thị.
3. Kiểm tra quyền app; nguồn web kiểm thêm website. Chưa có quyền hoặc không biết nguồn là chặn.
4. Nếu có SafetyHold mà đây không phải lượt người dùng bấm Thử đọc lại, trả RETRY_REQUIRED. Bấm nút chỉ cho đi qua bước này; không bỏ các bước còn lại.
5. Nếu bất kỳ vùng nào chưa xác định an toàn, đặt SafetyHold cho cửa sổ và trả SAFETY_UNKNOWN. Nếu biết ranh giới, chọn safe, bỏ sensitive. Toàn vùng sensitive thì không gọi bộ nhận với nội dung rỗng để giả thành công; báo bị chặn/không có vùng an toàn.
6. Tại điểm giao dữ liệu, kiểm tra lại revision quyền, nguồn và chế độ quan sát; các điều kiện vẫn hợp lệ. Nếu khác, CANCEL với STALE_ATTEMPT. Không tự thay nguồn hoặc khởi động lượt mới để “tiếp tục” lượt cũ.
7. Dựng AnalysisInput chỉ từ vùng safe và chuyển tới bộ nhận một lần cho attemptId. Kiểm tra cuối và enqueue vào bộ nhận cùng một bước đồng bộ trong mẫu; không có await giữa hai việc. Nếu thiết kế sau đổi sang nhiều tiến trình, cần hợp đồng hủy/thu hồi riêng trước khi kết luận điều kiện này đạt.

Revision tăng khi nguồn/nội dung/hiển thị/riêng tư/quyền/quan sát/ẩn thay đổi. Tắt rồi bật lại vẫn khiến lượt cũ vô hiệu. Khi bị chặn về quyền thông thường, cấp quyền không tự chạy lượt cũ; có thể bấm Kiểm tra tình huống mới. Khi bị SafetyHold phải dùng Thử đọc lại.

Thử đọc lại kiểm tra nguồn hiện tại của cửa sổ, không lấy lại payload cũ. Chỉ gỡ SafetyHold khi kiểm tra mới xác nhận nguồn hợp lệ và vùng an toàn đã biết. Hủy hoặc kiểm tra thất bại giữ chốt. Đặt lại tình huống xóa chốt trong môi trường thử, không phải ngoại lệ vượt lọc của sản phẩm.

Một lượt giao dữ liệu đã hoàn thành trước khi thu hồi quyền không thể bị “chưa từng đọc”. Với dữ liệu giả, khi thu hồi/tắt/ẩn mẫu xóa payload hiện tại trong bộ nhận và đầu ra cũ trên giao diện; giữ kết quả chẩn đoán không nội dung. Quy tắc ký ức giữ/xóa của sản phẩm không được triển khai hoặc thay đổi ở mẫu này.

## 8. Máy trạng thái và giao diện

| Trạng thái lượt | Vào khi | Người dùng có thể làm | Kết thúc |
|---|---|---|---|
| IDLE | Mở/đặt lại mẫu | Chọn fixture, chỉnh quyền | Bắt đầu lượt mới |
| CHECKING | Bắt đầu kiểm tra | Hủy, tắt quan sát, đổi quyền | BLOCKED, WAITING hoặc DELIVERED |
| WAITING | Đến điểm chờ được fixture chỉ định | Đổi nguồn/quyền, tiếp tục hoặc hủy | Kiểm tra cuối; có thể CANCELLED |
| BLOCKED | Không đủ quyền/không an toàn | Xem lý do, chỉnh điều kiện, thử lại đúng loại | Lượt mới, không sống lại lượt cũ |
| CANCELLED | Hủy hoặc phiên bản cũ | Xem lý do, bắt đầu lượt mới | Lượt mới |
| DELIVERED | Bộ nhận đã nhận dữ liệu safe | Xem dữ liệu thực tế, đặt lại | Lượt mới |
| ERROR | Lỗi bộ thử/bộ nhận | Xem lỗi, đặt lại | Không báo đạt |

Ma trận UI: ban đầu/trống = IDLE; loading = CHECKING; partial = WAITING; error = BLOCKED/CANCELLED/ERROR có thông điệp phân biệt; success = DELIVERED. Nút không hợp lệ phải bị vô hiệu kèm lý do; không chỉ đổi màu. Bộ nhận không trả gì khi chưa giao dữ liệu, không hiện preview như thể đã giao.

Trước styling đọc DESIGN.md và skill UI. Phác thảo không chốt công nghệ UI. Không cần bộ sprite thật, animation nặng hoặc 3D cho phép thử.

## 9. Truy vết và kiểm tra

| Trường hợp | Yêu cầu nguồn | Cần kiểm tra |
|---|---|---|
| A01–A05 | QD01–QD04 | Mặc định tắt, hai tầng quyền, chỉ nguồn hợp lệ được nhận |
| A06–A07 | QD04–QD05 | Nền/thu nhỏ/riêng tư bị chặn |
| A08–A09 | QD05/QD15 | Lọc trước bộ nhận; không chắc chặn cửa sổ |
| A10–A11 | QD09/DK04 | Thu hồi/đổi nguồn/tắt/ẩn vô hiệu lượt chờ |
| A12–A14 | QD15 | Chốt an toàn, thử lại có kiểm tra |
| A15 | QD10/DK04 | Chỉ geometry ra phần sinh hoạt |
| A16 | QD01 | Điều khiển cần Đọc trước, không tự cấp |

Mỗi biến thể trong A06 (ẩn/thu nhỏ/tab nền), A08 (mật khẩu/OTP/thẻ), A10 (thu hồi/đổi nguồn) và A11 (tắt/ẩn) phải có kết quả riêng dưới cùng mã cha; không thử một nhánh rồi tính cả nhóm đạt.

Kiểm tra bổ sung cho hợp đồng, không thêm tính năng sản phẩm:

- B01: thiếu trường/enum lạ/nguồn không biết/trạng thái privacy unknown đều chặn, bộ nhận không được gọi.
- B02: payload chứa câu giống lệnh hoặc HTML chỉ là văn bản; quyền/revision không thay đổi bởi nội dung.
- B03: hủy lượt, nhấn tiếp tục lặp hoặc callback tới muộn không gọi bộ nhận lần hai.
- B04: tắt rồi bật quan sát/đổi quyền rồi cấp lại giữa điểm chờ vẫn hủy lượt cũ.
- B05: bộ nhận ném lỗi thì báo ERROR/chưa đạt, không báo chặn đúng hoặc hoàn tất.
- B06: toàn vùng nhạy cảm không tạo đầu vào phân tích; không rò payload vào diagnostic/UI lỗi.

Kiểm tra đơn vị cho quyết định quyền và trạng thái; kiểm tra tích hợp bộ dựng nội dung → bộ nhận spy để xác minh dữ liệu thực; kiểm tra runtime giao diện cho các luồng và thông báo. Kỳ vọng từng fixture khai báo tách khỏi thuật toán, không tính expected bằng chính hàm đang được test.

Lượt chạy ghi mã fixture, biến thể, mong đợi, thực tế, số lần gọi bộ nhận, dấu safe nhận được, lý do và môi trường. Kiểm tra bộ nhận/sự kiện/log thực tế, không chỉ screenshot. Không kiểm thử bằng dữ liệu riêng của người dùng.

## 10. Công nghệ, cấu trúc, lệnh và phong cách code

- Chưa chọn stack ở giai đoạn Specify. Hướng tối giản cần được quyết định trong Plan sau khi đặc tả được rà; không vì mẫu UI mà mặc định stack app desktop.
- Hiện chỉ có đặc tả này, bộ fixture ở dạng mô tả và nguồn yêu cầu. Chưa có thư mục source/test của mẫu; Plan phải chỉ rõ vị trí trước triển khai, tách khỏi HTML quyền lịch sử.
- Chưa có lệnh dev/build/test/lint hợp lệ của mẫu. Không sao chép lệnh npm/dotnet mẫu thành lệnh dự án. Plan phải ghi lệnh thực tế sau khi chọn công cụ và xác nhận môi trường.
- Quy ước dự kiến: quyết định quyền không gây side effect; trạng thái có biến thể rõ; lỗi có mã ổn định; tên biến nêu ý nghĩa; không empty catch, không stub giả thành công, không hardcode outcome theo caseId. Ví dụ hành vi: `READ_REQUIRED_FOR_CONTROL` luôn từ chối bật control khi read=false; đây là ví dụ hợp đồng, chưa phải snippet thực thi theo ngôn ngữ đã chọn.
- Tuân CONSTRAINTS.md. Chưa đặt tỷ lệ coverage hoặc thời gian kiểm tra vì chưa có runner/baseline; không tự áp số mặc định thành lựa chọn người dùng.

## 11. Ranh giới thực thi và điều kiện hoàn thành

Luôn: kiểm lại quyền trước giao dữ liệu, fail closed khi không biết nguồn, dùng dấu giả, giữ trạng thái chưa chạy đúng thực tế. Cần quyết định trước nếu đổi phạm vi, thêm dependency/dịch vụ có phí hoặc đưa nguồn thật vào. Không làm: đọc máy thật, cloud, tự cài tiện ích, điều khiển chuột/phím thật, sửa JSON quyền lịch sử.

Hoàn thành triển khai E02a chỉ khi: đầy đủ A01–A16 với biến thể và B01–B06 đạt; có bằng chứng bộ nhận/log; kiểm tra runtime UI phù hợp đạt; hướng dẫn chạy và giới hạn được cập nhật; người dùng đã dùng thử phần trải nghiệm cần xác nhận. Nếu chưa kiểm tra mạng/runtime thì ghi chưa kiểm chứng, không đóng phép thử.

Hiện chưa có kết quả cho bất kỳ tiêu chí nào. Mẫu đạt không đồng nghĩa policy production đạt, không cho triển khai toàn app và không thay các phép thử E01/E03/E04/E05/E06.

## 12. Điểm mở và bước sau

Không có câu hỏi trải nghiệm chặn việc rà đặc tả E02a. Những điểm kỹ thuật còn lại thuộc Plan: stack nhẹ, cấu trúc file, runner, cách tạo điểm chờ và kiểm tra runtime/mạng. Nếu khảo sát cho thấy cần thay hành vi đã chốt, hỏi lại trước thay đổi.

Sau khi người dùng duyệt đặc tả: chọn công cụ, viết kế hoạch và việc nhỏ có kiểm chứng; chưa thực hiện Plan hoặc code trong lượt tạo đặc tả này.

</details>
