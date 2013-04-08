"""
PROJECT EULER
Problem 17

How many letters would be needed to write all the
numbers in words from 1 to 1000?


Author: Adam Beagle
"""

from Timer import Timer

################################################################################

#FIXME: Function too long, ugly.
#  Also needs generalizing for cases beyond 1000 or negative i's
def NumToWords(i, ones, teens, tens):
    """
    Returns i as it would be spoken, as a string.
    Currently only implemented for cases where 1 <= i <= 1000.
    ones, teens, and tens are dictionaries of words in each category,
    where key is integer and value is word.
    Ex: teens = {10: 'ten', 11: 'eleven', ... , 19: 'nineteen'}
    Ones should have keys, 1, 2, ... , 9; tens 10, 20, 30, ... , 90
    """
    words = ''
    teen = False
    
    if i < 10:
        words = ones[i]

    elif i < 20:
        words = teens[i]

    elif i < 100:
        words += tens[i / 10]
        words += ' ' if i % 10 > 0 else ''
        words += ones[i % 10] 

    elif i < 1000:
        words += ones[i / 100] + ' hundred'     #HUNDREDS

        ten = (i % 100) / 10                    #TENS
        if ten > 1:
            words += ' and ' + tens[ten]
        elif ten == 1:
            words += ' and ' + teens[i % 100]
            teen = True
        else:
            words += ' and'

        if not teen:                            #ONES
            one = (i % 100) % 10
            if one > 0:
                words += ' ' + ones[one]
            elif ten == 0:
                words = words[:-3]
                
    elif i == 1000:
        words = 'one thousand'
    
            
    return words

#-----------------------------------------------------------------------------
def Prob17():
    ones = {0:'', 1:'one', 2:'two', 3:'three', 4:'four',
        5:'five', 6:'six', 7:'seven', 8: 'eight',
        9:'nine'}

    teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',
             14:'fourteen', 15:'fifteen', 16:'sixteen',
             17:'seventeen', 18:'eighteen', 19:'nineteen'}

    tens = {1:'ten', 2:'twenty', 3:'thirty', 4:'forty',
            5:'fifty', 6:'sixty', 7:'seventy',
            8:'eighty', 9:'ninety'}

    letters = 0

    for i in range(1, 1001):
        numWords = NumToWords(i, ones, teens, tens)
        letters += len(numWords.replace(' ', ''))

    return letters
    
    
################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            print 'Answer: ' + str(Prob17())
    finally:
        print 'Time: %.5fs' % timer.Interval
