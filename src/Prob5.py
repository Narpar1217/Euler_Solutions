"""
PROJECT EULER
Problem 5

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?


Author: Adam Beagle
"""

from Timer import Timer

################################################################################
def CheckDivisibleByAll(n, start, stop):
    """
    Returns true if an integer n is evenly divisible by
    all integers in range start - stop, inclusive.
    Assumes start > stop.
    """
    
    while stop >= start:
        if not n % stop == 0:
            return False
        
        stop -= 1

    return True

#-----------------------------------------------------------------------------
#FIXME: Currently returns answer in ~4 seconds. Lots of optimization still to be found.
def Prob5():
    n = 20*19

    #Don't need to check 1-10; Will be covered with range 11-19.
    #Also don't need to check 20, as only multiples of 20 being tested.
    while not CheckDivisibleByAll(n, 11, 19):
        n += 20                                         

    return n

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob5())
    finally:
        print 'Time: %.5fs' % timer.Interval

