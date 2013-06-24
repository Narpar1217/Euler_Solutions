"""
PROJECT EULER
Problem 43

The number 1406357289 is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.


Author: Adam Beagle
"""

from EulerUtility import GetDigits, Multiples
from itertools import permutations
from Timer import Timer

################################################################################
def CheckPerm(n):
    """
    Tests a single 10-digit number against the criteria described in
    the problem description. Assumes the final 3 digits are divisible
    by 17; See Prob43(). Returns True if all criteria met, False otherwise.
    """
    s = str(n)
    
    if int(s[6:9]) % 13 > 0:
        return False
    if int(s[5:8]) % 11 > 0:
        return False
    if int(s[4:7]) % 7 > 0:
        return False
    if int(s[3:6]) % 5 > 0:
        return False
    if int(s[2:5]) % 3 > 0:
        return False
    if int(s[1:4]) % 2 > 0:
        return False

    return True
    
#-----------------------------------------------------------------------------
def CheckPerms(pool, end):
    """
    Checks each permutation of the digits in pool against the criteria
    in the problem description. 'end' is a number divisble by 17, the
    last 3 digits of a 10-digit pandigital number. Note 'end' can be < 100,
    it will be padded with zeroes in this function. Returns a list of
    valid 10-digit numbers, or an empty list if none found.
    """
    
    good = []
    
    for p in permutations(pool):
        s = ''.join((str(d) for d in p)) + '%03d' % end

        if CheckPerm(s):
            good.append(int(s))

    return good

#-----------------------------------------------------------------------------
#Algorithm description:
#  For each 3-distinct-digit multiple of 17, permutations
#  of the remaining digits are tested against the criteria
#  of the problem statement.
def Prob43():
    """Returns answer to Project Euler Problem 43."""
    _sum = 0

    for m in Multiples(17, 1000, 17):
        pool = range(10)

        if m < 100:
            #Account for 0 in front of 2-digit m
            pool.remove(0)
        elif len(set(GetDigits(m))) < 3:
            #m is not valid if it contains a repeated digit
            #Note no multiples of 17 < 100 fit this criteria, even with leading 0
            continue

        for d in GetDigits(m):
            pool.remove(d)
            
        for valid in CheckPerms(pool, m):
            _sum += valid

    return _sum

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob43())
    finally:
        print 'Time:   %.5fs' % timer.Interval
		
		

