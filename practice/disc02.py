"""Create a recursive countdown function that takes 
in an integer n and prints out a
countdown from n to 1.

"""

def countdown(n):
	if n <= 0:
		return
	print(n)
	countdown(n-1)