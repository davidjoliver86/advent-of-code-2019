"""
Test cases for day 12
"""
from aoc2019.day12 import run_step, create_moons, Moon

TEN_STEP_TEST_CASE = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""

ONE_HUNDRED_STEP_TEST_CASE = """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""


def test_moon_repr():
    moon = Moon(1, 2, 3)
    assert str(moon) == "pos=<x=1, y=2, z=3>, vel=<x=0, y=0, z=0>"


def test_velocity():
    ganymede = Moon(3, 3, 3)
    callisto = Moon(5, 3, 1)
    ganymede.gravity(callisto)
    ganymede.move()
    assert str(ganymede) == "pos=<x=4, y=3, z=2>, vel=<x=1, y=0, z=-1>"


def test_one_step():
    moons = [Moon(-1, 0, 2), Moon(2, -10, -7), Moon(4, -8, 8), Moon(3, 5, -1)]
    run_step(moons)
    reprs = [str(moon) for moon in moons]
    assert reprs == [
        "pos=<x=2, y=-1, z=1>, vel=<x=3, y=-1, z=-1>",
        "pos=<x=3, y=-7, z=-4>, vel=<x=1, y=3, z=3>",
        "pos=<x=1, y=-7, z=5>, vel=<x=-3, y=1, z=-3>",
        "pos=<x=2, y=2, z=0>, vel=<x=-1, y=-3, z=1>",
    ]


def test_ten_steps():
    moons = list(create_moons(TEN_STEP_TEST_CASE))
    for _ in range(10):
        run_step(moons)
    reprs = [str(moon) for moon in moons]
    assert reprs == [
        "pos=<x=2, y=1, z=-3>, vel=<x=-3, y=-2, z=1>",
        "pos=<x=1, y=-8, z=0>, vel=<x=-1, y=1, z=3>",
        "pos=<x=3, y=-6, z=1>, vel=<x=3, y=2, z=-3>",
        "pos=<x=2, y=0, z=4>, vel=<x=1, y=-1, z=-1>",
    ]


def test_ten_steps_total_energy():
    moons = list(create_moons(TEN_STEP_TEST_CASE))
    for _ in range(10):
        run_step(moons)
    assert sum([moon.total_energy for moon in moons]) == 179


def test_one_hundred_steps():
    moons = list(create_moons(ONE_HUNDRED_STEP_TEST_CASE))
    for _ in range(100):
        run_step(moons)
    assert sum([moon.total_energy for moon in moons]) == 1940
