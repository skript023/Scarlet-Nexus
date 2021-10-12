import dearpygui.dearpygui as imgui
import entity_pointer as player
from memory_scanner import pm
import win32api
from window_handler import g_window
from utility import is_window_exist
import sys
from logger import g_logger

def main():
    g_logger.logger("Renderer initialized")
    imgui.create_context()

    with imgui.font_registry():
        imgui.add_font("fonts/FiraCode-Regular.ttf", 14, tag="fira_code")
        imgui.bind_font("fira_code")

    with imgui.window(tag="Primary Window", label="Scarlet Nexus Trainer", width=600, height=400, no_move=True, min_size=[250,250], no_collapse=True, on_close=lambda:sys.exit(0)):
        with imgui.handler_registry():
            imgui.add_mouse_drag_handler(callback=g_window.drag_viewport)
        with imgui.tab_bar(label="Tabbar"):
            with imgui.tab(label="Player Option"):
                with imgui.group(horizontal=True, xoffset=150):
                    imgui.add_checkbox(label="Inf Pychic", tag="player_psy")
                    imgui.add_checkbox(label="SAS No Cooldown", tag="reset_sas")
                    imgui.add_checkbox(label="Inf SAS Duration", tag="sas_duration")

                with imgui.group(horizontal=True, xoffset=150):
                    imgui.add_checkbox(label="Inf Brain Dive", tag="inf_brain_dive")
                    imgui.add_checkbox(label="Instant Brain Field", tag="instant_brain_field")
                    imgui.add_checkbox(label="Inf BP", tag="inf_battle_points", callback=lambda:player.infinite_battle_points(imgui.get_value("inf_battle_points")))
                
                with imgui.group(horizontal=True, xoffset=150):
                    imgui.add_checkbox(label="No Item Use Delay", tag="item_no_cooldown")
                    imgui.add_checkbox(label="Inf Items", tag="infinite_items", callback=lambda:player.infinite_item(imgui.get_value("infinite_items")))
                    imgui.add_checkbox(label="Infinite Credits", tag="inf_creds", callback=lambda:player.infinite_credits(imgui.get_value("inf_creds")))

                imgui.add_button(label="Enter Brain Drive", tag="enter_brain_dive", callback=lambda:player.enter_brain_dive(True))
                imgui.add_slider_int(label="Attack", callback=lambda:pm.write_int(player.getCharacterBase() + 0xAEC, imgui.get_value("attack")), tag="attack", max_value=1000, width=200, default_value=pm.read_int(player.getCharacterBase() + 0xAEC))
                imgui.add_slider_int(label="Brain Dive Attack", callback=lambda:pm.write_int(player.getCharacterBase() + 0xAF0, imgui.get_value("brain_attack")), tag="brain_attack", max_value=1000, width=200, default_value=pm.read_int(player.getCharacterBase() + 0xAF0))
                imgui.add_separator()
                imgui.add_text("Skill Changer")
                imgui.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(imgui.get_value("slot_1")), 1), tag="slot_1", label="Slot 1", default_value=player.get_player_skill(1), width=200)
                imgui.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(imgui.get_value("slot_2")), 2), tag="slot_2", label="Slot 2", default_value=player.get_player_skill(2), width=200)
                imgui.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(imgui.get_value("slot_3")), 3), tag="slot_3", label="Slot 3", default_value=player.get_player_skill(3), width=200)
                imgui.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(imgui.get_value("slot_4")), 4), tag="slot_4", label="Slot 4", default_value=player.get_player_skill(4), width=200)
                imgui.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(imgui.get_value("slot_5")), 5), tag="slot_5", label="Slot 5", default_value=player.get_player_skill(5), width=200)
                imgui.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(imgui.get_value("slot_6")), 6), tag="slot_6", label="Slot 6", default_value=player.get_player_skill(6), width=200)
                imgui.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(imgui.get_value("slot_7")), 7), tag="slot_7", label="Slot 7", default_value=player.get_player_skill(7), width=200)
                imgui.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(imgui.get_value("slot_8")), 8), tag="slot_8", label="Slot 8", default_value=player.get_player_skill(8), width=200)
            with imgui.tab(label="Player Stats"):
                imgui.add_slider_float(label="DAMAGE FACTOR", tag="damage_factor", default_value=pm.read_float(player.getCharacterStats() + 0xC0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xC0, imgui.get_value("damage_factor")), width=200)
                imgui.add_slider_float(label="OBJECT DAMAGE FACTOR", tag="obj_dmg_factor", default_value=pm.read_float(player.getCharacterStats() + 0xC4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xC4, imgui.get_value("obj_dmg_factor")), width=200)
                imgui.add_slider_float(label="FIRE DAMAGE FACTOR", tag="fire_dmg_factor", default_value=pm.read_float(player.getCharacterStats() + 0xC8), callback=lambda:pm.write_float(player.getCharacterStats() + 0xC8, imgui.get_value("fire_dmg_factor")), width=200)
                imgui.add_slider_float(label="ELECTRIC DAMAGE FACTOR", tag="electric_dmg_factor", default_value=pm.read_float(player.getCharacterStats() + 0xCC), callback=lambda:pm.write_float(player.getCharacterStats() + 0xCC, imgui.get_value("electric_dmg_factor")), width=200)
                imgui.add_slider_float(label="RANDOM FACTOR_MIN", tag="random_factor_min", default_value=pm.read_float(player.getCharacterStats() + 0xD0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xD0, imgui.get_value("random_factor_min")), width=200)
                imgui.add_slider_float(label="RANDOM FACTOR MAX", tag="random_factor_max", default_value=pm.read_float(player.getCharacterStats() + 0xD4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xD4, imgui.get_value("random_factor_max")), width=200)
                imgui.add_slider_float(label="CRITICAL FACTOR", tag="critical_factor", default_value=pm.read_float(player.getCharacterStats() + 0xD8), callback=lambda:pm.write_float(player.getCharacterStats() + 0xD8, imgui.get_value("critical_factor")), width=200)
                imgui.add_slider_float(label="CRITICAL CRASH FACTOR", tag="critical_crash_factor", default_value=pm.read_float(player.getCharacterStats() + 0xDC), callback=lambda:pm.write_float(player.getCharacterStats() + 0xDC, imgui.get_value("critical_crash_factor")), width=200)
                imgui.add_slider_float(label="BAD STATE UP FACTOR", tag="bad_state_up_factor", default_value=pm.read_float(player.getCharacterStats() + 0xE0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xE0, imgui.get_value("bad_state_up_factor")), width=200)
                imgui.add_slider_float(label="BAD STATE DOWN FACTOR", tag="bad_state_down_factor", default_value=pm.read_float(player.getCharacterStats() + 0xE4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xE4, imgui.get_value("bad_state_down_factor")), width=200)
                imgui.add_slider_float(label="CRASH FACTOR", tag="crash_factor", default_value=pm.read_float(player.getCharacterStats() + 0xE8), callback=lambda:pm.write_float(player.getCharacterStats() + 0xE8, imgui.get_value("crash_factor")), width=200)
                imgui.add_slider_float(label="ARMOR DAMAGE UP FACTOR", tag="armor_dmg_up", default_value=pm.read_float(player.getCharacterStats() + 0xEC), callback=lambda:pm.write_float(player.getCharacterStats() + 0xEC, imgui.get_value("armor_dmg_up")), width=200)
                imgui.add_slider_float(label="COPY PSYCHIC ARMOR FACTOR", tag="copy_pychic_armor", default_value=pm.read_float(player.getCharacterStats() + 0xF0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xF0, imgui.get_value("copy_pychic_armor")), width=200)
                imgui.add_slider_float(label="PSYCHICFIELD DAMAGE FACTOR BOSS", tag="pychicfield_dmg", default_value=pm.read_float(player.getCharacterStats() + 0xF4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xF4, imgui.get_value("pychicfield_dmg")), width=200)
            with imgui.tab(label="Player Inventory"):
                imgui.add_text("Credits : 0", tag="total_creds")
                imgui.add_input_int(label="Credits", tag="add_credits", width=200)
                imgui.add_button(label="Set Credits", callback=lambda:pm.write_int(player.getUserParamsBase() + 0x50, imgui.get_value("add_credits")))
                imgui.add_text("Battle Points : 0", tag="battle_point")
                imgui.add_input_int(label="Battle Points", tag="add_battle_points", width=200)
                imgui.add_button(label="Set Battle Points", callback=lambda:pm.write_int(player.getUserParamsBase() + 0x2D0, imgui.get_value("add_battle_points")))
    vp = imgui.create_viewport(title='Scarlet Nexus Trainer', small_icon="fonts/Ellohim.ico", width=600, height=400, always_on_top=True, decorated=False, clear_color=(37.0, 37.0, 38.0, 0.0))
    imgui.setup_dearpygui()
    imgui.show_viewport()

    while imgui.is_dearpygui_running():
        if is_window_exist("ScarletNexus"):
            player.remove_sas_cooldown(imgui.get_value("reset_sas"))
            player.set_infinite_sas_duration(imgui.get_value("sas_duration"))
            player.set_infinite_brain_dive(imgui.get_value("inf_brain_dive"))
            player.instant_brain_field(imgui.get_value("instant_brain_field"))
            player.item_usage_no_cooldown(imgui.get_value("item_no_cooldown"))

            if imgui.get_value("player_psy"):
                player.set_player_pychic(1000.0)
            #Variable Reader
            Creds = pm.read_int(player.getUserParamsBase() + 0x50)
            BP = pm.read_int(player.getUserParamsBase() + 0x2D0)
            imgui.set_value("total_creds", f"Credits : {Creds}")
            imgui.set_value("battle_point", f"Battle Points : {BP}")
            #Render Handle
            window_width = imgui.get_item_width("Primary Window")
            window_height = imgui.get_item_height("Primary Window")
            imgui.configure_viewport(vp, width=window_width, height=window_height)

            #Window Handle
            if win32api.GetAsyncKeyState(0x2D)&0x8000:
                if g_window.window_toggle:
                    g_window.window_toggle = False 
                elif not g_window.window_toggle:
                    g_window.window_toggle = True

            g_window.window_tick += 1
            if g_window.window_tick >= 2:
                g_window.window_tick = 0
                if g_window.window_toggle and win32api.GetAsyncKeyState(0x2D)&0x8000: g_window.show_vp()
                if not g_window.window_toggle and win32api.GetAsyncKeyState(0x2D)&0x8000: g_window.hide_vp()
        if not is_window_exist("ScarletNexus"): sys.exit(0)
        imgui.render_dearpygui_frame()
    imgui.destroy_context()

if __name__ == "__main__":
    main()
