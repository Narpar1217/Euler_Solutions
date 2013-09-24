"""
PROJECT EULER
Problem 26

Author: Adam Beagle

PROBLEM DESCRIPTION:
  A unit fraction contains 1 in the numerator. The decimal representation of
  the unit fractions with denominators 2 to 10 are given:
  
  1/2	=   0.5
  1/3	=   0.(3)
  1/4	=   0.25
  1/5	=   0.2
  1/6	=   0.1(6)
  1/7	=   0.(142857)
  1/8	=   0.125
  1/9	=   0.(1)
  1/10	=   0.1
  
  Where 0.1(6) means 0.166666..., which has a 1-digit recurring cycle.
  It can be seen that 1/7 has a 6-digit recurring cycle.

  Find the value of d < 1000 for which 1/d contains the longest recurring
  cycle in its decimal fraction part.
  
"""

from eulerutility import sieve_of_eratosthenes
from timer import Timer

###############################################################################
def get_cycle_length(n):
    """
    For a positve integer n, return the length of the repeating cycle of 1/n.
    
    """

    #Essentially implements long division as it would be done by hand.
    #Once any dividend has been reached a second time,
    #the cycle has restarted.
    dividends = [1]

    dividend = 10
    while not dividend in dividends:
        dividends.append(dividend)
        if n > dividend:
            dividend *= 10
        else:
            dividend = 10*(dividend % n)

    return len(dividends) - dividends.index(dividend)

#Important properties:
#  For a prime p:
#   * The period of 1 / p <= p - 1
#   * The period of 1/p divides evenly into p - 1
#   * p's of form 40k + n, for n in (1, 3, 9, 13, 27, 31, 37, 39),
#     are guaranteed to not be full reptend.
#  See http://en.wikipedia.org/wiki/Full_reptend_prime for more.
def is_full_reptend(p):
    """Return true if prime p is a full reptend prime."""

    failNs = (1, 3, 9, 13, 27, 31, 37, 39)
    for n in failNs:
        if (p - n) % 40 == 0:
            return False
    
    reptend = str((10**(p - 1) - 1) / p)

    #Get number of leading zeroes
    zeroes = 0
    temp = (1.0 / p)
    while int(temp * 10) == 0:
        zeroes += 1
        temp *= 10

    reptend = '0'*zeroes + reptend

    #Return False if cycle of a length that divides evenly into p - 1 is found.
    for i in range(2, (p / 2) + 1):
        if (p - 1) % i == 0 and reptend[:i] == reptend[i:2*i]:
            return False

    #If this is reached, can assume cycle is of length p - 1, and
    #p is full reptend.
    return True

#Explanation:
# A full reptend prime is a prime for which (10**(p - 1) - 1) / p produces
# a cyclical number of length p - 1 that is equivalent to the recurring cycle
# of 1 / p. A prime number p that is not full reptend has a cycle length that
# is a factor of p - 1.
#
# The period of a composite number c is <= c - 2.
#
# The answer is found by stepping backwards from 999 until a full reptend prime
# is found, and returning the maximum cycle length found up to that point.
#
# The correct result is guaranteed, as a non-full reptend prime can not have a
# period > itself / 2, no number below a full reptend prime can have a longer
# period, and the cycle length of any greater composite numbers are found
# explicitly.
def prob26():
    primes = sieve_of_eratosthenes(1000)
    _max = (0, 0) #i, len

    for i in xrange(999, 0, -1):
        if i in primes:
            if is_full_reptend(i):
                return max(i, _max[1])
        else:
            _len = get_cycle_length(i)
            if _len > _max[1]:
                _max = (i, _len)

    return maxLen

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob26())
    finally:
        print 'Time:   %.5fs' % timer.interval

