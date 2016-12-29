"""
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


import math
from collections import Counter
from euler003 import get_prime_factors
from functools import reduce


def smallest_number_divisible_by_range(min=1, max=10, range_list=None):
    """
    Get the smallest number divisble by all numbers in a given range.
    """
    range_to_test = range_list if range_list else range(min, max + 1)
    factors_dict = dict.fromkeys(range(1, max + 1), [])
    for i in range_to_test:
        if i > 1:
            i_factors = get_prime_factors(num=i, factors=[], orig_num=0)
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


def test():
    return smallest_number_divisible_by_range(1, 10)


def solution():
    return smallest_number_divisible_by_range(1, 20)


if __name__ == "__main__":
    print(solution())
