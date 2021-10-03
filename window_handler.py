import dearpygui.dearpygui as imgui
from entity_pointer import show_minimized

class WindowHandle:
    window_tick = 0
    window_toggle = True
    def hide_vp():
        imgui.minimize_viewport()
        return False

    def show_vp():
        show_minimized("Scarlet Nexus Trainer")
        return True

    def drag_viewport():
        drag_deltas = imgui.get_mouse_drag_delta()
        viewport_current_pos = imgui.get_viewport_pos()
        if imgui.is_item_hovered("Primary Window"):
            imgui.set_viewport_pos([viewport_current_pos[0] + drag_deltas[0],viewport_current_pos[1] + drag_deltas[1]])

g_window = WindowHandle