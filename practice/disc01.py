"""Alfonso will only wear a jacket outside if 
it is below 60 degrees or it is raining. Fill
in the function wears jacket which takes in 
the current temperature and a boolean
value telling if it is raining and returns 
True if Alfonso will wear a jacket and False
otherwise.
This should only take one line of code!
"""


def wears_jacket(temp, raining):
	"""
	>>> rain = False
	>>> wears_jacket(90, rain)
	False
	>>> wears_jacket(40, rain)
	True
	>>> wears_jacket(100, True)
	True
	"""
	return temp < 60 or raining

"""To handle discussion section overflow, TA’s may direct students 
to a more empty section that is happening at the same time. Write 
the function handle overflow, which takes in the number of students
at two sections and prints out what to do if either section exceeds
30 students. See the doctests below for the behavior.
"""

def handle_overflow(s1, s2):
	"""
	>>> handle_overflow(27, 15)
	No overflow.
	>>> handle_overflow(35, 29)
	1 spot left in Section 2.
	>>> handle_overflow(20, 32)
	10 spots left in Section 1.
	>>> handle_overflow(35, 30)
	No space left in either section.
	"""

	if s1 <= 30 and s2 <= 30:
		print("No overflow.")
	elif s1 > 30 and s2 < 30: 
		print (str(30-s2) + " spots left in Section 2.")
	elif s1 < 30 and s2 > 30:
		print(str(30-s1) + " spots left in Section 1.")
	else: 
		print("No space left in either section.")

"""Fill in the is prime function, which returns True 
if n is a prime number and False otherwise.
"""
def is_prime(n):
	k = n - 1
	while k > 1: 
		if n % k == 0:
			return False
		else: 
			k -= 1
	return True

#my solution above seems to work, answer from prof is below: 
def is_prime2(n):
	if n == 1:
		return False
	k = 2
	while k < n:
		if n % k == 0:
			return False
		k += 1
	return True

"""Implement fizzbuzz(n), which prints numbers from 1 to n 
(inclusive). However, for numbers divisible by 3, print “fizz”. For numbers divisible by 5, print “buzz”. For
numbers divisible by both 3 and 5, print “fizzbuzz”.
"""

def fizzbuzz(n):
	"""
	>>> result = fizzbuzz(16)
	1
	2
	fizz
	4
	buzz
	fizz
	7
	8
	fizz
	buzz
	11
	fizz
	13
	14
	fizzbuzz
	16
	>>> result is None
	True
	"""
	count = 1
	while count < n + 1: 
		if count % 15 == 0:
			print('Fizzbuzz')
		elif count % 3 == 0:
			print('Fizz')
		elif count % 5 == 0:
			print('Buzz')
		else: 
			print(count)
		count += 1

"""Fill in the choose function, which returns 
the number of ways to choose k items from
n items. Mathematically, choose(n, k) is defined as:
n × (n − 1) × (n − 2) × · · · × (n − k + 1) /
k × (k − 1) × (k − 2) × · · · × 2 × 1
"""



def choose(n, k):
	"""Returns the number of ways to choose K items from
	N items.
	>>> choose(5, 2)
	10
	>>> choose(20, 6)
	38760
	"""
	total = 1
	i = 0
	while i < k:
		total = total * (n - i) // (i + 1)
		i += 1
	return total 

