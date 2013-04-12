"""
EulerUtility.py
Author: Adam Beagle

This file contains any functions that are used by
multiple Project Euler solutions.
"""

#-----------------------------------------------------------------------------
def FibGen(limit = -1):
    """
    Generator. If limit supplied, returns fibonacci numbers <= limit.
    If limit omitted, will run continuously until stopped elsewhere.
    """
    a = b = 1
    
    if limit >= 0:
        while b <= limit:
            yield b
            a, b = b, a + b
    else:
        while True:
            yield b
            a, b = b, a + b

#-----------------------------------------------------------------------------
def GetAlphaSum(word):
    """
    Returns the alphabetical sum of all characters in a word.
    Each character's value is its index in the alphabet
    (A = 1, B = 2, ... , Z = 26)
    """
    word = word.upper()
    asciiOffset = ord('A') - 1

    return sum(ord(c) - asciiOffset for c in word)
            
#-----------------------------------------------------------------------------
def GetDigits(n):
    """Generator. Yields each digit of an integer n, right to left."""
    if n == 0:
        yield 0

    while n > 0:
        yield n % 10
        n /= 10

            
#-----------------------------------------------------------------------------
def GetPrimeFactorization(n, primes):
    """
    Returns a list representing the prime factorization of n,
    or an empty list if factorization fails.
    Ex: Input 360, output [2, 2, 2, 3, 3, 5]; 2**3 x 3**2 x 5 = 360
    Factorization will fail if any prime factor of n is larger than the largest value in primes.
    Primes must be in increasing order.
    """
    factors = []

    if n in primes:
        return [n]
    
    for p in primes:
        if p > (n / 2):
          break
        
        if n % p == 0:
            factors.append(p)
            factors += GetPrimeFactorization(n / p, primes)
            break

    prod = 1
    for f in factors:
        prod *= f

    return factors if prod == n else []


#-----------------------------------------------------------------------------
def SieveOfEratosthenes(limit, generator=False, sieveForm=False):
    """
    Default return value is list of primes <= limit, in increasing order.
    If sieveForm is set, returns list wherein index n is True or False based on primality of n.
    (sieveForm is more efficient when direct indexing is needed, and not all primes need to be iterated through).
    If generator is set, primes returned as a generator.
    NOTE: If sieveForm is set, generator is ignored.
    """
    from math import sqrt
    from sys import stderr

    if sieveForm and generator:
        print >>stderr, 'WARNING: sieveForm and generator set to True on call to SieveOfEratosthenes. Generator will be ignored.'
    
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] =  False
    i = 2
    
    while i < sqrt(limit):
        if sieve[i]:
            m = 0
            j = i**2
            while j <= limit:
                sieve[j] = False
                m += 1
                j = (i**2) + (m*i)
                
        i += 1
    
    if sieveForm:
        return sieve
    
    elif not sieveForm and generator:
        return (index for index,value in enumerate(sieve) if value)
    
    elif not sieveForm and not generator:
        return [index for index,value in enumerate(sieve) if value]


#-----------------------------------------------------------------------------
def UniqueCounts(sequence):
    """
    Returns list of 2-tuples of elements, and how many times they appear in lst.
    Example: Input [3, 3, 2, 2, 2, 4] Output [(2, 3), (3, 2), (4, 1)]
    """
    counts = []
    
    unique = list(set(sequence))

    for el in unique:
        counts.append((el, sequence.count(el)))

    return sorted(counts)
