"""
Day 6: Universal Orbit Map
"""
from typing import Dict, List
import pathlib


class Orbit(dict):

    _orbit_count_cache = {}

    def _count_orbits(self, key: str) -> int:
        if key in self._orbit_count_cache:
            return self._orbit_count_cache[key]
        if key in self:
            value = 1 + self._count_orbits(self[key])
            self._orbit_count_cache[key] = value
            return value
        return 0

    def sum_orbits(self) -> int:
        return sum([self._count_orbits(key) for key in self])

    def get_path(self, key) -> List[str]:
        path = []
        while (orbits := self[key]) is not None:
            path.append(orbits)
            key = orbits
        return path


def create_orbit(raw_data: str) -> Dict[str, str]:
    """
    xxx)yyy where "yyy directly orbits xxx".

    If xxx is COM - it orbits nothing.
    """
    orbit = Orbit()
    for line in raw_data.splitlines():
        a, b = line.split(")")
        orbit[b] = a if a != "COM" else None
    return orbit


def path_steps(path_1: List[str], path_2: List[str]) -> int:
    """
    Presume that there is one common node between the two paths. Find the first such occurence
    within path_1 that also appears in path_2.

    Then just sum up the indices of those two nodes' since they each represent the number of
    orbital jumps.
    """
    for node in path_1:
        if node in path_2:
            return path_1.index(node) + path_2.index(node)
    raise ValueError("Paths do not share a common node")


def first_star(orbit: Orbit) -> int:
    return orbit.sum_orbits()


def second_star(orbit: Orbit) -> int:
    your_path = orbit.get_path("YOU")
    santas_path = orbit.get_path("SAN")
    return path_steps(your_path, santas_path)


def main():
    orbit_data = pathlib.Path("fixtures/day6_input1.txt").read_text()
    orbit = create_orbit(orbit_data)
    print(first_star(orbit))
    print(second_star(orbit))


if __name__ == "__main__":
    main()
