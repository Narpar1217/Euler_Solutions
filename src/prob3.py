"""
PROJECT EULER
Problem 3

Author: Adam Beagle

PROBLEM DESCRIPTION:
  The prime factors of 13195 are 5, 7, 13 and 29.
  What is the largest prime factor of the number 600851475143?

"""

from timer import Timer
from eulerutility import get_prime_factorization, sieve_of_eratosthenes

###############################################################################
def prob3():
    n = 600851475143
    primeLimit = 10**3
    factors = []

    #Start with relatively short sieve, if all prime factors not contained,
    #build again with increased size.
    while not factors:
        primeLimit *= 10
        primes = sieve_of_eratosthenes(primeLimit)
        factors = get_prime_factorization(n, primes)

    return max(factors)


###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob3())
    finally:
        print 'Time:   %.5fs' % timer.interval
