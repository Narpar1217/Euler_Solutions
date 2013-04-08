"""
EulerUtility.py

This file contains any functions that are used by
multiple Project Euler solutions.

Author: Adam Beagle
"""

#-----------------------------------------------------------------------------
def GetPrimeFactorization(n, primes):
    """
    Returns a list of 2-tuples representing the prime factorization of n,
    or an empty list if factorization fails.
    Tuples are of form (prime, exponent).
    Factorization will fail if any prime factor of n is larger than the largest value in primes.
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
def SieveOfEratosthenes(limit, generator=False):
    """
    Returns list of primes <= limit, in increasing order.
    If generator is set, primes returned as generator.
    """
    from math import sqrt
    
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

    if generator:
        return (index for index,value in enumerate(sieve) if index >= 2 and value)
    else:
        return [index for index,value in enumerate(sieve) if index >= 2 and value]
