"""
PROJECT EULER
Problem 25

The 12th term of the Fibonacci sequence, F12 = 144, is the first to contain 3 digits.
What is the first term in the Fibonacci sequence to contain 1000 digits?


Author: Adam Beagle
"""

from EulerUtility import FibGen
from Timer import Timer

################################################################################
def Prob25():
    stop = 10**999 #Lowest 1000-digit number
    for i, n in enumerate(FibGen()):
        if n >= stop:
            return i


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob25())
    finally:
        print 'Time:   %.5fs' % timer.Interval
