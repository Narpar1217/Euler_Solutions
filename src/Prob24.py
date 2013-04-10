"""
PROJECT EULER
Problem 24

Author: Adam Beagle


A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order.

The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0 - 9?
"""

from math import factorial
from Timer import Timer

################################################################################
# There are x! permutations of a sequence, seq, containing x elements.
# Therefore, if a particular starting element is chosen from seq, (x-1)!
# permutations exist of seq that begin with that element.
#
# Given a seq sorted in increasing order and an index i,
# the term of the lexicographically "highest" permutation with
# seq[i] as its first digit is given by i*(n - 1)!.
#
# This function uses the above fact recursively to get
# the "first" elements of an ever-smaller seq, until
# seq is empty and the nth lexicographic permutation
# has been found.
def NthLexicographicPerm(seq, n, perm=[], permN=0):
    """
    Returns a string representation of the nth lexicographic
    permutation of a sorted list seq.
    A user only needs to pass seq and n; The other two
    arguments are used for recursive calls.
    Note: seq is emptied in place. Send a copy if necessary.
    """
    fac = factorial(len(seq) - 1)
    i = 0

    temp = permN + fac
    while temp < n:
        i += 1
        temp += fac

    permN += fac * i
    perm.append(seq.pop(i))
    
    if not seq:
        return ''.join((str(d) for d in perm))
    else:
        return NthLexicographicPerm(seq, n, perm, permN)
    
#-----------------------------------------------------------------------------
def Prob24():
    return NthLexicographicPerm(range(10), 10**6)
    

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob24())
    finally:
        print 'Time:   %.5fs' % timer.Interval
		
		

