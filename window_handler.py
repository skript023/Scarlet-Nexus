import dearpygui.dearpygui as dpg
from entity_pointer import show_minimized
from settings import g_settings
from sys import exit

class WindowHandle:
    window_tick = 0
    window_toggle = True
    def save_dpg_setting():
        g_settings.dpg_save_config("Width", dpg.get_item_width("Primary Window")), g_settings.dpg_save_config("Height", dpg.get_item_height("Primary Window"))
        exit(0)
        
    def hide_vp():
        dpg.minimize_viewport()
        return False

    def show_vp():
        show_minimized("Scarlet Nexus Trainer")
        return True

    def drag_viewport():
        drag_deltas = dpg.get_mouse_drag_delta()
        viewport_current_pos = dpg.get_viewport_pos()
        if dpg.is_item_hovered("Primary Window"):
            dpg.set_viewport_pos([viewport_current_pos[0] + drag_deltas[0],viewport_current_pos[1] + drag_deltas[1]])

g_window = WindowHandle