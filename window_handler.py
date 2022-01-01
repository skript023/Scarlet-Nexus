import dearpygui.dearpygui as dpg
from entity_pointer import show_minimized
from settings import g_settings
from sys import exit

class WindowHandle:
    window_tick = 0
    window_toggle = True
    def save_dpg_setting(self):
        g_settings.dpg_save_config("Width", dpg.get_item_width("Primary Window")), g_settings.dpg_save_config("Height", dpg.get_item_height("Primary Window"))
        exit(0)
        
    def hide_vp(self):
        self.window_toggle = False
        dpg.minimize_viewport()
        return False

    def show_vp(self):
        self.window_toggle = True
        show_minimized("Scarlet Nexus Trainer")
        return True

    def drag_viewport(self):
        drag_deltas = dpg.get_mouse_drag_delta()
        viewport_current_pos = dpg.get_viewport_pos()
        if dpg.is_item_hovered("Primary Window"):
            dpg.set_viewport_pos([viewport_current_pos[0] + drag_deltas[0],viewport_current_pos[1] + drag_deltas[1]])

class Timer:
    def __init__(self, interval):
        self.total_time = dpg.get_total_time()
        self.last_total_time = dpg.get_total_time()
        self.interval = interval

    def update(self):
        self.total_time = dpg.get_total_time()
        delta_time = dpg.get_total_time() - self.last_total_time
        if delta_time > self.interval:
            self.last_total_time = self.total_time
            return True
        return False

g_window = WindowHandle()