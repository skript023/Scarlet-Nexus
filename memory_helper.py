from memory_scanner import pm


class Memory():
    def get_pointer(self, Address, offsets : list[int] = ()) -> int:
        temp_addr = pm.read_longlong(Address)
        ptr = 0x0
        if not offsets: return Address
        else:
            for offset in offsets:
                ptr = int(str(temp_addr), 0) + int(str(offset), 0)
                temp_addr = pm.read_longlong(ptr)
            return ptr
    def is_bit_set(_address,_bit) -> bool:
        v = pm.read_int(_address)
        if v == None:
            print("Cannot read value from:",_address)
            return
        else:
            return v & (1 << _bit) != 0

    def set_bit(_address,_bit) -> bool:
        v = pm.read_int(_address)
        if v == None:
            print("Cannot read value from:",_address)
            return False
        else:
            bm = (1 << _bit)
            bn = v | bm
            if bn and bn != v:
                pm.write_int(_address,bn)
                return True
        return False

    def clear_bit(_address,_bit) -> bool:
        v = pm.read_int(_address)
        if v == None:
            print("Cannot read value from:",_address)
            return False
        else:
            bm = (1 << _bit)
            if v & bm != 0:
                bn=(v & ~bm)
                if bn:
                    pm.write_int(_address,bn)
                    return True
                else: 
                    return False
            else: 
                return False