import dearpygui.dearpygui as imgui
import entity_pointer as player
from memory_scanner import pm
import win32api
from window_handler import g_window

def main():
    with imgui.font_registry():
        imgui.add_font("fonts/FiraCode-Regular.ttf", 12, default_font=True)

    #Theme
    with imgui.theme(id="listbox_theme"):
        imgui.add_theme_color(imgui.mvThemeCol_Header, (42, 91, 128), category=imgui.mvThemeCat_Core)#imgui.add_theme_color(imgui.mvThemeCol_FrameBg, (25, 60, 130), category=imgui.mvThemeCat_Core)

    vp = imgui.create_viewport(title='Scarlet Nexus Trainer', width=600, height=400, always_on_top=True, decorated=False, clear_color=(37.0, 37.0, 38.0, 0.0))
    with imgui.window(id="Primary Window", label="Scarlet Nexus Trainer", width=600, height=400, no_move=True, min_size=[250,250], no_collapse=True, on_close=lambda:exit(0)):
        with imgui.handler_registry():
            imgui.add_mouse_drag_handler(callback=g_window.drag_viewport)
        with imgui.tab_bar(label="Tabbar"):
            with imgui.tab(label="Player Option"):
                imgui.add_checkbox(label="Inf Pychic", id="player_psy")
                imgui.add_same_line(xoffset=150)
                imgui.add_checkbox(label="SAS No Cooldown", id="reset_sas")
                imgui.add_same_line(xoffset=300)
                imgui.add_checkbox(label="Inf SAS Duration", id="sas_duration")

                imgui.add_checkbox(label="Inf Brain Dive", id="inf_brain_dive")
                imgui.add_same_line(xoffset=150)
                imgui.add_checkbox(label="Instant Brain Field", id="instant_brain_field")
                imgui.add_same_line(xoffset=300)
                imgui.add_checkbox(label="Inf BP", id="inf_battle_points", callback=lambda:player.infinite_battle_points(imgui.get_value("inf_battle_points")))
                
                imgui.add_checkbox(label="No Item Use Delay", id="item_no_cooldown")
                imgui.add_same_line(xoffset=150)
                imgui.add_checkbox(label="Inf Items", id="infinite_items", callback=lambda:player.infinite_item(imgui.get_value("infinite_items")))
                imgui.add_same_line(xoffset=300)
                imgui.add_checkbox(label="Infinite Credits", id="inf_creds", callback=lambda:player.infinite_credits(imgui.get_value("inf_creds")))

                imgui.add_button(label="Enter Brain Drive", id="enter_brain_dive", callback=lambda:player.enter_brain_dive(True))
            with imgui.tab(label="Player Stats"):
                imgui.add_slider_float(label="DAMAGE FACTOR", id="damage_factor", default_value=pm.read_float(player.getCharacterStats() + 0xC0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xC0, imgui.get_value("damage_factor")), width=200)
                imgui.add_slider_float(label="OBJECT DAMAGE FACTOR", id="obj_dmg_factor", default_value=pm.read_float(player.getCharacterStats() + 0xC4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xC4, imgui.get_value("obj_dmg_factor")), width=200)
                imgui.add_slider_float(label="FIRE DAMAGE FACTOR", id="fire_dmg_factor", default_value=pm.read_float(player.getCharacterStats() + 0xC8), callback=lambda:pm.write_float(player.getCharacterStats() + 0xC8, imgui.get_value("fire_dmg_factor")), width=200)
                imgui.add_slider_float(label="ELECTRIC DAMAGE FACTOR", id="electric_dmg_factor", default_value=pm.read_float(player.getCharacterStats() + 0xCC), callback=lambda:pm.write_float(player.getCharacterStats() + 0xCC, imgui.get_value("electric_dmg_factor")), width=200)
                imgui.add_slider_float(label="RANDOM FACTOR_MIN", id="random_factor_min", default_value=pm.read_float(player.getCharacterStats() + 0xD0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xD0, imgui.get_value("random_factor_min")), width=200)
                imgui.add_slider_float(label="RANDOM FACTOR MAX", id="random_factor_max", default_value=pm.read_float(player.getCharacterStats() + 0xD4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xD4, imgui.get_value("random_factor_max")), width=200)
                imgui.add_slider_float(label="CRITICAL FACTOR", id="critical_factor", default_value=pm.read_float(player.getCharacterStats() + 0xD8), callback=lambda:pm.write_float(player.getCharacterStats() + 0xD8, imgui.get_value("critical_factor")), width=200)
                imgui.add_slider_float(label="CRITICAL CRASH FACTOR", id="critical_crash_factor", default_value=pm.read_float(player.getCharacterStats() + 0xDC), callback=lambda:pm.write_float(player.getCharacterStats() + 0xDC, imgui.get_value("critical_crash_factor")), width=200)
                imgui.add_slider_float(label="BAD STATE UP FACTOR", id="bad_state_up_factor", default_value=pm.read_float(player.getCharacterStats() + 0xE0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xE0, imgui.get_value("bad_state_up_factor")), width=200)
                imgui.add_slider_float(label="BAD STATE DOWN FACTOR", id="bad_state_down_factor", default_value=pm.read_float(player.getCharacterStats() + 0xE4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xE4, imgui.get_value("bad_state_down_factor")), width=200)
                imgui.add_slider_float(label="CRASH FACTOR", id="crash_factor", default_value=pm.read_float(player.getCharacterStats() + 0xE8), callback=lambda:pm.write_float(player.getCharacterStats() + 0xE8, imgui.get_value("crash_factor")), width=200)
                imgui.add_slider_float(label="ARMOR DAMAGE UP FACTOR", id="armor_dmg_up", default_value=pm.read_float(player.getCharacterStats() + 0xEC), callback=lambda:pm.write_float(player.getCharacterStats() + 0xEC, imgui.get_value("armor_dmg_up")), width=200)
                imgui.add_slider_float(label="COPY PSYCHIC ARMOR FACTOR", id="copy_pychic_armor", default_value=pm.read_float(player.getCharacterStats() + 0xF0), callback=lambda:pm.write_float(player.getCharacterStats() + 0xF0, imgui.get_value("copy_pychic_armor")), width=200)
                imgui.add_slider_float(label="PSYCHICFIELD DAMAGE FACTOR BOSS", id="pychicfield_dmg", default_value=pm.read_float(player.getCharacterStats() + 0xF4), callback=lambda:pm.write_float(player.getCharacterStats() + 0xF4, imgui.get_value("pychicfield_dmg")), width=200)
            with imgui.tab(label="Player Inventory"):
                imgui.add_text("Credits : 0", id="total_creds")
                imgui.add_input_int(label="Credits", id="add_credits", width=200)
                imgui.add_button(label="Set Credits", callback=lambda:pm.write_int(player.getUserParamsBase() + 0x50, imgui.get_value("add_credits")))
                imgui.add_text("Battle Points : 0", id="battle_point")
                imgui.add_input_int(label="Battle Points", id="add_battle_points", width=200)
                imgui.add_button(label="Set Battle Points", callback=lambda:pm.write_int(player.getUserParamsBase() + 0x2D0, imgui.get_value("add_battle_points")))
    imgui.setup_dearpygui(viewport=vp)
    imgui.show_viewport(vp)

    while imgui.is_dearpygui_running():
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
        g_window.window_tick += 1

        if win32api.GetAsyncKeyState(0x2D)&0x8000:
            if g_window.window_toggle:
                g_window.window_toggle = False 
            elif not g_window.window_toggle:
                g_window.window_toggle = True

        if g_window.window_tick >= 5:
            g_window.window_tick = 0
            if g_window.window_toggle: g_window.show_vp()
            if not g_window.window_toggle: g_window.hide_vp()

        imgui.render_dearpygui_frame()
    imgui.cleanup_dearpygui()

if __name__ == "__main__":
    main()