"""
PROJECT EULER
Problem 11

What is the greatest product of four adjacent numbers
in any direction (up, down, left, right, or diagonally)
in the 2020 grid?


Author: Adam Beagle
"""

from os import path
from Timer import Timer

################################################################################
def CheckHighProd(highProd, highSlice, prod, _slice):
    """
    Returns the product and slice of whichever of
    the passed products was larger.
    """
    if prod > highProd:
        return prod, _slice
    else:
        return highProd, highSlice

#-----------------------------------------------------------------------------
def GetMatrixDiagonals(grid, minSize):
    """
    Returns list of all diagonals from a square matrix
    that contain at least minSize elements.
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

#-----------------------------------------------------------------------------
def HighProdOfLine(line, slice_sz):
    """Returns highest product of slice_sz consecutive numbers in line"""
    highProd = 0
    highSlice = []

    for i in range(0, len(line) - slice_sz):
        prod = 1
        _slice = line[i: i + slice_sz]

        for n in _slice:
            prod *= n

        highProd, highSlice = CheckHighProd(highProd, highSlice, prod, _slice)
    
    return highProd, highSlice

#-------------------------------------------------------------------------------
def Prob11(filename):
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
        prod, _slice = HighProdOfLine(line[:], mult)
        highProd, highSlice = CheckHighProd(highProd, highSlice, prod, _slice)

    #Vertical
    for i in range(side):
        v_line = []
        for line in grid:
            v_line.append(line[i])
            
        prod, _slice = HighProdOfLine(v_line, mult)
        highProd, highSlice = CheckHighProd(highProd, highSlice, prod, _slice)
        

    #Diagonal
    for diagLine in GetMatrixDiagonals(grid, mult):
        prod, _slice = HighProdOfLine(diagLine, mult)
        highProd, highSlice = CheckHighProd(highProd, highSlice, prod, _slice)

    return highProd, highSlice


################################################################################
if __name__ == '__main__':
    
    try:
        with Timer() as timer:
            filename = path.join('..', 'res', 'Prob11_grid.txt')
            product, factors = Prob11(filename)
            operation = str(product) + ' = ' + " x ".join([str(n) for n in factors])
            print 'Answer:', operation
    finally:
        print 'Time:   %.5fs' % timer.Interval
