"""
Test cases for day 2
"""
from typing import List
import pytest
from aoc2019 import day2

TEST_CASES_INTCODE = (
    # (input, expected)
    ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
)


@pytest.mark.parametrize("initial,expected", TEST_CASES_INTCODE)
def test_run_intcode(initial: List, expected: List) -> None:
    """
    Run a sample Intcode program and verify the final state of the program after calling halt.
    """
    program = day2.Intcode(initial)
    program.run()
    assert program.get_program() == expected


def test_first_star() -> None:
    """
    First star answer for provided input.
    """
    assert day2.first_star() == 3765464


def test_second_star() -> None:
    """
    Second star answer for provided input.
    """
    assert day2.second_star(19690720) == 7610
