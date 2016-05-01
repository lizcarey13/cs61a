def inverse_cascade(n):
	grow(n)
	print(n)
	shrink()

def f_then_g(f, g, n):
	if n: 
		f(n)
		g(n)

grow = lambda n: f_then_g()
shrink = lambda n: f_then_g