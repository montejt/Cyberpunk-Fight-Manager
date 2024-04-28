from enum import Enum
from tools.types.weapons import Weapon

class Ranges(Enum):
    ZERO_TO_SIX = (0, 6)
    SEVEN_TO_TWELVE = (7, 12)
    THIRTEEN_TO_TWENTY_FIVE = (13, 25)
    TWENTY_SIX_TO_FIFTY = (26, 50)
    FIFTY_ONE_TO_ONE_HUNDRED = (51, 100)
    ONE_HUNDRED_ONE_TO_TWO_HUNDRED = (101, 200)
    TWO_HUNDRED_ONE_TO_FOUR_HUNDRED = (201, 400)
    FOUR_HUNDRED_ONE_TO_EIGHT_HUNDRED = (401, 800)

class RangeType(Enum):
    FEET = "ft"
    YARDS = "yds"
    METERS = "m"

    def __str__(self):
        return str(self.value)

"""
weapon -> range -> dv
"""
range_table = {
    Weapon.PISTOL.value: {
        Ranges.ZERO_TO_SIX: 13,
        Ranges.SEVEN_TO_TWELVE: 15,
        Ranges.THIRTEEN_TO_TWENTY_FIVE: 20,
        Ranges.TWENTY_SIX_TO_FIFTY: 25,
        Ranges.FIFTY_ONE_TO_ONE_HUNDRED: 30,
        Ranges.ONE_HUNDRED_ONE_TO_TWO_HUNDRED: 30,
        Ranges.TWO_HUNDRED_ONE_TO_FOUR_HUNDRED: "N/A",
        Ranges.FOUR_HUNDRED_ONE_TO_EIGHT_HUNDRED: "N/A"
    },
    Weapon.SMG.value: {
        Ranges.ZERO_TO_SIX: 15,
        Ranges.SEVEN_TO_TWELVE: 13,
        Ranges.THIRTEEN_TO_TWENTY_FIVE: 15,
        Ranges.TWENTY_SIX_TO_FIFTY: 20,
        Ranges.FIFTY_ONE_TO_ONE_HUNDRED: 25,
        Ranges.ONE_HUNDRED_ONE_TO_TWO_HUNDRED: 25,
        Ranges.TWO_HUNDRED_ONE_TO_FOUR_HUNDRED: 30,
        Ranges.FOUR_HUNDRED_ONE_TO_EIGHT_HUNDRED: "N/A"
    },
    Weapon.SHOTGUN.value: {
        Ranges.ZERO_TO_SIX: 13,
        Ranges.SEVEN_TO_TWELVE: 15,
        Ranges.THIRTEEN_TO_TWENTY_FIVE: 20,
        Ranges.TWENTY_SIX_TO_FIFTY: 25,
        Ranges.FIFTY_ONE_TO_ONE_HUNDRED: 30,
        Ranges.ONE_HUNDRED_ONE_TO_TWO_HUNDRED: 35,
        Ranges.TWO_HUNDRED_ONE_TO_FOUR_HUNDRED: "N/A",
        Ranges.FOUR_HUNDRED_ONE_TO_EIGHT_HUNDRED: "N/A"
    },
    Weapon.ASSAULT_RIFLE.value: {
        Ranges.ZERO_TO_SIX: 17,
        Ranges.SEVEN_TO_TWELVE: 16,
        Ranges.THIRTEEN_TO_TWENTY_FIVE: 15,
        Ranges.TWENTY_SIX_TO_FIFTY: 13,
        Ranges.FIFTY_ONE_TO_ONE_HUNDRED: 15,
        Ranges.ONE_HUNDRED_ONE_TO_TWO_HUNDRED: 20,
        Ranges.TWO_HUNDRED_ONE_TO_FOUR_HUNDRED: 25,
        Ranges.FOUR_HUNDRED_ONE_TO_EIGHT_HUNDRED: 30
    },
    Weapon.SNIPER_RIFLE.value: {
        Ranges.ZERO_TO_SIX: 30,
        Ranges.SEVEN_TO_TWELVE: 25,
        Ranges.THIRTEEN_TO_TWENTY_FIVE: 25,
        Ranges.TWENTY_SIX_TO_FIFTY: 20,
        Ranges.FIFTY_ONE_TO_ONE_HUNDRED: 15,
        Ranges.ONE_HUNDRED_ONE_TO_TWO_HUNDRED: 16,
        Ranges.TWO_HUNDRED_ONE_TO_FOUR_HUNDRED: 17,
        Ranges.FOUR_HUNDRED_ONE_TO_EIGHT_HUNDRED: 20
    },
    Weapon.BOWS_AND_CROSSBOW.value: {
        Ranges.ZERO_TO_SIX: 15,
        Ranges.SEVEN_TO_TWELVE: 13,
        Ranges.THIRTEEN_TO_TWENTY_FIVE: 15,
        Ranges.TWENTY_SIX_TO_FIFTY: 17,
        Ranges.FIFTY_ONE_TO_ONE_HUNDRED: 20,
        Ranges.ONE_HUNDRED_ONE_TO_TWO_HUNDRED: 22,
        Ranges.TWO_HUNDRED_ONE_TO_FOUR_HUNDRED: "N/A",
        Ranges.FOUR_HUNDRED_ONE_TO_EIGHT_HUNDRED: "N/A"
    },
    Weapon.GRENADE_LAUNCHER.value: {
        Ranges.ZERO_TO_SIX: 16,
        Ranges.SEVEN_TO_TWELVE: 15,
        Ranges.THIRTEEN_TO_TWENTY_FIVE: 15,
        Ranges.TWENTY_SIX_TO_FIFTY: 17,
        Ranges.FIFTY_ONE_TO_ONE_HUNDRED: 20,
        Ranges.ONE_HUNDRED_ONE_TO_TWO_HUNDRED: 22,
        Ranges.TWO_HUNDRED_ONE_TO_FOUR_HUNDRED: 25,
        Ranges.FOUR_HUNDRED_ONE_TO_EIGHT_HUNDRED: "N/A"
    },
    Weapon.ROCKET_LAUNCHER.value: {
        Ranges.ZERO_TO_SIX: 17,
        Ranges.SEVEN_TO_TWELVE: 16,
        Ranges.THIRTEEN_TO_TWENTY_FIVE: 15,
        Ranges.TWENTY_SIX_TO_FIFTY: 15,
        Ranges.FIFTY_ONE_TO_ONE_HUNDRED: 20,
        Ranges.ONE_HUNDRED_ONE_TO_TWO_HUNDRED: 20,
        Ranges.TWO_HUNDRED_ONE_TO_FOUR_HUNDRED: 25,
        Ranges.FOUR_HUNDRED_ONE_TO_EIGHT_HUNDRED: 30
    },
    Weapon.AF_SMG.value: {
        Ranges.ZERO_TO_SIX: 20,
        Ranges.SEVEN_TO_TWELVE: 17,
        Ranges.THIRTEEN_TO_TWENTY_FIVE: 20,
        Ranges.TWENTY_SIX_TO_FIFTY: 25,
        Ranges.FIFTY_ONE_TO_ONE_HUNDRED: 30,
        Ranges.ONE_HUNDRED_ONE_TO_TWO_HUNDRED: "N/A",
        Ranges.TWO_HUNDRED_ONE_TO_FOUR_HUNDRED: "N/A",
        Ranges.FOUR_HUNDRED_ONE_TO_EIGHT_HUNDRED: "N/A"
    },
    Weapon.AF_AR.value: {
        Ranges.ZERO_TO_SIX: 22,
        Ranges.SEVEN_TO_TWELVE: 20,
        Ranges.THIRTEEN_TO_TWENTY_FIVE: 17,
        Ranges.TWENTY_SIX_TO_FIFTY: 20,
        Ranges.FIFTY_ONE_TO_ONE_HUNDRED: 25,
        Ranges.ONE_HUNDRED_ONE_TO_TWO_HUNDRED: "N/A",
        Ranges.TWO_HUNDRED_ONE_TO_FOUR_HUNDRED: "N/A",
        Ranges.FOUR_HUNDRED_ONE_TO_EIGHT_HUNDRED: "N/A"
    }
}