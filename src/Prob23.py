"""
PROJECT EULER
Problem 23

Author: Adam Beagle


A perfect number is a number for which the sum of its proper
divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest number
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot
be written as the sum of two abundant numbers.
"""

from EulerUtility import SieveOfEratosthenes
from math import sqrt
from Timer import Timer

################################################################################
#NOTE: Perfect numbers must be taken note of because all multiples
#      of a perfect number, excluding iteself, are abundant.
def AbundanceState(n):
    """
    For a positive integer n, returns 0 if n is deficient,
    1 if perfect, 2 if abundant.
    """
    _sum = 1
    properDivisors = [1]

    d = 2
    while d <= sqrt(n):
        if n % d == 0:
            div = n / d
            properDivisors.append(d)
            _sum += d

            #Account for perfect squares
            if not d == div:
                properDivisors.append(div)
                _sum += div
            
            if _sum > n:
                return 2
            
        d += 1

    return int(_sum == n)


#----------------------------------------------------------------------------
#Important Properties:
#   * Every multiple of a perfect or abundant number is abundant.
def FillAbundanceSieve_Range(sieve, primes, limit, start, stop, step=1):
    """
    Fills sieve in-place for range(start, stop, step) with abundant numbers.
    (Utility function used by SieveOfAbundanceosthenes. See that function for
    more information).
    """
    for i in xrange(start, stop, step):
        if not sieve[i] and not primes[i]:
            state = AbundanceState(i)

            #Ignore deficient numbers.
            if state:
                #Set i abundant, unless it is perfect.
                sieve[i] = bool(state - 1)

                #Set all multiples of i as abundant
                m = 2
                while i*m < limit:
                    sieve[i*m] = True
                    m += 1


#----------------------------------------------------------------------------
#Important Properties:
#    * Every integer > 20161 can be written as the sum of two abundant numbers 
def Prob23():
    maxAbundant = 20161
    _sum = 0
    primes = SieveOfEratosthenes(maxAbundant, sieveForm=True)
    abundants = SieveOfAbundanceosthenes(maxAbundant + 1, primes)
    
    return SumAll_NotSumOfTwoAbundants(abundants)


#----------------------------------------------------------------------------
#Important Properties:
#   * The smallest odd abundant number is 945; no known odds are perfect.
def SieveOfAbundanceosthenes(limit, primes):
    """
    Returns list where index n, for n < limit, contains a bool representing
    whether n is an abundant number.
    Ex: sieve[12] will equal True because 12 is abundant.
    """
    sieve = [False]*limit

    #Only test evens < 945 (all odds deficient).
    FillAbundanceSieve_Range(sieve, primes, limit, 12, min(945, limit), 2)

    #Test remaining values < limit (odds and evens).
    if limit > 946:
        sieve[945] = True
        FillAbundanceSieve_Range(sieve, primes, limit, 946, limit)

    return sieve


#----------------------------------------------------------------------------
#Important Properties:
#   * The smallest odd abundant number is 945.
def SumAll_NotSumOfTwoAbundants(abundants):
    """
    Returns sum of all numbers less than the maximum index of abundants
    which can not be written as the sum of two abundant numbers.
    """
    _max = len(abundants)

    #Abundants must be iterated through one by one in SumRange,
    #but indexable array like abundants also useful for efficiency,
    #so a separate list comprehension is built once here rather that on
    #each iteration of SumRange.
    abundants_lst = [i for i, v in enumerate(abundants) if v]

    #Any number < 24 can not possibly be sum of two abundant numbers
    _sum = sum(xrange(min(_max, 24)))
    
    #Every odd < 945 + 12 can not possiby be sum of two abundant numbers
    _sum += sum(xrange(25, min(_max, 957), 2))

    #Account for evens < 957 that aren't sum of two abundants
    _sum += SumRange_NotSumOfTwoAbundants(abundants, abundants_lst, 24, min(_max, 957), 2)

    if _max > 958:
        #Account for rest of numbers < _max
        _sum += SumRange_NotSumOfTwoAbundants(abundants, abundants_lst, 958, _max)

    return _sum


#-----------------------------------------------------------------------------
def SumRange_NotSumOfTwoAbundants(abundants_sieve, abundants_lst, start, stop, step=1):
    """
    Returns sum of values in range(start, stop, step) that can not be
    written as the sum of two abundant numbers.
    """
    _sum = 0

    for i in xrange(start, stop, step):
        
        #Skip i if already known to be abundant.
        #I haven't proven this yet, but I believe all abundants >= 24,
        #at least for the range I'm working with,
        #can be expressed as the sum of two abundants.
        if abundants_sieve[i]:
                continue

        #i is the sum of two abundants if, for some abundant 'a',
        #i - a is an abundant.
        #Note that as 12 is the smallest abundant,
        #'a' can not exceed i - 12.
        for a in abundants_lst:
            if a > i - 12:
                failed = False
                break
            if abundants_sieve[i - a]:
                failed = True
                break

        if not failed:
            _sum += i

    return _sum


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob23())
    finally:
        print 'Time:   %.5fs' % timer.Interval
