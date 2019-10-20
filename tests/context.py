#!/home/istjohn/venvs/dads-wall/bin/python3.7

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from to_inches import to_inches
from main import calc_inner_arc_height
