"""
Test cases for day 9
"""
import copy
from aoc2019.intcode import Intcode


def test_quine():
    initial = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    program = Intcode(copy.deepcopy(initial))
    program.run()
    assert program.get_output_history() == initial


def test_huge_number():
    program = Intcode([104, 1125899906842624, 99])
    program.run()
    assert program.get_output_history() == [1125899906842624]


def test_16_digits():
    program = Intcode([1102, 34915192, 34915192, 7, 4, 7, 99, 0])
    program.run()
    assert (10 ** 15) < program.get_output_history()[0] < (10 ** 16)
