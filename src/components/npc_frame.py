import tkinter as tk

from tools.types.damagetype import DamageType
from tools.types.target import Target
from tools.npc import Npc
from tools.npcmanager import NpcManager
from tools.types.conditions import Conditions

from style.colors import *
from style.fonts import *
from style.numbers import *

class NpcFrame(tk.Frame):

    def __init__(self, parent, npc_manager: NpcManager, refresh_modifier_frame):
        super(NpcFrame, self).__init__(master=parent, bg=WINDOW_BACKGROUND_COLOR)

        self.manager = npc_manager

        # Callback to trigger a refresh of the modifiers
        self.refresh_modifier_frame = refresh_modifier_frame

        self.create_npc_manager()

    """
        Creates a Frame to house a list of Npcs, and then populates it with Npcs from the Npc Manager
    """
    def create_npc_manager(self):
        manager_frame = tk.Frame(self, bg=PRIMARY_COLOR_ONE, name="manager_frame", relief="solid", bd=COMPONENT_FRAME_BD)
        manager_frame.pack(side="top", fill="x")

        title = tk.Label(manager_frame, text="Npcs", bg=PRIMARY_COLOR_ONE, fg=PRIMARY_COLOR_FG, font=TITLE_FONT)
        title.pack()

        # Populate the frame with npcs
        populated_npc_frame = tk.Frame(manager_frame, name="populated_npc_frame")
        populated_npc_frame.pack(side="top", fill="x")
        self.populate_npcs(populated_npc_frame)

        # Create the Npc input Frame
        self.create_input_npc_frame(manager_frame, populated_npc_frame)

    """
        Populates the given frame with all Npcs from the Npc Manager. Npcs are listed from top to bottom, and include:
        hp (changeable), spb (changeable), sph (changeable), ds (changeable), and a list of modifiers. Modifiers
        can be added, and removed.
    """
    def populate_npcs(self, populated_npc_frame):
        
        for child in populated_npc_frame.winfo_children():
            child.destroy()

        for npc in self.manager.npcs:
            self.create_npc_frame(populated_npc_frame, npc)

    """
        Creates and populates an npc frame within the parent for the given npc
    """
    def create_npc_frame(self, populated_npc_frame, npc: Npc):
        # Create Frame to house all of the npc's info
        npc_frame = tk.Frame(populated_npc_frame, relief="solid", bd=2)
        npc_frame.pack(side="top", fill="x")

        del_btn = tk.Button(npc_frame, bg=CANCEL_COLOR, text="-", font=DEL_FONT, command=lambda: self.delete_npc(populated_npc_frame, npc))
        del_btn.pack(side="right", fill="y")

        name_label = tk.Label(npc_frame, text=npc.name)
        name_label.pack(side="top", fill="x")

        # The info frame holds all the npc's stats
        info_frame = tk.Frame(npc_frame, name="info_frame")
        info_frame.pack(side="top")

        # HP
        tk.Label(info_frame, text="HP:").pack(side="left", padx=SMALL_TEXT_PADDING)
        hpvar = tk.IntVar()
        hpvar.set(npc.hp)
        hp_entry = tk.Entry(info_frame, textvariable=hpvar, name="hp", width=SMALL_ENTRY_SIZE, justify="center")
        hp_entry.pack(side="left")
        hp_entry.bind("<Key-Return>", lambda event: self.set_npc_hp(npc, hpvar.get()))
        hp_entry.bind("<FocusOut>", lambda event: self.set_npc_hp(npc, hpvar.get()))
        tk.Label(info_frame, text=" / " + str(npc.maxhp)).pack(side="left")

        # SPH
        tk.Label(info_frame, text="SPH:").pack(side="left")
        sphvar = tk.IntVar()
        sphvar.set(npc.sph)
        sph_entry = tk.Entry(info_frame, textvariable=sphvar, name="sph", width=SMALL_ENTRY_SIZE, justify="center")
        sph_entry.pack(side="left")
        sph_entry.bind("<Key-Return>", lambda event: self.set_npc_sph(npc, sphvar.get()))
        sph_entry.bind("<FocusOut>", lambda event: self.set_npc_sph(npc, sphvar.get()))
        tk.Label(info_frame, text=" / " + str(npc.maxsph)).pack(side="left")

        # SPB
        tk.Label(info_frame, text="SPB:").pack(side="left")
        spbvar = tk.IntVar()
        spbvar.set(npc.spb)
        spb_entry = tk.Entry(info_frame, textvariable=spbvar, name="spb", width=SMALL_ENTRY_SIZE, justify="center")
        spb_entry.pack(side="left")
        spb_entry.bind("<Key-Return>", lambda event: self.set_npc_spb(npc, spbvar.get()))
        spb_entry.bind("<FocusOut>", lambda event: self.set_npc_spb(npc, spbvar.get()))
        tk.Label(info_frame, text=" / " + str(npc.maxspb)).pack(side="left")

        # DS
        tk.Label(info_frame, text="DS:").pack(side="left")
        dsvar = tk.IntVar()
        dsvar.set(npc.ds)
        ds_entry = tk.Entry(info_frame, textvariable=dsvar, name="ds", width=SMALL_ENTRY_SIZE, justify="center")
        ds_entry.pack(side="left")
        ds_entry.bind("<Key-Return>", lambda event: npc. self.set_npc_ds(npc, dsvar.get()))
        ds_entry.bind("<FocusOut>", lambda event: self.set_npc_ds(npc, dsvar.get()))

        # Create the hurt frame
        self.create_npc_hurt_frame(npc_frame, npc)

        # Create frame to hold modifier option menu and modifiers
        modsframe = tk.Frame(npc_frame)
        modsframe.pack(side="top", fill="x")

        input_mod_frame = tk.Frame(modsframe)
        input_mod_frame.pack(side="left")

        mod_selected = tk.StringVar()
        mod_selected.set("CONDITION")
        mod_drop = tk.OptionMenu(input_mod_frame, mod_selected, *Conditions.get_all_conditions().keys())
        mod_drop.pack(side="left")

        confirm_image = tk.PhotoImage(file="src/resources/confirm_button.png").subsample(CONFIRM_BUTTON_SUBSAMPLE, CONFIRM_BUTTON_SUBSAMPLE)
        mod_add_btn = tk.Button(input_mod_frame, image=confirm_image, bd=0, padx=0, pady=0,
                                command=lambda modsframe=modsframe, npc=npc, mod_input=mod_selected:
                                self.add_modifier(modsframe, npc, mod_input))
        mod_add_btn.image = confirm_image
        mod_add_btn.pack(side="right")

        # Create the frame for modifiers. Each modifier has text and a delete button
        for modifier in npc.modifiers:
            self.create_npc_modifier_frame(modsframe, npc, modifier)

        # Refresh the modifiers info frame
        self.refresh_modifier_frame()

    def create_npc_hurt_frame(self, npc_frame, npc):
        # Create the hurt frame
        frame = tk.Frame(npc_frame)
        frame.pack(side="top")

        # Create the hurt button
        hurt_btn = tk.Button(frame, text="DMG", relief="raised", bd=5, bg=HURT_BTN_COLOR, font=HURT_FONT)
        hurt_btn.pack(side="left", fill="y", padx=5)

        # Create the Damage frame
        dmg_frame = tk.Frame(frame)
        dmg_frame.pack(side="left", fill="y")
        tk.Label(dmg_frame, text="DMG").pack(side="top")
        dmg_value = tk.IntVar()
        dmg_entry = tk.Entry(dmg_frame, textvariable=dmg_value, width=SMALL_ENTRY_SIZE, justify="center")
        dmg_entry.pack(side="bottom", padx=5)

        # Create the damage type Frame
        type_frame = tk.Frame(frame)
        type_frame.pack(side="left", padx=5)
        tk.Label(type_frame, text="TYPE").pack(side="top")
        type_def = tk.StringVar()
        type_def.set(DamageType.STANDARD.value)
        type_menu = tk.OptionMenu(type_frame, type_def, *[dt.value for dt in DamageType])
        type_menu.config(width=TYPE_SELECTOR_WIDTH)
        type_menu.pack(side="left")

        # Create the damage target Frame
        target_frame = tk.Frame(frame)
        target_frame.pack(side="left", padx=5)
        tk.Label(target_frame, text="TARGET").pack(side="top")
        target_def = tk.StringVar()
        target_def.set(Target.BODY.value)
        target_menu = tk.OptionMenu(target_frame, target_def, *[t.value for t in Target])
        target_menu.config(width=TARGET_SELECTOR_WIDTH)
        target_menu.pack(side="left")

        # Create the crit Button
        crit_frame = tk.Frame(frame)
        crit_frame.pack(side="left", padx=5)
        tk.Label(crit_frame, text="Crit").pack(side="top")
        crit_var = tk.IntVar()
        crit_btn = tk.Checkbutton(crit_frame, variable=crit_var)
        crit_btn.pack(side="bottom")

        # Hurt button will call the hurt function when clicked
        hurt_btn["command"] = lambda: self.hurt_npc(npc_frame, npc, dmg_value, type_def, target_def, crit_var)

    def hurt_npc(self, npc_frame, npc: Npc, dmg_var, dmg_type_var, target_var, crit_var):
        if dmg_var.get() >= 0:
            self.manager.hurt(npc.name, dmg_var.get(), dmg_type_var.get(), target_var.get(), crit_var.get() == 1)

            # Update gui npc values
            self.update_npc(npc_frame, npc)
        else:
            print("Invalid hurt user gui input")

    def update_npc(self, npc_frame, npc):
        hp_entry = npc_frame.nametowidget("info_frame.hp")
        hp_entry.delete(0, tk.END)
        hp_entry.insert(0, npc.hp)

        sph_entry = npc_frame.nametowidget("info_frame.sph")
        sph_entry.delete(0, tk.END)
        sph_entry.insert(0, npc.sph)

        spb_entry = npc_frame.nametowidget("info_frame.spb")
        spb_entry.delete(0, tk.END)
        spb_entry.insert(0, npc.spb)

        ds_entry = npc_frame.nametowidget("info_frame.ds")
        ds_entry.delete(0, tk.END)
        ds_entry.insert(0, npc.ds)

    """
        Creates a template Npc Frame as a child of the given parent. This Frame can be filled out and used to create
        an Npc and populated Npc Frame
    """
    def create_input_npc_frame(self, manager_frame, populated_npc_frame):
        # Overall frame, which houses input Frame, and the button Frame
        frame = tk.Frame(manager_frame, pady=10, relief="sunken", bd=10, name="npc_input_frame")
        frame.pack(side="top", fill="x")

        # Create the Input Frame
        input_frame = tk.Frame(frame)
        input_frame.pack(side="left")

        namevar = tk.StringVar()
        namevar.set("NAME")
        name_input = tk.Entry(input_frame, textvariable=namevar, width=MED_ENTRY_SIZE)
        name_input.pack(side="top")

        # Create and fill the info frame
        info_frame = tk.Frame(input_frame)
        info_frame.pack(side="top")

        # HP
        tk.Label(info_frame, text="HP:").pack(side="left", padx=SMALL_TEXT_PADDING)
        hpvar = tk.IntVar()
        tk.Entry(info_frame, textvariable=hpvar, name="inputhp", width=SMALL_ENTRY_SIZE, justify="center")\
            .pack(side="left", padx=SMALL_TEXT_PADDING)

        # SPH
        tk.Label(info_frame, text="SPH:").pack(side="left")
        sphvar = tk.IntVar()
        tk.Entry(info_frame, textvariable=sphvar, name="inputsph", width=SMALL_ENTRY_SIZE, justify="center")\
            .pack(side="left", padx=SMALL_TEXT_PADDING)

        # SPB
        tk.Label(info_frame, text="SPB:").pack(side="left")
        spbvar = tk.IntVar()
        tk.Entry(info_frame, textvariable=spbvar, name="inputspb", width=SMALL_ENTRY_SIZE, justify="center")\
            .pack(side="left", padx=SMALL_TEXT_PADDING)

        # DS
        tk.Label(info_frame, text="DS:").pack(side="left")
        dsvar = tk.IntVar()
        tk.Entry(info_frame, textvariable=dsvar, name="inputds", width=SMALL_ENTRY_SIZE, justify="center")\
            .pack(side="left", padx=SMALL_TEXT_PADDING)

        # Create the button Frame, which houses the add button
        btn_frame = tk.Frame(frame)
        btn_frame.pack(side="right", fill="y")

        add_btn = tk.Button(btn_frame, text="+", bg=CONFIRM_COLOR, font=ADD_FONT,
                            command=lambda: self.create_npc(populated_npc_frame, namevar, hpvar, sphvar, spbvar, dsvar))
        add_btn.pack(side="right", fill="y")

    """
        Creates and packs a modifier frame within the given parent for the given npc. The modifier has the given name
    """
    def create_npc_modifier_frame(self, parent, npc, modifier):
        modframe = tk.Frame(parent)
        modframe.pack(side="left")

        tk.Label(modframe, text=modifier).pack(side="left")

        cancel_image = tk.PhotoImage(file="src/resources/cancel_button.png").subsample(CANCEL_BUTTON_SUBSAMPLE, CANCEL_BUTTON_SUBSAMPLE)
        mod_del_btn = tk.Button(modframe, image=cancel_image, bd=0, padx=0, pady=0,
                                command=lambda: self.delete_modifier(modframe, npc, modifier))
        # Save image as reference to avoid garbage collection: https://stackoverflow.com/questions/22200003/tkinter-button-not-showing-image
        mod_del_btn.image = cancel_image
        mod_del_btn.pack(side="left")

    """
        Destroys the given frame (meant to be a modifier Frame), and removes the given modifier from the given npc
    """
    def delete_modifier(self, frame, npc, modifier):
        frame.destroy()
        npc.modifiers.remove(modifier)

        # Refresh the modifier info frame
        self.refresh_modifier_frame()

    """
        Adds the modifier in the given mod_input to the npc (then clears it), and creates a mod Frame and fills it:
        adding it to the given modsframe
    """
    def add_modifier(self, modsframe, npc, mod_input: tk.StringVar):
        modifier = mod_input.get()
        mod_input.set("CONDITION")
        npc.modifiers.append(modifier)
        self.create_npc_modifier_frame(modsframe, npc, modifier)

        # Refresh the modifier info frame
        self.refresh_modifier_frame()

    """
        Creates an Npc using the given info, adds them to the Npc Manager, and then creates and populates an Npc Frame
        for the created Npc as a child of the given parent Frame.
    """
    def create_npc(self, populated_npc_frame, name, hp, sph, spb, ds):
        if hp.get() != "" and sph.get() != "" and spb.get() != "" and ds.get() != "" and self.manager.get(name.get()) is None:
            npc = Npc(name.get(), hp.get(), sph.get(), spb.get(), ds.get())
            self.manager.add(npc)

            self.populate_npcs(populated_npc_frame)

    def delete_npc(self, populated_npc_frame, npc):
        self.manager.remove(npc)

        self.populate_npcs(populated_npc_frame)
        self.refresh_modifier_frame()

    def set_npc_ds(self, npc, ds):
        npc.ds = ds
        print("Set {} ds to {}".format(npc.name, ds))

    def set_npc_spb(self, npc, spb):
        npc.spb = spb
        print("Set {} spb to {}".format(npc.name, spb))

    def set_npc_sph(self, npc, sph):
        npc.sph = sph
        print("Set {} sph to {}".format(npc.name, sph))

    def set_npc_hp(self, npc, hp):
        npc.hp = hp
        print("Set {} hp to {}".format(npc.name, hp))
