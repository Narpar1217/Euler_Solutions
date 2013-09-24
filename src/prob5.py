"""
PROJECT EULER
Problem 5

Author: Adam Beagle

PROBLEM DESCRIPTION:

  2520 is the smallest number that can be divided by each
  of the numbers from 1 to 10 without any remainder.

  What is the smallest positive number that is evenly
  divisible by all of the numbers from 1 to 20?

"""

from eulerutility import get_prime_factorization, unique_counts
from timer import Timer

###############################################################################

#Finding LCM of set of numbers:
    #  Find prime factorization for each number
    #  The LCM is the product of the highest powers of each prime from the
    #    factorizations
def compute_set_LCM(nums, primes):
    """
    Return the least common multiple of sequence of ints nums.
    Primes must be list of primes <= max(nums), in increasing order.
    
    """
    maxPrimeOccurences = {} #Keys, values will be a prime, and its highest
                            #power found in a prime factorization of a number
                            #in nums, respectively.

    #Fill maxPrimeOccurences
    for n in nums:
        pFacs = get_prime_factorization(n, primes)

        for factor, count in unique_counts(pFacs):
            if factor in maxPrimeOccurences:
                maxPrimeOccurences[factor] = max(maxPrimeOccurences[factor],
                                                 count)
            else:
                maxPrimeOccurences[factor] = count

    #Compute LCM
    lcm = 1
    for prime, exp in maxPrimeOccurences.items():
        lcm *= prime ** exp

    return lcm

def prob5():
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
       
    return compute_set_LCM(range(1, 21), primes)

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob5())
    finally:
        print 'Time:   %.5fs' % timer.interval

