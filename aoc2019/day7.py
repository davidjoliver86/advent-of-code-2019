import collections
import itertools
from typing import List
from aoc2019.intcode import Intcode

Signal = collections.namedtuple("Signal", ["phase_sequence", "value"])


def find_max_signal(program: List[int]) -> Signal:
    max_signal = Signal((0, 0, 0, 0, 0), 0)
    for phase_sequence in itertools.permutations((0, 1, 2, 3, 4)):
        p1 = Intcode(program, [phase_sequence[0], 0])
        p1.run()
        p2 = Intcode(program, [phase_sequence[1], p1.get_output_history()[0]])
        p2.run()
        p3 = Intcode(program, [phase_sequence[1], p2.get_output_history()[0]])
        p3.run()
        p4 = Intcode(program, [phase_sequence[1], p3.get_output_history()[0]])
        p4.run()
        p5 = Intcode(program, [phase_sequence[1], p4.get_output_history()[0]])
        p5.run()
        final_output = p5.get_output_history()[0]
        if final_output > max_signal.value:
            max_signal = Signal(phase_sequence, final_output)
    return max_signal
