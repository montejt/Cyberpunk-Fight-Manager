import tkinter as tk
import webbrowser

from style.colors import *

class MenuBar(tk.Menu):

    def __init__(self, parent, configure_rangefinder_window, configure_initiative_window):
        super(MenuBar, self).__init__(background=WINDOW_BAR_COLOR, fg=PRIMARY_COLOR_FG)

        # Tools Menu
        self.tool_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Tools", menu=self.tool_menu)
        self.tool_menu.add_command(label="Range Finder", command=lambda: configure_rangefinder_window(parent))
        self.tool_menu.add_command(label="Initiative Tracker", command=lambda: configure_initiative_window(parent))
        
        # Links Menu
        self.links_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Links", menu=self.links_menu)
        self.links_menu.add_command(label="Cheat Sheet", command=lambda: webbrowser.open("https://www.worldanvil.com/w/cyberpunk-red-glodarin/a/rules-cheat-sheet-article"))
        self.links_menu.add_command(label="Night City Map", command=lambda: webbrowser.open("https://i0.wp.com/rtalsoriangames.com/wp-content/uploads/2020/10/NightCity2045Map.jpg?w=1049&ssl=1"))
