###Print vs. Return
Print     | Return
-------- | ---
Statement | (non-pure) function
1. Denotes what the function evaluates to <br> 2. Terminates the function    | 1. Displays its argument(s) to the terminal (side effect) <br> 2. Evaluates to None
Used only in functions     | Used anywhere

###Examples:
```
def square1(x):
  return x * x

def square2(x):
  print (x * x)

def square3(x):
  print (x * x)
  return x * x
```

Expression | Evaluates to | Displays in Interpreter
:-----------:| :-------------: | :-----------------:
square1(4) | 16 | 16
square2(4) | None | 16
square3(4) | 16 | 16 <br> 16
print(square2(4)) | None | 16 <br> None
