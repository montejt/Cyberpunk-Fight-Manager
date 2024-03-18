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

        frame = tk.Frame(self, bg=PRIMARY_COLOR_ONE, name="frame", relief="solid", bd=COMPONENT_FRAME_BD)
        frame.pack(side="top", fill="x")

        tk.Label(frame, text="Conditions", bg=PRIMARY_COLOR_ONE, fg=PRIMARY_COLOR_FG, font=TITLE_FONT)\
            .pack(side="top", fill="x")

        mods_frame = tk.Frame(frame, name="modifiers")
        mods_frame.pack(side="top", fill="x")

        # Unify col weights to enable scaling
        for i in range(CONDITIONS_COLUMNS):
            mods_frame.columnconfigure(i, weight=1)

        self.refresh_modifiers_frame()

    def refresh_modifiers_frame(self):
        mods_frame = self.nametowidget("frame.modifiers")

        # Destroy old info
        for child in mods_frame.winfo_children():
            child.destroy()

        tk.Label(mods_frame, text="Status").grid(row=0, column=0, sticky='ew')
        tk.Label(mods_frame, text="Effect").grid(row=0, column=1, sticky='ew')
        tk.Label(mods_frame, text="Quick Fix / Stabilization").grid(row=0, column=2, sticky='ew')
        tk.Label(mods_frame, text="Treatment").grid(row=0, column=3, sticky='ew')

        all_conditions = Conditions.get_all_conditions()

        # Create new info
        conditions = set()
        for npc in self.manager.npcs:
            for modifier in npc.modifiers:
                if modifier in all_conditions.keys():
                    conditions.add(modifier)

        for i, condition in enumerate(conditions):

            curr_row = i + 1
            curr_row_color = BG_COLOR_ONE if curr_row % 2 == 1 else BG_COLOR_TWO

            effect = all_conditions[condition][0]
            quick_fix = all_conditions[condition][1]
            treatment = all_conditions[condition][2]

            # Name
            tk.Label(mods_frame, text="{}".format(condition), wraplength=100, bg=curr_row_color)\
                .grid(row=curr_row, column=0, sticky="nesw", padx=0, ipadx=2)

            # Effect
            tk.Label(mods_frame, text="{}".format(effect), justify="left", wraplength=200, bg=curr_row_color)\
                .grid(row=curr_row, column=1, sticky="nesw", padx=0, ipadx=2)

            # Quick Fix
            tk.Label(mods_frame, text="{}".format(quick_fix if quick_fix is not None else ""), justify="left", wraplength=200, bg=curr_row_color)\
                .grid(row=curr_row, column=2, sticky="nesw", padx=0, ipadx=2)
                
            # Treatment
            tk.Label(mods_frame, bd=1, text="{}".format(treatment if treatment is not None else ""), justify="left", wraplength=200, bg=curr_row_color)\
                .grid(row=curr_row, column=3, sticky="nesw", padx=0, ipadx=2)
