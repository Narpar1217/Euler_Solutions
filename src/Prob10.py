"""
PROJECT EULER
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


Author: Adam Beagle
"""

from math import sqrt

################################################################################
def SieveOfEratosthenes(limit):
    """Returns list of primes <= limit, in increasing order."""
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

primes = SieveOfEratosthenes(2000000)
print 'Answer:', sum(primes)
