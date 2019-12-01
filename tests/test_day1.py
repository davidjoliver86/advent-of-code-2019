import pytest
from aoc2019.day1 import main

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


@pytest.mark.parametrize("input,expected", TEST_CASES_CALC_FUEL)
def test_calculate_fuel(input: int, expected: int) -> None:
    assert main.calculate_fuel(input) == expected


@pytest.mark.parametrize("input,expected", TEST_CASES_MOAR_FUEL)
def test_moar_fuel(input: int, expected: int) -> None:
    assert main.moar_fuel(input) == expected


def test_first_star() -> None:
    assert main.first_star() == 3365459


def test_second_star() -> None:
    assert main.second_star() == 5045301
