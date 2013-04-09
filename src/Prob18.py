"""
PROJECT EULER
Problem 18

Find the maximum total from top to bottom of
the triangle in ../res/Prob18_triangle.txt


Author: Adam Beagle
"""

from os import path
from Timer import Timer

################################################################################
def MaxTriangleSum(tri, h, r=0, c=0, currSum=0, maxSum=0):
    """
    Returns maximum sum obtainable by travelling from
    top to bottom of triangle tri.
    """
    if r < h - 1:
        currSum += tri[r][c]
        
        maxSum = MaxTriangleSum(tri, h, r + 1, c + 1, currSum, maxSum)
        maxSum = MaxTriangleSum(tri, h, r + 1, c, currSum, maxSum)
        
    else:
        maxSum = max(currSum + tri[r][c], maxSum)

    return maxSum

#-----------------------------------------------------------------------------
def Prob18(filename):
    triangle = []

    with open(filename, 'r') as f:
        for line in f:
            triangle.append([int(n) for n in line.split(' ')])
            
    return MaxTriangleSum(triangle, len(triangle))

        
################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            filename = path.join('..', 'res', 'Prob18_triangle.txt')
            print 'Answer: ' + str(Prob18(filename))
    finally:
        print 'Time:   %.5fs' % timer.Interval
