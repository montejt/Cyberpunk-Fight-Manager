import tkinter as tk
import ctypes as ct
import logging
from tkinter.scrolledtext import ScrolledText

from components.initiative_frame import InitiativeFrame
from components.modifier_frame import ModifierFrame
from components.npc_frame import NpcFrame
from components.toolbar_menu import MenuBar
from components.text_handler import TextHandler
from components.rangefinder_frame import RangeFinderFrame
from tools.npcmanager import NpcManager

from style.fonts import *
from style.colors import *

class Application(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=WINDOW_BACKGROUND_COLOR)
        self.pack(side="top", fill="both")

        self.npc_manager = NpcManager()

        # Initialize menu bar
        self.menubar = MenuBar(parent)
        parent.config(menu=self.menubar)

        # Initialize component frames
        self.rowconfigure(0, weight=1)
        self.modifier_frame = ModifierFrame(self, self.npc_manager)
        self.npc_frame = NpcFrame(self, self.npc_manager, self.modifier_frame.refresh_modifiers_frame)
        self.initiative_frame = InitiativeFrame(self)

        # Add text widget to damage log info
        st = ScrolledText(parent, state='disabled', bg=WINDOW_BACKGROUND_COLOR, fg=PRIMARY_COLOR_FG)
        st.configure(font='TkFixedFont')
        st.pack(side='bottom', fill='x')

        # Configure logging into the scrolled text
        text_handler = TextHandler(st)
        logging.basicConfig(filename='test.log', level=logging.INFO, format='%(message)s')        
        logger = logging.getLogger()
        logger.addHandler(text_handler)

def configure_rangefinder_window(root):
    rangefinder_window = tk.Toplevel(root)
    rangefinder_window.transient(root)
    rangefinder_window.title("Range Finder")
    configure_window(rangefinder_window)

    range_frame = RangeFinderFrame(rangefinder_window)

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

primary_app = Application(root)
primary_app.master.title("Cyberpunk Fight Manager")

configure_rangefinder_window(root)

primary_app.mainloop()
