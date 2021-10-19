import win32gui
import win32con
from logger import g_logger
import sys
import datetime as date
import os
import winxpgui
import win32api

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

def is_window_exist(window_name):
    top_windows = []
    win32gui.EnumWindows(windowEnumHandler, top_windows)
    for i in top_windows:
        if window_name.lower() in i[1].lower():
            return True
    return False

def set_window_transparent(window_name:str, transparency:int):
    hwnd = win32gui.FindWindow(None, window_name)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong (hwnd, win32con.GWL_EXSTYLE ) | win32con.WS_EX_LAYERED )
    winxpgui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), transparency, win32con.LWA_ALPHA)

def exit_program():
    g_logger.log_to_console(g_logger.info, "Pointers uninitialized")
    g_logger.log_to_console(g_logger.info, "Renderer uninitialized")
    g_logger.log_to_console(g_logger.info, "Exit Program")
    g_logger.log_to_console(g_logger.info, "Farewell!")
    sys.exit(0)

def when_opened():
    tanggal = date.datetime.now()
    scr = '%s\\Scarlet Nexus Trainer\\Ellohim Log.log' %  os.environ['APPDATA']
    dst = '%s\\Scarlet Nexus Trainer\History\\Ellohim Log.log' %  os.environ['APPDATA']
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    g_logger.copy_file(scr, dst)
    g_logger.rename_file('%s\\Scarlet Nexus Trainer\History\\Ellohim Log.log' %  os.environ['APPDATA'], f"{os.environ['APPDATA']}\\Scarlet Nexus Trainer\History\\{tanggal.year}-{tanggal.month}-{tanggal.day}-{tanggal.hour}-{tanggal.minute}-{tanggal.second}.log")
    g_logger.clean_log_file()

def uint_to_bytes(number: int) -> bytes:
    return number.to_bytes((number.bit_length() + 7) // 8, 'big')
    
def uint_from_bytes(binary_data: bytes) -> int:
    return int.from_bytes(binary_data, 'big')

def int_to_bytes(number: int) -> bytes:
    return number.to_bytes(length=(8 + (number + (number < 0)).bit_length()) // 8, byteorder='big', signed=True)

def int_from_bytes(binary_data: bytes) -> int:
    return int.from_bytes(binary_data, byteorder='big', signed=True)