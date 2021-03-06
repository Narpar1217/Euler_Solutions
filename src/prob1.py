"""
PROJECT EULER
Problem 1

Author: Adam Beagle

PROBLEM DESCRIPTION:
  Add all the natural numbers below one thousand that are multiples of 3 or 5.

"""

from timer import Timer

###############################################################################
def prob1():
    return sum((n for n in xrange(1, 1000)
                if n % 3 == 0 or n % 5 == 0)
               )

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob1())
    finally:
        print 'Time:   %.5fs' % timer.interval
		
		

