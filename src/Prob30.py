"""
PROJECT EULER
Problem 30

Author: Adam Beagle


Surprisingly there are only three numbers that can be written as
the sum of fourth powers of their digits:
1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the
sum of fifth powers of their digits.
"""

from EulerUtility import GetDigits
from Timer import Timer

################################################################################
def CheckPowerSum(n, p):
    """
    Returns True if the sum of the pth power of each digit
    of n is equal to n, False otherwise.
    Returns False as soon as sum exceeds n.
    """
    _sum = 0
    
    for d in GetDigits(n):
        _sum += d**p

        if _sum > n:
            return False

    return _sum == n


#-----------------------------------------------------------------------------
def Prob30():
    _sum = 0

    #Find upper limit.
    # Upper limit is 9**5 * p, where p is the n at which the largest
    # power sum of an n-digit number, 9**5 * n (the sum of n 9's
    # raised to the 5th power), is less than the smallest n+1-digit number.
    # The power sum of any greater number will be less than the number itself,
    # thus any greater number cannot satisfy the solution condition.
    p = 2
    limit = 9**5 * p
    while limit > 10**p - 1:
        p += 1
        limit = 9**5 * p

    #Accumulate answer
    for i in xrange(2, limit):
        if CheckPowerSum(i, 5):
            _sum += i

    return _sum

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob30())
    finally:
        print 'Time:   %.5fs' % timer.Interval
		
		



