"""
PROJECT EULER
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


Author: Adam Beagle
"""

from math import sqrt
from Timer import Timer

################################################################################
def Prob10():
    primes = SieveOfEratosthenes(2000000)
    return sum(primes)

#-----------------------------------------------------------------------------
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
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob10())
    finally:
        print 'Time: %.5fs' % timer.Interval
        
    
