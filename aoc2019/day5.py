import pathlib
import functools
from typing import List
from aoc2019.intcode import Intcode


@functools.lru_cache
def _get_initial_list() -> List:
    raw = pathlib.Path("fixtures/day5_input1.txt").read_text()
    return [int(x) for x in raw.split(",")]


def first_star() -> None:
    program = Intcode(_get_initial_list(), [1])
    program.run()


if __name__ == "__main__":
    first_star()
