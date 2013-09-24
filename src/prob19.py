"""
PROJECT EULER
Problem 19

Author: Adam Beagle

PROBLEM DESCRIPTION:
  How many Sundays fell on the first of the month during the twentieth
  century (1 Jan 1901 to 31 Dec 2000)?

"""

from datetime import date

from timer import Timer

###############################################################################
def prob19():
    count = 0

    for year in range(1901, 2001):
        for month in range(1, 13):
            count += (date(year, month, 1).weekday() == 6)

    return count

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(prob19())
    finally:
        print 'Time:   %.5fs' % timer.interval
