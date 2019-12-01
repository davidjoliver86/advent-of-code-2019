import pathlib
import typing


def calculate_fuel(mass: int) -> int:
    return (mass // 3) - 2


def moar_fuel(mass: int) -> int:
    if (fuel := calculate_fuel(mass)) >= 0:
        return fuel + moar_fuel(fuel)
    return 0


def _sum_fuel_requirements(func: typing.Callable) -> int:
    total = 0
    with pathlib.Path("fixtures/day1_input1.txt").open("r") as fp:
        for line in fp:
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
