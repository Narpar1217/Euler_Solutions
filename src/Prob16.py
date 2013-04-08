"""
PROJECT EULER
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

Author: Adam Beagle
"""

from Timer import Timer

################################################################################
def GetDigits(n):
    """Generator. Yields each digit of an integer n, right to left."""
    a = n
    while a > 0:
        yield a % 10
        
        if a > 1:
            a /= 10
        else:
            a = 0

#-----------------------------------------------------------------------------
def Prob16():
    n = 2**1000
    return sum(GetDigits(n))
    

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob16())
    finally:
        print 'Time: %.5fs' % timer.Interval
		
		

