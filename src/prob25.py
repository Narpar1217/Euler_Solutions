"""
PROJECT EULER
Problem 25

Author: Adam Beagle

PROBLEM DESCRIPTION:
  The 12th term of the Fibonacci sequence, F12 = 144, is the first to contain
  3 digits.
  
  What is the first term in the Fibonacci sequence to contain 1000 digits?
  
"""

from eulerutility import fibs
from timer import Timer

###############################################################################
def prob25():
    stop = 10**999 #Lowest 1000-digit number
    for i, n in enumerate(fibs()):
        if n >= stop:
            return i

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob25())
    finally:
        print 'Time:   %.5fs' % timer.interval
