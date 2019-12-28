"""
Intcode interpreter
"""
import operator
import collections
from typing import List, Callable, Tuple, Union


ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
ADJ_RELATIVE_BASE = 9
HALT = 99

MODE_POSITION = 0
MODE_IMMEDIATE = 1
MODE_RELATIVE = 2


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

    def __init__(self, data: Union[List, str], input_stack: List = None) -> None:
        if isinstance(data, list):
            self._program: List = data
        elif isinstance(data, str):
            self._program: List = [int(x) for x in data.split(",")]
        self._index: int = 0
        self._relative_base: int = 0
        self._halted: bool = False
        self._input_stack = input_stack or []
        self._output_history = []  # mainly to make testing easier

    def _get_parameter(self, mode: int, index_increment: int) -> int:
        """
        Value is taken as one of the parameters of the opcode.
        If that particular parameter is in "immediate" mode - just return the value.
        If it's in "position" mode - return the value at the "index" of 'value'.
        """
        value = self._program[self._index + index_increment]
        if mode == MODE_IMMEDIATE:
            return value
        if mode == MODE_POSITION:
            return self._get_value_at_index(value)
        if mode == MODE_RELATIVE:
            return self._get_value_at_index(value + self._relative_base)
        raise ValueError("you dun goofed your parameter modes")

    def _expand(self, index: int) -> None:
        target_length = index + 1 - len(self._program)
        self._program.extend([0] * target_length)

    def _get_value_at_index(self, index: int) -> int:
        try:
            return self._program[index]
        except IndexError:
            self._expand(index)
            return self._program[index]

    def _get_opcode(self) -> Opcode:
        return _parse_opcode(self._program[self._index])

    def _set_value_at_index(self, index_increment: int, value: int, relative_offset: bool = False):
        """
        Look up the value at index - then set *that* index to value.

        index_increment: Steps after self._index to lookup the value.
        value: The value to set.
        relative_offset: If True, add the relative base to the index retrieved (not the index
            *to* retrieve*).
        """
        lookup = self._program[self._index + index_increment]
        if relative_offset:
            lookup += self._relative_base
        try:
            self._program[lookup] = value
        except IndexError:
            self._expand(lookup)
            self._program[lookup] = value

    def _pop_input(self) -> int:
        return self._input_stack.pop(0)

    def push_input(self, val: int) -> None:
        self._input_stack.append(val)

    def halted(self) -> bool:
        return self._halted

    def run(self, suppress_output: bool = False) -> None:
        """
        Runs the intcode program until it reaches a halt command.
        """
        while not self._halted:
            opcode = self._get_opcode()
            if opcode.instruction in (ADD, MULTIPLY):
                p1 = self._get_parameter(opcode.mode_1, 1)
                p2 = self._get_parameter(opcode.mode_2, 2)
                func = operator.add if opcode.instruction == ADD else operator.mul
                self._set_value_at_index(3, func(p1, p2), opcode.mode_3 == MODE_RELATIVE)
                self._index += 4
            if opcode.instruction == INPUT:
                try:
                    input_value = self._pop_input()
                except IndexError:
                    return  # blocks for more input
                self._set_value_at_index(1, input_value, opcode.mode_1 == MODE_RELATIVE)
                self._index += 2
            if opcode.instruction == OUTPUT:
                p1 = self._get_parameter(opcode.mode_1, 1)
                if not suppress_output:
                    print(p1)
                self._output_history.append(p1)
                self._index += 2
            if opcode.instruction in (JUMP_IF_TRUE, JUMP_IF_FALSE):
                p1 = self._get_parameter(opcode.mode_1, 1)
                p2 = self._get_parameter(opcode.mode_2, 2)
                func = operator.ne if opcode.instruction == JUMP_IF_TRUE else operator.eq
                if func(p1, 0):
                    self._index = p2
                else:
                    self._index += 3
            if opcode.instruction in (LESS_THAN, EQUALS):
                p1 = self._get_parameter(opcode.mode_1, 1)
                p2 = self._get_parameter(opcode.mode_2, 2)
                func = operator.lt if opcode.instruction == LESS_THAN else operator.eq
                value = 1 if func(p1, p2) else 0
                self._set_value_at_index(3, value, opcode.mode_3 == MODE_RELATIVE)
                self._index += 4
            if opcode.instruction == HALT:
                self._halted = True
            if opcode.instruction == ADJ_RELATIVE_BASE:
                p1 = self._get_parameter(opcode.mode_1, 1)
                self._relative_base += p1
                self._index += 2

    def get_program(self) -> List:
        """
        Returns the state of the program.
        """
        return self._program

    def get_output_history(self) -> List[int]:
        return self._output_history
