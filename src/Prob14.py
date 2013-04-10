"""
PROJECT EULER
Problem 14

The following iterative sequence is defined for the set of positive integers:
n = n/2 (n is even)
n = 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13  40  20  10  5  16  8  4  2  1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proven yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


Author: Adam Beagle
"""

from Timer import Timer

################################################################################
def NextOddCollatz(n):
    """
    Given an odd positive integer n, returns next odd value
    in a Collatz sequence, and number of steps taken to reach it.
    Undefined behavior for even values of n. 
    """
    count = 1
    n = 3*n + 1

    while n % 2 == 0:
        n /= 2
        count += 1

    return n, count

#-----------------------------------------------------------------------------
def Prob14():
    longest = longestI = 0
    limit = 10**6
    colMap = {} #Keys are starts of Collatz sequence;
                #values are number of steps from key to 1.

    #Iterate through odd i's < limit, find longest chain
    #Note: A lower initial value for this loop is more efficient,
    #  as more values will be added to colMap, thus fewer
    #  chains will need to be entirely iterated through.
    for i in xrange(3, limit, 2):
        count = 0
        
        n = i
        while n > 1:
            #Case: Number of steps from n to 1 already known (in map)
            if n in colMap:
                count += colMap[n]
                break
            #Case: Get number of steps to next odd, loop again
            else:
                n, steps = NextOddCollatz(n)
                count += steps

        colMap[i] = count
        
        if count > longest:
            longest = count
            longestI = i

    return longestI, longest
    

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: %d (length %d)' % Prob14()
    finally:
        print 'Time:   %.5fs' % timer.Interval
