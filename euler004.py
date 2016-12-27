"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


MAGIC_NUMBER = 999


import itertools
import operator


def is_palindrome(num):
    num_str = str(num)
    return all([num_str[i] == num_str[-(i + 1)] for i in range(int(len(num_str) / 2))])


def largest_palindrome(target):
    products = {x[0] * x[1]: x for x in itertools.product(range(target + 1), range(target + 1)) if is_palindrome(x[0] * x[1])}
    sorted_products = sorted(products.items(), key=operator.itemgetter(0), reverse=True)
    for x in sorted_products:
        return x[0]
    return 0


if __name__ == "__main__":
    print(largest_palindrome(MAGIC_NUMBER))
