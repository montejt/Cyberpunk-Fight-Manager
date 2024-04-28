from tools.types.ranges import Ranges
from tools.types.ranges import RangeType
from tools.types.ranges import range_table
from tools.types.weapons import Weapon

def calc_range_dv(weapon: Weapon, range: int, rangeType=RangeType.FEET):

    # If using feet: convert to yards
    range_in_yards = range
    if (rangeType == RangeType.FEET.value):
        range_in_yards = round(range / 3.0)

    range_dvs = range_table[weapon]
    
    for curr_range in Ranges:
        if (curr_range.value[0] <= range_in_yards and range_in_yards <= curr_range.value[1]):
            return range_dvs[curr_range]
    
    raise ValueError("Given range does not fit within the range table: " + range)