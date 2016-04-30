# Newton's Method

A general strategy for solving an equation:
>Guess a solution<br>
	*while your guess isn’t good enough:* <br>
		update your guess

```
def iter_solve(guess, done, update):
	"""Return the result of repeatedly applying UPDATE,
	starting at GUESS, until DONE yields a true value
	when applied to the result. UPDATE takes a guess
	and returns an updated guess."""

	def solution(guess):
		if done(guess):
			return guess
	else:
		return solution(update(guess))
	return solution(guess)
```
Need to make sure that the function doesn’t loop forever, getting no closer to a solution.

```
def iter_solve(guess, done, update, iteration_limit=32):
	"""Return the result of repeatedly applying UPDATE,
	starting at GUESS, until DONE yields a true value
	when applied to the result. Causes error if more than
	ITERATION_LIMIT applications of UPDATE are necessary."""
	
	def solution(guess, iteration_limit):
		if done(guess):
			return guess
		elif iteration_limit <= 0:
			raise ValueError("failed to converge")
		else:
			return solution(update(guess), iteration_limit-1)
	return solution(guess, iteration_limit)
```
A little cleaner: 
```
def iter_solve(guess, done, update, iteration_limit=32):
	"""Return the result of repeatedly applying UPDATE,
	starting at GUESS, until DONE yields a true value
	when applied to the result. Causes error if more than
	ITERATION_LIMIT applications of UPDATE are necessary."""
	
	while not done(guess):
		if iteration_limit <= 0:
			raise ValueError("failed to converge")
		guess, iteration_limit = update(guess), iteration_limit-1
	return guess
```

#### Newton’s method (aka the Newton-Raphson method): 
* A general numerical technique for finding approximate solutions to f(x) = 0, given the function f, its derivative f′, and an initial guess, x0. It produces a result to some desired tolerance (that is, to some definition of “close enough”).

![Newton's Method gif](https://upload.wikimedia.org/wikipedia/commons/e/e0/NewtonIteration_Ani.gif)

Given a guess, x<sub>k</sub>, compute the next guess, x<sub>k</sub>+1 by <br>
x<sub>k</sub>+1 = x<sub>k</sub> − f(x<sub>k</sub>) / f′(x<sub>k</sub>) 

```
def newton_solve(func, deriv, start, tolerance):
	"""Return x such that |FUNC(x)| < TOLERANCE, given initial
	estimate START, assuming DERIV is the derivatative of FUNC."""
	
	def close_enough(x):
		return abs(func(x)) < tolerance
	def newton_update(x):
		return x - func(x) / deriv(x)
	
	return iter_solve(start, close_enough, newton_update)
```
