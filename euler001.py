"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def fizz_buzz(min=1, max=10):
    return [x for x in range(min, max) if x % 3 == 0 or x % 5 == 0]


def solution():
    return sum(fizz_buzz(max=1000))


if __name__ == "__main__":
    print(solution())
