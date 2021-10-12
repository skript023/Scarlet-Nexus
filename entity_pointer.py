from pymem.memory import allocate_memory, free_memory
from memory_scanner import pm
from pointers import *
import memory_helper
from enum import Enum
import utility as utl

memory = memory_helper.Memory()
g_pointers = Pointers()

class player_skill(Enum):
    pyrokinesis=0
    sclerokinesis=1
    clairvoyance=2
    teleportation=3
    invisibility=4
    electrokinesis=5
    duplication=6
    hypervelocity=7
    psychokinesis=8
    psychokinesis_kasane=9
    no_skill=10

skill_list = ["Pyrokinesis","Sclerokinesis","Clairvoyance","Teleportation","Invisibility","Electrokinesis","Duplication","Hypervelocity","Psychokinesis","Psychokinesis","No Skill",]

def getUserParamsBase():
	return memory.get_pointer(g_pointers.m_unreal_engine, [0xE08, 0x2D8, 0x80, 0x0])

def getCharacterBase():
    address = memory.get_pointer(g_pointers.m_unreal_engine, [0xE08, 0x38, 0x0, 0x30, 0x270, 0x0])
    if not address : return 0
    return address

def getCharacterStats():
    return memory.get_pointer(g_pointers.m_unreal_engine, [0xE08, 0x38, 0x0, 0x30, 0x270, 0x9A8, 0x0])

def getCharacterParamsBase():
	return memory.get_pointer(g_pointers.m_unreal_engine, [0xE08, 0x38, 0x0, 0x30, 0x270, 0x948, 0x0])

def getPlayerGaugeBase():
	return memory.get_pointer(g_pointers.m_unreal_engine, [0xE08, 0x38, 0x0, 0x30, 0x270, 0x1198, 0x0])

def getSASStateBase():
	return memory.get_pointer(g_pointers.m_unreal_engine, [0xE08, 0x38, 0x0, 0x30, 0x270, 0x1B38, 0x0])

def getBrainDriveBase():
	return memory.get_pointer(g_pointers.m_unreal_engine, [0xE08, 0x38, 0x0, 0x30, 0x270, 0x1068, 0x0])

def getSASRecastBase():
	return memory.get_pointer(g_pointers.m_unreal_engine, [0xE08, 0x38, 0x0, 0x30, 0x270, 0x11C0, 0xE8])

def getSASDelayBase():
	return memory.get_pointer(g_pointers.m_unreal_engine, [0xE08, 0x38, 0x0, 0x30, 0x270, 0x11C0, 0x108])

def getItemUseRecastBase():
	return memory.get_pointer(g_pointers.m_unreal_engine, [0xE08, 0x38, 0x0, 0x30, 0x270, 0x1170, 0xF8])

def getPlayerSkillBase():
    return memory.get_pointer(g_pointers.m_unreal_engine, [0xE08, 0x38, 0x0, 0x30, 0x270, 0x11C0, 0xD8, 0x0])

def set_velocity_jump(number:float):
    player_base = getCharacterBase()
    if not player_base: return
    jump_velocity = memory.get_pointer(player_base + 0x298, [0x168])
    pm.write_float(jump_velocity, number)

def set_player_health(health:int):
    player_base = getCharacterBase()
    if not player_base: return
    player_health = memory.get_pointer(player_base + 0x948, [0x0])
    pm.write_int(player_health, health)

def set_ignore_damage(activate:bool):
    player = getCharacterBase()
    if player:
        base = pm.read_longlong(player + 0x998)
    if activate:
        pm.write_longlong(player + 0x998, 0)
    elif not activate:
        check_pointer = pm.read_longlong(player + 0x998)
        if check_pointer != 0: return
        if base and base != 0:
            pm.write_longlong(player + 0x998, base)

def set_player_pychic(pychic:float):
    pychic_addr = getPlayerGaugeBase()
    if not pychic_addr: return
    if pychic_addr: pm.write_float(pychic_addr + 0x188, pychic)

def remove_sas_cooldown(activate:bool):
    if activate:
        base = getSASRecastBase()
        if base == None : return
        num = pm.read_int(base + 0x8)
        base = pm.read_longlong(base)
        for i in range(num): pm.write_bytes(base+0xC*i+8, b"\x00", 1)

def set_infinite_sas_duration(activate:bool):
    base = getSASStateBase()
    if activate:
        if base: pm.write_bytes(base+0xE0,b"\x01", 1)
    elif not activate:
        if base: pm.write_bytes(base+0xE0,b"\x00", 1)

def set_infinite_brain_dive(activate:bool):
    if activate:
        base = getBrainDriveBase()
        if base: pm.write_float(base+0x24C, 0.0)

def instant_brain_field(activate:bool):
    if activate:
        base = getBrainDriveBase()
        if base: pm.write_float(base+0x21C,0)

def enter_brain_dive(activate:bool):
    if activate:
        base = getBrainDriveBase()
        if base: pm.write_bytes(base+0x1A2, b"\x01", 1)

def item_usage_no_cooldown(activate:bool):
    base = getItemUseRecastBase()
    if base == None : return
    num = pm.read_int(base+8)
    base = pm.read_longlong(base)
    if base == None: return 
    for i in range(num): pm.write_bytes(base+0xC*i+8,b"\x00", 1)

def infinite_item(activate:bool):
    if activate:
        pm.write_longlong(g_pointers.items_handle, 8743312298854633)
        pm.write_bytes(g_pointers.items_handle - 0xF84433, b"\x85\xFF\x0F\x89\x02\x00\x00\x00\x31\xFF\x45\x8D\x24\x3F\x45\x89\x65\x08\xE9\x24\x44\xF8\x00", 23)
    elif not activate:
        pm.write_longlong(g_pointers.items_handle, 605040655456308549)
        new_addr = g_pointers.items_handle - 0xF84433
        free_memory(pm.process_handle, new_addr)

def infinite_credits(activate:bool):
    if activate:
        pm.write_longlong(g_pointers.credits_handle, 7820862488088955881)
    elif not activate:
        pm.write_longlong(g_pointers.credits_handle, 7820861427712559432)

def infinite_battle_points(activate:bool):
    if activate:
        pm.write_bytes(g_pointers.battle_points_handle, b"\xC3", 1)
    elif not activate:
        pm.write_bytes(g_pointers.battle_points_handle, b"\x48", 1)

def set_player_skill(skill_id, slot):
    match slot:
        case 1:
            pm.write_bytes(getPlayerSkillBase() + 0x2, utl.uint_to_bytes(skill_id), 1)
        case 2:
            pm.write_bytes(getPlayerSkillBase() + 0x0, utl.uint_to_bytes(skill_id), 1)
        case 3:
            pm.write_bytes(getPlayerSkillBase() + 0x1, utl.uint_to_bytes(skill_id), 1)
        case 4:
            pm.write_bytes(getPlayerSkillBase() + 0x3, utl.uint_to_bytes(skill_id), 1)
        case 5:
            pm.write_bytes(getPlayerSkillBase() + 0x6, utl.uint_to_bytes(skill_id), 1)
        case 6:
            pm.write_bytes(getPlayerSkillBase() + 0x4, utl.uint_to_bytes(skill_id), 1)
        case 7:
            pm.write_bytes(getPlayerSkillBase() + 0x5, utl.uint_to_bytes(skill_id), 1)
        case 8:
            pm.write_bytes(getPlayerSkillBase() + 0x7, utl.uint_to_bytes(skill_id), 1)

def get_player_skill(slot:int) -> str:
    match slot:
        case 1:
            return skill_list[utl.uint_from_bytes(pm.read_bytes(getPlayerSkillBase() + 0x2, 1))]
        case 2:
            return skill_list[utl.uint_from_bytes(pm.read_bytes(getPlayerSkillBase() + 0x0, 1))]
        case 3:
            return skill_list[utl.uint_from_bytes(pm.read_bytes(getPlayerSkillBase() + 0x1, 1))]
        case 4:
            return skill_list[utl.uint_from_bytes(pm.read_bytes(getPlayerSkillBase() + 0x3, 1))]
        case 5:
            return skill_list[utl.uint_from_bytes(pm.read_bytes(getPlayerSkillBase() + 0x6, 1))]
        case 6:
            return skill_list[utl.uint_from_bytes(pm.read_bytes(getPlayerSkillBase() + 0x4, 1))]
        case 7:
            return skill_list[utl.uint_from_bytes(pm.read_bytes(getPlayerSkillBase() + 0x5, 1))]
        case 8:
            return skill_list[utl.uint_from_bytes(pm.read_bytes(getPlayerSkillBase() + 0x7, 1))]