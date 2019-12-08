"""
Test cases for day 1
"""
import pytest
from aoc2019 import day1

TEST_CASES_CALC_FUEL = (
    # (input, expected)
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
)

TEST_CASES_MOAR_FUEL = (
    # (input, expected)
    (14, 2),
    (1969, 966),
    (100756, 50346),
)


@pytest.mark.parametrize("input_,expected", TEST_CASES_CALC_FUEL)
def test_calculate_fuel(input_: int, expected: int) -> None:
    """
    Verify that calculate_fuel() works with the test cases.
    """
    assert day1.calculate_fuel(input_) == expected


@pytest.mark.parametrize("input_,expected", TEST_CASES_MOAR_FUEL)
def test_moar_fuel(input_: int, expected: int) -> None:
    """
    Verify that moar_fuel() works with the test cases.
    """
    assert day1.moar_fuel(input_) == expected


def test_first_star() -> None:
    """
    First star answer for provided input.
    """
    assert day1.first_star() == 3365459


def test_second_star() -> None:
    """
    Second star answer for provided input.
    """
    assert day1.second_star() == 5045301
