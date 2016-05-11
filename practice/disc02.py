"""Create a recursive countdown function that takes 
in an integer n and prints out a
countdown from n to 1.

"""

def countdown(n):
	if n == 1:
		return 1
	else:
		print (n)
		return countdown(n-1)