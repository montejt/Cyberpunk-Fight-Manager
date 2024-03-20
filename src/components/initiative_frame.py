import tkinter as tk

from tools.initiative import InitiativeList

from style.colors import *
from style.fonts import *
from style.numbers import *

class InitiativeFrame(tk.Frame):

    def __init__(self, parent):
        super(InitiativeFrame, self).__init__(master=parent, padx=COMPONENT_PADDING, bg=WINDOW_BACKGROUND_COLOR)
        
        self.initiativeList = InitiativeList()

        # Create the initiative queue gui
        self.create_initiative_queue()

    def create_initiative_queue(self):
        frame = tk.Frame(self, bg=PRIMARY_COLOR_ONE, name="initframe", relief="solid", bd=COMPONENT_FRAME_BD)
        frame.pack(side="top", fill="x")

        title = tk.Label(frame, text="Initiative Queue", name="queuelabel", bg=PRIMARY_COLOR_ONE, fg=PRIMARY_COLOR_FG, font=TITLE_FONT)
        title.pack()

        self.refresh_initiative_list(frame)

    # Refreshes the ui initiative list
    def refresh_initiative_list(self, frame):
        # Clear old list
        for child in (c for c in frame.winfo_children() if c.winfo_name() != "queuelabel"):
            child.destroy()

        # Fill the list with entries
        for name, initiative in self.initiativeList.initiatives:
            # Create the name label
            entryframe = tk.Frame(frame, relief="solid", bd=2)
            entryframe.pack(side="top", fill="x")
            entryname = tk.Label(entryframe, text=name, anchor="center")
            entryname.pack(side="left", fill="x")

            # Create a delete button
            deletebtn = tk.Button(entryframe, text="-", bg=CANCEL_COLOR, font=DEL_FONT,
                                  command=lambda entryframe=entryframe, name=name: self.remove_initiative_entry(entryframe, name))
            deletebtn.pack(side="right")

            # Create initiative entry
            initvar = tk.IntVar()
            initvar.set(initiative)
            entryinit = tk.Entry(entryframe, textvariable=initvar, width=SMALL_ENTRY_SIZE)
            entryinit.bind("<Key-Return>", lambda event, n=name, i=initvar: self.update_initiative_entry(frame, n, i.get()))
            entryinit.bind("<FocusOut>", lambda event, n=name, i=initvar: self.update_initiative_entry(frame, n, i.get()))
            entryinit.pack(side="right")

        # Create a custom entry
        customframe = tk.Frame(frame, relief="sunken", bd=5)
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
        addbtn = tk.Button(customframe, text="+", bg=CONFIRM_COLOR, font=ADD_FONT,
                           command=lambda: self.add_queue_entry(frame, namevar.get(), initiative.get()))
        addbtn.pack(side="right")

    # Adds the given name and initiative to the queue, and refreshes the gui
    def add_queue_entry(self, frame, name, initiative):
        self.initiativeList.add(name, initiative)
        self.refresh_initiative_list(frame)

    # Updates the initiative of the given name and refreshes the initiative list gui
    def update_initiative_entry(self, frame, name, initiative):
        # Initiative has updated, so update in backend
        self.initiativeList.remove(name)
        self.initiativeList.add(name, initiative)
        self.refresh_initiative_list(frame)

    # Removes the given entry frame and name from the list
    def remove_initiative_entry(self, entryframe, name: str):
        entryframe.destroy()
        self.initiativeList.remove(name)
