"""
Day 9: Sensor Boost
"""
import pathlib
from aoc2019.intcode import Intcode


def main():
    initial = pathlib.Path("fixtures/day9_input1.txt").read_text()
    program = Intcode(initial, [1])
    program.run()
    program = Intcode(initial, [2])
    program.run()


if __name__ == "__main__":
    main()
