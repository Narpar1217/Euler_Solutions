"""
PROJECT EULER
Problem 19

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


Author: Adam Beagle
"""

from datetime import date
from Timer import Timer

################################################################################
def Prob19():
    count = 0

    for year in range(1901, 2001):
        for month in range(1, 13):
            count += (date(year, month, 1).weekday() == 6)

    return count


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob19())
    finally:
        print 'Time:   %.5fs' % timer.Interval
