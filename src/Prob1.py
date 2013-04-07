"""
PROJECT EULER
Problem 1

Add all the natural numbers below one thousand that are multiples of 3 or 5.

Author: Adam Beagle
"""

print sum([n for n in xrange(1, 1000) if n % 3 == 0 or n % 5 == 0])
