import math
import random

from .triggerint import TriggerInt
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

        self.hp = TriggerInt(hp, self.refresh_wound_status)
        self.maxhp = TriggerInt(hp, self.refresh_wound_status)

        self.spb = TriggerInt(spb, self.refresh_wound_status)
        self.maxspb = TriggerInt(spb, self.refresh_wound_status)

        self.sph = TriggerInt(sph, self.refresh_wound_status)
        self.maxsph = TriggerInt(sph, self.refresh_wound_status)

        self.ds = ds
        self.modifiers = set()

    def refresh_wound_status(self):
        if (self.hp.value < 1):
            self.modifiers.add("Mortally Wounded")

        elif (self.hp.value < self.maxhp.value):
            self.modifiers.add("Lightly Wounded")
            
        elif (self.hp.value < math.ceil(self.maxhp.value / 2.0)):
            self.modifiers.add("Seriously Wounded")

    def print(self):
        print(str(self))

    def __str__(self):
        main_info = "{}: {}/{} hp | {}/{} head sp | {}/{} body sp".format(self.name, self.hp, self.maxhp, self.sph,
                                                                          self.maxsph, self.spb, self.maxspb)
        death_save = "  Death Save: {}".format(self.ds)
        modifiers = "  Modifiers: {}".format(self.modifiers)
        return main_info + "\n" + death_save + "\n" + modifiers
