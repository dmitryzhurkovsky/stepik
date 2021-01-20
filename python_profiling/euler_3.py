"""Project Euler problem 3 solve"""
from __future__ import print_function
import sys
import math

def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if not num % i:
            return False
    return True

def find_prime_factors(num):
    """Find prime factors of num"""
    result = []
    for i in range(2, int(math.sqrt(num)) + 1):
        if is_prime(i) and not num % i:
            result.append(i)
    return result

if __name__ == '__main__':
    try:
        num = int(sys.argv[1])
    except (TypeError, ValueError, IndexError):
        sys.exit("Usage: euler_3.py number")

    prime_factors = find_prime_factors(num)
    if len(prime_factors) == 0:
        print("Can't find prime factors of %d" % num)
    else:
        print("Answer: %d" % prime_factors[-1])

