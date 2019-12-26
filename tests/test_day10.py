"""
Test cases for day 10
"""
from typing import Tuple
import pytest
from aoc2019.day10 import find_best_asteroid, get_observations, Asteroid

TEST_MAP_1 = """
.#..#
.....
#####
....#
...##
"""

TEST_MAP_2 = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
"""

TEST_MAP_3 = """
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
"""

TEST_MAP_4 = """
.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
"""

TEST_MAP_5 = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""

TEST_CASES = (
    # map, coordinates of best location, number of stars observed
    (TEST_MAP_1, Asteroid(3, 4), 8),
    (TEST_MAP_2, Asteroid(5, 8), 33),
    (TEST_MAP_3, Asteroid(1, 2), 35),
    (TEST_MAP_4, Asteroid(6, 3), 41),
    (TEST_MAP_5, Asteroid(11, 13), 210),
)


@pytest.mark.parametrize("ast_map,expected_loc,expected_count", TEST_CASES)
def test_calculate_fuel(ast_map: str, expected_loc: Tuple[int, int], expected_count: int) -> None:
    location, number = find_best_asteroid(get_observations(ast_map))
    assert (location, number) == (expected_loc, expected_count)
