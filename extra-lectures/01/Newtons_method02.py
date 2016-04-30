def find_zero(f, df):
	def near_zero(x):
		return approx_eq(f(x),0)
	return improve(newton_update(f, df), near_zero)

derive = lambda f: lambda x: slope(f, x)

def approx_zero(f):
	df = lambda x: slope(f, x)
	return find_zero(f, df)

def approx_zero02(f):
	return find_zero(f, derive(f))

def newton_update(f, df):
	def update(x):
		return x - f(x)/df(x)
	return update

def square_root(a):
	def f(x):
		return x * x - a
	def df(x):
		return 2 * x
	return find_zero(f, df)

def square_root02(a):
	return find_zero(lambda x: x * x - a,
					lambda x: 2 * x)

def improve(update, close, guess=1):
	k = 1
	while not close(guess) and k < 1000:
		guess = update(guess)
		k = k + 1
	return guess

def approx_eq(x, y, tolerance= 1e-15):
	return abs(x-y) < tolerance

def cube_root(a):
	return find_zero(
		lambda x: x*x*x - a,
		lambda x: 3*x*x)

cube_root02 = lambda a: find_zero(
		lambda x: x*x*x - a,
		lambda x: 3*x*x)

def nth_root(a, n):
	return find_zero(
		lambda x: pow(x, n) - a,
		lambda x: n * pow(x, n-1))

def nth_root02(a, n):
	return approx_zero(
		lambda x: pow(x, n) - a)

def slope(f, x, a=1e-10):
	return (f(x+a) - f(x)) / a
