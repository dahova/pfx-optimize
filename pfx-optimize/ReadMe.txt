🛡️ PFX Exporter Pro - Optimizely Tier 1
Công cụ trích xuất chứng chỉ số (All-in-One Python Script).

⚡ Hướng dẫn cài đặt nhanh (Làm 1 lần)
Để chạy được tool này, máy anh em cần có môi trường Python. Anh em mở CMD và dán lệnh sau để cài đặt tự động:

DOS
winget install -e --id Python.Python.3.12 --scope machine --silent --accept-package-agreements
(Sau khi chạy lệnh xong, hãy tắt CMD đi và mở lại để hệ thống nhận diện Python).

🚀 Cách sử dụng
🚀 Hướng dẫn cài đặt Shortcut (Khuyên dùng)
Để sử dụng tool nhanh nhất (giống như một phần mềm thực thụ), anh em nên tạo Shortcut và Pin vào Taskbar theo các bước sau:

Bước 1: Tạo Shortcut

Chuột phải vào Desktop chọn New -> Shortcut.

Trong ô Type the location of the item, dán dòng lệnh sau: cmd /c python "ĐƯỜNG_DẪN_FILE_CỦA_BẠN" (Ví dụ: cmd /c python "C:\Tools\pfx_exporter.py". Lưu ý: Giữ nguyên dấu ngoặc kép nếu đường dẫn có khoảng trắng).

Đặt tên Shortcut là: PFX Exporter.

Bước 2: Thay Icon cho "ngầu"
Chuột phải vào Shortcut vừa tạo -> Properties.

Chọn tab Shortcut -> Click nút Change Icon...

Anh em có thể chọn hình cái "Chìa khóa" hoặc "Chứng chỉ" trong danh sách mặc định của Windows để dễ nhận diện.

Bước 3: Pin vào Taskbar
Chuột phải vào Shortcut ngoài Desktop.

Chọn Show more options (trên Win 11) -> Pin to taskbar.

📂 Cách sử dụng
Click vào biểu tượng trên Taskbar.

Kéo file .pfx vào cửa sổ hiện ra.

Nhập mật khẩu (màn hình hiện ****).

Xong! Thư mục chứa file .key và .crt sẽ tự động bật lên.

🛠 Yêu cầu hệ thống
Python 3.x đã được cài đặt và add vào PATH.

Quyền truy cập thư mục chứa file PFX để xuất kết quả.

🛠 Lưu ý kỹ thuật
Auto-Lib: Tool sẽ tự động cài thư viện cryptography ngay lần đầu chạy, anh em không cần cài thủ công.

Bảo mật: Đây là file mã nguồn (.py), không phải file .exe nên cực kỳ an toàn và né được SentinelOne quét nhầm.

Quyền hạn: Lệnh cài đặt winget nên được chạy với quyền Admin để đạt hiệu quả tốt nhất.

Developed with ❤️ by Optimizely Tier 1