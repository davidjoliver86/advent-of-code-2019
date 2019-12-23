import pathlib
from aoc2019.intcode import Intcode


def main():
    program = Intcode(pathlib.Path("fixtures/day9_input1.txt").read_text(), [1])
    program.run()


if __name__ == "__main__":
    main()
