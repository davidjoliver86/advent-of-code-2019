from aoc2019 import day6

TEST_DATA = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

TEST_DATA_SANTA = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""


def test_sample_orbit():
    orbit = day6.create_orbit(TEST_DATA)
    assert orbit.sum_orbits() == 42


def test_santa_orbit():
    orbit = day6.create_orbit(TEST_DATA_SANTA)
    your_path = orbit.get_path("YOU")
    santas_path = orbit.get_path("SAN")
    assert day6.path_steps(your_path, santas_path) == 4
