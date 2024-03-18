from enum import Enum

class DamageType(str, Enum):
    STANDARD = "Standard",
    MELEE = "Melee",
    STRAIGHT = "Straight",
    ARMOR_BREAKING = "Armor Breaking",
    ARMOR_PIERCING = "Armor Piercing"
