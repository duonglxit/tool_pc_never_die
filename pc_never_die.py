import ctypes
import time
import threading
import pystray
from pystray import MenuItem as item, Icon
from PIL import Image, ImageDraw

# Cờ giữ máy thức
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001

# Biến trạng thái
keep_awake = True  
tray_icon = None  

def prevent_sleep():
    """Hàm chạy nền để ngăn máy sleep"""
    global keep_awake
    while True:
        if keep_awake:
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
        time.sleep(60)

# Bắt đầu luồng chạy nền
threading.Thread(target=prevent_sleep, daemon=True).start()

def create_icon_image(color):
    """Tạo hình icon với màu tùy chỉnh"""
    icon_image = Image.new("RGB", (64, 64), color)
    draw = ImageDraw.Draw(icon_image)
    draw.ellipse((10, 10, 54, 54), fill=(255, 255, 255))
    return icon_image

def update_tooltip():
    """Cập nhật tooltip"""
    tray_icon.title = "✔ pc never die is on" if keep_awake else "❌ pc never die is off"

def toggle_awake(icon, item):
    """Hàm bật/tắt chế độ giữ máy thức"""
    global keep_awake, tray_icon
    keep_awake = not keep_awake
    tray_icon.icon = create_icon_image((0, 255, 0) if keep_awake else (255, 0, 0))  
    update_tooltip()
    icon.update_menu()  

def exit_program(icon, item):
    """Hàm thoát chương trình"""
    icon.stop()

def create_icon():
    """Tạo tray icon"""
    global tray_icon

    menu = (item(lambda text: f"Bật pc never die ({'✔' if keep_awake else '❌'})", toggle_awake),
            item("Thoát", exit_program))

    tray_icon = Icon("keep_awake", create_icon_image((0, 255, 0)))
    tray_icon.menu = menu
    update_tooltip()  # Thiết lập tooltip ban đầu
    tray_icon.run()

# Chạy tray icon
create_icon()
