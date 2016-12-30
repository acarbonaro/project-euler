"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


from euler008 import list_product
from functools import reduce


def get_pythagorean_triplet_from_value(value=12):
    for a in range(2, value + 1):
        for b in range(a + 1, value + 1):
            for c in range(b + 1, value +1):
                if a + b + c == value and a**2 + b**2 == c**2:
                    return [a, b, c]
    return None


def test():
    return list_product(get_pythagorean_triplet_from_value())


def solution():
    return list_product(get_pythagorean_triplet_from_value(1000))


if __name__ == '__main__':
    print(solution())
