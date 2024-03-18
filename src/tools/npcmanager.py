import math
import random
from .npc import Npc
from .types.damagetype import DamageType
from .types.target import Target

"""
    The NpcManager contains npcs and performs operations upon them
"""
class NpcManager:
    def __init__(self):
        self.npcs = set()

    def add(self, npc: Npc):
        self.npcs.add(npc)
        print("Added npc \"{}\"".format(npc.name))

    def remove(self, npc: Npc):
        self.npcs.remove(npc)
        print("Removed npc \"{}\"".format(npc.name))

    def clear(self):
        self.npcs.clear()

    def get(self, name: str) -> Npc:
        for npc in (n for n in self.npcs if n.name == name):
            return npc
        else:
            print("No npc with name \"{}\"".format(name))

    def hurt(self, name: str, damage: int, dmg_type=DamageType.STANDARD.value, target=Target.BODY.value, crit=False):

        npc = self.get(name)

        # Calculate hp loss
        hploss = self.calcHpLoss(damage, dmg_type, target, npc.spb if target == Target.BODY.value else npc.sph, crit)

        # Ablate armor from npc
        armor_ablation = 2 if dmg_type == DamageType.ARMOR_BREAKING.value else 1
        if (target == Target.BODY.value and dmg_type != DamageType.STRAIGHT.value and hploss > 0):
            npc.spb = max(npc.spb - armor_ablation, 0)
        elif (target == Target.HEAD.value and dmg_type != DamageType.STRAIGHT.value and hploss > 0):
            npc.sph = max(npc.sph - armor_ablation, 0)

        if (crit):
            # Crit damage (5) goes straight to health and doesn't ablate armor
            hploss += 5

        npc.hp = max(npc.hp - hploss, 0)

        print("Target status:\n" + str(npc))

    def calcHpLoss(self, dmg: int, type: str, target: str, sp: int, crit: bool):
        
        hploss = 0
        match type:
            case DamageType.STANDARD | DamageType.ARMOR_BREAKING:
                hploss = max(dmg - sp, 0)

            case DamageType.MELEE:
                # Stopping power is halved against melee
                hploss = max(dmg - math.floor(sp / 2), 0)

            case DamageType.STRAIGHT:
                hploss = max(dmg, 0)

            case DamageType.ARMOR_PIERCING:
                penetrating_damage = max(dmg - max(sp - 4, 0), 0)
                # If any damage penetrates, reduce it by 1d6 (min 1 damage) and ablate armor
                if penetrating_damage > 0:
                    hploss = max(penetrating_damage - random.randint(1, 6), 1)
        
        if (target == Target.HEAD.value):
            # Headshot damage is multiplied by two
            hploss *= 2

        return hploss

    def print(self):
        print(str(self))

    def __str__(self):
        string = "-----Npcs-----\n"
        for npc in self.npcs:
            string += str(npc) + "\n"
        return string
