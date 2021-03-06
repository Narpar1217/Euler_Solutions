"""
PROJECT EULER
Problem 7

Author: Adam Beagle

PROBLEM DESCRIPTION:
  By listing the first six prime numbers:
  2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
  What is the 10,001st prime number?
  
"""

from math import log

from eulerutility import sieve_of_eratosthenes
from timer import Timer

###############################################################################
def prob7():
    desiredPrime = 10001 # Ex: desiredPrime = 20 means 20th prime desired
    upperLimit = 10**4   # Arbitrary starting point. Accuracy improved below.
    limitMult = 5
    primes = []

    # Number of primes below a given n is approximately n / ln n
    # This fact is used to approximate a suitable upper limit for the sieve.
    while (upperLimit / log(upperLimit)) <= desiredPrime:
        upperLimit *= limitMult

    # If approximated upper limit was insufficient, ask user if reattempt
    # desired.
    while len(primes) < desiredPrime:
        if len(primes) > 0:
            print ('WARNING: upperLimit too low. %d primes found below %d.' %
                   (len(primes), upperLimit))
            print 'Reattempting with upperLimit * %d\n' % limitMult
            
        primes = sieve_of_eratosthenes(upperLimit)
        upperLimit *= limitMult
        
    return primes[desiredPrime - 1]

            
###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob7())
    finally:
        print 'Time:   %.5fs' % timer.interval


