import dearpygui.dearpygui as dpg
import entity_pointer as player
import win32api, sys, asyncio
from memory_scanner import pm
from window_handler import g_window, Timer
from utility import is_window_exist, set_window_transparent
from logger import g_logger
from settings import g_settings
from os import system


async def render():
    g_logger.logger("Renderer initialized")
    dpg.create_context()

    with dpg.font_registry():
        dpg.add_font("fonts/Rubik.ttf", g_settings.dpg_load_config("Font"), tag="fira_code")
        dpg.bind_font("fira_code")

    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 10, 10, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 4, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 10, 8, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing, 6, 6, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 0, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_IndentSpacing, 21, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 15, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize, 8, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_TabRounding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign, 0.5, 0.5, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0.5, 0.5, category=dpg.mvThemeCat_Core)
            
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (15, 15, 15, 229), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (0, 0, 0, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (20, 20, 20, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Border, (76, 76, 76, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (53, 53, 53, 138), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (71, 71, 71, 198), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (71, 71, 71, 198), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (43, 43, 43, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (48, 48, 48, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, (0, 0, 0, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (35, 35, 35, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (5, 5, 5, 135), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (0, 0, 0, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (79, 79, 79, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (104, 104, 104, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (255, 255, 255, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (86, 86, 86, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (99, 96, 96, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, (104, 104, 104, 188), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (114, 114, 114, 211), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (114, 114, 114, 198), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Header, (94, 93, 93, 79), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Separator, (60, 60, 60, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip, (60, 60, 60, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Tab, (60, 60, 60, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TabActive, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)

    with dpg.window(tag="Primary Window", label="Scarlet Nexus Trainer", width=g_settings.dpg_load_config("Width"), height=g_settings.dpg_load_config("Height"), no_move=True, min_size=[250,250], no_collapse=True, on_close=g_window.save_dpg_setting):
        with dpg.handler_registry():
            dpg.add_mouse_drag_handler(callback=g_window.drag_viewport)
        with dpg.tab_bar(label="Tabbar"):
            with dpg.tab(label="Player Option"):
                with dpg.group(horizontal=True, xoffset=150):
                    dpg.add_checkbox(label="Inf Pychic", tag="player_psy")
                    dpg.add_checkbox(label="SAS No Cooldown", tag="reset_sas")
                    dpg.add_checkbox(label="Inf SAS Duration", tag="sas_duration")

                with dpg.group(horizontal=True, xoffset=150):
                    dpg.add_checkbox(label="Inf Brain Dive", tag="inf_brain_dive")
                    dpg.add_checkbox(label="Instant Brain Field", tag="instant_brain_field")
                    dpg.add_checkbox(label="Inf BP", tag="inf_battle_points", callback=lambda:player.infinite_battle_points(dpg.get_value("inf_battle_points")))
                
                with dpg.group(horizontal=True, xoffset=150):
                    dpg.add_checkbox(label="No Item Use Delay", tag="item_no_cooldown")
                    dpg.add_checkbox(label="Inf Items", tag="infinite_items", callback=lambda:player.infinite_item(dpg.get_value("infinite_items")))
                    dpg.add_checkbox(label="Infinite Credits", tag="inf_creds", callback=lambda:player.infinite_credits(dpg.get_value("inf_creds")))

                dpg.add_button(label="Enter Brain Drive", tag="enter_brain_dive", callback=lambda:player.enter_brain_dive(True))
                dpg.add_slider_int(label="Attack", callback=lambda:pm.write_int(player.getCharacterBase() + 0xAEC, dpg.get_value("attack")), tag="attack", max_value=1000, width=200, default_value=pm.read_int(player.getCharacterBase() + 0xAEC))
                dpg.add_slider_int(label="Brain Dive Attack", callback=lambda:pm.write_int(player.getCharacterBase() + 0xAF0, dpg.get_value("brain_attack")), tag="brain_attack", max_value=1000, width=200, default_value=pm.read_int(player.getCharacterBase() + 0xAF0))
                dpg.add_separator()
                dpg.add_text("Skill Changer")
                dpg.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(dpg.get_value("slot_1")), 1), tag="slot_1", label="Slot 1", default_value=player.get_player_skill(1), width=200)
                dpg.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(dpg.get_value("slot_2")), 2), tag="slot_2", label="Slot 2", default_value=player.get_player_skill(2), width=200)
                dpg.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(dpg.get_value("slot_3")), 3), tag="slot_3", label="Slot 3", default_value=player.get_player_skill(3), width=200)
                dpg.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(dpg.get_value("slot_4")), 4), tag="slot_4", label="Slot 4", default_value=player.get_player_skill(4), width=200)
                dpg.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(dpg.get_value("slot_5")), 5), tag="slot_5", label="Slot 5", default_value=player.get_player_skill(5), width=200)
                dpg.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(dpg.get_value("slot_6")), 6), tag="slot_6", label="Slot 6", default_value=player.get_player_skill(6), width=200)
                dpg.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(dpg.get_value("slot_7")), 7), tag="slot_7", label="Slot 7", default_value=player.get_player_skill(7), width=200)
                dpg.add_combo(player.skill_list, callback=lambda:player.set_player_skill(player.skill_list.index(dpg.get_value("slot_8")), 8), tag="slot_8", label="Slot 8", default_value=player.get_player_skill(8), width=200)
            with dpg.tab(label="Player Stats"):
                dpg.add_slider_float(label="DAMAGE FACTOR", tag="damage_factor", default_value=pm.read_float(player.getCharacterStats() + 0xC0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xC0, dpg.get_value("damage_factor")), width=200)
                dpg.add_slider_float(label="OBJECT DAMAGE FACTOR", tag="obj_dmg_factor", default_value=pm.read_float(player.getCharacterStats() + 0xC4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xC4, dpg.get_value("obj_dmg_factor")), width=200)
                dpg.add_slider_float(label="FIRE DAMAGE FACTOR", tag="fire_dmg_factor", default_value=pm.read_float(player.getCharacterStats() + 0xC8), callback=lambda:pm.write_float(player.getCharacterStats() + 0xC8, dpg.get_value("fire_dmg_factor")), width=200)
                dpg.add_slider_float(label="ELECTRIC DAMAGE FACTOR", tag="electric_dmg_factor", default_value=pm.read_float(player.getCharacterStats() + 0xCC), callback=lambda:pm.write_float(player.getCharacterStats() + 0xCC, dpg.get_value("electric_dmg_factor")), width=200)
                dpg.add_slider_float(label="RANDOM FACTOR_MIN", tag="random_factor_min", default_value=pm.read_float(player.getCharacterStats() + 0xD0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xD0, dpg.get_value("random_factor_min")), width=200)
                dpg.add_slider_float(label="RANDOM FACTOR MAX", tag="random_factor_max", default_value=pm.read_float(player.getCharacterStats() + 0xD4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xD4, dpg.get_value("random_factor_max")), width=200)
                dpg.add_slider_float(label="CRITICAL FACTOR", tag="critical_factor", default_value=pm.read_float(player.getCharacterStats() + 0xD8), callback=lambda:pm.write_float(player.getCharacterStats() + 0xD8, dpg.get_value("critical_factor")), width=200)
                dpg.add_slider_float(label="CRITICAL CRASH FACTOR", tag="critical_crash_factor", default_value=pm.read_float(player.getCharacterStats() + 0xDC), callback=lambda:pm.write_float(player.getCharacterStats() + 0xDC, dpg.get_value("critical_crash_factor")), width=200)
                dpg.add_slider_float(label="BAD STATE UP FACTOR", tag="bad_state_up_factor", default_value=pm.read_float(player.getCharacterStats() + 0xE0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xE0, dpg.get_value("bad_state_up_factor")), width=200)
                dpg.add_slider_float(label="BAD STATE DOWN FACTOR", tag="bad_state_down_factor", default_value=pm.read_float(player.getCharacterStats() + 0xE4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xE4, dpg.get_value("bad_state_down_factor")), width=200)
                dpg.add_slider_float(label="CRASH FACTOR", tag="crash_factor", default_value=pm.read_float(player.getCharacterStats() + 0xE8), callback=lambda:pm.write_float(player.getCharacterStats() + 0xE8, dpg.get_value("crash_factor")), width=200)
                dpg.add_slider_float(label="ARMOR DAMAGE UP FACTOR", tag="armor_dmg_up", default_value=pm.read_float(player.getCharacterStats() + 0xEC), callback=lambda:pm.write_float(player.getCharacterStats() + 0xEC, dpg.get_value("armor_dmg_up")), width=200)
                dpg.add_slider_float(label="COPY PSYCHIC ARMOR FACTOR", tag="copy_pychic_armor", default_value=pm.read_float(player.getCharacterStats() + 0xF0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xF0, dpg.get_value("copy_pychic_armor")), width=200)
                dpg.add_slider_float(label="PSYCHICFIELD DAMAGE FACTOR BOSS", tag="pychicfield_dmg", default_value=pm.read_float(player.getCharacterStats() + 0xF4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xF4, dpg.get_value("pychicfield_dmg")), width=200)
            with dpg.tab(label="Player Inventory"):
                dpg.add_text("Credits : 0", tag="total_creds")
                dpg.add_input_int(label="Credits", tag="add_credits", width=200)
                dpg.add_button(label="Set Credits", callback=lambda:pm.write_int(player.getUserParamsBase() + 0x50, dpg.get_value("add_credits")))
                dpg.add_text("Battle Points : 0", tag="battle_point")
                dpg.add_input_int(label="Battle Points", tag="add_battle_points", width=200)
                dpg.add_button(label="Set Battle Points", callback=lambda:pm.write_int(player.getUserParamsBase() + 0x2D0, dpg.get_value("add_battle_points")))
    vp = dpg.create_viewport(title='Scarlet Nexus Trainer', small_icon="fonts/Ellohim.ico", width=600, height=400, always_on_top=True, decorated=False, clear_color=(37.0, 37.0, 38.0, 0.0))
    dpg.bind_theme(global_theme)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    
    window_timer = Timer(0.2)

    while dpg.is_dearpygui_running():
        window_event = window_timer.update()
        if is_window_exist("ScarletNexus"):
            player.remove_sas_cooldown(dpg.get_value("reset_sas"))
            player.set_infinite_sas_duration(dpg.get_value("sas_duration"))
            player.set_infinite_brain_dive(dpg.get_value("inf_brain_dive"))
            player.instant_brain_field(dpg.get_value("instant_brain_field"))
            player.item_usage_no_cooldown(dpg.get_value("item_no_cooldown"))

            if dpg.get_value("player_psy"):
                player.set_player_pychic(1000.0)
            #Variable Reader
            Creds = pm.read_int(player.getUserParamsBase() + 0x50)
            BP = pm.read_int(player.getUserParamsBase() + 0x2D0)
            dpg.set_value("total_creds", f"Credits : {Creds}")
            dpg.set_value("battle_point", f"Battle Points : {BP}")
            #Render Handle
            window_width = dpg.get_item_width("Primary Window")
            window_height = dpg.get_item_height("Primary Window")
            dpg.configure_viewport(vp, width=window_width, height=window_height)

            #Window Handle
            if g_window.window_toggle: g_window.show_vp()
            if not g_window.window_toggle: g_window.hide_vp()
            if window_event:
                if win32api.GetAsyncKeyState(0x2D)&0x1:
                    g_window.window_toggle = not g_window.window_toggle
                
        
        if not is_window_exist("ScarletNexus"): sys.exit(0)
        set_window_transparent("Scarlet Nexus Trainer", 229)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

if __name__ == "__main__":
    try:
        asyncio.run(render())
    except Exception as er:
        g_logger.log_to_console(g_logger.warning, "Renderer Failed To Start")
        g_logger.log_to_console(g_logger.warning, f"Reason : {er}")
        dpg.stop_dearpygui()
        system("pause")