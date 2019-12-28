"""
Day 11: Space Police
"""
import pathlib
from typing import Tuple
from aoc2019.intcode import Intcode

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)
CYCLE = [UP, LEFT, DOWN, RIGHT]

TURN_LEFT = 0
TURN_RIGHT = 1

BLACK = 0
WHITE = 1
BLACK_CHAR = "."
WHITE_CHAR = "#"
DEFAULT_COLOR = BLACK


def run(starting_value: int) -> Intcode:
    """
    Run the paint robot. Provide a starting value of either BLACK or WHITE.
    """
    program = Intcode(pathlib.Path("fixtures/day11_input1.txt").read_text(), [starting_value])
    squares = {}
    current_square = (0, 0)
    direction_index = 0
    while not program.halted():
        program.run(suppress_output=True)
        color, turn = program.get_output_history()[-2:]  # pylint: disable=unbalanced-tuple-unpacking
        squares[current_square] = color
        if turn == TURN_LEFT:
            direction_index = (direction_index + 1) % 4
        elif turn == TURN_RIGHT:
            direction_index = (direction_index - 1) % 4
        else:
            raise ValueError("What kind of direction is that")
        new_x = current_square[0] + CYCLE[direction_index][0]
        new_y = current_square[1] + CYCLE[direction_index][1]
        current_square = (new_x, new_y)
        program.push_input(squares.get(current_square, DEFAULT_COLOR))
    return squares


def first_star():
    squares = run(BLACK)
    print(len(squares.keys()))


def second_star():
    def get_x(coordinates: Tuple[int, int]) -> int:
        x, _ = coordinates
        return x

    def get_y(coordinates: Tuple[int, int]) -> int:
        _, y = coordinates
        return y

    squares = run(WHITE)
    coordinates = squares.keys()
    min_x = min([get_x(coord) for coord in coordinates])
    min_y = min([get_y(coord) for coord in coordinates])
    max_x = max([get_x(coord) for coord in coordinates])
    max_y = max([get_y(coord) for coord in coordinates])

    # Debugging discovered that y ranges ranged from -5 to 0.
    # So we have to do the rows in reverse.

    for row in range(max_y, min_y - 1, -1):
        for col in range(min_x, max_x + 1):
            color = squares.get((col, row), BLACK)
            if color == BLACK:
                print(BLACK_CHAR, end="")
            elif color == WHITE:
                print(WHITE_CHAR, end="")
            else:
                raise ValueError("What kind of color is that")
        print()


if __name__ == "__main__":
    first_star()
    second_star()
