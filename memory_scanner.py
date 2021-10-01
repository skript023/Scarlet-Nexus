from time import sleep
from pymem import Pymem
import pymem

pm = Pymem('ScarletNexus-Win64-Shipping.exe')
print('Process id: ', hex(pm.process_id).upper(), "Process Handle : ", str(pm.process_handle))

class pattern_scan():
    Pointer = 0
    SignatureName = ""
    SigPattern = b""
    final = ""
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
            print("scanning: ", self.SignatureName, "Address : ", hex(self.Pointer).upper())
            return self.Pointer
        except Exception as e:
            print(e)

