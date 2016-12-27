"""
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import math
from collections import Counter
from functools import reduce


def get_prime_factors(num, factors=[], orig_num=0, sieve_results=None):
    """
    Get all prime factors of `num`
    """
    if orig_num == 0:
        orig_num = num
    if not sieve_results:
        sieve_results = [x for x in sieve(num)]
    for prime in [x for x in sieve_results if num % x == 0]:
        if num % prime == 0:
            factors.append(prime)
            get_prime_factors(int(num / prime), factors, orig_num, sieve_results)
        if num < 2 or (factors and reduce(lambda x, y: x * y, factors) == orig_num):
            return factors
    return factors


def sieve(num):
    """
    Run through the Sieve of Eratosthenes for `num` returing a list
    """
    integers = [True] * num
    integers[0] = integers[1] = False

    for (i, is_prime) in enumerate(integers):
        if is_prime:
            yield i
            for j in range(i * i, num, i):
                integers[j] = False



def smallest_number_divisible_by_range(min=1, max=10, range_list=None):
    """
    Get the smallest number divisble by all numbers in a given range.
    """
    range_to_test = range_list if range_list else range(min, max + 1)
    factors_dict = dict.fromkeys(range(1, max + 1), [])
    for i in range_to_test:
        if i > 1:
            i_factors = get_prime_factors(i, [], 0)
            # If the number has factors, ensure that the greatest number of a
            # given factor is considered when creating the result
            if i_factors:
                new = True
                # Create a dictionary of factors grouped by value and reduce
                # that dictionary to only keys with values
                i_factors_dict = dict.fromkeys(range(1, max + 1), [])
                for x in set(i_factors):
                    factor_group = [x for i in i_factors if x == i]
                    if factor_group and len(factor_group) > len(i_factors_dict[x]):
                        i_factors_dict[x] = factor_group
                grouped_dict = {j[0]: j for j in i_factors_dict.values() if j}
                # Replace any saved groups when a newer instance of a group has
                # more of a value in it, eg. [2, 2, 2] will replace [2, 2]
                for index in grouped_dict.keys():
                    if len(list(Counter(factors_dict[index]) - Counter(grouped_dict[index]))) == 0:
                        factors_dict[index] = grouped_dict[index]
            # If the nubmer doesn't have factors, it's prime and needs to be
            # added to the dictionary for consideration
            else:
                factors_dict[i] = [i]
    # Turn the dictionary of factors into a list for easy consumption
    factors = [i for sublist in list(factors_dict.values()) for i in sublist]
    # Reduce the list by multiplying each item in the list with the next
    return reduce(lambda x, y: x * y, factors)

print(smallest_number_divisible_by_range(1, 20))
