"""
PROJECT EULER
Problem 9

A Pythagorean triplet is a set of three natural numbers, a b c, for which a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


Author: Adam Beagle
"""

from Timer import Timer

################################################################################
def GetPythagTriplets(sum):
    """
    Returns all pythagorean triplets whose sum equals passed sum.
    Naive solution. Would not scale well for large sums.
    """
    triplets = []

    for a in range(1, sum + 1):
        for b in range(1, sum + 1):
            c = sum - b - a

            if a**2 + b**2 == c**2:
                if not tuple(sorted((a, b, c))) in triplets:
                    triplets.append((a, b, c))

    return triplets

#-----------------------------------------------------------------------------
def Prob9():
    triplet = GetPythagTriplets(1000)[0]

    return triplet, triplet[0] * triplet[1] * triplet[2]


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            triplet, product = Prob9()
            operation = str(product) + ' = ' + " x ".join([str(n) for n in triplet])
            print 'Answer:', operation
    finally:
        print 'Time:   %.5fs' % timer.Interval

