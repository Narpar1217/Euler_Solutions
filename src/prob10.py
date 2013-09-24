"""
PROJECT EULER
Problem 10

Author: Adam Beagle

PROBLEM DESCRIPTION:
  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
  Find the sum of all the primes below two million.

"""

from eulerutility import sieve_of_eratosthenes
from timer import Timer

###############################################################################
def prob10():
    return sum(sieve_of_eratosthenes((10**6)*2, generator=True))

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob10())
    finally:
        print 'Time:   %.5fs' % timer.interval
