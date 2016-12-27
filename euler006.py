"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


import math


def difference_between_sum_of_squares_and_square_of_sum(min=1, max=10):
    return int(math.pow(sum(range(min, max + 1)), 2) - sum([math.pow(x, 2) for x in range(min, max + 1)]))


if __name__ == "__main__":
    print(difference_between_sum_of_squares_and_square_of_sum(max=100))
