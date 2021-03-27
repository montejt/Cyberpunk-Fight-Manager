"""
CyberPunk Fight Manager

Provides a terminal interface which provides tools for handling Cyberpunk fights. Meant for use by GMs.

The first word is the command, the rest are args. Each should be separated by a space
"""
import math

user_input = None
initiativeQueue = []
NUM_NPC_ARGS = 4
NUM_NPC_ARGS_ERROR = "Missing one or more of: name, hp, body sp, head sp"
npcSet = set()
HURT_TYPE_ERROR = "Given damage type is unknown"


def runProgram():
    global user_input
    # Constantly look for user input until they type q or quit.
    # Splits the user input into the command (case insensitive) and arguments (case sensitive), and then attempts to
    # call the corresponding function with the given arguments.
    while user_input != "q" and user_input != "quit":
        user_input = input("Enter Command: ")
        if len(user_input.split()) == 0:
            continue
        cmd = user_input.split()[0].lower()
        args = user_input.split()[1:]
        if cmd in cmdToFunc.keys():
            try:
                cmdToFunc[cmd](args)
            except ValueError:
                print("Input error occured: make sure number values are plain numbers")
        else:
            print(cmd + " is not a valid command\n(type \"help\" for a list of commands)")
        print("")


def printHelp(args):
    global cmdToFunc
    print("For help with a specific command, please type: \"help cmd\"\n")
    print("Commands:")
    longcmd = None
    for cmd in cmdToFunc:
        if longcmd is None:
            longcmd = cmd
        else:
            print(longcmd + ", " + cmd)
            longcmd = None


# Wipes the initiative queue
def clearInitiative(args):
    global initiativeQueue
    initiativeQueue.clear()
    print("Initative cleared")


# Removes the character with the given name from the initiative queue
def removeFromInitiative(args):
    global initiativeQueue
    if len(args) < 1:
        print("Missing character name")
    else:
        character = args[0]
        for char, initiative in ((c, i) for c, i in initiativeQueue if c == character):
            # We found the character! Remove them!
            initiativeQueue.remove((char, initiative))
            print("character removed!")
            return
        # No Character found, give an error
        print("\"" + args[0] + "\" is not in the initiative queue")


# Adds character with the given name and initiative to the initiative queue
def addToInitiative(args):
    global initiativeQueue
    if len(args) < 2:
        print("Missing character name and/or initiative number")
    elif args[0] in (char for char, i in initiativeQueue):
        print("\"" + args[0] + "\" already in initiative queue")
    else:
        for i, (char, initiative) in enumerate(initiativeQueue):
            if int(args[1]) == initiative:
                print("Tie! Roll initiative again")
                break
            elif int(args[1]) > initiative:
                initiativeQueue.insert(i, (args[0], int(args[1])))
                print("\"" + args[0] + "\" placed in initiative queue")
                break
        else:
            initiativeQueue.append((args[0], int(args[1])))
            print("\"" + args[0] + "\" placed in initiative queue")


# Displays the initiative queue
def displayInitiative(args):
    global initiativeQueue
    print("-----Initiative Queue-----")
    for char, initiative in initiativeQueue:
        print(char + " : " + str(initiative))


class Npc:
    def __init__(self, name, hp, spb, sph):
        self.name = name
        self.maxhp = int(hp)
        self.hp = int(hp)
        self.spb = int(spb)
        self.sph = int(sph)
        self.modifiers = []

    def __str__(self):
        return self.name + ": " + str(self.hp) + "hp, " + str(self.spb) + " body sp, " + str(self.sph) + " head sp" + "\n\t" + "Modifiers: " + str(self.modifiers)


def createNpc(args):
    global npcSet
    if len(args) < NUM_NPC_ARGS:
        print(NUM_NPC_ARGS_ERROR)
    else:
        npc = Npc(*args[0:NUM_NPC_ARGS])
        if npc.name in (n.name for n in npcSet):
            print("Npc with this name already exists!")
        else:
            npcSet.add(npc)
            print("\"" + args[0] + "\" created")


def displayNpcs(args):
    global npcSet
    print("-----Npcs-----")
    for npc in npcSet:
        print(npc)


def removeNpc(args):
    global npcSet
    if len(args) < 1:
        print("Missing npc name")
    for npc in npcSet:
        if npc.name == args[0]:
            npcSet.remove(npc)
            print("\"" + npc.name + "\" removed")
            break
    else:
        print("npc does not exist")


def clearNpcs(args):
    global npcSet
    npcSet.clear()
    print("Cleared all npcs")


def hurtNpc(args):
    global npcSet
    if len(args) < 3:
        print("Missing required args\n"
              "Proper usage: npc_name target(b or h) damage damage_type(default[d], melee[m], or straight[s])[OPTIONAL] crit?[OPTIONAL]")
    elif args[0] not in (n.name for n in npcSet):
        print("Npc does not exist!")
    else:
        dmg_type = "default"
        target = args[1]
        damage = int(args[2])
        npc = next(n for n in npcSet if n.name == args[0])
        if target == "b":
            nocrit = False
            if len(args) >= 4:
                dmg_type = args[3]
            if dmg_type == "default" or dmg_type == "d":
                npc.hp -= max(damage - npc.spb, 0)
                npc.spb -= 1
            elif dmg_type == "melee" or dmg_type == "m":
                npc.hp -= max(damage - math.ceil(npc.spb / 2), 0)
                npc.sph -= 1
            elif dmg_type == "straight" or dmg_type == "s":
                npc.hp -= max(damage, 0)
            else:
                nocrit = True
                print(HURT_TYPE_ERROR)

            if not nocrit and len(args) >= 5 and (args[4] == "yes" or args[4] == "y"):
                print("Crit! Please roll for body crit")
                npc.hp -= max(0, npc.hp - 5)
        elif target == "h":
            nocrit = False
            if len(args) >= 4:
                dmg_type = args[3]
            if dmg_type == "default" or dmg_type == "d":
                npc.hp -= max(2*(damage - npc.sph), 0)
                npc.sph -= 1
            elif dmg_type == "melee" or dmg_type == "m":
                npc.hp -= max(2*(damage - math.ceil(npc.sph / 2)), 0)
                npc.sph -= 1
            elif dmg_type == "straight" or dmg_type == "s":
                npc.hp -= 2*max(damage, 0)
            else:
                nocrit = True
                print(HURT_TYPE_ERROR)

            if not nocrit and len(args) >= 5 and (args[4] == "yes" or args[4] == "y"):
                print("Crit! Please roll for head crit")
                npc.hp -= max(0, npc.hp - 5)
        else:
            print("Target must be \"b\" (body) or \"h\" (head)")
        print("Target status:\n" + npc.__str__())


def addModifiers(args):
    global npcSet
    if len(args) < 2:
        print("Missing npc name and/or modifier(s)")
    elif args[0] not in (n.name for n in npcSet):
        print("Npc does not exist!")
    else:
        npc = next(n for n in npcSet if n.name == args[0])
        for arg in args[1:]:
            npc.modifiers.append(arg)
        print("Modifiers added")


def removeModifiers(args):
    global npcSet
    if len(args) < 2:
        print("Missing npc name and/or modifier(s)")
    elif args[0] not in (n.name for n in npcSet):
        print("Npc does not exist!")
    else:
        npc = next(n for n in npcSet if n.name == args[0])
        for arg in args[1:]:
            if arg in npc.modifiers:
                npc.modifiers.remove(arg)
        print("Modifiers removed")


cmdToFunc = {"help": printHelp,
             "h": printHelp,
             "display_initiative": displayInitiative,
             "di": displayInitiative,
             "add_initiative": addToInitiative,
             "ai": addToInitiative,
             "remove_initiative": removeFromInitiative,
             "ri": removeFromInitiative,
             "clear_initiative": clearInitiative,
             "ci": clearInitiative,
             "display_npcs": displayNpcs,
             "dn": displayNpcs,
             "add_npc": createNpc,
             "an": createNpc,
             "remove_npc": removeNpc,
             "rn": removeNpc,
             "clear_npcs": clearNpcs,
             "cn": clearNpcs,
             "hurt_npc": hurtNpc,
             "hn": hurtNpc,
             "add_modifiers": addModifiers,
             "am": addModifiers,
             "remove_modifiers": removeModifiers,
             "rm": removeModifiers}

cmdToHelp = {}

runProgram()
print("Goodbye!")
