"""
PROJECT EULER
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


Author: Adam Beagle
"""

from math import sqrt
from EulerUtility import SieveOfEratosthenes
from Timer import Timer

################################################################################
def Prob10():
    return sum(SieveOfEratosthenes(2000000, generator=True))


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob10())
    finally:
        print 'Time:   %.5fs' % timer.Interval
        
    
