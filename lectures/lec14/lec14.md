###Classes
----

> a class serves as a template for its instances

```python
>>> a  = Account('Jim')
>>> a.holder
'Jim'
>>> a.balance
0

# all accounts should have withdraw and deposit behaviors that all work the same way
>>> a.deposit(15)
15
>>> a.withdraw(10)
5
>>> a.balance
5
```

####The Class Statement
---

```python
class <name>:
	<suite>
```

> a class statement creates a new class and binds that class to <name> in the first frame of the current environment 
> assigment and def statements in <suite> create attributes of the class (not names in frames)

###Object Construction
---
When a class is called:

1. a new instance of that class is created. 

2. the \__init__ method of the class is called with the new object as its first argument (named self), along with anay additional arguments provided in the call expression
