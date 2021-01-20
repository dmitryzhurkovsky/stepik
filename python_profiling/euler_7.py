"""Project euler problem 7 solve"""
from __future__ import print_function
import math
import sys
import cProfile


def profile(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper


def is_prime(num):
    """
       Checks if num is prime number.

       >>> is_prime(2)
       True
       >>> is_prime(3)
       True
       >>> is_prime(4)
       False
       >>> is_prime(5)
       True
       >>> is_prime(41)
       True
       >>> is_prime(42)
       False
       >>> is_prime(43)
       True
       """
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


@profile
def get_prime_numbers(count):
    """
    Get 'count' prime numbers.

    >>> get_prime_numbers(1)
    [2]
    >>> get_prime_numbers(2)
    [2, 3]
    >>> get_prime_numbers(3)
    [2, 3, 5]
    >>> get_prime_numbers(6)
    [2, 3, 5, 7, 11, 13]
    >>> get_prime_numbers(9)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> get_prime_numbers(19)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
    """
    prime_numbers = [2]
    next_numbers = 3

    while len(prime_numbers) < count:
        if is_prime(next_numbers):
            prime_numbers.append(next_numbers)
        next_numbers += 1

    return prime_numbers


if __name__ == '__main__':
    try:
        count = int(sys.argv[1])
    except (TypeError, ValueError, IndexError):
        sys.exit("Usage: euler_7.py number")
    if count < 1:
        sys.exit("Error: number must be greater than zero")

    prime_numbers = get_prime_numbers(count)
    print(f'Answer: {prime_numbers[-1]}')
