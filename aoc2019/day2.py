"""
Day 2: 1202 Program Alarm
"""
import copy
import pathlib
from typing import List
from aoc2019.intcode import Intcode


def _get_initial_list() -> List:
    raw = pathlib.Path("fixtures/day2_input1.txt").read_text()
    return [int(x) for x in raw.split(",")]


def first_star() -> int:
    """
    Load and run the provided intcode program, then return the value in index 0.
    """
    initial = _get_initial_list()
    initial[1] = 12
    initial[2] = 2
    program = Intcode(initial)
    program.run()
    return program.get_program()[0]


def second_star(target: int) -> int:
    """
    Find the "noun" and "verb" - integers from 0-99 - to replace input indices 1 and 2 - that when
    running the program, produces the target value in index 0.
    Load list from file once; copy as needed to iterate over different input parameters.
    """
    initial = _get_initial_list()
    for noun in range(0, 100):
        for verb in range(0, 100):
            modified = copy.deepcopy(initial)
            modified[1] = noun
            modified[2] = verb
            program = Intcode(modified)
            program.run()
            if program.get_program()[0] == target:
                return noun * 100 + verb
    raise RuntimeError("Can't find suitable inputs")


if __name__ == "__main__":
    print(first_star())
    print(second_star(19690720))
