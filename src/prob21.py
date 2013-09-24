"""
PROJECT EULER
Problem 21

Author: Adam Beagle

PROBLEM DESCRIPTION:
  Let d(n) be defined as the sum of proper divisors of n (numbers less than n
  which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then a
  and b are an amicable pair and each of a and b are called amicable numbers.

  For example, the proper divisors of 220 are
  1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; Therefore d(220) = 284.

  The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

  Evaluate the sum of all the amicable numbers under 10000.

"""

from math import sqrt

from timer import Timer

###############################################################################
def get_proper_divisors(n):
    """
    Generator; yields proper divisors of n.
    Note: Will not yield divisors in increasing order.
    
    """
    limit = int(sqrt(n)) + 1
    
    if n == 1:
        yield 0
        return

    yield 1
    
    for d in range(2, limit):
        if n % d == 0:
            yield d
            
            if not (n / d) == d: #Accounts for perfect squares
                yield n / d

def prob21():
    limit = 10**4
    amicableNums = []

    for i in range(2, 10000):
        if i in amicableNums:
            continue
        
        s1 = sum(get_proper_divisors(i))

        #All s1 <= i already tested; Only check for pair if s1 > i
        if s1 > i: 
            s2 = sum(get_proper_divisors(s1))

            if s2 == i and not s1 == i:
                amicableNums += [s1, s2]
            
    return sum(amicableNums)

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob21())
    finally:
        print 'Time:   %.5fs' % timer.interval
