import pymem
from logger import g_logger
from utility import run

pm = run()

class pattern_scan():
    def __init__(self, name, signature) -> None:
        self.__signature = self.__insert_string(signature, r"\x", 0).replace(r" ", r"\x").replace(r"\x?", r".")
        base = pymem.process.module_from_name(pm.process_handle, "ScarletNexus-Win64-Shipping.exe")#.lpBaseOfDll
        self.pointer = pymem.pattern.pattern_scan_module(pm.process_handle, base, self.__signature.encode())
        self.__signature_name = name

    def __insert_string(self, string, str_to_insert, index) -> str:
        return string[:index] + str_to_insert + string[index:]

    def add(self, offset):
        self.pointer += offset
        return self

    def sub(self, offset):
        self.pointer -= offset
        return self

    def rip(self):
        return self.add(pm.read_int(self.pointer) + 4)

    def scan(self):
        try:
            g_logger.log_to_file(f"Found '{self.__signature_name}' ScarletNexus-Win64-Shipping.exe+{hex(self.pointer-pm.base_address).upper()}")
            return self.pointer
        except Exception as e:
            g_logger.log_to_console(g_logger.warning, f"Failed Scan '{self.__signature_name}'.")
            return 0

