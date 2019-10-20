#!/home/istjohn/venvs/dads-wall/bin/python3.7

from context import to_inches
import pytest

@pytest.mark.parametrize("test_input, expected", [
    ('1/8"', 0.125),
    ('2"', 2),
    ('2 1/8"', 2.125),
    ("2'", 24),
    ("2'1\"", 25),
    ("2' 1\"", 25),
    ("2' 1/8\"", 24.125),
    ("2' 1 3/8\"", 25.375),
    ("0' 0\"", 0),
    ('35"', 35),
    ("2' 1/8\"", 24.125),
    ("2' 0 1/8\"", 24.125),
    ("2' 0\"", 24)
])
def test_to_inches(test_input, expected):
    assert to_inches(test_input) == expected

