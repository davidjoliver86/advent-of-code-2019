"""
Day 1: The Tyranny of the Rocket Equation
"""
import pathlib
import typing


def calculate_fuel(mass: int) -> int:
    """
    Fuel needed for a given mass is the mass divided by 3 (integer division) minus 2.
    """
    return (mass // 3) - 2


def moar_fuel(mass: int) -> int:
    """
    Recursively calculates the fuel needed for the amount of fuel calculated for a mass, and so on
    until the needed fuel becomes insignificant.
    """
    if (fuel := calculate_fuel(mass)) >= 0:
        return fuel + moar_fuel(fuel)
    return 0


def _sum_fuel_requirements(func: typing.Callable) -> int:
    total = 0
    with pathlib.Path("fixtures/day1_input1.txt").open("r") as f_p:
        for line in f_p:
            total += func(int(line))
    return total


def first_star() -> int:
    """
    From the given input - a list of masses - sum up and calculate the fuel requirements.
    """
    return _sum_fuel_requirements(calculate_fuel)


def second_star() -> int:
    """
    The fuel requirements also, recursively, require fuel on their own.
    """
    return _sum_fuel_requirements(moar_fuel)


if __name__ == "__main__":
    print(first_star())
    print(second_star())
