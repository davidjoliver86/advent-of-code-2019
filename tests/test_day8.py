"""
Test cases for day 8
"""
from aoc2019 import day8


def test_create_layers():
    assert day8.create_layers("123456789012", 3, 2) == ["123456", "789012"]
