###The Sequence Abstraction
----

- There isn't just one sequence class or data abstraction 
- the sequence abstraction is a collection of behaviors:
	- **length:** A sequence has a finite length
	- **Element selection:** a sequence has an element element corresponding to any non-negative integer index less than its length, starting at 0. 



```python
>>>odds = [41, 43, 47, 49]
>>>odds[0] + odds[1]
84
>>>odds[odds[3] - odds[2]]
47
>>>odds[3]-odds[2]
2
>>>odds[len(odds) - 1]
49
>>>odds[-1]
49
```

###Lists are Sequences
----
- Add lists together
```python
>>> digits = [1, 8, 2, 8]
>>> [2+7] + digits * 2
[2, 7, 1, 8, 2, 8, 1, 8, 2, 8]
```

- List within a list
```python
>>> pairs = [[10, 20], [30, 40]]
>>> pairs[1]
[30, 40]
>>> pairs[1][0]
30
```

###For Statements
----

For statement execution procedure:

```python
for <name> in <expression>:
	<suite>
```

1. Evaluate the header \<expression>, which must yield an iterable value (a sequence)

2. For each element in that sequence, in order: 
	- Bind \<name> to that element in the current frame
	- Execute the \<suite>

Sequence unpacking in For statements
- Need fized length of sequences to work

```python
>>>pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
>>>same_count = 0
>>> for x, y in pairs:
		if x == y: 
			same_count += 1
>>> same_count
2
```

###Ranges
---
- a range is a sequence of consecutive integers*

..., -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, ...

-**length** = ending value - starting value

-**element selection** =  starting value + index

- call list function to see what's in a range

```python
>>> range(-2, 2)
range(-2,2)
>>> list(range(-2, 2))
[-2, -1, 0, 1]
```
- Used to repeat an action
```python
>>>def cheer():
		for _ in range(3):
			print("Go Bears!")
Go Bears!
Go Bears!
Go Bears!
```
###List Comprehensions
----
```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'm', 'n', 'o', 'p']
>>> [letters[i], for i in [3, 4, 6, 8]]
['d', 'e', 'm', 'o']
```

```python
[<map exp> for <name> in <iter exp> if <filter exp>]

 Short Version: [<map exp> for <name> in <iter exp>]
```
A combined expression that evaluates to a list using this evaluation procedure:

1. Add a new frame with the current frame as its parent

2. Create an empty *result list* that is the value of the expression

3. For each element in the iterable value of \<iter exp>:
	- Bind \<name> to that element in the new frame from step 1
	- If \<filter exp> evaluates to a true value, than add the vale of \<map exp> to the result list

###Strings are an Abstraction
----
- text can represent data:
	- '200'  '1.2e-5' 'False'
- text can reprsent language:
	- """ And as imagination bodies forth
		The forms of things to uknown, and the poet's pen..
		"""
- text can represent programs:
	- 'curry = lambda f: lambda x: lambda y: f(x,y)'
```python
>>>exec('curry = lambda f: lambda x: lambda y: f(x,y)')
>>> curry
>>> curry(pow)(2)(4)
16
````

**String literals have three forms:***
- single quoted, double quoted, and triple quotd (to span multiple lines)
-import this: read the zen of python
-'\n' prints a new line

**strings are sequences**
- length and element selection are similar to all sequences
- an element of a string is itself a string, but with only one element
```python
>>> city = Berkeley
>>> len(city)
8
>>> city[3]
'k'
```

###Dictionaries
-----
- associate a value with an arbitrary key
- no control over the order of the elements

```python
>>> numerals = {'I': 1, 'V': 5, 'X': 10}
>>> numerals['X']
10
>>> numerals['V']
5
>>> numeravls.values()
dict values ([10, 1, 5])
>>> list(numerals.values())
[10, 1, 5]
>>> dict([('X', 10), ('v', 5)])
>>> {x: x*x for x in range(5)}
```


