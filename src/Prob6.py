"""
PROJECT EULER
Problem 6

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.


Author: Adam Beagle
"""
from Timer import Timer

################################################################################
def Prob6():
    sumOfSquares = sum((n**2 for n in xrange(1, 101)))
    squareOfSum = sum(xrange(1, 101))**2

    return squareOfSum - sumOfSquares

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob6())
    finally:
        print 'Time: %.5fs' % timer.Interval
