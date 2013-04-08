"""
PROJECT EULER
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?


Author: Adam Beagle
"""

from math import sqrt
from Timer import Timer

################################################################################
def GetPrimeFactorization(n, primes):
    """
    Returns a list of 2-tuples representing the prime factorization of n,
    or an empty list if factorization not successful.
    Tuples are of form (prime, exponent)
    Factorization will only fail if a prime factor of n is larger
    than the largest value in primes.
    Primes must be in increasing order.
    """
    factors = []

    if n in primes:
        return [n]
    
    for p in primes:
        if p > (n / 2):
          break
        
        if n % p == 0:
            factors.append(p)
            factors += GetPrimeFactorization(n / p, primes)
            break

    prod = 1
    for f in factors:
        prod *= f

    return factors if prod == n else []

#-----------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------
def SieveOfEratosthenes(limit):
    """
    Returns list of primes <= limit, in increasing order.
    """
    sieve = [True] * (limit + 1)
    i = 2
    
    while i < sqrt(limit):
        if sieve[i]:
            m = 0
            j = i**2
            while j <= limit:
                sieve[j] = False
                m += 1
                j = (i**2) + (m*i)
                
        i += 1

    return [index for index,value in enumerate(sieve) if index >= 2 and value]

  
################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob3())
    finally:
        print 'Time: %.5fs' % timer.Interval
