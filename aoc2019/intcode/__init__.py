"""
Intcode interpreter
"""
import operator
import collections
from typing import List, Callable, Tuple


ADD = 1
MULTIPLY = 2
HALT = 99

MODE_POSITION = 0
MODE_IMMEDIATE = 1


Opcode = collections.namedtuple("Opcode", ["mode_1", "mode_2", "mode_3", "instruction"])


def _parse_opcode(opcode: int) -> Tuple[int]:
    mode_3 = opcode // 10000
    mode_2 = opcode // 1000 % 10
    mode_1 = opcode // 100 % 10
    instruction = opcode % 100
    return Opcode(mode_1, mode_2, mode_3, instruction)


class Intcode:
    """
    Intcode programs take in a comma-separated list of integers
    """

    def __init__(self, initial: List) -> None:
        self._program: List = initial
        self._index: int = 0
        self._halted: bool = False

    def _get_parameter(self, mode: int, value: int) -> int:
        """
        Value is taken as one of the parameters of the opcode.
        If that particular parameter is in "immediate" mode - just return the value.
        If it's in "position" mode - return the value at the "index" of 'value'.
        """
        if mode == MODE_IMMEDIATE:
            return value
        if mode == MODE_POSITION:
            return self._program[value]
        raise ValueError("you dun goofed your parameter modes")

    def _get_opcode(self) -> Opcode:
        return _parse_opcode(self._program[self._index])

    def _set_value_at_index(self, index: int, value: int):
        """
        Look up the value at index - then set *that* index to value.
        """
        lookup = self._program[index]
        self._program[lookup] = value

    def run(self) -> None:
        """
        Runs the intcode program until it reaches a halt command.
        """
        while not self._halted:
            opcode = self._get_opcode()
            if opcode.instruction == ADD:
                p1 = self._get_parameter(opcode.mode_1, self._program[self._index + 1])
                p2 = self._get_parameter(opcode.mode_2, self._program[self._index + 2])
                self._set_value_at_index(self._index + 3, p1 + p2)
                self._index += 4
            if opcode.instruction == MULTIPLY:
                p1 = self._get_parameter(opcode.mode_1, self._program[self._index + 1])
                p2 = self._get_parameter(opcode.mode_2, self._program[self._index + 2])
                self._set_value_at_index(self._index + 3, p1 * p2)
                self._index += 4
            if opcode.instruction == HALT:
                self._halted = True

    def get_program(self) -> List:
        """
        Returns the state of the program.
        """
        return self._program
