"""
Day 7: Amplification Circuit
"""
import collections
import itertools
import pathlib
import copy
from typing import List, Tuple, Callable
from aoc2019.intcode import Intcode

Signal = collections.namedtuple("Signal", ["phase_sequence", "value"])

THRUSTER_SIGNAL_SIGNATURE = Callable[[List[int], Tuple[int]], int]

SINGLE_PASS = 1
FEEDBACK_LOOP = 2


def _get_thruster_signal_once(program: List[int], phase_sequence: Tuple[int]) -> int:
    """
    Run through all of the five amplifiers in sequence. Take the output of the final amplifier
    (which would have been the "input value" of a sixth hypothetical amplifier).
    """
    input_value = 0
    for ps in phase_sequence:
        computer = Intcode(copy.deepcopy(program), [ps, input_value])
        computer.run()
        input_value = computer.get_output_history()[0]
    return input_value


def _get_thruster_signal_loop(program: List[int], phase_sequence: Tuple[int]) -> int:
    """
    Loop through all amplifiers in a "round robin" style. Introduces the possibliity that a
    running Intcode program can exhaust its input stack, blocking until more input is given.

    As before - inputs from the previous amplifier are fed into the next until all programs have
    formally halted.
    """
    input_value = 0
    count = 0
    programs = [Intcode(copy.deepcopy(program), [ps]) for ps in phase_sequence]
    halted = [program.halted() for program in programs]
    while True:
        index = count % 5
        program = programs[index]
        program.push_input(input_value)
        program.run()
        halted[index] = program.halted()
        input_value = program.get_output_history()[-1]
        count += 1
        if all(halted):
            return input_value


def find_max_signal(program: List[int], mode: int) -> Signal:
    max_signal = Signal((0, 0, 0, 0, 0), 0)
    if mode == SINGLE_PASS:
        phase_sequences = itertools.permutations((0, 1, 2, 3, 4))
        func = _get_thruster_signal_once
    elif mode == FEEDBACK_LOOP:
        phase_sequences = itertools.permutations((5, 6, 7, 8, 9))
        func = _get_thruster_signal_loop
    else:
        raise ValueError("I dont know that mode")
    for phase_sequence in phase_sequences:
        final_output = func(program, phase_sequence)
        if final_output > max_signal.value:
            max_signal = Signal(phase_sequence, final_output)
    return max_signal


def main():
    raw = pathlib.Path("fixtures/day7_input1.txt").read_text()
    initial_program = [int(x) for x in raw.split(",")]
    first_star_signal = find_max_signal(copy.deepcopy(initial_program), SINGLE_PASS)
    second_star_signal = find_max_signal(copy.deepcopy(initial_program), FEEDBACK_LOOP)
    print(first_star_signal)
    print(second_star_signal)


if __name__ == "__main__":
    main()
