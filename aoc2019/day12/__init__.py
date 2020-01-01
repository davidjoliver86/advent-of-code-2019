from typing import Iterable
from itertools import combinations
from .moon import Moon


def run_step(moons: Iterable[Moon]):
    for moon_a, moon_b in combinations(moons, 2):
        moon_a.gravity(moon_b)
    for moon in moons:
        moon.move()
