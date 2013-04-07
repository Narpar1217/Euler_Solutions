"""
PROJECT EULER
Problem 6

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.


Author: Adam Beagle
"""

sumOfSquares = sum([n**2 for n in xrange(1, 101)])
squareOfSum = sum(xrange(1, 101))**2

print 'Answer:', squareOfSum - sumOfSquares
