from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return max(a*a+b*b, a*a+c*c, b*b+c*c)

def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, ...
    8
    """
    #n*n-1 is equal to (n-1) * (n+1), so n-1 always evenly divides n*n-1.
    return n-1


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition == True:
        return true_result
    else:
        return false_result

#write functions c, t, and f such that with_if_statement 
#returns the number 1, but with_if_function does not (it can do anything else):
#The function with_if_function uses a call expression, 
#which guarantees that all of its operand subexpressions will be evaluated 
#before if_function is applied to the resulting arguments. 
#Therefore, even if c returns False, the function t will be called. 
#By contrast, with_if_statement will never call t if c returns False.


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return False

def t():
    1/0

def f():
    return 1


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    count = 1
    while n != 1:
        print (n) 
        if (n % 2) == 0: 
            n = n//2
        else:
            n = n*3+1
        count += 1
    print(n)
    return count



"""Write a one-line program that prints itself, using only the following 
features of the Python language:

Number literals
Assignment statements
String literals that can be expressed using single or double quotes
The arithmetic operators +, -, *, and /
The built-in print function
The built-in eval function, which evaluates a string as a Python expression
The built-in repr function, which returns an expression that evaluates to its argument
You can concatenate two strings by adding them together with + and repeat a string by 
multipying it by an integer. Semicolons can be used to separate multiple statements on 
the same line."""

challenge_question_program ='a'; print('hello', "world" * 2 + ' How are you?'); print(eval('2+2')); x = "hello"; repr(x); print(repr(5))

