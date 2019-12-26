"""
Day 8: Space Image Format
"""
from typing import List
import pathlib
import itertools
import collections

BLACK = "0"
WHITE = "1"
TRANSPARENT = "2"


def create_layers(image_data: str, length: int, height: int) -> List[str]:
    layer_size = length * height
    return ["".join(layer) for layer in itertools.zip_longest(*[iter(image_data)] * layer_size)]


def layer_pixel_data(layers: List[str]) -> List[collections.Counter]:
    return [collections.Counter(layer) for layer in layers]


def _number_of_zeroes(counter: collections.Counter) -> int:
    return counter["0"]


def decode_image(layers: List[str], length: int, height: int):
    final_image = [[" " for x in range(length)] for y in range(height)]
    for y in range(height):
        for x in range(length):
            pixel_index = (y * length) + x
            for layer in layers:
                if layer[pixel_index] == BLACK:
                    break
                if layer[pixel_index] == WHITE:
                    final_image[y][x] = "X"
                    break
    for line in final_image:
        print("".join(line))


def first_and_second_star():
    data = pathlib.Path("fixtures/day8_input1.txt").read_text().strip()
    layers = create_layers(data, 25, 6)
    pixel_data = layer_pixel_data(layers)
    fewest_zeroes = sorted(pixel_data, key=_number_of_zeroes)[0]
    ones_times_twos = fewest_zeroes["1"] * fewest_zeroes["2"]
    decode_image(layers, 25, 6)
    return ones_times_twos


if __name__ == "__main__":
    print(first_and_second_star())
