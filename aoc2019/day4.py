"""
Day 4: Secure Container
"""
from typing import List, Callable

LOW = 145852
HIGH = 616942

VALID_PASSWORD_SIG = Callable[[List[int]], bool]


def _decompose_number(num: int) -> List[int]:
    """
    Break out the number into a list containing its digits.
    """
    return [((num // 10 ** x) % 10) for x in range(5, -1, -1)]


def valid_password_first_star(digits: List[int]) -> bool:
    """
    For a given 6-digit number, validate that:
    A) The digits do not decrease from left to right.
    B) There exists at least one pair of equal digits.
    """
    found_double = False
    for index in range(1, 6):
        previous = digits[index - 1]
        if digits[index] < previous:
            # Found a smaller digit; we can return False immediately
            return False
        if digits[index] == digits[index - 1]:
            found_double = True
    return found_double


def valid_password_second_star(digits: List[int]) -> bool:
    """
    Same as valid_password_first_star but with a new rule: pairs of doubles cannot be within a
    larger group of equal numbers. In other words, we want a "double", but no "triples" or
    anything greater.

    So we need to break down the group sizes in order to verify that any "double" we found earlier
    is indeed *only* a double.
    """
    if not valid_password_first_star(digits):
        return False
    group_sizes = [1]
    for index in range(1, 6):
        if digits[index] == digits[index - 1]:
            group_sizes[-1] += 1
        else:
            group_sizes.append(1)
    return 2 in group_sizes


def count_valid_passwords(low: int, high: int, func: VALID_PASSWORD_SIG) -> int:
    return len([num for num in range(low, high + 1) if func(_decompose_number(num))])


def first_star():
    print(count_valid_passwords(LOW, HIGH, valid_password_first_star))


def second_star():
    print(count_valid_passwords(LOW, HIGH, valid_password_second_star))


if __name__ == "__main__":
    first_star()
    second_star()
