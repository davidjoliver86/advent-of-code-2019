"""
Test cases for day 4
"""
from typing import List
import pytest
from aoc2019 import day4

VALID_PASSWORD_FIRST_STAR_TEST_CASES = (
    ([1, 1, 1, 1, 1, 1], True),
    ([2, 2, 3, 4, 5, 0], False),  # decreasing digit
    ([1, 2, 3, 7, 8, 9], False),  # no double
)

VALID_PASSWORD_SECOND_STAR_TEST_CASES = (
    ([1, 1, 2, 2, 3, 3], True),
    # 444 is a triple
    ([1, 2, 3, 4, 4, 4], False),
    # 1111 is a "quadruple", but there is still a "22" double
    ([1, 1, 1, 1, 2, 2], True),
    # 3333 is a quadruple
    ([1, 2, 3, 3, 3, 3], False),
)


@pytest.mark.parametrize("number,valid", VALID_PASSWORD_FIRST_STAR_TEST_CASES)
def test_valid_password_first_star(number: List[int], valid: bool):
    assert day4.valid_password_first_star(number) == valid


@pytest.mark.parametrize("number,valid", VALID_PASSWORD_SECOND_STAR_TEST_CASES)
def test_valid_password_second_star(number: List[int], valid: bool):
    assert day4.valid_password_second_star(number) == valid
