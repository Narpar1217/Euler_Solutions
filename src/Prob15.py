"""
PROJECT EULER
Problem 15

Starting in the top left corner of a 2x2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?


Author: Adam Beagle
"""

from Timer import Timer

################################################################################
def BuildGraph(size):
    """
    Creates a graph from a size x size grid where nodes
    have connections such that 'movement' is only possible
    to the right or down. Nodes are numbered starting at 0 in the
    top left, and increasing along rows.
    Returns a dictionary where node # is key. Values are 2-tuples
    representing connected nodes. If node has only one connection,
    the second value will be None.
    """

    #NOTE: For optimization in this problem, only one starting leg used.
    # Path count for either other starting leg will be the same.
    connecs = {0 : [1, None]}
    node = 1
    
    for r in range(0, size + 1):
        for c in range(0, size):
            if r == size and c == size - 1:
                break
            elif r == size:
                connecs[node] = [node + 1, None]
            elif c == size - 1:
                connecs[node] = [node + size, None]
            else:
                connecs[node] = [node + 1, node + size]
            
            node += 1

    return connecs

#-----------------------------------------------------------------------------
def DFTraverse(start, stop, count, connecs, counts={}):
    """
    Depth first traversal of grid graph.
    Returns count of possible paths from start to stop nodes.
    """
    count_start = count

    if start == None:
        pass
    elif start == stop:
        count += 1
    elif start in counts:
        count += counts[start]
    else:
        count = DFTraverse(connecs[start][0], stop, count, connecs, counts)
        count = DFTraverse(connecs[start][1], stop, count, connecs, counts)

        if start % 5 == 0 and start > 0:
            counts[start] = count - count_start

    return count

#-----------------------------------------------------------------------------
def Prob15():
    size = 20
    connecs = BuildGraph(size)

    #Double result to account for other starting leg
    return 2*DFTraverse(0, len(connecs), 0, connecs)


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob15())
    finally:
        print 'Time:   %.5fs' % timer.Interval


