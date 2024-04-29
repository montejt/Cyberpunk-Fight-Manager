import tkinter as tk
import webbrowser

from style.colors import *

class MenuBar(tk.Menu):

    def __init__(self, parent, configureRangeFinder):
        super(MenuBar, self).__init__(background=WINDOW_BAR_COLOR, fg=PRIMARY_COLOR_FG)

        self.tool_menu = tk.Menu(self, tearoff=0)

        self.tool_menu.add_command(label="Cheat Sheet", command=lambda: webbrowser.open("https://www.worldanvil.com/w/cyberpunk-red-glodarin/a/rules-cheat-sheet-article"))
        self.tool_menu.add_command(label="Night City Map", command=lambda: webbrowser.open("https://i0.wp.com/rtalsoriangames.com/wp-content/uploads/2020/10/NightCity2045Map.jpg?w=1049&ssl=1"))
        self.add_cascade(label="Tools", menu=self.tool_menu)
        self.tool_menu.add_command(label="Range Finder", command=lambda: configureRangeFinder(parent))
