# Python Lesson 3

[All Lessons](https://zsiegel92.github.io/Eitan_S/)

[TOC]

## Review of Lesson 2

### Variable Types: `int`, `str`, `list`, `bool`

We can view the **type** of a variable using the `type` keyword. The type of a variable has to do with what kind of data that variable stores.

```python
x = 5
print(type(x))
```

>`int` variables are "Integers", which are whole numbers like 1, 2, 3, ...

```python
x = 'hello'
print(type(x))
```

>`str` variables are "Strings", which are sequences of characters, like `'hello'` or `'taco'` or `'a'`. We can create them with double quotes (`"hello"`) or single quotes (`'hello'`).

```python
x = (4 < 5)
print(x)
print(type(x))
```

>`bool` variables are "Booleans", which are either `True` or `False`. When we use a comparison operator, like `<`, `>`, `<=`, `>=`, or `==`, we get a `bool` variable. These are used in `if` and `elif` statements.

```python
x = [1,2,3]
print(x)
print(type(x))
```

>`list` variables are "Lists", which store other variables, in order. More on that later.

### Conditionals: `if`, `else`, and `elif`

Refer to Lesson 2 for the behavior of the following code:

```python
if x > 5:
	print("I have enough money for a taco")
elif x == 5:
	print("I have exactly enough money for a taco")
else:
	print("I don't have enough money for a taco")
```

#### The `pass` Command

If we want to "Do Nothing" when we satisfy a condition, we can use the command `pass`:

```python
if x < 5:
	pass
else:
	print("Woohoo! I can buy a taco.")
```

## Loops: `while`

### Parts of a Loop
We have seen "conditional" expressions, which only execute if a conditional evaluates to `True`. What if we wanted to execute an expression over and over, as long as a conditional evaluated to `True`? We can do this with `while`.

```python
x = 1
while x < 10:
	print(x)
	x=x+1
```

**There are three main parts to a `while`  loop**:

1. The **initialization** of the variables and environment:
```python
x=1
```

2. The **conditional** expression, which determines whether the loop should repeat:
```python
while x < 10:
```

3. The **body** of the loop, where the activity happens:
```python
	print(x)
	x = x+1
```

### Termination of Loops

The most important thing to consider when creating a loop is that it terminates!

#### A non-Terminating Loop
Try running this code:

```python
x = 1
while x < 10:
	print(x)
```
Remember that you can press <kbd>ctrl</kbd>+<kbd>C</kbd> to stop Python code!

#### How to Ensure Loops Terminate

If the activity in the **body** of the loop will eventually make the loop conditional evaluate to `False`, then the loop will terminate. In our loop above, the line `x = x + 1` always brought our conditional closer to evaluating the `False`.

#### Loops Inside Loops

Say we wanted to print every consecutive sequence of numbers from 1 to 9 starting with 1. Try reading then executing this code:

```python
x = 0
while x < 10:
	print()
	x = x + 1
	y = 0
	while y < x:
		y = y + 1
		print(y)
```

# Assignment

## Printing Sequences of Numbers

Write code that prints the following output:

```python

1

1
2

1
2
3

1
2
3
4

1
2
3
4
5
```



## Printing without Skipping Lines
When we print, we can stay on the same line by putting `end=''` inside our `print()` statement. Try the following:

```python
print('x', end='')
print('x',end='')
```
and compare it to

```python
print('x')
print('x')
```

With that in mind, write code that produces the following output, and save it in a file called `assignment.py`:

```python
1
12
123
1234
12345
123456
1234567
12345678
123456789
12345678910
```

## Printing with Conditionals

Produce the same sequence output as the "Printing Sequences of Numbers" assignment, but skip all the 5's:

```python

1

1
2

1
2
3

1
2
3
4

1
2
3
4
```
>**Hint**: Use
```python
if y == 5:
	pass
else:
	print(y)
```
somewhere in the code that produced the output for "Printing Sequences of Numbers".

## Resources

Run the script `conditionals.py` using `python conditionals.py`.

Run the webapp `app_conditionals.py` using `python app_conditionals.py`.
