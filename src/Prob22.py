"""
PROJECT EULER
Problem 22

Author: Adam Beagle


Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list
to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

from EulerUtility import GetAlphaSum
from os import path
from Timer import Timer

################################################################################
def Prob22(filename):
    _sum = 0
    
    with open(filename, 'r') as f:
        for i, name in enumerate(n.strip('\"') for n in sorted(f.read().split(','))):
            _sum += (i + 1) * GetAlphaSum(name)

    return _sum


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            filename = path.join('..', 'res', 'Prob22_names.txt')
            print 'Answer: ' + str(Prob22(filename))
    finally:
        print 'Time:   %.5fs' % timer.Interval
