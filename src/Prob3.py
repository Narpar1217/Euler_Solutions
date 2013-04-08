"""
PROJECT EULER
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?


Author: Adam Beagle
"""

from Timer import Timer
from EulerUtility import GetPrimeFactorization, SieveOfEratosthenes

################################################################################
def Prob3():
    n = 600851475143
    primeLimit = 10**3
    factors = []

    #Start with relatively short sieve, if all prime factors not contained,
    #build again with increased size.
    while not factors:
        primeLimit *= 10
        primes = SieveOfEratosthenes(primeLimit)
        factors = GetPrimeFactorization(n, primes)

    return max(factors)


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob3())
    finally:
        print 'Time: %.5fs' % timer.Interval
