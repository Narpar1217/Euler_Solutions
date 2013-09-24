/*
PROJECT EULER
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.


Author: Adam Beagle
*/

#include <stdio.h>
#include <stdbool.h>

int reverse_int(int n);


int main()
{
	int n1, n2, prod, largest;
	
	largest = 0;
	
	for (n1 = 999; n1 > 99; --n1) {
		for (n2 = n1; n2 > 99; --n2) {
			prod = n1 * n2;
			
			//If prod < largest, can't be answer
			if (prod < largest)
				break;
				
			//If palindromic, must be largest
			if (prod == reverse_int(prod))
				largest = prod;
		}
	}
	
	printf("Answer: %d\n", largest);
	
	return 0;
}

/* 
Returns reversed version of int n. 
Ex: input 1234, output 4321
Works for positive and negative n's.
*/
int reverse_int(int n)
{
	int reversed = 0;
	bool negFlag = n < 0;
	
	if (negFlag) n *= -1;
	
	while (n > 9) {
		reversed += n % 10;
		reversed *= 10;
		n /= 10;
	}
	reversed += n;
	
	return (negFlag) ? -1*reversed : reversed;
}
