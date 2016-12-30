"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


from euler003 import sieve


def test():
    return sum(list(sieve(10)))


def solution():
    return sum(list(sieve(2000000)))


if __name__ == '__main__':
    print(solution())
