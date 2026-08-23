import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLayout, QWidget
from PySide6.QtCore import Qt, QSize

# متغیرهای سراسری برای مدیریت وضعیت برنامه
_app = None
_window = None
_root = None
_screen_size = (300, 300)

def _get_app():
    global _app
    _app = QApplication.instance()
    if _app is None:
        _app = QApplication(sys.argv)
    return _app

def screen(size=(300, 300), color=(255, 255, 255), title="FGE Window"):
    global _app, _window, _root, _screen_size
    
    _app = _get_app()
    _screen_size = size

    _window = QMainWindow()
    _window.setWindowTitle(title)
    _window.resize(size[0], size[1])

    # ایجاد ویجت اصلی (Root)
    _root = QWidget()
    _window.setCentralWidget(_root)

    # تنظیم رنگ پس‌زمینه با استفاده از StyleSheet
    r, g, b = color[:3]
    _root.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")
    
    return _root

def _convert_pos(pos, size, parent_size):
    """تبدیل مختصات از پایین-چپ (FGE) به بالا-چپ (Qt)"""
    x, y = pos
    w, h = size
    # y_qt = H - y_fge - h
    return x, parent_size[1] - y - h

def label(parent, pos, text="Label", font_size=12, color=(0, 0, 0)):
    global _screen_size
    lbl = QLabel(text, parent)
    lbl.setStyleSheet(f"font-size: {font_size}px; color: rgb({color[0]}, {color[1]}, {color[2]});")
    
    # اندازه پیش‌فرض اگر داده نشود (تخمینی)
    lbl.adjustSize() 
    w, h = lbl.size().width(), lbl.size().height()
    
    # تبدیل مختصات
    new_pos = _convert_pos(pos, (w, h), _screen_size)
    lbl.move(new_pos[0], new_pos[1])
    lbl.show()
    return lbl

def button(parent, pos, size, text="Button", font_size=10, bg_color=(200, 200, 200), text_color=(0, 0, 0), action=None):
    btn = QPushButton(text, parent)
    btn.setFixedSize(size[0], size[1])
    
    # استایل دکمه
    btn.setStyleSheet(f"""
        QPushButton {{
            background-color: rgb({bg_color[0]}, {bg_color[1]}, {bg_color[2]});
            color: rgb({text_color[0]}, {text_color[1]}, {text_color[2]});
            font-size: {font_size}px;
            border: 1px solid gray;
        }}
    """)

    # تنظیم موقعیت
    new_pos = _convert_pos(pos, size, _screen_size)
    btn.move(new_pos[0], new_pos[1])

    # اتصال Callback
    if action:
        btn.clicked.connect(action)
    
    btn.show()
    return btn

def run():
    global _window, _app
    if _window is None:
        raise RuntimeError("ابتدا باید تابع screen() را فراخوانی کنید.")
    
    _window.show()
    sys.exit(_app.exec())
