"""
PROJECT EULER
Problem 42

Author: Adam Beagle

PROBLEM DESCRIPTION:
  The nth term of the sequence of triangle numbers is given by
  Tn = (1/2)*n*(n+1);

  So the first ten triangle numbers are:
  1, 3, 6, 10, 15, 21, 28, 36, 45, 55

  By converting each letter in a word to a number corresponding to
  its alphabetical position and adding these values we form a word value.
  For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
  If the word value is a triangle number then we shall call the word a
  triangle word.

  Find the number of triangle words in ../res/Prob42_words.txt.
  
"""

from os import path

from eulerutility import get_alpha_sum
from timer import Timer

###############################################################################
def get_triangle_nums(limit):
    """
    Generator; yields tuple of triangle numbers < limit, and their n-values
    (i.e. their term number). Triangle numbers are of form Tn = (1/2)*n*(n+1).
    
    If limit is 0, will yield continuously until broken elsewhere.
    
    """
    n = 1
    num = 0

    if limit > 0:
        while num < limit:
            num = int(0.5 * n * (n + 1))
            yield num, n
            n += 1
            
    elif limit == 0:
        while True:
            yield int(0.5 * n * (n + 1)), n
            n += 1

def is_triangle_word(word, triangleNums):
    """
    Return True if word is a triangle word, False otherwise.

    'triangleNums' assumed to contain values large enough to potentially
    contain the alphabetical sum of word.
    
    """
    return get_alpha_sum(word) in triangleNums

def prob42(filename):
    triNumCount = 0
    maxWordLen = 20 #Triangle numbers will be generated to a point
                    #where alphabetical sum of word of length <= maxWordLen
                    #will be guaranteed to be contained.

    triangleNums = list(triNum for triNum, n in
                        get_triangle_nums(26*maxWordLen))
    
    with open(filename, 'r') as f:
        for line in f:
            for word in (w.strip('\"') for w in line.split(',')):
                triNumCount += int(is_triangle_word(word, triangleNums))

    return triNumCount

###############################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            filename = path.join('..', 'res', 'Prob42_words.txt')
            print 'Answer: ' + str(prob42(filename))
    finally:
        print 'Time:   %.5fs' % timer.interval
