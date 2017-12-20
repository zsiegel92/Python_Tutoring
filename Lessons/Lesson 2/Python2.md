# Python Lesson 2

## Running Python

#### Running Python Scripts (`something.py`)

Use `cd` and `dir` to navigate to the folder containing a Python file with the `.py` extension. Type `python filename.py` to execute all the Python commands in the `.py` file.

#### Running the Python Interactive Console (REPL)

Type `python` <kbd>enter</kbd> from the command prompt at any time to open the Python Interactive Console, which will **R**ead **E**valuate **P**rint and **L**oop as you provide commands.

## Variable "Types" and the `type` Keyword

Open the Python Interactive Console by typing `python`<kbd>enter</kbd> in the command prompt.

To create a variable named `x` storing the value `5`, we write `x=5`. The `=` symbol is called the "assignment operator", because we use it to "assign" values to variables.

```python
x = 5
print(x)
```

Now, change the value of `x` and print the new value.

```python
x = 'hello'
print(x)
```

Wouldn't you say that the value `'hello'` and the value `5` are fundamentally different? That's because they have different **type**. Some variables hold numbers, others hold words or other data. The **type** keeps track of what a variable holds, and a computer treats different types differently.

Check the type of `x` with the keyword `type`.

```python
x = 5
print(type(x))
```

>`int` is short for "Integer", which is what we call numbers like 0, 1, and 2. Some numbers are not integers, like "two and a half". Negative numbers are integers.

```python
x = 'hello'
print(type(x))
```

>`str` is short for "String", which is what we call sequences of characters. To create strings, we usually have to put text between quotes (like `"hello"` or `'hello'`)

```python
x = [1,2,3]
print(type(x))
```

>`list` is what Python calls ordered sequences of other variables. We can create a `list` of `str` variables (like `['a','b','c']`), a `list` of `int` variables (like `[1,2,3]`), or a `list` of both (like `[1,2,'a']`)! More on that later.

```python
x = 1.5
print(type(x))
```

>`float` is what Python calls most numbers that are not integers (`int`). These are numbers like "two and a half", which can be represented with a decimal as 2.5. The word "float" is used because the decimal point "floats" between numbers.

```python
x = 'True'
print(type(x))
```

>This is another `str` variable because it is between quotes (`""`).

```python
x = True
print(type(x))
x = False
print(type(x))
```

>`bool` is short for "Boolean", which means "True or False". In fact, all `bool` variables are either `True` or `False`.

### Boolean Variables of Type `bool`: `True` and `False`

We saw that the **type** of `True` was `bool`. Let's analyze some more `bool` data.

```python
print(4 < 5)
type(4 < 5)
```
Note that `print(4 < 5)` printed `True`. That's because the `<` symbol is an "operator" that tells Python to compare what's on its left to what's on its right, and to "turn into" `True` if what's on the left **is less than** what's on the right, and `False` otherwise.

```python
print(5 < 4)
type(5 < 4)
```

### Comparison Operators: `<`, `>`, `<=`, `>=`, and `==`

We have seen that the operator `<` can be placed between two numbers, and the whole expression will either "turn into" `True` or `False` depending on whether the number on the left is "less than" the number on the right.

Think about what the output of each `print` statement will bebefore running these commands:

```python
print(4 < 4)
print(4 < 5)

print(4 > 4)
print(4 > 5)

print(4 <= 4)
print(4 >= 4)
print(4 <= 5)
print(4 >= 5)

print(4 == 4)
print(4 == 5)
print(4 == 'hello')
print('hello' == 'hello')
```

>**NOTE:** We call the double equals sign `==` the "**equality operator**", and it turns an expression into `True` or `False` (like `5 == 5`). Remember we call the single equals sign `=` the "**assignment operator**" and we use it to "assign" values to variables (like `x = 5`).

Think about what the output of each `print` statement will bebefore running these commands:

```python
print(5 == 5)
x = (5 == 5)
print(x)
print(True == True)
print(False == False)
```

## Conditionals and Tacos: The `if`, `else`, and `elif` Keywords

>Is 5 greater than 4? Is 5 less than 4? If you don't know what "less than", "equal to", and "less than or equal to" mean, then please ask a Math teacher at this moment (or Google it)!

Suppose `x` represents the amount of money I have, and a taco costs $5. I want to print "I have enough money for a taco" only if `x` is greater than 5. We could use

```python
if x>5:
	print("I have enough money for a taco")
```

Let's test this code by copying the following two snippets into
the python shell:

```python
x=4
if x>5:
	print("I have enough money for a taco")
```
and
```python
x=6
if x>5:
	print("I have enough money for a taco")
```

Did Python execute these snippets as you'd expect?

Now, what if we wanted to print "I don't have enough money for a taco" when `x` is less than 5? We can use `if` and `else` together as follows:

```python
if x >5:
	print("I have enough money for a taco")
else:
	print("I don't have enough money for a taco")
```

Finally, we can create additional conditions using `elif`. The code after `else` will only be executed if our first conditions are `True`.

```python
if x > 5:
	print("I have enough money for a taco")
elif x == 5:
	print("I have exactly enough money for a taco")
else:
	print("I don't have enough money for a taco")
```

Try executing `x=5`, then copying the above code into Python. What happened? Execute `x=4` and do the same. Execute `x=6` and do the same.

Run the script `conditionals.py` using `python conditionals.py`.
