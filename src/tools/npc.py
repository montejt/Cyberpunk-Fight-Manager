import math
import random
from .types.target import Target

HURT_TYPE_ERROR = "Given damage type is unknown"

class Npc:

    """
    Initializes the npc with the provided stats:

    name: name of entity
    hp: max hit points
    sph: stopping power of head armor
    spb: stopping power of body armor
    ds: death save
    """
    def __init__(self, name, hp, sph, spb, ds):
        self.name = name

        self.hp = int(hp)
        self.maxhp = int(hp)

        self.spb = int(spb)
        self.maxspb = int(spb)

        self.sph = int(sph)
        self.maxsph = int(sph)

        self.ds = ds
        self.modifiers = []

    def print(self):
        print(str(self))

    def __str__(self):
        main_info = "{}: {}/{} hp | {}/{} head sp | {}/{} body sp".format(self.name, self.hp, self.maxhp, self.sph,
                                                                          self.maxsph, self.spb, self.maxspb)
        death_save = "Death Save: {}".format(self.ds)
        modifiers = "Modifiers: {}".format(self.modifiers)
        return main_info + "\n" + death_save + "\n" + modifiers
