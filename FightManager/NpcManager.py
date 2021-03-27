"""
    The NpcManager serves as a way to keep track of Npcs
"""
from FightManager.Npc import Npc


class NpcManager:
    def __init__(self):
        self.npcs = set()

    def add(self, npc):
        assert type(npc) is Npc
        self.npcs.add(npc)
        print("Added npc \"{}\"".format(npc.name))

    def remove(self, npc):
        assert type(npc) is Npc
        self.npcs.remove(npc)
        print("Removed npc \"{}\"".format(npc.name))

    def clear(self):
        self.npcs.clear()

    def get(self, name):
        for npc in (n for n in self.npcs if n.name == name):
            return npc
        else:
            print("No npc with name \"{}\"".format(name))

    def print(self):
        print(str(self))

    def __str__(self):
        string = "-----Npcs-----\n"
        for npc in self.npcs:
            string += str(npc) + "\n"
        return string
