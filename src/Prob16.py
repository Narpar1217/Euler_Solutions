"""
PROJECT EULER
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

Author: Adam Beagle
"""

from EulerUtility import GetDigits
from Timer import Timer

################################################################################
def Prob16():
    n = 2**1000
    return sum(GetDigits(n))
    

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob16())
    finally:
        print 'Time:   %.5fs' % timer.Interval
		
		

