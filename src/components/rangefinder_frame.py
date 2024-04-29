import tkinter as tk

from style.fonts import DV_FONT, HURT_FONT, NUMBER_INPUT_FONT
from style.colors import HURT_BTN_COLOR, PRIMARY_COLOR_ONE, WINDOW_BACKGROUND_COLOR
from style.numbers import RANGE_ENTRY_SIZE
from tools.types.ranges import RangeType
from tools.types.weapons import Weapon
from tools.rangefinder import calc_range_dv
from util.options_menu import calc_max_pixel_width

class RangeFinderFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=WINDOW_BACKGROUND_COLOR)
        self.create_input_frame(parent)
        
    def create_input_frame(self, parent):
        input_frame = tk.Frame(parent)
        input_frame.pack(side="top", fill="x")

        # Weapon selector
        selected_weapon = tk.Variable()
        selected_weapon.set(Weapon.PISTOL)
        weapon_drop = tk.OptionMenu(input_frame, selected_weapon, *[e for e in Weapon])
        weapon_drop.config(width=calc_max_pixel_width([e.value for e in Weapon]))
        weapon_drop.pack(side="left")

        # Range input
        inputted_range = tk.IntVar()
        inputted_range.set(0)
        range_entry = tk.Entry(input_frame, textvariable=inputted_range, width=RANGE_ENTRY_SIZE,
                               justify="center", font=NUMBER_INPUT_FONT)
        range_entry.pack(side="left", fill="y")

        # Range type selector
        selected_type = tk.Variable()
        selected_type.set(RangeType.FEET)
        type_drop = tk.OptionMenu(input_frame, selected_type, *[e for e in RangeType])
        type_drop.config(width=calc_max_pixel_width([e.value for e in RangeType]))
        type_drop.pack(side="left")

        # Calculated DV label
        dv_label = tk.Label(parent, text="0", font=DV_FONT, bg=WINDOW_BACKGROUND_COLOR, fg=PRIMARY_COLOR_ONE)
        dv_label.pack(side="top")

        # Calculate button
        calc_range_btn = tk.Button(input_frame, text="CALC", bd=3, relief="raised", bg=HURT_BTN_COLOR, font=HURT_FONT,
                                   command=lambda:
                                   dv_label.config(text=(str(calc_range_dv(selected_weapon.get(), inputted_range.get(), selected_type.get())))))
        calc_range_btn.pack(side="right")
