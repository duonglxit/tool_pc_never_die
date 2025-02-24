import os
from win32com.client import Dispatch

# Hàm thêm khởi động cùng window
def add_to_startup():
    # Đường dẫn tới tệp thực thi đã đóng gói
    exe_path = os.path.join(os.path.dirname(__file__), "dist", "pc_never_die.exe")
    
    # Đường dẫn thư mục Startup của Windows
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shortcut_path = os.path.join(startup_folder, "PC_Never_Die.lnk")
    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = exe_path
    shortcut.WorkingDirectory = os.path.dirname(exe_path)
    # Bạn có thể chỉ định icon nếu muốn, ví dụ: shortcut.IconLocation = exe_path
    shortcut.save()

# Chạy hàm thêm vào startup khi chạy tệp này
if __name__ == "__main__":
    add_to_startup()
