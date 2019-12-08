"""
Test cases for day 3
"""
import pytest
from aoc2019 import day3

TEST_1_PATH_1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
TEST_1_PATH_2 = "U62,R66,U55,R34,D71,R55,D58,R83"
TEST_2_PATH_1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
TEST_2_PATH_2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

MANHATTAN_TEST_CASES = (
    (TEST_1_PATH_1, TEST_1_PATH_2, 159),
    (TEST_2_PATH_1, TEST_2_PATH_2, 135),
)

SHORTEST_INTERSECTION_TEST_CASES = (
    (TEST_1_PATH_1, TEST_1_PATH_2, 610),
    (TEST_2_PATH_1, TEST_2_PATH_2, 410),
)


@pytest.mark.parametrize("path_1,path_2,expected", MANHATTAN_TEST_CASES)
def test_manhattan_distance(path_1: str, path_2: str, expected: int):
    """
    Given the test paths, test that smallest_manhattan_distance() works.
    """
    assert day3.smallest_manhattan_distance(path_1, path_2) == expected


@pytest.mark.parametrize("path_1,path_2,expected", SHORTEST_INTERSECTION_TEST_CASES)
def test_shortest_intersection(path_1: str, path_2: str, expected: int):
    """
    Given the test paths, test that shortest_intersection() works.
    """
    assert day3.shortest_intersection(path_1, path_2) == expected


def test_first_star():
    """
    First star answer for provided input.
    """
    assert day3.first_star() == 316


def test_second_star():
    """
    Second star answer for provided input.
    """
    assert day3.second_star() == 16368
