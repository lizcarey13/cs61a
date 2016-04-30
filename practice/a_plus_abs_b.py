def a_plus_abs_b(a, b):
	if b < 0:
		f = a - b
	else:
		f = a + b
	return f

from operator import add, sub

def a_plus_abs_b_short(a,b):
	if b < 0:
		f = sub
	else: 
		f = add
	return f(a,b)