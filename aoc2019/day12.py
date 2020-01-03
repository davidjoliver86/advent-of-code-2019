import re
from typing import Iterable
from itertools import combinations

INPUT = """
<x=3, y=3, z=0>
<x=4, y=-16, z=2>
<x=-10, y=-6, z=5>
<x=-3, y=0, z=-13>
"""

TEN_STEP_TEST_CASE = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""


class Moon:
    x: int = 0
    y: int = 0
    z: int = 0
    v_x: int = 0
    v_y: int = 0
    v_z: int = 0

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>".format(
            self.x, self.y, self.z, self.v_x, self.v_y, self.v_z
        )

    @staticmethod
    def _velocity_dimension(dimension: str) -> str:
        return f"v_{dimension}"

    @property
    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    @property
    def kinetic_energy(self):
        return abs(self.v_x) + abs(self.v_y) + abs(self.v_z)

    @property
    def total_energy(self):
        return self.potential_energy * self.kinetic_energy

    def gravity(self, other):
        for dimension in "xyz":
            velocity_dimension = self._velocity_dimension(dimension)
            this_velocity = getattr(self, velocity_dimension)
            other_velocity = getattr(other, velocity_dimension)
            this_position = getattr(self, dimension)
            other_position = getattr(other, dimension)
            if this_position < other_position:
                setattr(self, velocity_dimension, this_velocity + 1)
                setattr(other, velocity_dimension, other_velocity - 1)
            elif this_position > other_position:
                setattr(self, velocity_dimension, this_velocity - 1)
                setattr(other, velocity_dimension, other_velocity + 1)

    def move(self):
        for dimension in "xyz":
            velocity_dimension = self._velocity_dimension(dimension)
            position = getattr(self, dimension)
            velocity = getattr(self, velocity_dimension)
            setattr(self, dimension, position + velocity)


def create_moons(description: str) -> Moon:
    pattern = r"<x=([-\d]+), y=([-\d]+), z=([-\d]+)>"
    for line in description.splitlines():
        if (match := re.match(pattern, line.strip())) is not None:
            x, y, z = match.groups()
            yield Moon(int(x), int(y), int(z))


def run_step(moons: Iterable[Moon]):
    for moon_a, moon_b in combinations(moons, 2):
        moon_a.gravity(moon_b)
    for moon in moons:
        moon.move()


def first_star():
    moons = list(create_moons(INPUT))
    for _ in range(1000):
        run_step(moons)
    print(sum([moon.total_energy for moon in moons]))


def second_star():
    moons = list(create_moons(TEN_STEP_TEST_CASE))
    states = set()
    steps = 0
    while True:
        state = tuple(
            [(moon.x, moon.y, moon.z, moon.v_x, moon.v_y, moon.v_z) for moon in moons]
        )
        if state in states:
            break
        states.add(state)
        run_step(moons)
        steps += 1
    print(steps)


if __name__ == "__main__":
    first_star()
    second_star()
