# Python Lesson 8 - Input and Challenges

[All Lessons](https://zsiegel92.github.io/Eitan_S/)

[TOC]

## Input: `input()`

So far we have interacted with Python in the following two ways:

1. We execute code line-by-line in a **REPL** (**R**ead **E**valuate **P**rint **L**oop) environment by typing `python` from the *command prompt*.
2. We Execute every line of code in a `.py` file by typing `python <filename>.py` from the *command prompt*.

The REPL environment allows us to *interact* with Python code. **We can *interact* with Python code in `.py` files by using `input()`!**

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Input?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Just like `len` and `type`, the `input` function can be called from any Python environment.

### More `input` Examples

The function `input` returns a variable of type `str`. If `x = input()` is executed and `5` <kbd>Enter</kbd> is typed, then `type(x)` will yield `<class 'str'>`.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Input2?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Notice that the variable `age` stores a number but its type is `str`.

### Casting Input: `int()` and `str()`

Recall that we can **cast** variables to create variables with different **type** that store roughly the same information. This is common with with `input`.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Input3casting?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

If we have a `str` variable storing digits, like `"5"`, then we can cast with no problems:
```python
>>> print(int("5"))
5
```

However, sometimes, casting can cause problems.
```python
>>> print(int("five"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'five'
```

Be careful!
>Soon, we will learn about **handling exceptions**. Just like `if`, `while`, and `for` statements, we have a code structure called `try`...`except` that allows us to execute code with exceptions without exiting. This is called **handling exceptions**. More on that later!

### Infinite Input Loops: `while True`

Many programs (like **games**) keep running and accepting input until the user exits. We can create an **infinite loop** using `while` without terminating.

Recall that `while` loops need a terminating condition:
```python
x = 0 # initializing x
while x < 5:
	print("Executing the loop")
	x += 1 # incrementing x
```

Since `x += 1` increases `x` by `1` on each loop iteration, eventually the condition `x < 5` will evaluate to `False` and the loop will stop executing!

We can create an infinite loop easily, but it doesn't do us much good:

```python
>>> while True:
...     print("Executing the loop")
...
Executing the loop
Executing the loop
Executing the loop
Executing the loop
Executing the loop
Executing the loop
Executing the loop
.
.
.
```

**With `input()`, we can create infinite loops that are actually useful!**

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Inputinfiniteloop?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

## Assignment

1. **Create a game** that asks for a direction on an infinite loop and keeps track of your coordinates. Your coordinates should start at `x = 0` and `y = 0`, and you should use the following directions:

	* If input is `a`, **move left** by decreasing your `x` coordinate using `x -= 1`
	* If input is `s`, **move down** by decreasing your `y` coordinate using `y -= 1`
	* If input is `d`, **move right** by increasing your `x` coordinate using `x += 1`
	* If input is `w`, **move up** by increasing your `y` coordinate using `y += 1`

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/InputNavigationGame?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	***NOTE:*** An **ordered pair** is two numbers in parentheses that give coordinates. For example, `(1,2)` means "The point where \\(x\\) is \\(1\\) and \\(y\\) is \\(2\\)".

	<div style="text-align: center;">
		<img src="coordinates.jpg" width="500" alt="coordinates"/>
		Ordered Pairs
	</div>

2. Another assignment.







