# Hướng Dẫn Sử Dụng Chương Trình PC Never Die

PC Never Die giúp ngăn máy tính chuyển sang chế độ sleep. Dưới đây là các bước và thông tin cần thiết để sử dụng chương trình:

## 1. Chạy Chương Trình
- **File Đóng Gói:** Nếu bạn sử dụng phiên bản đã đóng gói, chạy file [pc_never_die.exe](build/pc_never_die/EXE-00.toc).
- **Mã Nguồn:** Để chạy từ mã nguồn, execute file [pc_never_die.py](pc_never_die.py) với Python.

## 2. Chức Năng Chính
- **Ngăn Máy Ngủ:** Hàm [prevent_sleep](pc_never_die.py) tự động gửi yêu cầu giữ máy thức mỗi 60 giây khi chế độ "awake" được bật.
- **Tray Icon:** 
  - Icon hiện thị trên khay hệ thống với màu **xanh** khi bật (keep_awake = True) và **đỏ** khi tắt.
  - Nhấp chuột phải để mở menu:
    - **Bật/Tắt pc never die:** Thực hiện toggle bật/tắt chế độ ngăn máy ngủ qua hàm [toggle_awake](pc_never_die.py).
    - **Thoát:** Kết thúc chương trình qua hàm [exit_program](pc_never_die.py).

## 3. Thêm Khởi Động Cùng Windows
- Để tự động chạy chương trình khi Windows khởi động, hãy chạy file [create_shortcut.py](create_shortcut.py). File này sẽ tạo một shortcut trong thư mục Startup của Windows.

## 4. Cấu Hình và Chỉnh Sửa
- Mã nguồn chính được định nghĩa trong [pc_never_die.py](pc_never_die.py).
- Bạn có thể tùy chỉnh thời gian gửi yêu cầu giữ máy thức trong hàm [prevent_sleep](pc_never_die.py).

## 5. Yêu Cầu Hệ Thống
- **Hệ Điều Hành:** Windows
- **Python:** Python 3.12 hoặc tương thích
- **Thư viện:** `pystray`, `Pillow`, `ctypes`, `win32com`

## 6. Thông Tin Tác Giả
- **Tác giả:** duonglxit

---
