"""
PROJECT EULER
Problem 28

Author: Adam Beagle


Starting with the number 1 and moving to the right in aclockwise
direction a 5 by 5 spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a
1001 by 1001 spiral formed in the same way?
"""

from Timer import Timer

################################################################################
def SpiralDiagTerms(maxSide):
    """
    Generator. Yields next element that is on either of a
    maxSide x maxSide clockwise spiral built of integers starting
    at 1, and increasing by 1 for each term, where the 2nd term
    is to the right of 1.
    """
    diag = 1
    yield diag

    for skip in xrange(2, maxSide, 2):
        for x in xrange(4):
            diag += skip
            yield diag
    
#-----------------------------------------------------------------------------
def Prob28():
    return sum(SpiralDiagTerms(1001))


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob28())
    finally:
        print 'Time:   %.5fs' % timer.Interval
		
		

