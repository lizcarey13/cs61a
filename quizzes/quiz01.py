"""Quiz 1

1. When do we make a new frame in an environment diagram?

We make a new frame whenever we call a user-defined function. 
This means we don't create frames for builtin function calls like abs(x) and 3 + 4. 
We also don't create frames for imported functions!

2. Implement the function nearest_two, which takes a positive 
number x as input, and returns the power of two 
(..., 1/8, 1/4, 1/2, 1, 2, 4, 8, ...) that is nearest to x. 
If there is a tie, return the larger value."""

def nearest_two(x):
    """Returns the power of two that is nearest to x.
    >>> nearest_two(8)
    8.0
    >>> nearest_two(11.5)  # closer to 8 than to 16
    8.0
    >>> nearest_two(0.75)  # tie between 0.5 and 1
    1.0
    """
    power_of_two = 1.0

    if x < 1:
    	factor = 0.5
    else: 
    	factor = 2.0
    while abs(power_of_two * factor - x) < abs(power_of_two - x):
    	power_of_two *= factor

    if abs(power_of_two * 2 - x) == abs(power_of_two - x):
    	power_of_two *= 2

    return power_of_two

"""Question3. 
Fill in the blanks so that cs and 61a alternate printing for a total
 of n times.
"""
def cs61a(n):
    """
    >>> cs61a(3)
    cs
    61a
    cs
    >>> cs61a(2)
    cs
    61a
    """
    i = 0
    while i < n:
        if i % 2 == 0:
            print("cs")
        else:
            print("61a")
        i += 1