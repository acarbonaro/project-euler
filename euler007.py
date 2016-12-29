"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""


def limited_sieve(limit, original_limit=None, primes_count=0):
    """
    Run through the Sieve of Eratosthenes until you find the value with a
    position of `limit` returning a list of the preceeding values
    """
    if limit < 2:
        return [False] * limit

    if not original_limit:
        original_limit = limit

    integers = [True] * (limit)
    if integers[0] == True:
        integers[0] = integers[1] = False

    for (i, is_prime) in enumerate(integers):
        if is_prime:
            primes_count += 1
            for j in range(i * i, limit, i):
                integers[j] = False

    primes = [y for y in range(limit) if integers[y]]

    if len(primes) <= original_limit:
        primes = limited_sieve(limit * 2, original_limit, primes_count)

    return primes[:original_limit]


def test():
    return limited_sieve(6)[-1]


def solution():
    return limited_sieve(10001)[-1]


if __name__ == "__main__":
    print(test())
    print(solution())
