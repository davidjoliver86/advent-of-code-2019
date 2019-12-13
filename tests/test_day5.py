"""
Test cases for day 5
"""

import random
from typing import List
import pytest
from aoc2019.intcode import Intcode

LONG_EXAMPLE = [
    3,
    21,
    1008,
    21,
    8,
    20,
    1005,
    20,
    22,
    107,
    8,
    21,
    20,
    1006,
    20,
    31,
    1106,
    0,
    36,
    98,
    0,
    0,
    1002,
    21,
    125,
    20,
    4,
    20,
    1105,
    1,
    46,
    104,
    999,
    1105,
    1,
    46,
    1101,
    1000,
    1,
    20,
    4,
    20,
    1105,
    1,
    46,
    98,
    99,
]

TEST_CASES_INPUT_OUTPUT = (
    # program, input, output
    # is input equal to 8?
    ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [8], [1]),
    ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [7], [0]),
    ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [9], [0]),
    # is input less than 8?
    ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [7], [1]),
    ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [0], [1]),
    ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [8], [0]),
    ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [9], [0]),
    # is input equal to 8? (immediate)
    ([3, 3, 1108, -1, 8, 3, 4, 3, 99], [8], [1]),
    ([3, 3, 1108, -1, 8, 3, 4, 3, 99], [7], [0]),
    ([3, 3, 1108, -1, 8, 3, 4, 3, 99], [9], [0]),
    # is input less than 8? (immediate)
    ([3, 3, 1107, -1, 8, 3, 4, 3, 99], [7], [1]),
    ([3, 3, 1107, -1, 8, 3, 4, 3, 99], [0], [1]),
    # jump tests
    ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [0], [0]),
    ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [1], [1]),
    ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [-1], [1]),
    ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [0], [0]),
    ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [1], [1]),
    ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [-1], [1]),
    (LONG_EXAMPLE, [7], [999]),
    (LONG_EXAMPLE, [8], [1000]),
    (LONG_EXAMPLE, [9], [1001]),
)


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


@pytest.mark.parametrize("code,input_,expected", TEST_CASES_INPUT_OUTPUT)
def test_input_Poutput(code: List[int], input_: List[int], expected: List[int]):
    program = Intcode(code, input_)
    program.run()
    assert program.get_output_history() == expected
