"""
Day 2: 1202 Program Alarm
"""
import copy
import pathlib
import operator
from typing import List, Callable


ADD = 1
MULTIPLY = 2
HALT = 99


class Intcode:
    """
    Intcode programs take in a comma-separated list of integers
    """

    def __init__(self, initial: List) -> None:
        self._program: List = initial
        self._index: int = 0
        self._halted: bool = False

    def _mutate(self, func: Callable) -> None:
        index_1 = self._program[self._index + 1]
        value_1 = self._program[index_1]
        index_2 = self._program[self._index + 2]
        value_2 = self._program[index_2]
        dest_index = self._program[self._index + 3]
        self._program[dest_index] = func(value_1, value_2)

    def _add(self) -> None:
        self._mutate(operator.add)

    def _multiply(self) -> None:
        self._mutate(operator.mul)

    def run(self) -> None:
        """
        Runs the intcode program until it reaches a halt command.
        """
        while not self._halted:
            if self._program[self._index] == ADD:
                self._add()
            elif self._program[self._index] == MULTIPLY:
                self._multiply()
            elif self._program[self._index] == HALT:
                self._halted = True
            self._index += 4

    def get_program(self) -> List:
        """
        Returns the state of the program.
        """
        return self._program


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
