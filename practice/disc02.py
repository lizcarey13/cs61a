"""Create a recursive countdown function that takes 
in an integer n and prints out a
countdown from n to 1.

"""

def countdown(n):
	if n <= 0:
		return
	print(n)
	countdown(n-1)

"""Have countdown count up
"""

def countup(n):
	if n <= 0:
		return
	countup(n-1)
	print(n)

"""Write a recursive function that sums the digits of a number n. 
Assume n is positive. You might find the operators // and % useful.

>>> sum_digits(7)
7
>>> sum_digits(30)
3
>>> sum_digits(228)
12

"""

def sum_digits(n):
	if n % 10 == n:
		return n 
	else: 
		return (n % 10) + sum_digits(n // 10)
		