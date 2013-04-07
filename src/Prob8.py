"""
PROJECT EULER
Problem 8

Find the greatest product of five consecutive digits in the 1000-digit number.

Author: Adam Beagle
"""

from os import path

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
        prod = DoOneProduct(five)
        
        if prod > highProd:
            highProd = prod
            highFive = five

    print 'Answer:', highProd
    print highFive
        

#--------------------------------------------------
def DoOneProduct(nums):
    prod = 1
    
    for n in nums:
        prod *= n

    return prod

    
################################################################################
if __name__ == '__main__':
    fName = path.join('..', 'res', 'bignum.txt')
    Prob8(fName)
