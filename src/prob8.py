"""
PROJECT EULER
Problem 8

Author: Adam Beagle

PROBLEM DESCRIPTION:
  Find the greatest product of five consecutive digits in the 1000-digit
  number.

"""

from os import path

from timer import Timer

###############################################################################
def prob8(filename):
    highProd = 0
    highFive = []
    
    with open(filename, 'r') as f:
        bignum = f.read()

    bignum = bignum.replace('\n', '')

    for i in xrange(len(bignum) - 4):
        five = [int(n) for n in bignum[i:i+5]]
        prod = list_product(five)
        
        if prod > highProd:
            highProd = prod
            highFive = five
    
    return highFive, highProd
   
def list_product(nums):
    prod = 1
    
    for n in nums:
        prod *= n

    return prod

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            fName = path.join('..', 'res', 'Prob8_bignum.txt')
            factors, product = prob8(fName)
            operation = (str(product) + ' = ' +
                         " x ".join([str(n) for n in factors]))
            print 'Answer:', operation
    finally:
        print 'Time:   %.5fs' % timer.interval

