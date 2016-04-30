"""Fill in the is prime function, which returns True 
if n is a prime number and False otherwise.
"""
def is_prime(n):
	k = n
	while k > 0: 
		if n % k == 0:
			return True
		k -= 1