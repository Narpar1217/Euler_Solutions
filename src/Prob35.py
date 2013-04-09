"""
PROJECT EULER
Problem 35

Author: Adam Beagle


The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.
There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from EulerUtility import GetDigits, SieveOfEratosthenes
from Timer import Timer

################################################################################
def CheckAllDigitsOdd(n):
    """Returns True if all digits of n are odd, false otherwise."""
    for d in GetDigits(n):
        if d % 2 == 0 or d % 5 == 0:
            return False

    return True

#-----------------------------------------------------------------------------
def IsCircular(n, primes, circular):
    """
    Returns true if n is a circular prime, False otherwise.
    If n is circular, it and all its permutations will be added to list 'circular.'
    Assumes n is prime.
    
    """
    newCircs = []
    for perm in PermuteInt(n):
        #Don't need to check n, already know it's prime
        if not perm == n and not perm in primes:
            return False

        newCircs.append(perm)

    circular += newCircs

    return True

#-----------------------------------------------------------------------------
def PermuteInt(n):
    """Generator. Yields all circular permutations of int n, including n itself, as integers."""
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
        
        
#-----------------------------------------------------------------------------
def Prob35():
    primes = [p for p in SieveOfEratosthenes(10**6, True) if p > 99 and CheckAllDigitsOdd(p)]
    circular = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]

    for prime in primes:
        if not prime in circular and IsCircular(prime, primes, circular):
            #IsCircular will accumulate circular primes in list 'circular'
            pass

    return len(circular)

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob35())
    finally:
        print 'Time:   %.5fs' % timer.Interval
		
		

