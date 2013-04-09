"""
PROJECT EULER
Problem 59

Author: Adam Beagle


Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption
key on the cipher text, restores the plain text; for example,
65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain
text message, and the key is made up of random bytes.
The user would keep the encrypted message and the encryption key in
different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the
modified method is to use a password as a key. If the password is
shorter than the message, which is likely, the key is repeated cyclically
throughout the message. The balance for this method is using a
sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of
three lower case characters. Using cipher1.txt (right click and
'Save Link/Target As...'), a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.
"""

from os import path
from sys import exit, stderr
from Timer import Timer

################################################################################
def Decrypt(key, data):
    """
    Generator; yields next character of data XOR'd with key.
    If key < len(data) key cycles starting at key[0].
    """
    keyI = 0
    keyCycle = len(key) - 1

    for c in data:
        yield chr(c ^ key[keyI])

        if keyI == keyCycle:
            keyI = 0
        else:
            keyI += 1

#-----------------------------------------------------------------------------
#TODO: A generalized case for keys of any length would be interesting.
def GetMostLikelyKey(testData):
    """
    Returns key most likely to accurately decrypt testData,
    or None if no such key is found.
    """
    highestMatch = 0
    commonWords = ['the', 'be', 'to',   #Most commonn words in English.
                   'of', 'and', 'a',    #From http://en.wikipedia.org/wiki/Most_common_words_in_English
                   'in', 'that','have'] 
    start = ord('a')                                                          
    stop = ord('z') + 1
    key = None

    #Key is three lower case characters (from problem description)
    for k1 in xrange(start, stop):
        for k2 in xrange(start, stop):
            for k3 in xrange(start, stop):
                testKey = [k1, k2, k3]
                matches = TestKey(testKey, testData, commonWords, highestMatch)

                if matches:
                    highestMatch = matches
                    key = testKey
    return key

#-----------------------------------------------------------------------------
#Assumes the following:
#  * Decrypted cipher contains English, and utilizes many common English words
#  * Length of cipher is unknown
#  * Decryption key is three lowercase characters.
def Prob59(filename):
    
    #Create encrypted from cipher file
    with open(filename, 'r') as f:
        try:
            encrypted = [int(x.strip()) for x in f.read().split(',')]
        except ValueError:
            exit('\nFile %s improperly formatted;\nExpected to contain integers separated by commas.\nEnding execution...' % filename)
            

    #Get reasonably-sized slice from middle of encrypted text to test keys against
    #(50 characters, or half the length of encrypted if len(encrypted) < 100)
    halfLen = len(encrypted) / 2
    sliceSize = min(50, halfLen)
    testSlice = encrypted[halfLen:halfLen + sliceSize]

    #Find key
    key = GetMostLikelyKey(testSlice)

    #Note: None returned by default if no key found
    if key:
        text = ''.join(Decrypt(key, encrypted))
        return sum([ord(x) for x in text]), ''.join((chr(c) for c in key))

    
#-----------------------------------------------------------------------------
def TestKey(key, testData, compareTo, minMatch, maxWordLen=10):
    """
    Returns number of words in testData that are in compareTo, after testData
    has been decrypted with key.
    If number of word matches does not exceed minMatch, 0 will be returned.
    If a space is not in the first maxWordLen characters, 0 will be returned.
    """
    decrypted = ''.join(Decrypt(key, testData))
    matches = 0

    if ' ' in decrypted[:maxWordLen]:
        for i, word in enumerate(decrypted.split(' ')):
            if word in compareTo:
                matches += 1

            if matches > minMatch:
                return matches

    return 0


################################################################################
if __name__ == '__main__':
    try:
        with Timer() as timer:
            filename = path.join('..', 'res', 'Prob59_cipher.txt')
            print 'Answer: %d (Key: %s)' % Prob59(filename)
    finally:
        print 'Time:   %.5fs' % timer.Interval
