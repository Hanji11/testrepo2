"""CSCA08: Functions for the tic-tac-toe game.

Instructions (READ THIS FIRST!)
===============================

Make sure that the files tictactoe_game.py and a1_checker.py are in the same
folder as this file (tictactoe_functions.py).

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the course CSC108/CSCA08 at the University of Toronto. Copying for 
purposes other than this use is expressly prohibited. All forms of distribution 
of this code, whether as given or with any changes, are expressly prohibited.

All of the files in this folder are:
Copyright (c) 2022 the University of Toronto CSC108/CSCA08 Teaching Team.
"""


EMPTY_CELL = '-'


def is_between(value: int, min_value: int, max_value: int) -> bool:
    """Return True if and only if value is between min_value and max_value.

    Precondition: min_value < max_value

    >>> is_between(1, 0, 2)
    True
    >>> is_between(0, 2, 3)
    False
    >>> is_between(1, 1, 3)
    False
    """

