def make_adder(n):
	def adder(k):
		return k + n
	return adder

def make_adder_better(n):
	return lambda k: n + k

make_adder_short = lambda n: lambda k: n + k

#Lambdas are expressions! 
#You can use them anywhere you can use any other expression.
#A lambda’s body can only be a single expression. This is the return expression.
#Use sparingly! Better to have clear names.