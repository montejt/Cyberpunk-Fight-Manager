import tkinter as tk
import ctypes as ct

from components.initiative_frame import InitiativeFrame
from components.modifier_frame import ModifierFrame
from components.npc_frame import NpcFrame
from components.toolbar_menu import MenuBar
from tools.npcmanager import NpcManager

from style.fonts import *
from style.colors import *

class Application(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=WINDOW_BACKGROUND_COLOR)
        self.pack(side="top", fill="x")

        self.npc_manager = NpcManager()

        # Initialize menu bar
        self.menubar = MenuBar(parent)
        parent.config(menu=self.menubar)

        # Initialize component frames
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.modifier_frame = ModifierFrame(self, self.npc_manager)
        self.modifier_frame.grid(row=0, column=0, sticky="new")

        self.columnconfigure(1, weight=3)
        self.npc_frame = NpcFrame(self, self.npc_manager, self.modifier_frame.refresh_modifiers_frame)
        self.npc_frame.grid(row=0, column=1, sticky="new")

        self.columnconfigure(2, weight=1)
        self.initiative_frame = InitiativeFrame(self)
        self.initiative_frame.grid(row=0, column=2, sticky="new")

def configure_window(window):
    # Dark title bar
    """
    MORE INFO:
    https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value), 4)

    # Dark window background
    window.configure(bg=WINDOW_BACKGROUND_COLOR)

    # Fix blurry fonts due to dpi issues
    ct.windll.shcore.SetProcessDpiAwareness(1)

    # Scale all components
    root.tk.call('tk', 'scaling', 2.0)

root = tk.Tk()
configure_window(root)
app = Application(parent=root)
app.master.title("Cyberpunk Fight Manager")
app.mainloop()
