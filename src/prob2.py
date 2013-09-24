"""
PROJECT EULER
Problem 2

Author: Adam Beagle

PROBLEM DESCRIPTION:
  Each new term in the Fibonacci sequence is generated by adding the
  previous two terms. By starting with 1 and 2, the first 10 terms will be:

  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

  By considering the terms in the Fibonacci sequence whose values do not
  exceed four million, find the sum of the even-valued terms.

"""

from eulerutility import fibs
from timer import Timer

################################################################################
def prob2():
    limit = 4*(10**6)
    return sum((n for n in fibs(limit) if n % 2 == 0))

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob2())
    finally:
        print 'Time:   %.5fs' % timer.interval
		
		

