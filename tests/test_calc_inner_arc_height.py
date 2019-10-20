#!/home/istjohn/venvs/dads-wall/bin/python3.7

from context import calc_inner_arc_height

def test_calc_inner_arc_height():
    assert calc_inner_arc_height(
        outer_arc_len='130\' 10"',
        outer_arc_rad='186\'',
        wall_thick='2\' 8 1/2"') == 134.64
