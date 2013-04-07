"""
PROJECT EULER
Problem 7

By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?


Author: Adam Beagle
"""
from math import sqrt, log

################################################################################
def SieveOfEratosthenes(limit):
    """Returns list of primes <= limit"""
    sieve = [True] * (limit + 1)
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

    return [index for index,value in enumerate(sieve) if index >= 2 and value]
            

################################################################################

desiredPrime = 10001
upperLimit = 10**4  #arbitary starting point
limitMult = 5

#Number of primes below a given n is approximately n / ln n
#The above fact is used to approximate a suitable upper limit for the sieve.
while (upperLimit / log(upperLimit)) <= desiredPrime:
    upperLimit *= limitMult

primes = SieveOfEratosthenes(upperLimit)

#If approximated upper limit was insufficient, ask user if reattempt desired.
while len(primes) < desiredPrime:
    print 'WARNING: upperLimit too low. %d primes found below %d.' % (len(primes), upperLimit)
    print 'Reattempting with upperLimit * %d\n' % limitMult
    upperLimit *= limitMult
    primes = SieveOfEratosthenes(upperLimit)
    
print 'Answer:', primes[desiredPrime - 1]
