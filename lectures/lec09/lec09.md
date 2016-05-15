###Representing Pairs Using Lists
------

```python
>>>pair = [1,2]
>>>pair
[1,2]

>>>x, y = pair # unpacking a list
>>>x
1
>>>y
2

>>>pair[0]
1

>>>from operator import getitem
>>>getitem(pair, 0)
1

>>> [2+3, 4] # expressions are evaluated
[5,4]
```


###Abstraction Barriers
________

Parts of the program that... | Treat rationals as... | Using ...
---| --- | ---
Use rational numbers to perform computation | whole data values | add_rational, mul_rational, rationals_are_equal, print_rational 
Create rationals or implement rational opertaions | numerators or denominators | rational, numer, denom
Implement selectors and constructor for rationals | two-element lists | List Literals and element selection


**Violation abstraction barriers:** 
- Will still run, but it's harder to change program. 

```python
add_rational([1,2], [1,4])
```

###Data Representations:
------
####What is Data?
- Constructor and selecor functions work together to specify the right behavior
- If we contruct rational number x from numerator n and denominator d, then numer(x)/denom(x) must equal n/d
- Data abstraction uses selectors and constructions to define behavior 
- If behavior conditions are met, then the representation is valid

>**You can recognize an abstract data representation by its behavior**
