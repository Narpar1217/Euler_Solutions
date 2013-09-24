"""
PROJECT EULER
Problem 11

Author: Adam Beagle

PROBLEM DESCRIPTION:
  What is the greatest product of four adjacent numbers in any direction
  (up, down, left, right, or diagonally) in the 20x20 grid?

"""

from os import path

from timer import Timer

###############################################################################
def check_high_prod(highProd, highSlice, prod, _slice):
    """
    Return the product and slice of whichever of the passed products
    was larger.
    
    """
    if prod > highProd:
        return prod, _slice
    else:
        return highProd, highSlice

def get_matrix_diagonals(grid, minSize):
    """
    Return list of all diagonals from a square matrix that contain at least
    minSize elements.
    
    """
    side = len(grid)
    diags = []
    
    for startRow in range(minSize - 1, side):
        newDiags = [[], [], [], []]
        
        for dec, inc in zip(range(startRow, -1, -1), range(startRow + 1)):
            newDiags[0].append(grid[inc][dec])
            newDiags[1].append(grid[-1 - inc][dec])

            if startRow < side - 1:
                newDiags[2].append(grid[-1 - dec][-1 - inc])
                newDiags[3].append(grid[inc][-dec - 1])

        diags += newDiags

    return diags[:-2]

def get_high_prod_of_line(line, slice_sz):
    """Return highest product of slice_sz consecutive numbers in line."""
    highProd = 0
    highSlice = []

    for i in range(0, len(line) - slice_sz):
        prod = 1
        _slice = line[i: i + slice_sz]

        for n in _slice:
            prod *= n

        highProd, highSlice = check_high_prod(highProd, highSlice,
                                              prod, _slice)
    
    return highProd, highSlice

def prob11(filename):
    grid = []
    
    with open(filename, 'r') as f:
        for line in f:
            grid.append([int(n) for n in line.split(' ')])

    mult = 4            #This many adjacent numbers will be multiplied
    highProd = 1        #Highest product yet found
    highSlice = []      #Factors in highest highProd
    side = len(grid)

    #Horizontal
    for line in grid:
        prod, _slice = get_high_prod_of_line(line[:], mult)
        highProd, highSlice = check_high_prod(highProd, highSlice,
                                              prod, _slice)

    #Vertical
    for i in range(side):
        v_line = []
        for line in grid:
            v_line.append(line[i])
            
        prod, _slice = get_high_prod_of_line(v_line, mult)
        highProd, highSlice = check_high_prod(highProd, highSlice,
                                              prod, _slice)
        
    #Diagonal
    for diagLine in get_matrix_diagonals(grid, mult):
        prod, _slice = get_high_prod_of_line(diagLine, mult)
        highProd, highSlice = check_high_prod(highProd, highSlice,
                                              prod, _slice)

    return highProd, highSlice

###############################################################################
if __name__ == '__main__':
    
    try:
        with Timer() as timer:
            filename = path.join('..', 'res', 'Prob11_grid.txt')
            product, factors = prob11(filename)
            operation = (str(product) + ' = ' +
                         " x ".join([str(n) for n in factors]))
            print 'Answer:', operation
    finally:
        print 'Time:   %.5fs' % timer.interval
