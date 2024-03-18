import tkinter as tk

from tools.types.conditions import Conditions
from tools.npcmanager import NpcManager

from style.colors import *
from style.fonts import *
from style.numbers import *

class ModifierFrame(tk.Frame):

    def __init__(self, parent, npc_manager: NpcManager):
        super(ModifierFrame, self).__init__(padx=COMPONENT_PADDING, name="mod_frame", bg=WINDOW_BACKGROUND_COLOR)
        self.pack(expand="true", side="left", fill="both")

        self.manager = npc_manager

        self.create_mod_info_frame()

    def create_mod_info_frame(self):
        modifier_frame = tk.Frame(self, bg=PRIMARY_COLOR_ONE, relief="solid", bd=2, name="frame")
        modifier_frame.pack(side="top", fill="both")

        tk.Label(modifier_frame, text="Modifiers", bg=PRIMARY_COLOR_ONE, fg=PRIMARY_COLOR_FG, font=TITLE_FONT).pack(side="top")

        tk.Frame(modifier_frame, name="modifiers").pack(expand="true", side="top", fill="both")

        self.refresh_modifiers_frame()

    def refresh_modifiers_frame(self):
        mods_frame = self.nametowidget("frame.modifiers")

        # Destroy old info
        for child in mods_frame.winfo_children():
            child.destroy()

        curr_mods = set()

        tk.Label(mods_frame, text="Status").grid(row=0, column=0)
        tk.Label(mods_frame, text="Effect").grid(row=0, column=1)
        tk.Label(mods_frame, text="Quick Fix / Stabilization").grid(row=0, column=2)
        tk.Label(mods_frame, text="Treatment").grid(row=0, column=3)

        all_conditions = Conditions.get_all_conditions()

        # Create new info
        conditions = set()
        for npc in self.manager.npcs:
            for modifier in npc.modifiers:
                if modifier in all_conditions.keys():
                    conditions.add(modifier)

        for i, condition in enumerate(conditions):

            effect = all_conditions[condition][0]
            quick_fix = all_conditions[condition][1]
            treatment = all_conditions[condition][2]

            # Name
            tk.Label(mods_frame, text="{}".format(condition), wraplength=100)\
                .grid(row=(i + 1) * 2, column=0, sticky="w", padx=2)

            # Effect
            tk.Label(mods_frame, text="{}".format(effect), justify="left", wraplength=200)\
                .grid(row=(i + 1) * 2, column=1, sticky="w", padx=2)

            # Quick Fix
            if quick_fix is not None:
                tk.Label(mods_frame, text="{}".format(quick_fix), justify="left", bd=0, wraplength=200)\
                    .grid(row=(i + 1) * 2, column=2, sticky="w", padx=2)
                
            # Treatment
            if treatment is not None:
                tk.Label(mods_frame, bd=1, text="{}".format(treatment), justify="left", wraplength=200)\
                    .grid(row=(i + 1) * 2, column=3, sticky="w", padx=2)
