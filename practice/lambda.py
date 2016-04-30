def summation(term, n):
	"""
	>>>summation(lambda x: x**2, 3)
	14
	"""
	i, total = 1, 0
	while i <= n:
		total += term(i)
		i += 1
	return total
	