# Đọc NYUA bằng ngữ cảnh nhỏ

Chỉ công cụ/tài liệu cục bộ; không cho phép sửa sản phẩm, chạy lại ứng dụng, gửi repository,
gọi AI bên ngoài hoặc cập nhật PR. Nghiệm thu người dùng E02a/C3 còn mở.

## Bắt đầu cho AI

1. Đọc `graphify-out/GRAPH_REPORT.md`, không đọc toàn `graph.json`.
2. Chạy `python docs/context/context_nav.py check` để chặn bản đồ cũ.
3. Tra module: `python docs/context/context_nav.py module policy`.
4. Lấy một task: `python docs/context/context_nav.py task P10-03 --out <TEMP-file>`.
   Đọc file pack đó; dùng source anchors để mở thêm đúng đoạn gốc khi cần.
5. Không tự đóng blocker/human gate. Pack giữ nguyên task, requirement source_text và acceptance,
   quyết định đã chốt/phần dư, full CONSTRAINTS, scope, whitelist thực có/dự kiến, dependency và bootstrap.

Python thực đã dùng: `C:/Users/phamp/AppData/Local/Programs/Python/Python312/python.exe`.
Các lệnh dùng `python` trong hướng dẫn giả định interpreter có graphifyy0.9.97; trên máy này
`python` mặc định MSYS khác interpreter đó. Không cần cài skill/hook hay đổi global configuration.

## Graphify đã xác minh

- Công cụ đã có: graphifyy0.9.97; nguồn [tag chính thức](https://github.com/Graphify-Labs/graphify/tree/v0.9.97).
  [pyproject](https://github.com/Graphify-Labs/graphify/blob/v0.9.97/pyproject.toml) ghim version,
  license Apache-2.0 cho core, kèm LICENSE-MIT/NOTICE của upstream. Không đóng gói mã Graphify bên thứ ba.
- SHA256 `graphify/extract.py` và `cli.py` cài trên máy đã so với tag chính thức, khớp.
  Adapter dùng API thực `graphify.extract.extract(paths, root=..., cache_root=TEMP,
  parallel=False, max_workers=1)`, không giả định tính năng từ skill. API/docstring và entry
  `python -m graphify.extract` có trong extract.py của tag. CLI cũng có
  `graphify extract --code-only --no-cluster`; integration dùng API explicit allowlist để khóa phạm vi chặt hơn.
- Trong lúc extract, socket/create_connection và subprocess.Popen bị chặn. Import Graphify cục bộ,
  không backend semantic, không embeddings/LLM/token API. Wrapper build có timeout120 giây.
- Chỉ mã `.cs` của lab hiện có và `.py` trong docs/tasks, bỏ bin/obj/artifacts/TestResults/cache,
  không model/SDK/git/secret, không đọc file nội dung người dùng hay quét đa phương tiện.
- Đây là trích xuất AST/resolver, không build/runtime/type-check C#. Dynamic dispatch, reflection,
  XAML bindings và hành vi Windows không được chứng minh. Không quét XAML trong allowlist hiện tại.
  Cạnh INFERRED do resolver cục bộ vẫn INFERRED, không đổi thành EXTRACTED.

## Hai nguồn quan hệ riêng

`graphify-out/graph.json` chứa raw nodes/edges do Graphify tạo, giữ source_file/source_location,
confidence EXTRACTED/INFERRED và origin. Wrapper schema_version2 của NYUA được ghi rõ, không giả
schema/communities/report của pipeline upstream. Không chạy Leiden, không tuyên bố God Nodes.

`registry-index.json` là chỉ mục phụ sinh từ canonical backlog/requirements, với nhãn
REGISTRY_DECLARED_NOT_CODE. Dependencies/task→requirement là kế hoạch đã khai báo, không cạnh gọi hàm.
Tham chiếu module→lab do người viết chỉ mục chọn có nhãn MANUAL_REFERENCE_NOT_IMPLEMENTATION:
ví dụ lab không có module life-state sản phẩm. Đường dẫn src/Unity dự kiến không biến thành file thực.
Canonical219 task/109 requirement/7 module không sửa ý nghĩa bởi integration này.

## Giới hạn và độ mới

- Default và tối đa pack160000 byte UTF-8. Task/yêu cầu/acceptance/decision/full CONSTRAINTS không cắt.
  Quá budget: exit2 OVERFLOW, không in hoặc viết pack một phần, kể cả caller chọn budget nhỏ.
- Neighborhood tùy chọn chỉ1 hop, tối đa12 cạnh; số cạnh tùy chọn bị bỏ có ghi rõ. Không dùng giới hạn này
  để bỏ ràng buộc an toàn. Pack không đưa toàn đồ thị vào prompt.
- Mỗi lookup kiểm inventory nguồn, SHA256 văn bản UTF-8 chuẩn hóa BOM/LF, schema và hash các output cốt lõi.
  Đổi nguồn/thêm file/xóa file/sửa map => STALE, phải build lại. Graph là cache, source thắng.
- `build` có thể tái tạo graph/report/index/manifest; `test` kiểm219 pack, module coverage,
  giữ acceptance/deps/decision/constraints, unknown-ID/stale-source/budget-overflow controls.
  Negative control đổi manifest trong memory, không sửa input thật.
- Module query chỉ liệt kê ID + anchor, không in tất cả task. Checkpoint vẫn có nhiều prerequisites;
  chúng được giữ đầy đủ trong task pack, không giả tất cả phase là chuỗi tuần tự.

## Tái tạo và đo

```powershell
$py = 'C:/Users/phamp/AppData/Local/Programs/Python/Python312/python.exe'
& $py docs/context/context_nav.py build
& $py docs/context/context_nav.py check
& $py docs/context/context_nav.py test
& $py docs/context/context_nav.py measure
```

MEASUREMENTS.json ghi baseline file list tường minh: canonical source + CONSTRAINTS + SRS + DECISIONS
+ full backlog/requirements + module specs. Không tính duplicated phase cards để thổi baseline.
So3 task P01-01/P10-03/P40-05. Unicode chars và UTF-8 bytes của input text đo chính xác sau bỏ BOM/chuẩn hóa newline LF; không phải tổng byte file thô; ceil(chars/4) chỉ là ước tính
token, không tokenizer thật, không chứng minh mức giảm phí hay tiết kiệm thời gian mỗi phiên.
Đọc ít hơn baseline không có nghĩa được bỏ thông tin cần thiết của task; source anchors vẫn dùng khi điều tra sâu.


## Gói ZIP tài liệu

ZIP kèm graph/index/tools và hash manifest nhưng không kèm mã sản phẩm C# hoặc thư viện Graphify bên thứ ba.
Để tái tạo hoặc kiểm freshness/query, dùng tại checkout repository có các nguồn trong manifest và Graphify đúng phiên bản.
Nếu giải nén ZIP đứng riêng thiếu nguồn, check phải trả STALE; không bỏ check để dùng snapshot như nguồn hiện hành.
Các liên kết cần checkout được liệt kê trong REPOSITORY-ONLY-LINKS.md của gói. Không cài/copy source sản phẩm ngầm.


## Độ mới của phép đo

Manifest nguồn bao gồm mọi file baseline, kể cả SRS. MEASUREMENTS.json chứa SHA256 từng baseline,
source fingerprint, map fingerprint, schema/version, hash thuật toán và hash ba pack. measurements-manifest.json
kiểm SHA256 văn bản measurement theo cùng chính sách BOM/LF và gắn nguồn/map revision; không tự hash hoặc vòng phụ thuộc.
`build` tái tạo source/map manifest rồi tự đo lại; `measure` chỉ chạy khi source/map còn đúng, có thể sửa
snapshot measurement hỏng mà không thay source/map manifest. `check` kiểm cả measurement integrity/revision.
Sửa SRS hoặc nội dung measurement phải bị từ chối; controls kiểm trong memory/bản TEMP, không đổi input thật.


## Portable checkout fingerprints — schema2

Freshness dùng chính sách có phiên bản `utf8-text-bom-removed-universal-newlines-lf-v1` cho mọi nguồn/output
văn bản UTF-8 được theo dõi: bỏ duy nhất BOM đầu file, chuẩn hóa CRLF/CR thành LF, không trim khoảng trắng,
không parse rồi bỏ field hoặc bỏ nội dung. LF Git blob và CRLF checkout cùng nội dung phải cùng hash;
sửa nội dung hoặc thêm khoảng trắng vẫn STALE. Measurement certificate dùng cùng chính sách và version.
Hash byte upstream Graphify distribution/extractor và checksum ZIP/binary giữ nguyên raw bytes, không chuẩn hóa.
Số byte measurement là input text đã chuẩn hóa LF như đã ghi, không đổi định nghĩa số đo để né lỗi.
Schema1 cache phải build lại; schema không được nhận ngầm. Regression kiểm git archive LF và bản sao CRLF,
đồng thời thay đổi source/measurement thật trong bản tạm vẫn phải bị từ chối.

Kiểm checkout thực từ commit: Python312 `docs/context/check_checkout.py HEAD`. Script chỉ giải nén git archive vào TEMP, kiểm LF/CRLF và sửa/restored source trong bản TEMP; không đổi working tree hoặc chạy mã sản phẩm.
