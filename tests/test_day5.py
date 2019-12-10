"""
Test cases for day 5
"""

import random
from aoc2019.intcode import Intcode


def test_intcode_input():
    input_ = random.randint(0, 100)
    program = Intcode([3, 0, 4, 0, 99], [input_])
    program.run()
    assert program.get_program() == [input_, 0, 4, 0, 99]


def test_multiplication_parameter_modes():
    program = Intcode([1002, 4, 3, 4, 33])
    program.run()
    assert program.get_program() == [1002, 4, 3, 4, 99]


def test_negative_values():
    program = Intcode([1101, 100, -1, 4, 0])
    program.run()
    assert program.get_program() == [1101, 100, -1, 4, 99]
