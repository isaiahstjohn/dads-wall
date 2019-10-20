#!/home/istjohn/venvs/dads-wall/bin/python3.7

import math
from to_inches import to_inches


def calc_inner_arc_height(*, outer_arc_len, outer_arc_rad, wall_thick):
    outer_arc_len = to_inches(outer_arc_len)
    outer_arc_rad = to_inches(outer_arc_rad)
    wall_thick = to_inches(wall_thick)
    arc_angle = outer_arc_len / outer_arc_rad
    inner_arc_rad = outer_arc_rad - wall_thick
    apothem = inner_arc_rad * math.cos(arc_angle / 2)
    inner_height = inner_arc_rad - apothem
    return round(inner_height, 2)


if __name__ == "__main__":
    print(
        calc_inner_arc_height(
            outer_arc_len="130' 10\"", outer_arc_rad="186'", wall_thick="2' 8 1/2\""
        )
    )
