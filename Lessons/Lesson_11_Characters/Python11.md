# Python Lesson 11 - Characters and Stopwatches

[All Lessons](https://zsiegel92.github.io/Eitan_S/)

[TOC]

## Review: Letting Time Pass with `time.sleep`

We have used Python's `time` module (`import time`) to access the `time.sleep` function, which allows a certain number of seconds to pass.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Countingtimesleep?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Try changing `time.sleep(1)` to `time.sleep(2)`.

## How to Time Durations with `time.time`

### Activity: Timing a Ball Rolling

>**Question**: Can you tell me how long it takes for a ball to roll from one side of the room to the other?

#####Materials:

* Ball
* Watch or clock
* Paper and Pencil
* Something flat

##### Instructions

1. Use something flat to build a small ramp across the room from a wall. Roll the ball down the ramp a few times until you can make the ball roll around the same speed every time.

2. **If you have a stopwatch**, try timing how long it takes for the ball to roll from the ramp to the closest wall. When the ball leaves the ramp, you **start** the stopwatch, and when it hits the wall, you **stop** the stopwatch. The time on the stopwatch is the duration of the roll.

3. **Now time the roll without a stopwatch, just with a clock**. You will need to keep track of the time when the ball leaves the ramp and the time when the ball hits the wall. *You will then have to "subtract" the times to find the number of seconds the ball was rolling.*

>You have a paper and pencil to help you keep track of times and do "subtraction". Have someone else roll the ball and try to get the timing right.

### The Current Time: `time.time`

Just like timing the ball, we will time processes by recording the current time at the **start** of a process, allowing the process to run, then recording the time at the **end** of a process.

The current time is returned by `time.time()`:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/timetime1?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

**`time.time` returns the number of seconds since the "epoch" start date**, with `float` precision.

>"On Windows and most Unix systems, the epoch is January 1, 1970, 00:00:00 (UTC) and leap seconds are not counted towards the time in seconds since the epoch. This is commonly referred to as Unix time." -[Python Documentation](https://docs.python.org/3.6/library/time.html)

#### Timing Processes with `time.time`

"Subtracting times from each other" sounds confusing. However, since `time.time` returns the current time as a number of seconds, "subtracting times" is easy!

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/timetimesubtractingtimes?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Change `time.sleep(1)` to `time.sleep(2)`, and `time.sleep(x)` for various values of `x`.

Run this code several times and notice that a slightly different value of `duration` is obtained each time. That's because `time.sleep` causes Python to wait a very precise number of seconds, but each command also takes a small amount of time to execute, including assigning values to the variables `start` and `end`.

The expression `str(int(duration))` casts the `float` variable `duration` as an `int`, *then casts that* as a `str`.

Recall that **casting a `float` as an `int` returns a rounded-down integer**. Casting an `int` or a `float` as a `str` returns a `str` variable containing the characters representing the number.

```python
>>> str(1.9)
'1.9'
>>> int(1.9)
1
>>> str(int(1.9))
'1'
```

## All the Characters: `chr`

We have iterated through integers using `while` loops, such as:

```python
>>> x = 0
>>> while x < 5:
...     print(x)
...     x += 1
...
0
1
2
3
4
```

We have also created random `int` variables:

```python
>>> import random
>>> random.randint(0,15)
8
>>> random.randint(0,15)
13
```

>**Question**: What if we wanted to *iterate through* or *randomly generate* `str` variables?

We know `str` variables are made up of individual characters.

```python
>>> "h" + "e" + "y" == "hey"
True
```

**Iterating through or randomly generating strings can be achieved by generating individual characters.**

### Special Characters: `\n`, `\t`, and the "Escape Character" `\`

We have seen the **special character** `\n`, which produces a new line, and is thus called the "new line character". We have also seen the "tab character" `\t`. Python actually has many more **special characters**, all of which start with a `\` symbol.

```python
>>> print("\nThe rain\nIn Spain\nFalls gently\nOn the plain.")

The rain
In Spain
Falls gently
On the plain.
```
>A "character" in this case consists of two symbols: `\` and `n`. Python recognizes these symbols as a single character.

```python
>>> print("Tabs create\tspaces\tin strings.")
Tabs create		space		in strings.
```

*All Python **special characters** start with a `\` symbol*. **The `\` symbol is called the *escape character***. It tells Python to "escape" the usual interpretation of the following symbol.

#### Escaping Characters

##### Escaping Escape Characters
>**Question**: What if we wanted to print an escape character without escaping it, such as `"\n"`?

We can **escape special characters to interpret them as regular characters**.

```python
>>> print("\n")


>>> print("\\n")
\n
```

We can even escape the escape character itself:

```python
>>> print("\\")
\
```

>If we try to print the escape character without escaping it, we get an error, which we will understand in a moment:
	```python
	>>> print("\")
	File "<stdin>", line 1
	  print("\")
	           ^
	SyntaxError: EOL while scanning string literal
	```
	Any string containing a `\` character **must** escape that character.

##### Quotes Between Quotes

We know we can put single quotes `' '` in strings formed by double quotes `" "` and vice versa:

```python
>>> print("I said 'hey'!")
I said 'hey'!
>>> print('I said "hey"!')
I said "hey"!
```

>**Question**: But what if we wanted both kinds of quotes in a string?
	**Answer**: We can *escape quotes* to interpret them as characters!

```python
>>> print("I said \"I'm Zach.\"")
I said "I'm Zach."
```

If double quotes `" "` or single quotes `' '` are used to construct a string, they must be escaped within the string to include them.

### ASCII Values: The `chr` and `ord` Functions

Python's `chr` function generates characters one by one.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/chr1?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Try calling `chr(i)` for `i` that is less than `32` or greater than `126`. You will see something like
	```python
	>>> chr(20)
	'\x14'
	```
	Because those are all special characters. All the standard characters have values between `32` and `126`, but there are *many* special characters.
	<br>"The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). ValueError will be raised if i is outside that range." -[Python documentation](https://docs.python.org/3/library/functions.html#chr)

There is an inverse function `ord` that gives the number of each character:

```python
>>> ord('a')
97
>>> chr(97)
'a'
```

>The numerical code of each character is called its **ASCII Value** (American Standard Code for Information Interchange).
	<div style="text-align: center;">
		<img src="ASCII_Chart.png" width="300" alt="ascii"/>
		<br>
		"ASCII chart from an earlier-than 1972 printer manual (b1 is the least significant bit.)" -[Wikipedia (ASCII)](https://en.wikipedia.org/wiki/ASCII)
	</div>

#### Converting Between ASCII Values and Characters

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/chrord?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


## Assignments


1. **Create a game** called "Guess My Character".

	1. The game should start by generating a random character by generating a random integer between `32` and `126` using `random.randint` (remember to `import random`), then converting it to a `str` using `chr`:
		```python
		chr(random.randint(32,126))
		```

	2. The game should then ask for the user to input a character using `input()` (which returns a `str`) until the user inputs the correct character.

	3. If the ASCII value of a guess is too low, the game should print `ASCII value too low!`; If the ASCII value is too high, the game should print `ASCII value too high!`.


	4. Your game should print a list of **all** ASCII characters at some point so that the user knows which characters are "too low" or "too high".

		You may use the following snippets of helper code for this part:
		<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Guessmycharacterhelpers?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	Use this "Guess my Number" game as a starting point:

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Guessmynumberforguessmycharacter?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	Save your work as `guess_my_character.py` or fork the snippets above on repl.it.

2. Time how long it takes to "crack" a safe! Note that this isn't the same process it takes to crack a real password, because a safe-cracker knows when they get an individual number/letter correct. A password-cracker has to guess the whole password at once.

	Below is a password cracker. Use the `time.time` function from this lesson to time how long it takes to crack different passwords!

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Guessmywordtiming?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	Save your work as `guess_my_word_timer.py` or fork the snippets above on repl.it.

3. Build a "Guess my Character" bot that plays the game from Assignment 1 (rather than using `input()`). The bot should use binary search to make optimal guesses.

	Note that the average of two numbers is the number directly between them. To find the average of two numbers, we can add them and divide by two:

	\\[\text{Average of 5 and 9} = \frac{5 + 9}{2} = \frac{14}{2} = 7\\]

	and

	\\[\text{Average of $x$ and $y$} = \frac{x + y}{2}\\]

	In Python we can find the average using the following function:

	```python
	def avg(x,y):
		return int((x+y)/2)
	```

	which we call as follows:

	```python
	>>> avg(5,9)
	7
	>>> avg(0,100)
	50
	```

	Binary search always guesses the number directly between the two bounds we know our number is between.
