from aoc2019.day12 import run_step
from aoc2019.day12.moon import Moon


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
