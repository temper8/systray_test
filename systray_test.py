from infi.systray import SysTrayIcon
import tk_win

def say_hello(systray):
    print("Hello, World!")
    tk_win.show_tk_win()

menu_options = (("Say Hello", None, say_hello),)
systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)
systray.start()