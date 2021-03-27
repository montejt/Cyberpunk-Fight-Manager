import math
import random

HURT_TYPE_ERROR = "Given damage type is unknown"


class Npc:

    statuses = {
        "lightly wounded": ("None", "DV10"),
        "seriously wounded": ("-2 all actions", "DV13"),
        "mortally wounded": ("-4 all actions, -6 MOVE (min 1), roll DS, any attack = crit and -1 DS", "DV15 = 1HP and unconscious"),
        "dead": ("Death", "N/A"),
        "dismembered arm": ("Arm gone, -1 DS", "N/A", "Surgery DV17"),
        "dismembered hand": ("Hand gone, -1 DS", "N/A", "Surgery DV17"),
        "collapsed lung": ("-2 MOVE (min 1), -1 DS", "Paramedic DV15", "Surgery DV15"),
        "broken ribs": ("Move more than 4m/yds in turn = -5 HP", "Paramedic DV13", "Paramedic DV15, Surgery DV13"),
        "broken arm": ("Can't use arm, drop item", "Paramedic DV13", "Paramedic DV15, Surgery DV13"),
        "foreign object": ("Move more than 4m/yds in turn = -5 HP", "FirstAid/Paramedic DV13", "Quick Fix"),
        "broken leg": ("-4 MOVE (min 1)", "Paramedic DV13", "Paramedic DV15, Surgery DV13"),
        "torn muscle": ("-2 Melee Attacks", "FirstAid/Paramedic DV13", "Quick Fix"),
        "spinal injury": ("next turn: no action except MOVE, -1 DS", "Paramedic DV15", "Surgery DV15"),
        "crushed fingers": ("-4 all actions involving hand", "Paramedic DV13", "Surgery DV15"),
        "dismembered leg": ("Leg gone, -6 MOVE (min 1), cannot dodge, -1 DS", "N/A", "Surgery DV17"),
        "lost eye": ("Eye gone, -4 to vision ranged attack and perception checks, -1 DS", "N/A", "Surgery DV17"),
        "brain injury": ("-2 all actions, -1 DS", "N/A", "Surgery DV17"),
        "damaged eye": ("-4 to vision ranged attack and perception checks", "Paramedic DV15", "Surgery DV13"),
        "concussion": ("-2 all actions", "FirstAid/Paramedic DV13", "Quick Fix"),
        "broken jaw": ("-4 all speech based actions", "Paramedic DV13", "Paramedic/Surgery DV13"),
        # "foreign object": (),
        "whiplash": ("-1 DS", "Paramedic DV13", "Paramedic/Surgery DV13"),
        "cracked skull": ("Headshot multiplier = 3x from 2x, -1 DS", "Paramedic DV15", "Paramedic/Surgery DV15"),
        "damaged ear": ("Move more than 4m/yds in turn = no MOVE next turn, -2 hearing perception checks", "Paramedic DV13", "Surgery DV13"),
        "crushed windpipe": ("Can't speak, -1 DS", "N/A", "Surgery DV15"),
        "lost ear": ("Ear gone, move more than 4m/yds in turn = no MOVE next turn, -4 hearing perception checks, -1 DS", "Paramedic DV13", "Surgery DV13")
    }

    short_status_to_long = {
        "lw": "lightly wounded",
        "sw": "seriously wounded",
        "mw": "mortally wounded",
        "d": "dead",
        "da": "dismembered arm",
        "dh": "dismembered hand",
        "cl": "collapsed lung",
        "br": "broken ribs",
        "ba": "broken arm",
        "fo": "foreign object",
        "bl": "broken leg",
        "tm": "torn muscle",
        "si": "spinal injury",
        "cf": "crushed fingers",
        "dl": "dismembered leg",
        "leye": "lost eye",
        "bi": "brain injury",
        "deye": "damaged eye",
        "c": "concussion",
        "bj": "broken jaw",
        "w": "whiplash",
        "cs": "cracked skull",
        "dear": "damaged ear",
        "cw": "crushed windpipe",
        "lear": "lost ear"
    }

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

    def hurt(self, damage, dmg_type="default", target="b", crit=False):
        if target == "b" or target == "body":
            nocrit = False
            if dmg_type == "default" or dmg_type == "d":
                hploss = max(damage - self.spb, 0)
                self.hp -= hploss
                if hploss > 0:
                    self.spb -= 1
            elif dmg_type == "melee" or dmg_type == "m":
                hploss = max(damage - math.floor(self.spb / 2), 0)
                self.hp -= hploss
                if hploss > 0:
                    self.spb -= 1
            elif dmg_type == "straight" or dmg_type == "s":
                self.hp -= max(damage, 0)
            elif dmg_type == "armor breaking" or dmg_type == "ab":
                hploss = max(damage - self.spb, 0)
                self.hp -= hploss
                if hploss > 0:
                    self.spb -= 2
            elif dmg_type == "armor piercing" or dmg_type == "ap":
                # Effective armor is 4 less
                effective_armor = max(self.spb - 4, 0)
                # penetrating damage is the damage - the effective armor (min 0)
                penetrating_damage = max(damage - effective_armor, 0)
                # If any damage penetrates, reduce it by 1d6 (min 1 damage) and ablate armor
                if penetrating_damage > 0:
                    penetrating_damage = max(penetrating_damage - random.randint(1, 6), 1)
                    self.hp -= penetrating_damage
                    self.spb -= 1

            else:
                nocrit = True
                print(HURT_TYPE_ERROR)

            if not nocrit and crit:
                print("Crit! Please roll for body crit")
                self.hp -= 5

        elif target == "h" or target == "head":
            nocrit = False
            if dmg_type == "default" or dmg_type == "d":
                hploss = max(2 * (damage - self.sph), 0)
                self.hp -= hploss
                if hploss > 0:
                    self.sph -= 1
            elif dmg_type == "melee" or dmg_type == "m":
                hploss = max(2 * (damage - math.floor(self.sph / 2)), 0)
                self.hp -= hploss
                if hploss > 0:
                    self.sph -= 1
            elif dmg_type == "straight" or dmg_type == "s":
                self.hp -= 2 * max(damage, 0)
            elif dmg_type == "armor breaking" or dmg_type == "ab":
                hploss = max(2 * (damage - self.sph), 0)
                self.hp -= hploss
                if hploss > 0:
                    self.sph -= 2
            elif dmg_type == "armor piercing" or dmg_type == "ap":
                # Effective armor is 4 less
                effective_armor = max(self.sph - 4, 0)
                # penetrating damage is the damage - the effective armor (min 0)
                penetrating_damage = max(damage - effective_armor, 0)
                # If any damage penetrates, reduce it by 1d6 (min 1 damage) and ablate armor
                if penetrating_damage > 0:
                    penetrating_damage = max(penetrating_damage - random.randint(1, 6), 1)
                    # headshot = 2 * damage
                    self.hp -= 2 * penetrating_damage
                    self.sph -= 1
            else:
                nocrit = True
                print(HURT_TYPE_ERROR)

            if not nocrit and crit:
                print("Crit! Please roll for head crit")
                self.hp -= 5
        else:
            print("target must be \"b\" (body) or \"h\" (head)")
        self.hp = max(0, self.hp)
        self.spb = max(0, self.spb)
        self.sph = max(0, self.sph)
        print("Target status:\n" + str(self))


