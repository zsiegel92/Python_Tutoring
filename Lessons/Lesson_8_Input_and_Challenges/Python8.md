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

1. **Create a game** called "Guess My Number" that satisfies the following requirements:

	1. Generates a random number called `secret`
	2. Asks the user for input between `1` and `10`, over and over, until the input matches the random number.
	3. When the user enters input, if the input is equal to the random number (`== secret`), the game should print `You got it!`. **If the input is not a valid number, the game should throw a `ValueError`.**
	4. If the user's guess is too low, the game should print `too low`, and if it's too high, the game should print `too high`.

	Below is a version of "Guess My Number" that achieves requirements i, ii, and iii:

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Guess-My-Number?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

2. Create another version of "Guess My Number" that asks for a lower bound and an upper bound, then generates a random number called `secret` between those bounds, reminding the user of the bounds before each guess. The input-output stream should look approximately like this:
	```python
	Enter a lower bound for random numbers
	10
	Enter an upper bound for random numbers
	16
	Guess a number between 10 and 16
	13
	Too high!
	Guess a number between 10 and 16
	12
	Too high!
	Guess a number between 10 and 16
	11
	You got it!
	```
	If your lower bound is greater than your upper bound, your program should do one of the following:
	1. Throw a `ValueError` as follows:
		```python
		Enter a lower bound for random numbers
		10
		Enter an upper bound for random numbers
		5
		Traceback (most recent call last):
		 ...
		ValueError: empty range for randrange()
		```
	2. Ask for another number as follows:
		```python
		Enter a lower bound for random numbers
		10
		Enter an upper bound for random numbers
		5
		Enter an upper bound for random numbers
		6
		Enter an upper bound for random numbers
		15
		Guess a number between 10 and 15
		```
3. **Create a game** called "Coin Flip" that fulfills the following requirements:

	1. Asks for either `h` or `t` as input and generates a random string that is either `h` or `t`, over and over, until the input does not match the random string. The game should then tell the user how many "**coin flips**" they guessed correctly.
	2. Repeats the process for "Player 2", then prints which "Player" won the game by guessing more "coin flips" correctly.

	The input-output sequence should resemble the following:

	```python
	(p1) Enter 'h' or 't'h
	Player 1 gets a point!
	(p1) Enter 'h' or 't't
	Player 1 gets a point!
	(p1) Enter 'h' or 't't
	Player 1 gets a point!
	(p1) Enter 'h' or 't't
	Player 1 gets a point!
	(p1) Enter 'h' or 't'h

	WRONG. Player 2's turn!

	(p2) Enter 'h' or 't'h


	Player 1's score is 4. Player 2's score is 0.


	Player 1 wins!
	```

	Below is a partially-completed version of this game:

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/CoinFlipStreak?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	**Note** that the Python `random` library includes a function called `choice`. The function `choice` takes as an argument a `list` and returns a randomly-selected element of that `list`.

	```python
	>>> print(random.choice(['hi','hello','hey']))
	hey
	>>> print(random.choice(['hi','hello','hey']))
	hey
	>>> print(random.choice(['hi','hello','hey']))
	hello
	>>> print(random.choice(['hi','hello','hey']))
	hello
	>>> print(random.choice(['hi','hello','hey']))
	hello
	>>> print(random.choice(['hi','hello','hey']))
	hi
	```


4. **Create a game** that asks for a direction on an infinite loop and keeps track of your coordinates. Your coordinates should start at `x = 0` and `y = 0`, and you should use the following directions:

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







