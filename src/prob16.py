"""
PROJECT EULER
Problem 16

Author: Adam Beagle

PROBLEM DESCRIPTION:
  2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
  What is the sum of the digits of the number 2^1000?
  
"""

from eulerutility import get_digits
from timer import Timer

###############################################################################
def prob16():
    n = 2**1000
    return sum(get_digits(n))

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob16())
    finally:
        print 'Time:   %.5fs' % timer.interval
