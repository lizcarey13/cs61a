def summation(term, n):
	i, total = 1, 0
	while i <= n: 
		total += term(i)
		i += 1
	return total


def square(x):
	return x * x

def sum_squares(n):
	i, total = 1, 0
	while i <= n:
		total += square(i)
		i += 1
	return total

"""Sum the first n powers of two
>>>summation()
