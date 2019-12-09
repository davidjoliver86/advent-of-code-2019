"""
Intcode interpreter
"""
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
