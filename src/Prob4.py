"""
PROJECT EULER
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91  99.
Find the largest palindrome made from the product of two 3-digit numbers.

Author: Adam Beagle
"""

from Timer import Timer

################################################################################
def Prob4():
    n1 = 999
    done = False
    largest = 0

    for n1 in xrange(999, 99, -1):
        for n2 in xrange(n1, 99, -1):
            prod = n1 * n2

            if prod < largest:
                break           #Prod too small; Can't be answer

            #If palindromic, must be largest
            if prod == ReverseInt(prod):
                largest = prod
                
    return largest

#---------------------------------------------------------------
def ReverseInt(n):
    """
    Returns a reversed n. (ex: input 1234, ouput 4321)
    Works for positive and negative n's.
    """
    reverse = 0
    negFlag = n < 0

    if negFlag:
        n *= -1

    while n > 9:
        reverse += n % 10
        reverse *= 10
        n /= 10

    reverse += n

    return reverse if not negFlag else -1*reverse
    

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob4())
    finally:
        print 'Time: %.5fs' % timer.Interval
        

