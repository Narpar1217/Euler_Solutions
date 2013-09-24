"""
PROJECT EULER
Problem 48

Author: Adam Beagle

PROBLEM DESCRIPTION:
  The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
  Find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""

from eulerutility import get_digits
from timer import Timer

###############################################################################
def prob48():
    return sum((n**n for n in xrange(1, 1001))) % 10**10

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob48())
    finally:
        print 'Time:   %.5fs' % timer.interval
