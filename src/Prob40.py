"""
PROJECT EULER
Problem 40

Author: Adam Beagle


An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

from Timer import Timer

################################################################################
def Prob40():
    prod = 1
    charCount = 0
    goals = [1, 10, 100, 1000, 10**4, 10**5, 10**6]
    n = 1
    
    while goals:
        for c in str(n):
            charCount += 1
            
            if charCount in goals:
                prod *= int(c)
                goals.remove(charCount)

        n += 1

    return prod


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob40())
    finally:
        print 'Time:   %.5fs' % timer.Interval
		
		

