from enum import Enum

class Weapon(Enum):
    PISTOL = "Pistol"
    SMG = "SMG"
    SHOTGUN = "Shotgun (Slug)"
    ASSAULT_RIFLE = "Assault Rifle"
    SNIPER_RIFLE = "Sniper Rifle"
    BOWS_AND_CROSSBOW = "Bows & Crossbow"
    GRENADE_LAUNCHER= "Grenade Launcher"
    ROCKET_LAUNCHER = "Rocket Launcher"
    AF_SMG = "Autofire SMG"
    AF_AR = "Autofire Assault Rifle"

    def __str__(self):
        return str(self.value)