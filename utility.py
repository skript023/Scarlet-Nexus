import win32gui
import win32con
import sys
import datetime as date
import os
import winxpgui
import win32api
from logger import g_logger
from pymem import Pymem

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
    scr = '%s\\Scarlet Nexus Trainer\\Scarlet Nexus Log.log' %  os.environ['APPDATA']
    dst = '%s\\Scarlet Nexus Trainer\History\\Scarlet Nexus Log.log' %  os.environ['APPDATA']
    os.makedirs(os.path.dirname(scr), exist_ok=True)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if not os.path.isfile(scr) and not os.access(scr, os.R_OK) and not os.path.isfile(dst) and not os.access(dst, os.R_OK):
        g_logger.log_to_file("Log Created")
        
    g_logger.copy_file(scr, dst)
    g_logger.rename_file('%s\\Scarlet Nexus Trainer\History\\Scarlet Nexus Log.log' %  os.environ['APPDATA'], f"{os.environ['APPDATA']}\\Scarlet Nexus Trainer\History\\{tanggal.year}-{tanggal.month}-{tanggal.day}-{tanggal.hour}-{tanggal.minute}-{tanggal.second}.log")
    g_logger.clean_log_file()

def uint_to_bytes(number: int) -> bytes:
    return number.to_bytes((number.bit_length() + 7) // 8, 'big')
    
def uint_from_bytes(binary_data: bytes) -> int:
    return int.from_bytes(binary_data, 'big')

def int_to_bytes(number: int) -> bytes:
    return number.to_bytes(length=(8 + (number + (number < 0)).bit_length()) // 8, byteorder='big', signed=True)

def int_from_bytes(binary_data: bytes) -> int:
    return int.from_bytes(binary_data, byteorder='big', signed=True)

def run():
    print(f"""{g_logger.CGREEN2}
  _____                _      _   _   _                  _______        _                 
 / ____|              | |    | | | \ | |                |__   __|      (_)                
| (___   ___ __ _ _ __| | ___| |_|  \| | _____  ___   _ ___| |_ __ __ _ _ _ __   ___ _ __ 
 \___ \ / __/ _` | '__| |/ _ \ __| . ` |/ _ \ \/ / | | / __| | '__/ _` | | '_ \ / _ \ '__|
 ____) | (_| (_| | |  | |  __/ |_| |\  |  __/>  <| |_| \__ \ | | | (_| | | | | |  __/ |   
|_____/ \___\__,_|_|  |_|\___|\__|_| \_|\___/_/\_,\____|___/_|_|  \__,_|_|_| |_|\___|_|                                                                                                            
{g_logger.CEND}""")

    when_opened()

    if not is_window_exist("ScarletNexus"):
        g_logger.log_to_console(g_logger.info, "Waiting Game Window")
        input("Press Enter to When Game Is Started")

    pm = Pymem('ScarletNexus-Win64-Shipping.exe')
    g_logger.log_to_console(g_logger.info, f"Process id: {hex(pm.process_id).upper()} Process Handle : {str(pm.process_handle)}")
    g_logger.log_to_console(g_logger.info, "Initializing Pointer")
    return pm