"""
PROJECT EULER
Problem 20

Find the sum of the digits in the number 100! (100 factorial).


Author: Adam Beagle
"""

from EulerUtility import GetDigits
from math import factorial
from Timer import Timer

################################################################################
def Prob20():
    return sum(GetDigits(factorial(100)))


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob20())
    finally:
        print 'Time:   %.5fs' % timer.Interval
