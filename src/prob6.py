"""
PROJECT EULER
Problem 6

Author: Adam Beagle

PROBLEM DESCRIPTION:
  Find the difference between the sum of the squares of the
  first one hundred natural numbers and the square of the sum.
  
"""
from timer import Timer

###############################################################################
def prob6():
    sumOfSquares = sum((n**2 for n in xrange(1, 101)))
    squareOfSum = sum(xrange(1, 101))**2

    return squareOfSum - sumOfSquares

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob6())
    finally:
        print 'Time:   %.5fs' % timer.interval
