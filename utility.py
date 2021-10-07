import win32gui
import win32con

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

def uint_to_bytes(number: int) -> bytes:
    return number.to_bytes((number.bit_length() + 7) // 8, 'big')
    
def uint_from_bytes(binary_data: bytes) -> int:
    return int.from_bytes(binary_data, 'big')

def int_to_bytes(number: int) -> bytes:
    return number.to_bytes(length=(8 + (number + (number < 0)).bit_length()) // 8, byteorder='big', signed=True)

def int_from_bytes(binary_data: bytes) -> int:
    return int.from_bytes(binary_data, byteorder='big', signed=True)