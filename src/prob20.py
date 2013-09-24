"""
PROJECT EULER
Problem 20

Author: Adam Beagle

PROBLEM DESCRIPTION:
  Find the sum of the digits in the number 100! (100 factorial).

"""
from math import factorial

from eulerutility import get_digits
from timer import Timer

###############################################################################
def prob20():
    return sum(get_digits(factorial(100)))

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob20())
    finally:
        print 'Time:   %.5fs' % timer.interval
