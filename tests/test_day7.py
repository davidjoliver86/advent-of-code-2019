"""
Test cases for day 7
"""
import pytest
from typing import List
from aoc2019 import day7

TEST_CASES_MAX_SIGNAL = (
    # (program, signal)
    (
        [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
        day7.Signal((4, 3, 2, 1, 0), 43210),
    ),
    (
        [
            3,
            23,
            3,
            24,
            1002,
            24,
            10,
            24,
            1002,
            23,
            -1,
            23,
            101,
            5,
            23,
            23,
            1,
            24,
            23,
            23,
            4,
            23,
            99,
            0,
            0,
        ],
        day7.Signal([0, 1, 2, 3, 4], 54321),
    ),
    (
        [
            3,
            31,
            3,
            32,
            1002,
            32,
            10,
            32,
            1001,
            31,
            -2,
            31,
            1007,
            31,
            0,
            33,
            1002,
            33,
            7,
            33,
            1,
            33,
            31,
            31,
            1,
            32,
            31,
            31,
            4,
            31,
            99,
            0,
            0,
            0,
        ],
        day7.Signal([1, 0, 4, 3, 2], 65210),
    ),
)


@pytest.mark.parametrize("program,signal", TEST_CASES_MAX_SIGNAL)
def test_max_signal(program: List[int], signal: day7.Signal):
    assert day7.find_max_signal(program) == signal
