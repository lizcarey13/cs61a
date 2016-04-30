def foo(n):
	while n > 0:
		if n*n == 8 * n - 16:
			return True
		n -= 1
		print(n)
	return False
