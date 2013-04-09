"""
PROJECT EULER
Problem 27

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| < 1000

Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum
number of primes for consecutive values of n, starting with n = 0.


Author: Adam Beagle
"""

from EulerUtility import SieveOfEratosthenes
from Timer import Timer

################################################################################
def Prob27():
    primes = SieveOfEratosthenes(10**4)
    ABPrimes = [0, 1]
    ABPrimes += primes[:primes.index(1009)] #1009 is first prime over 1000
    maxLen, maxA, maxB = 0, 0, 0

    #In the two sample quadratics, |b| and |a| have ratios 41:1 and 20:1.
    #Thus, an educated guess says |a| will be low, |b| will be high
    #Raise aStop, lower bStop to expand range of search
    aStop = len(ABPrimes) / 2
    bStop = int(len(ABPrimes) * (2.0 / 3))

    for a in ABPrimes[:aStop]:
        for bI in xrange(len(ABPrimes) - 1, bStop, -1):
            b = ABPrimes[bI]
            _len, i, j = TestQuadratic_AllPerms(a, b, primes)
            if _len > maxLen:
                maxLen, maxA, maxB = _len, i, j

    return maxLen, maxA, maxB

#-----------------------------------------------------------------------------
def QuadraticGen(a, b, nStop, nStart=0):
    """
    Generator. Yields results of quadratic function n**2 + a*n + b
    for n values of nStart to nStop, inclusive.
    If nStop is 0, generator will run continuously.
    """
    if nStop:
        for n in xrange(nStart, nStop + 1):
            yield n**2 + a*n + b
    else:
        n = nStart
        while True:
            yield n**2 + a*n + b
            n += 1
    

#-----------------------------------------------------------------------------
def TestQuadratic(a, b, primes):
    chainLen = 0
    maxPrime = primes[-1]

    for n in QuadraticGen(a, b, 0):
        if n > maxPrime:
            raise ValueError("Exceeded max prime with a: %d, b: %d, n: %d" % (a, b, n))
        
        if n in primes:
            chainLen += 1
        else:
            break

    return chainLen

#-----------------------------------------------------------------------------
def TestQuadratic_AllPerms(a, b, primes):
    """
    Returns longest chain of primes created by any permuation
    of a and b. I.E., tested are a and b, -a and b,
    a and -b, -a and -b.
    """
    maxLen, maxA, maxB = 0, 0, 0

    for pair in ((a, b), (-a, b), (a, -b), (-a, -b)):
        _len = TestQuadratic(pair[0], pair[1], primes)
        
        if _len > maxLen:
            maxLen, maxA, maxB = _len, pair[0], pair[1]

    return (maxLen, maxA, maxB)
    

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            _len, a, b = Prob27()
            print 'Answer: ' + '%d (a: %d, b: %d, primes: %d)' % (a*b, a, b, _len)
    finally:
        print 'Time:   %.5fs' % timer.Interval
		
		

