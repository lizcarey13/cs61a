Recursion
======
####What are three things you find in every recursive function?
1. One or more Base Cases
2. Way(s) to make the problem into a smaller problem of the same type (so that it can be solved recursively).
3. One or more Recursive Cases that solve the smaller problem and then uses the solution the smaller problem to solve the original (large) problem

**Factorial(n)**
```python
def factorial(n):           # Domain is integers, Range is integers
  if n <= 1:                # base case
    return 1
  else:                     # recursive case
    return n*factorial(n-1) # make a smaller problem
```
