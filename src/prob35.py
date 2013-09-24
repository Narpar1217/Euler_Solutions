"""
PROJECT EULER
Problem 35

Author: Adam Beagle

PROBLEM DESCRIPTION:
  The number, 197, is called a circular prime because all rotations of the
  digits: 197, 971, and 719, are themselves prime.

  There are thirteen such primes below 100:
  2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

  How many circular primes are there below one million?
  
"""

from eulerutility import get_digits, sieve_of_eratosthenes
from timer import Timer

###############################################################################
def check_all_digits_odd(n):
    """Return True if all digits of n are odd, false otherwise."""
    for d in get_digits(n):
        if d % 2 == 0 or d % 5 == 0:
            return False

    return True

def is_circular(n, primes, circular):
    """
    Returns true if n is a circular prime, False otherwise.
    If n is circular, it and all its permutations will be added to list
    'circular.'
    
    Assumes n is prime.
    
    """
    newCircs = []
    for perm in permute_int(n):
        #Don't need to check n, already know it's prime
        if not perm == n and not perm in primes:
            return False

        newCircs.append(perm)

    circular += newCircs

    return True

def permute_int(n):
    """
    Generator; yields all circular permutations of int n, including n itself,
    as integers.

    """
    origN = n
    deg = 0
    temp = n
    
    while temp > 10:
        temp /= 10
        deg += 1

    for i in xrange(deg + 1):
        yield n
        right = n % 10
        n = (n / 10) + right * 10**deg

def prob35():
    primes = [p for p in sieve_of_eratosthenes(10**6, True)
              if p > 99 and check_all_digits_odd(p)]
    circular = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]

    for prime in primes:
        if not prime in circular and is_circular(prime, primes, circular):
            #IsCircular will accumulate circular primes in list 'circular'
            pass

    return len(circular)

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob35())
    finally:
        print 'Time:   %.5fs' % timer.interval
