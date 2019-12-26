"""
Day 10: Monitoring Station
"""
import math
import collections
import pathlib
import functools
import copy
from typing import Dict, List

Asteroid = collections.namedtuple("Asteroid", ["x", "y"])


def intialize_asteroid_map(asteroid_map: str) -> Dict[Asteroid, None]:
    """
    Reads a map of asteroids and returns a dictionary of all asteroids in their spots.
    """
    asteroids = {}
    for y, row in enumerate(asteroid_map.strip().splitlines()):
        for x, col in enumerate(row):
            if col == "#":
                asteroids[Asteroid(x, y)] = None
    return asteroids


def get_observations(asteroid_map: str) -> Dict[Asteroid, List[Asteroid]]:
    """
    For all asteroids - create a list of all other asteroids that are in its line of sight.
    Calculate the angle between each asteroid; if the angles are identical to a previous asteroid,
    add it to the existing angle list.

    Return a dictionary of all asteroids with a dictionary of angled asteroid sightings.
    """
    # initialize asteroid map
    asteroids = intialize_asteroid_map(asteroid_map)
    all_observations = {}
    for asteroid_1 in asteroids:
        asteroid_1_observations = {}
        for asteroid_2 in asteroids:
            if asteroid_1 == asteroid_2:
                continue
            angle = calculate_angle(asteroid_1, asteroid_2)
            if angle in asteroid_1_observations:
                asteroid_1_observations[angle].append(asteroid_2)
            else:
                asteroid_1_observations[angle] = [asteroid_2]
        all_observations[asteroid_1] = asteroid_1_observations
    return all_observations


def calculate_angle(asteroid_1: Asteroid, asteroid_2: Asteroid) -> float:
    """
    Calculate the angle in degrees between asteroid_1 and asteroid_2.
    """
    dy = asteroid_2.y - asteroid_1.y
    dx = asteroid_2.x - asteroid_1.x
    return math.atan2(dy, dx) * 180.0 / math.pi


def calculate_distance(asteroid_1: Asteroid, asteroid_2: Asteroid) -> float:
    """
    Calculate the distance between asteroid_1 and asteroid_2 (Pythagorean theorem).
    """
    dy = asteroid_2.y - asteroid_1.y
    dx = asteroid_2.x - asteroid_1.x
    return math.sqrt(dy * dy + dx * dx)


def find_best_asteroid(asteroid_observations: Dict[Asteroid, List[Asteroid]]) -> Asteroid:
    """
    First star - identify the asteroid that has the most number of direct sightings. that is:
    which asteroid has the greatest number of *unique* angles across its sightings?
    """

    def by_sightings(asteroid_sightings):
        _, sighting_count = asteroid_sightings
        return sighting_count

    num_sightings = [(asteroid, len(sightings)) for asteroid, sightings in asteroid_observations.items()]
    sorted_sightings = sorted(num_sightings, key=by_sightings)
    return sorted_sightings[-1]


def ima_firin_mah_lazor(observations: Dict, best_asteroid: Asteroid):
    """
    Rotate the laser clockwise (starting at the first angle >= -90 degrees). It shoots one asteroid at a time.
    Keep rotating the laser, tracking the asteroids that get zapped. Return the list of zapped asteroids in order.
    """
    # ensure that we don't mutate asteroids, and then ensure each sighting is sorted
    fry_zone = copy.deepcopy(observations[best_asteroid])
    for angle, angle_obs in fry_zone.items():
        fry_zone[angle] = sorted(angle_obs, key=functools.partial(calculate_distance, best_asteroid))

    # take the angle keys and transform them into a sorted list
    # and first find the angle that's at least -90 degrees - start from that index
    sorted_angles = sorted(fry_zone.keys())
    number_of_angles = len(sorted_angles)
    empty_rotations = 0
    asteroids_zapped = []
    i = 0
    for i, angle in enumerate(sorted_angles):
        if angle >= -90.0:
            break
    while empty_rotations < number_of_angles:
        try:
            angle = sorted_angles[i % number_of_angles]
            zapped = fry_zone[angle].pop(0)
            asteroids_zapped.append(zapped)
            empty_rotations = 0
        except IndexError:
            empty_rotations += 1
        i += 1
    return asteroids_zapped


def main():
    map_data = pathlib.Path("fixtures/day10_input1.txt").read_text()
    observations = get_observations(map_data)
    best_asteroid, length = find_best_asteroid(observations)
    print(best_asteroid, length)
    zapped = ima_firin_mah_lazor(observations, best_asteroid)
    print(zapped[199])


if __name__ == "__main__":
    main()
