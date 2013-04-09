"""
PROJECT EULER
Problem 8

Find the greatest product of five consecutive digits in the 1000-digit number.

Author: Adam Beagle
"""

from os import path
from Timer import Timer

################################################################################
def Prob8(filename):
    """Project Euler, problem 8"""

    highProd = 0
    highFive = []
    
    with open(filename, 'r') as f:
        bignum = f.read()

    bignum = bignum.replace('\n', '')

    for i in xrange(len(bignum) - 4):
        five = [int(n) for n in bignum[i:i+5]]
        prod = ListProduct(five)
        
        if prod > highProd:
            highProd = prod
            highFive = five
    
    return highFive, highProd
   
#-----------------------------------------------------------------------------
def ListProduct(nums):
    prod = 1
    
    for n in nums:
        prod *= n

    return prod


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            fName = path.join('..', 'res', 'Prob8_bignum.txt')
            factors, product = Prob8(fName)
            operation = str(product) + ' = ' + " x ".join([str(n) for n in factors])
            print 'Answer:', operation
    finally:
        print 'Time:   %.5fs' % timer.Interval

