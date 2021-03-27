import tkinter as tk
from tkinter import scrolledtext

from FightManager import NpcManager as nm
from FightManager import InitiativeQueue as iq
from FightManager.Npc import Npc

SMALL_ENTRY_SIZE = 5
MED_ENTRY_SIZE = 20
QUEUE_PADDING = 10

CANCEL_COLOR = "#ff3b48"
CONFIRM_COLOR = "#00d123"

MODIFIERS_FRAME = "mod_frame.frame.modifiers"

queue = iq.InitiativeQueue()
manager = nm.NpcManager()

""""""

queue.add("bob", 17)
queue.add("him", 16)

manager.add(Npc("bob", 30, 11, 11, 3))
manager.get("bob").modifiers.append("mortally wounded")
manager.get("bob").modifiers.append("broken leg")
""""""


def set_npc_ds(npc, ds):
    npc.ds = ds
    print("Set {} ds to {}".format(npc.name, ds))


def set_npc_spb(npc, spb):
    npc.spb = spb
    print("Set {} spb to {}".format(npc.name, spb))


def set_npc_sph(npc, sph):
    npc.sph = sph
    print("Set {} sph to {}".format(npc.name, sph))


def set_npc_hp(npc, hp):
    npc.hp = hp
    print("Set {} hp to {}".format(npc.name, hp))


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        mod_frame = tk.Frame(self, padx=QUEUE_PADDING, name="mod_frame")
        mod_frame.pack(side="left", fill="both")

        self.create_mod_info_frame(mod_frame)

        npc_frame = tk.Frame(self)
        npc_frame.pack(side="left")

        # Create the interactive npc manager gui
        self.create_npc_manager(npc_frame)

        queue_frame = tk.Frame(self, padx=QUEUE_PADDING)
        queue_frame.pack(side="right", fill="y")

        # Create the initiative queue gui
        self.create_initiative_queue(queue_frame)

    def create_mod_info_frame(self, parent):
        modifier_frame = tk.Frame(parent, bg="red", relief="solid", bd=2, name="frame")
        modifier_frame.pack(side="top", fill="both")

        tk.Label(modifier_frame, text="Modifiers").pack(side="top")

        tk.Frame(modifier_frame, name="modifiers").pack(side="top")

        self.refresh_modifiers_frame()

    """
        Creates a Frame to house a list of Npcs, and then populates it with Npcs from the Npc Manager. Parent of the
        frame is given
    """
    def create_npc_manager(self, parent):
        manager_frame = tk.Frame(parent, bg="red", name="managerframe", relief="solid", bd=2)
        manager_frame.pack(side="top")

        title = tk.Label(manager_frame, text="Npcs", name="manager_title")
        title.pack()

        # Populate the frame with npcs
        self.populate_npcs(manager_frame)

        # Create the Npc input Frame
        self.create_input_npc_frame(manager_frame)

    """
        Populates the given frame with all Npcs from the Npc Manager. Npcs are listed from top to bottom, and include:
        hp (changeable), spb (changeable), sph (changeable), ds (changeable), and a list of modifiers. Modifiers
        can be added, and removed.
    """
    def populate_npcs(self, frame):
        for npc in manager.npcs:
            self.create_npc_frame(frame, npc)

    """
        Creates and populates an npc frame within the parent for the given npc
    """
    def create_npc_frame(self, parent, npc):
        # Create Frame to house npc frame and button frame
        frame = tk.Frame(parent, relief="solid", bd=2, name=npc.name.lower() + "_npc_main_frame")
        frame.pack(side="top", fill="x")

        npc_frame = tk.Frame(frame, name="npc_frame")
        npc_frame.pack(side="left")

        name_label = tk.Label(npc_frame, text=npc.name)
        name_label.pack(side="top")

        # Create and fill the info frame
        info_frame = tk.Frame(npc_frame, name="info_frame")
        info_frame.pack(side="top")

        # HP
        tk.Label(info_frame, text="HP:").pack(side="left")
        hpvar = tk.IntVar()
        hpvar.set(npc.hp)
        hp_entry = tk.Entry(info_frame, textvariable=hpvar, name="hp", width=SMALL_ENTRY_SIZE)
        hp_entry.pack(side="left")
        hp_entry.bind("<Key-Return>", lambda event: set_npc_hp(npc, hpvar.get()))
        hp_entry.bind("<FocusOut>", lambda event: set_npc_hp(npc, hpvar.get()))
        tk.Label(info_frame, text="/" + str(npc.maxhp)).pack(side="left")

        # SPH
        tk.Label(info_frame, text="SPH:").pack(side="left")
        sphvar = tk.IntVar()
        sphvar.set(npc.sph)
        sph_entry = tk.Entry(info_frame, textvariable=sphvar, name="sph", width=SMALL_ENTRY_SIZE)
        sph_entry.pack(side="left")
        sph_entry.bind("<Key-Return>", lambda event: set_npc_sph(npc, sphvar.get()))
        sph_entry.bind("<FocusOut>", lambda event: set_npc_sph(npc, sphvar.get()))
        tk.Label(info_frame, text="/" + str(npc.maxsph)).pack(side="left")

        # SPB
        tk.Label(info_frame, text="SPB:").pack(side="left")
        spbvar = tk.IntVar()
        spbvar.set(npc.spb)
        spb_entry = tk.Entry(info_frame, textvariable=spbvar, name="spb", width=SMALL_ENTRY_SIZE)
        spb_entry.pack(side="left")
        spb_entry.bind("<Key-Return>", lambda event: set_npc_spb(npc, spbvar.get()))
        spb_entry.bind("<FocusOut>", lambda event: set_npc_spb(npc, spbvar.get()))
        tk.Label(info_frame, text="/" + str(npc.maxspb)).pack(side="left")

        # DS
        tk.Label(info_frame, text="DS:").pack(side="left")
        dsvar = tk.IntVar()
        dsvar.set(npc.ds)
        ds_entry = tk.Entry(info_frame, textvariable=dsvar, name="ds", width=SMALL_ENTRY_SIZE)
        ds_entry.pack(side="left")
        ds_entry.bind("<Key-Return>", lambda event: set_npc_ds(npc, dsvar.get()))
        ds_entry.bind("<FocusOut>", lambda event: set_npc_ds(npc, dsvar.get()))

        # Create an add button for new modifiers
        modsframe = tk.Frame(npc_frame)
        modsframe.pack(side="top")

        input_mod_frame = tk.Frame(modsframe)
        input_mod_frame.pack(side="left")

        mod_input = tk.StringVar()
        mod_input.set("MODIFIER")
        tk.Entry(input_mod_frame, textvariable=mod_input, width=MED_ENTRY_SIZE).pack(side="left")

        mod_add_btn = tk.Button(input_mod_frame, text="+", bg=CONFIRM_COLOR,
                                command=lambda modsframe=modsframe, npc=npc, mod_input=mod_input:
                                self.add_modifier(modsframe, npc, mod_input))
        mod_add_btn.pack(side="right")

        # Create the frame for modifiers. Each modifier has text and a delete button
        for modifier in npc.modifiers:
            self.create_modifier_frame(modsframe, npc, modifier)

        # Create the delete button Frame
        del_btn_frame = tk.Frame(frame)
        del_btn_frame.pack(side="right", fill="y")

        del_btn = tk.Button(del_btn_frame, bg=CANCEL_COLOR, text="X",
                            command=lambda: self.delete_npc(frame, npc))
        del_btn.pack(side="right", fill="y")

        # Create the hurt frame
        self.create_npc_hurt_frame(npc_frame, npc)

        # Refresh the modifiers info frame
        self.refresh_modifiers_frame()

    def create_npc_hurt_frame(self, parent, npc):
        # Create the hurt frame
        frame = tk.Frame(parent)
        frame.pack(side="bottom")

        # Create the hurt button
        hurt_btn = tk.Button(frame, text="Hurt")
        hurt_btn.pack(side="left", padx=5)

        # Create the Damage frame
        dmg_frame = tk.Frame(frame)
        dmg_frame.pack(side="left")
        tk.Label(dmg_frame, text="DMG").pack(side="top")
        dmg_value = tk.IntVar()
        dmg_entry = tk.Entry(dmg_frame, textvariable=dmg_value, width=SMALL_ENTRY_SIZE)
        dmg_entry.pack(side="bottom", padx=5)

        # Create the damage type Frame
        type_frame = tk.Frame(frame)
        type_frame.pack(side="left", padx=5)
        tk.Label(type_frame, text="TYPE").pack(side="top")
        type_def = tk.StringVar()
        type_def.set("Select Type")
        type_menu = tk.OptionMenu(type_frame, type_def, *["Default", "Melee", "Armor Piercing", "Armor Breaking", "Straight"])
        type_menu.pack(side="left")

        # Create the damage target Frame
        target_frame = tk.Frame(frame)
        target_frame.pack(side="left", padx=5)
        tk.Label(target_frame, text="TARGET").pack(side="top")
        target_def = tk.StringVar()
        target_def.set("Select Target")
        target_menu = tk.OptionMenu(target_frame, target_def, *["Body", "Head"])
        target_menu.pack(side="left")

        # Create the crit Button
        crit_frame = tk.Frame(frame)
        crit_frame.pack(side="left", padx=5)
        tk.Label(crit_frame, text="Crit").pack(side="top")
        crit_var = tk.IntVar()
        crit_btn = tk.Checkbutton(crit_frame, variable=crit_var)
        crit_btn.pack(side="bottom")

        # Hurt button will call the hurt function when clicked
        hurt_btn["command"] = lambda: self.hurt_npc(parent.master, npc, dmg_value, type_def, target_def, crit_var)

    def hurt_npc(self, manager_frame, npc, dmg_var, dmg_type_var, target_var, crit_var):
        if dmg_var.get() >= 0 and dmg_type_var.get() != "Select Type" and target_var.get() != "Select Target" and crit_var.get() in [0, 1]:
            npc.hurt(dmg_var.get(), dmg_type_var.get().lower(), target_var.get().lower(), crit_var.get() == 1)

            # Update gui npc values
            self.update_npc(manager_frame, npc)
        else:
            print("Invalid hurt user gui input")

    def update_npc(self, manager_frame, npc):
        hp_entry = manager_frame.nametowidget("npc_frame.info_frame.hp")
        hp_entry.delete(0, tk.END)
        hp_entry.insert(0, npc.hp)

        sph_entry = manager_frame.nametowidget("npc_frame.info_frame.sph")
        sph_entry.delete(0, tk.END)
        sph_entry.insert(0, npc.sph)

        spb_entry = manager_frame.nametowidget("npc_frame.info_frame.spb")
        spb_entry.delete(0, tk.END)
        spb_entry.insert(0, npc.spb)

        ds_entry = manager_frame.nametowidget("npc_frame.info_frame.ds")
        ds_entry.delete(0, tk.END)
        ds_entry.insert(0, npc.ds)

    """
        Creates a template Npc Frame as a child of the given parent. This Frame can be filled out and used to create
        an Npc and populated Npc Frame
    """
    def create_input_npc_frame(self, parent):
        # Overall frame, which houses input Frame, and the button Frame
        frame = tk.Frame(parent, pady=10, relief="sunken", bd=10, name="npc_input_frame")
        frame.pack(side="bottom", fill="x")

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
        tk.Label(info_frame, text="HP:").pack(side="left")
        hpvar = tk.IntVar()
        tk.Entry(info_frame, textvariable=hpvar, name="inputhp", width=SMALL_ENTRY_SIZE).pack(side="left")

        # SPH
        tk.Label(info_frame, text="SPH:").pack(side="left")
        sphvar = tk.IntVar()
        tk.Entry(info_frame, textvariable=sphvar, name="inputsph", width=SMALL_ENTRY_SIZE).pack(side="left")

        # SPB
        tk.Label(info_frame, text="SPB:").pack(side="left")
        spbvar = tk.IntVar()
        tk.Entry(info_frame, textvariable=spbvar, name="inputspb", width=SMALL_ENTRY_SIZE).pack(side="left")

        # DS
        tk.Label(info_frame, text="DS:").pack(side="left")
        dsvar = tk.IntVar()
        tk.Entry(info_frame, textvariable=dsvar, name="inputds", width=SMALL_ENTRY_SIZE).pack(side="left")

        # Create the button Frame, which houses the add button
        btn_frame = tk.Frame(frame)
        btn_frame.pack(side="right", fill="y")

        add_btn = tk.Button(btn_frame, text="+", bg=CONFIRM_COLOR, font=('Helvetica', '12', "bold"),
                            command=lambda: self.create_npc(parent, namevar, hpvar, sphvar, spbvar, dsvar))
        add_btn.pack(side="right", fill="y")

    """
        Creates an autosorted and interactable initiative queue
    """
    def create_initiative_queue(self, parent):
        frame = tk.Frame(parent, bg="red", name="initframe", relief="solid", bd=2)
        frame.pack(side="top")

        title = tk.Label(frame, text="Initiative Queue", name="queuelabel")
        title.pack()

        self.fill_initiative_queue(frame)

    """
        Fills the given frame with an interactable auto-sorting initiative queue
    """
    def fill_initiative_queue(self, frame):
        # Clear old queue
        for child in (c for c in frame.winfo_children() if c.winfo_name() != "queuelabel"):
            child.destroy()
        # Fill the queue with entries
        for name, initiative in queue.queue:
            # Create the name label
            entryframe = tk.Frame(frame, relief="solid", bd=2)
            entryframe.pack(side="top", fill="x")
            entryname = tk.Label(entryframe, text=name, anchor="center")
            entryname.pack(side="left", fill="x")

            # Create a delete button
            deletebtn = tk.Button(entryframe, text="DEL", bg=CANCEL_COLOR,
                                  command=lambda entryframe=entryframe, name=name: remove_queue_entry(entryframe, name))
            deletebtn.pack(side="right")

            # Create initiative entry
            initvar = tk.IntVar()
            initvar.set(initiative)
            entryinit = tk.Entry(entryframe, textvariable=initvar, width=SMALL_ENTRY_SIZE)
            entryinit.bind("<Key-Return>", lambda event, n=name, i=initvar: self.update_queue_entry(frame, n, i.get()))
            entryinit.bind("<FocusOut>", lambda event, n=name, i=initvar: self.update_queue_entry(frame, n, i.get()))
            entryinit.pack(side="right")



        # Create a custom entry
        customframe = tk.Frame(frame)
        customframe.pack(side="top", fill="x")

        namevar = tk.StringVar()
        namevar.set("NAME")
        entername = tk.Entry(customframe, textvariable=namevar, width=MED_ENTRY_SIZE)
        entername.pack(side="left", fill="x")

        initiative = tk.IntVar()
        initiative.set("0")
        enterinit = tk.Entry(customframe, textvariable=initiative, width=SMALL_ENTRY_SIZE)
        enterinit.pack(side="left")

        # Create an add button, which adds the inputted entry
        addbtn = tk.Button(customframe, text="ADD", bg=CONFIRM_COLOR,
                           command=lambda: self.add_queue_entry(frame, namevar.get(), initiative.get()))
        addbtn.pack(side="right")

    """
        Adds the given name and initiative to the queue, and refreshes the gui
    """
    def add_queue_entry(self, frame, name, initative):
        queue.add(name, initative)
        self.fill_initiative_queue(frame)

    """
        Updates the initiative of the given name to be the given initiative and then refreshes the initative queue gui
    """
    def update_queue_entry(self, frame, name, initiative):
        if queue.get_initiative(name) != initiative:
            # Initiative has updated, so update in backend
            queue.remove(name)
            queue.add(name, initiative)
            self.fill_initiative_queue(frame)

    """
        Creates and packs a modifier frame within the given parent for the given npc. The modifier has the given name
    """
    def create_modifier_frame(self, parent, npc, modifier):
        modframe = tk.Frame(parent)
        modframe.pack(side="left")

        tk.Label(modframe, text=modifier).pack(side="left")

        mod_del_btn = tk.Button(modframe, text="X", bg=CANCEL_COLOR, height=0,
                                command=lambda: self.delete_modifier(modframe, npc, modifier))
        mod_del_btn.pack(side="right")

    """
        Destroys the given frame (meant to be a modifier Frame), and removes the given modifier from the given npc
    """
    def delete_modifier(self, frame, npc, modifier):
        frame.destroy()
        npc.modifiers.remove(modifier)

        # Refresh the modifier info frame
        self.refresh_modifiers_frame()

    """
        Adds the modifier in the given mod_input to the npc (then clears it), and creates a mod Frame and fills it:
        adding it to the given modsframe
    """
    def add_modifier(self, modsframe, npc, mod_input):
        modifier = mod_input.get()
        mod_input.set("")
        npc.modifiers.append(modifier)
        self.create_modifier_frame(modsframe, npc, modifier)

        # Refresh the modifier info frame
        self.refresh_modifiers_frame()

    """
        Creates an Npc using the given info, adds them to the Npc Manager, and then creates and populates an Npc Frame
        for the created Npc as a child of the given parent Frame.
    """
    def create_npc(self, parent, name, hp, sph, spb, ds):
        if hp.get() != "" and sph.get() != "" and spb.get() != "" and ds.get() != "" and manager.get(name.get()) is None:
            npc = Npc(name.get(), hp.get(), sph.get(), spb.get(), ds.get())
            manager.add(npc)
            self.create_npc_frame(parent, npc)

    def delete_npc(self, npc_frame, npc):
        npc_frame.destroy()
        manager.remove(npc)

        # Refresh the modifiers info frame
        self.refresh_modifiers_frame()

    def refresh_modifiers_frame(self):
        mods_frame = self.nametowidget(MODIFIERS_FRAME)

        # Destroy old info
        for child in mods_frame.winfo_children():
            child.destroy()

        curr_mods = set()

        tk.Label(mods_frame, text="Status").grid(row=0, column=0)
        tk.Label(mods_frame, text="Effect").grid(row=0, column=1)
        tk.Label(mods_frame, text="Quick Fix").grid(row=0, column=2)
        tk.Label(mods_frame, text="Treatment").grid(row=0, column=3)

        # Create new info
        for npc in manager.npcs:
            for mod in npc.modifiers:
                mod = mod.lower()
                if mod in npc.short_status_to_long.keys():
                    mod = npc.short_status_to_long[mod]
                if mod in npc.statuses and mod not in curr_mods:
                    curr_mods.add(mod)
                    # Name
                    tk.Label(mods_frame, text="{}".format(mod.capitalize()))\
                        .grid(row=len(curr_mods) * 2, column=0)

                    # Effect
                    effect_scrollbar = tk.Scrollbar(mods_frame, orient="horizontal")
                    effect_scrollbar.grid(row=len(curr_mods)*2 + 1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
                    effect_text = tk.Text(mods_frame, wrap=tk.NONE, height=0, width=50,
                                          xscrollcommand=effect_scrollbar.set, font=("Helvetica", 8))
                    effect_text.grid(row=len(curr_mods) * 2, column=1)
                    effect_scrollbar.config(command=effect_text.xview)
                    effect_text.insert(tk.END, npc.statuses[mod][0])

                    # Quick Fix
                    tk.Label(mods_frame, text="{}".format(npc.statuses[mod][1])) \
                        .grid(row=len(curr_mods) * 2, column=2)

                    if len(npc.statuses[mod]) >= 3:
                        # Treatment
                        tk.Label(mods_frame, text="{}".format(npc.statuses[mod][2])) \
                            .grid(row=len(curr_mods) * 2, column=3)


"""
    Destroys the given Frame and removes the given name from the initiative queue
"""
def remove_queue_entry(entryframe, name: str):
    entryframe.destroy()
    queue.remove(name)


root = tk.Tk()
app = Application(master=root)
app.master.title("Cyberpunk Fight Manager")
app.mainloop()
