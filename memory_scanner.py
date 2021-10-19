from logger import g_logger
from pymem import Pymem
import pymem
from utility import is_window_exist

print(f"""{g_logger.CGREEN2}
  _____                _      _   _   _                  _______        _                 
 / ____|              | |    | | | \ | |                |__   __|      (_)                
| (___   ___ __ _ _ __| | ___| |_|  \| | _____  ___   _ ___| |_ __ __ _ _ _ __   ___ _ __ 
 \___ \ / __/ _` | '__| |/ _ \ __| . ` |/ _ \ \/ / | | / __| | '__/ _` | | '_ \ / _ \ '__|
 ____) | (_| (_| | |  | |  __/ |_| |\  |  __/>  <| |_| \__ \ | | | (_| | | | | |  __/ |   
|_____/ \___\__,_|_|  |_|\___|\__|_| \_|\___/_/\_,\____|___/_|_|  \__,_|_|_| |_|\___|_|                                                                                                            
{g_logger.CEND}""")

g_logger.logger("Waiting Game Window")

if not is_window_exist("ScarletNexus"):
    input("Press Enter to When Game Is Started")

pm = Pymem('ScarletNexus-Win64-Shipping.exe')
g_logger.logger(f"Process id: {hex(pm.process_id).upper()} Process Handle : {str(pm.process_handle)}")
g_logger.logger("Initializing Pointer")

class pattern_scan():
    def __init__(self, name, signature) -> None:
        self.signature_scan(name, signature)

    def insert_string(self, string, str_to_insert, index):
        return string[:index] + str_to_insert + string[index:]

    def signature_scan(self, name, signature):
        self.first = signature
        self.second = self.insert_string(self.first, r"\x", 0)
        self.third = self.second.replace(r" ", r"\x")
        self.final = self.third.replace(r"\x?", r".")
        base = pymem.process.module_from_name(pm.process_handle, "ScarletNexus-Win64-Shipping.exe")#.lpBaseOfDll
        self.Pointer = pymem.pattern.pattern_scan_module(pm.process_handle, base, self.final.encode())
        self.SignatureName = name
        self.SigPattern = signature
        return self

    def add(self, offset):
        self.Pointer += offset
        return self

    def sub(self, offset):
        self.Pointer -= offset
        return self

    def rip(self):
        return self.add(pm.read_int(self.Pointer) + 4)

    def scan(self):
        try:
            g_logger.logger(f"{self.SignatureName} : ScarletNexus-Win64-Shipping.exe+{hex(self.Pointer-pm.base_address).upper()}")
            return self.Pointer
        except Exception as e:
            print(e)

