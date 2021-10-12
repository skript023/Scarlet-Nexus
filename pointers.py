import memory_scanner as scanner
import win32gui
import win32con
from logger import g_logger

class Pointers:
    def __init__(self) -> None:
        self.m_unreal_engine = scanner.pattern_scan("Game Engine", "48 8B 0D ? ? ? ? E8 ? ? ? ? 48 85 ? 74 ? 33 DB").add(3).rip().scan()
        self.battle_points_handle = scanner.pattern_scan("Battle Points Hanlder", "48 89 ? ? ? 57 48 83 EC ? 8B FA 48 8B ? E8 ? ? ? ? 3C ? 75 ? 8B 93").scan()
        self.credits_handle = scanner.pattern_scan("Credits Handler", "48 89 ? ? ? 48 89 ? ? ? 48 89 ? ? ? 57 48 83 EC ? 4C 8B ? ? ? ? ? 33 F6").scan()
        self.items_handle = scanner.pattern_scan("Items Handler", "45 8D ? ? 45 89 ? ? 45 3B").scan()
        g_logger.logger("Pointer Initialized")

def windowEnumHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def show_minimized(window_name):
    top_windows = []
    win32gui.EnumWindows(windowEnumHandler, top_windows)
    for i in top_windows:
        # print(i[1])
        if window_name.lower() in i[1].lower():
            # print("found", window_name)
            win32gui.ShowWindow(i[0], win32con.SW_SHOWNORMAL)#SW_SHOWNORMAL
            #win32gui.SetForegroundWindow(i[0])