# Môi trường máy khảo sát

Ngày đọc: 2026-11-13. Chỉ dùng truy vấn thông tin; không benchmark, cài đặt, tải model hoặc chạy code nhân vật.

## Thông tin thu được

| Hạng mục | Kết quả |
|---|---|
| Hệ điều hành | Windows 11 Pro, build 26300 |
| CPU | AMD Ryzen 9 8945HX with Radeon Graphics |
| RAM hệ thống | Khoảng 15.8 GiB theo Win32_ComputerSystem |
| GPU được truy vấn | NVIDIA GeForce RTX 5070 Laptop GPU |
| Bộ nhớ GPU | 8151 MiB theo nvidia-smi |
| Driver GPU | 592.01 theo nvidia-smi |

- Git, Node, Python, rustc và cargo có executable trong PATH; chưa xác minh toàn toolchain build, phiên bản/dependency hoặc bản quyền phân phối.
- Không tìm thấy dotnet trong PATH ở lần đọc này. Không kết luận máy chắc chắn chưa cài bất kỳ .NET runtime/SDK nào ở vị trí khác; chưa cài bổ sung.
- Đây là máy hiện tại để thiết kế thử nghiệm, không phải cấu hình tối thiểu của sản phẩm hoặc bằng chứng hiểu cảnh dưới 1 giây.
- Cần thêm cấu hình phổ thông cho mức cơ bản và các cấu hình khác trước tuyên bố hỗ trợ công khai. Không tự đặt mốc RAM/GPU tối thiểu khi chưa đo.

## Phương án lớp hiển thị đang khảo sát

- [WPF AllowsTransparency](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window.allowstransparency): có cửa sổ phi chữ nhật/trong suốt; tài liệu yêu cầu WindowStyle None khi bật AllowsTransparency.
- [Tauri window customization](https://v2.tauri.app/learn/window-customization/), [configuration](https://v2.tauri.app/reference/config/): có tùy chỉnh cửa sổ trong suốt và thuộc tính cửa sổ; chưa chọn runtime/version của dự án.
- Đây là chứng cứ API tồn tại, chưa chứng minh bộ sprite/click-through/vùng nhận input/nhiều DPI/fullscreen đáp ứng yêu cầu. Phải thử K01/E01–E03; không lấy báo cáo cộng đồng làm bằng chứng thay phép thử.
- Chưa chọn WPF, Tauri hoặc phương án khác; không bắt người dùng chọn API/framework thay AI.
