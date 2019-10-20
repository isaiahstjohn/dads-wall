#!/home/istjohn/venvs/dads-wall/bin/python3.7

import math
import re


class InvalidDistanceError(Exception):
    pass


def to_inches(distance):
    """Convert distance:string to distance:float

    distance is a string of the form 5' 2 1/8" """
    regexp = r"""
(                               # Feet
    (?P<feet>\d+)
    \'
)?
\s*
(                               # Inches
    (
        \s*                     # fraction
        (?P<numerator1>\d+)
        /
        (?P<denominator1>\d+)
        |   (?P<whole1>\d+)     # or whole number and fraction
            \s+
            (?P<numerator2>\d+)
            /
            (?P<denominator2>\d+)
        |   (?P<whole2>\d+)     # or whole number
    )
    "
)?
"""
    matches = re.match(regexp, distance, flags=re.VERBOSE)
    if not matches:
        raise InvalidDistanceError
    matches = matches.groupdict()
    feet = matches["feet"]
    feet = int(feet) if feet else 0
    whole = matches["whole1"] if matches["whole1"] else matches["whole2"]
    whole = int(whole) if whole else 0

    numerator = (
        matches["numerator1"] if matches["numerator1"] else matches["numerator2"]
    )
    denominator = (
        matches["denominator1"] if matches["denominator1"] else matches["denominator2"]
    )
    if numerator and denominator:
        numerator = int(numerator)
        denominator = int(denominator)
        fraction = numerator / denominator
    else:
        fraction = 0
    inches = feet * 12 + whole + fraction
    return inches
