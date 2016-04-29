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
	add1, add2 = 0, 0
	if s1 < 30: 
		add1 = 30 - s1
	if s2 > 30: 
		add2 = 30 - s2

	if s1 >= 30 and s2 >= 30:
		return "No space in either section"
	elif s1 <= 30 and s2 <= 30:
		return "No overflow"
	elif s1 > 30 and s2 < 30: 
		add2 = 30 - s2
		return add2, "spot left in Section 2"
	elif s1 < 30 and s2 > 30:
		add1 = 30 - s1
		return add1, "spot left is Section 1"


