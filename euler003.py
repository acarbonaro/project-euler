"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


import math
from functools import reduce


MAGIC_NUMBER = 600851475143


def get_prime_factors(num=None, factors=[], orig_num=0, sieve_results=None):
    """
    Get all prime factors of `num`
    """
    if not num:
        return []
    if orig_num == 0:
        orig_num = num
    if not sieve_results:
        sieve_results = [x for x in sieve(num)]
    for prime in [x for x in sieve_results if num % x == 0]:
        if num % prime == 0:
            factors.append(prime)
            get_prime_factors(num=int(num / prime), factors=factors, orig_num=orig_num, sieve_results=sieve_results)
        if num < 2 or (factors and reduce(lambda x, y: x * y, factors) == orig_num):
            return factors
    return factors


def sieve(num):
    """
    Run through the Sieve of Eratosthenes for `num` returing a list
    """
    if num < 2:
        return [False] * num

    integers = [True] * num
    integers[0] = integers[1] = False

    for (i, is_prime) in enumerate(integers):
        if is_prime:
            yield i
            for j in range(i * i, num, i):
                integers[j] = False


def test():
    return sorted(get_prime_factors(num=13195))[-1]


def solution():
    return sorted(get_prime_factors(num=13195))[-1]


if __name__ == "__main__":
    print(solution())
