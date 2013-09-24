"""
PROJECT EULER
Problem 4

Author: Adam Beagle

PROBLEM DESCRIPTION:
  A palindromic number reads the same both ways.
  The largest palindrome made from the product of
  two 2-digit numbers is 9009 = 91  99.
  Find the largest palindrome made from the product of two 3-digit numbers.

"""

from timer import Timer

###############################################################################
def prob4():
    largest = 0

    for n1 in xrange(999, 99, -1):
        for n2 in xrange(n1, 99, -1):
            prod = n1 * n2
            
            if prod < largest:
                break

            #If palindromic, must be largest
            if prod == reverse_int(prod):
                largest = prod
                
    return largest

def reverse_int(n):
    """
    Return a reversed integer 'n.' (ex: input 1234, ouput 4321)
    Works for positive and negative values of n.
    
    """
    reverse = 0
    negFlag = n < 0
    n = abs(n)

    while n > 9:
        reverse += n % 10
        reverse *= 10
        n /= 10

    reverse += n

    return reverse if not negFlag else -1*reverse
    

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob4())
    finally:
        print 'Time:   %.5fs' % timer.interval
        

