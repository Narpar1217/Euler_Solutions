"""
PROJECT EULER
Problem 13

Author: Adam Beagle

PROBLEM DESCRIPTION:
  Work out the first ten digits of the sum of the
  one-hundred 50-digit numbers in ../res/Prob13_largenums.txt

"""

from os import path

from timer import Timer

################################################################################
def prob13(filename):
    with open(filename, 'r') as f:
        _sum = sum((int(line) for line in f))

    return str(_sum)[:10]

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            filename = path.join('..', 'res', 'Prob13_largeNums.txt')
            print 'Answer: ' + str(prob13(filename))
    finally:
        print 'Time:   %.5fs' % timer.interval
