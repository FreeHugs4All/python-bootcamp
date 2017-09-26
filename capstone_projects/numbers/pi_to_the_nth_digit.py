# Pi to the Nth Digit

# Input: User enter an integer value n
# Output: Prints out the digits of pi up to and including the n-th digit
# Note: we are not calculating the value of pi. We get this from math.pi

import math

############################################################################
# Function: validate_input
# Parameters: none
# Internal vars: n: the n-th digit that a user wishes to print up to 
# Purpose: continually asks user to input a positive integer value for n
# Returns: n
############################################################################
def validate_input():
	while True:
		try:
			n = int(input("Up to what digit would you like to print out pi? "))
			if( n <= 0):
				print("Please enter a positive number. ")
			else:
				return n
		except(ValueError): # catch error if n is not an integer
			print("Please enter a valid integer input. ")

############################################################################
# Here, we'll use a generator function as we don't actually need to store 
# or manipulate the digits of pi. We are only interested in printing out 
# each digit up to and including  n
############################################################################

############################################################################
# Generator Function: get_pi()
# Parameters: n: number of digits of pi user wishes to display
# Purpose & Result: returns a generator function object in which a digit 
#                   of pi can be yielded
############################################################################

def get_pi(n):
	for i in range(n+1):
		yield str(math.pi)[i]

############################################################################
# get input then get generator function object
pi_digits = get_pi(validate_input())

# print out each digit in pi_digits (run the generator function to yield each digit)
for i in pi_digits:
	print(i, end="")  # end is used to ensure it's printed on one line, not separate ones

