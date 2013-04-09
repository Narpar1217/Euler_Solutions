"""
PROJECT EULER
Problem 89

The 11K text file, Prob89_roman.txt,
contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals;
That is, they are arranged in descending units
and obey the subtractive pair rule.

Find the number of characters saved by writing
each of these in their minimal form.

RULES:
-----------
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Only I, X, and C can be used as the leading numeral in part of a
subtractive pair.

I can only be placed before V and X.
X can only be placed before L and C.
C can only be placed before D and M.
-----------

Author: Adam Beagle
"""

from EulerUtility import GetDigits
from os import path
from Timer import Timer

########################################################################
def IntToRoman(n):
    """Returns integer n as minimum-length roman numeral string"""
    rom = ''
    
    charMap = {1     : 'I',
               5     : 'V',
               10    : 'X',
               50    : 'L',
               100   : 'C',
               500   : 'D',
               1000  : 'M'
               }

    subtractMap = {4   : 'IV',
                   9   : 'IX',
                   40  : 'XL',
                   90  : 'XC',
                   400 : 'CD',
                   900 : 'CM'
                   }

    for deg, digit in enumerate(GetDigits(n)):
        #Case: Subtractive pair
        if deg < 3 and (digit == 4 or digit == 9):
            rom += subtractMap[digit *(10 ** deg)]
            
        #Case: Multiple differing characters needed (ex: 6 -> VI)
        elif digit >= 5:
            rom += charMap[5 * (10 ** deg)]
            rom += (digit % 5) * charMap[10 ** deg]
            
        #Case: Multiple of one character can represent digit (ex: 3 -> III)
        else:
            rom += digit * charMap[10 ** deg]

    return rom

#-----------------------------------------------------------------------------
def Prob89(filename):
    saved = 0
    
    with open(filename, 'r') as f:
        for line in f:
            romLong = line.strip()
            romMin = IntToRoman(RomanToInt(romLong))
            saved += len(romLong) - len(romMin)

    return saved

#-----------------------------------------------------------------------------
def RomanToInt(rom):
    """
    Returns roman numeral rom as integer.
    Assumes rom is a valid roman numeral, though
    it need not be minimal-length (i.e. the following are
    all valid input values for the number 12:
    XII, VVII, VIIIIIII, IIIIIIIIIIII).
    """
    num = 0     #Holds int version of rom
    sub = False #Previous iteration found subtraction (ex: IV)
    
    charMap = {'I' : 1,
               'V' : 5,
               'X' : 10,
               'L' : 50,
               'C' : 100,
               'D' : 500,
               'M' : 1000
               }

    #Keys are subtracted from values, if they precede them in rom.
    subtractFrom = {'I' : ['V', 'X'],
                    'X' : ['L', 'C'],
                    'C' : ['D', 'M']
                    }

    #Iterate through rom to determine num
    for i, c in enumerate(rom):
        if i == len(rom) - 1 and not sub:
                num += charMap[c]
        elif not sub:
            if c in subtractFrom and rom[i + 1] in subtractFrom[c]:
                num += charMap[ rom[i + 1] ] - charMap[c]
                sub = True
            else:
                num += charMap[c]

        #Character handled on previous iteration during subtraction
        else:
            sub = False

    return num

################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            filename = path.join('..', 'res', 'Prob89_roman.txt')
            print 'Answer: ' + str(Prob89(filename))
    finally:
        print 'Time:   %.5fs' % timer.Interval













