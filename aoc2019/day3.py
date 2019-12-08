"""
Day 3: Crossed Wires
"""
import pathlib
import functools
from typing import List, Tuple, Set


def _trace_path(path: str) -> List[Tuple]:
    steps = path.split(",")
    path = []
    x = 0
    y = 0
    for step in steps:
        direction, distance = step[0], int(step[1:])
        if direction == "U":
            dy = 1
            dx = 0
        if direction == "D":
            dy = -1
            dx = 0
        if direction == "L":
            dx = -1
            dy = 0
        if direction == "R":
            dx = 1
            dy = 0
        for _ in range(distance):
            x += dx
            y += dy
            path.append((x, y))
    return path


@functools.lru_cache
def _get_intersections(path_1: str, path_2: str) -> Set[Tuple]:
    points_1 = _trace_path(path_1)
    points_2 = _trace_path(path_2)
    return set(points_1) & set(points_2)


def smallest_manhattan_distance(path_1: str, path_2: str) -> int:
    """
    Find all intersections between path_1 and path_2. Then return the shortest "Manhattan distance"
    between the intersections.
    """
    return min([(abs(x) + abs(y)) for x, y in _get_intersections(path_1, path_2)])


def shortest_intersection(path_1: str, path_2: str) -> int:
    """
    Given the intersections we found earlier, trace each path's distance to that intersection. Then
    from all the intersection distances, return the shortest.
    """
    points_1 = _trace_path(path_1)
    points_2 = _trace_path(path_2)
    intersections = _get_intersections(path_1, path_2)
    intersection_distances = []
    for intersection in intersections:
        intersection_distances.append(
            points_1.index(intersection) + points_2.index(intersection) + 2
        )
    if intersection_distances:
        return min(intersection_distances)
    return None


@functools.lru_cache
def _load_fixtures() -> List[str]:
    return pathlib.Path("fixtures/day3_input1.txt").read_text().split()


def first_star():
    """
    Find the shortest Manhattan distance.
    """
    path_1, path_2 = _load_fixtures()
    return smallest_manhattan_distance(path_1, path_2)


def second_star():
    """
    Find the shortest intersection.
    """
    path_1, path_2 = _load_fixtures()
    return shortest_intersection(path_1, path_2)


if __name__ == "__main__":
    first_star()
    second_star()
