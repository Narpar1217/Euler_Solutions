/*
PROJECT EULER
Problem 14

Author: Adam Beagle

PROBLEM DESCRIPTION:
  The following iterative sequence is defined for the set of positive 
  integers:
  n = n / 2  (n is even)
  n = 3n + 1 (n is odd)

  Using the rule above and starting with 13, we generate the following 
  sequence:
  13  40  20  10  5  16  8  4  2  1

  It can be seen that this sequence (starting at 13 and finishing at 1) 
  contains 10 terms. Although it has not been proven yet (Collatz Problem),
  it is thought that all starting numbers finish at 1.

  Which starting number, under one million, produces the longest chain?
*/

#include <stdio.h>

#define START 	3			//First n to test (must be odd)
#define STOP 	1000000		//Exclusive upper limit to n
#define STEP	2			//Step size in n loop

unsigned next_odd_collatz(unsigned n, int *count);

int main()
{
	unsigned start, n;
	int chainLen, longestChain, longestChainI;
	
	longestChain = 0;
	longestChainI = 0;
	
	for (start = START; start < STOP; start += STEP) {
		n = start;
		chainLen = 0;
		
		while (n > 1) 
			n = next_odd_collatz(n, &chainLen);
		
		if (chainLen > longestChain) {
			longestChain = chainLen;
			longestChainI = start;
		}
	}
	
	printf("\nPROBLEM 14\n----------\nAnswer: %d\nLength: %d\n", 
		longestChainI, longestChain);
	
	return 0;
}

/*
For positive off integer n, returns next off value
in Collatz sequence. Adds how many steps were taken
to reach the next value to count.
Undefined behavior for even values of n.
*/
unsigned next_odd_collatz(unsigned n, int *count)
{
	//Equivalent to n = 3*n + 1
	n += ((n << 1) | 1);
	*count += 1;

	//Divide by 2 until n odd; 
	//Add to count for each division.
	while (n % 2 == 0) {
		*count += 1;
		n /= 2;
	}
		
	return n;
}
