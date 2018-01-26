# Python Lesson 9 - Sorting Lists

[All Lessons](https://zsiegel92.github.io/Eitan_S/)

[TOC]

## Random Functions in the `random` module: `randint`, `choice` and `shuffle`

We have used Python's `random` module several times. [Learn about the random module here](https://docs.python.org/3.6/library/random.html).

* We usually use the `random.randint` function to generate a random integer betwen an upper and a lower bound.
	```python
	>>> print(random.randint(1,10))
	7
	>>> print(random.randint(1,10))
	6
	>>> print(random.randint(1,10))
	8
	>>> print(random.randint(1,10))
	2
	>>> print(random.randint(1,10))
	4
	>>> print(random.randint(1,10))
	10
	```
* We have also seen the `random.choice` function, which generates a random element from a `list`:
	```python
	>>> print(random.choice(['a','b','c']))
	a
	>>> print(random.choice(['a','b','c']))
	c
	>>> print(random.choice(['a','b','c']))
	c
	>>> print(random.choice(['a','b','c']))
	c
	>>> print(random.choice(['a','b','c']))
	b
	>>> print(random.choice(['a','b','c']))
	b
	>>> print(random.choice(['a','b','c']))
	a
	>>> print(random.choice(['a','b','c']))
	b
	>>> print(random.choice(['a','b','c']))
	b
	```

Now, we will learn about `random.shuffle`:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/RandomShuffle?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Run this code several times to verify that `random.shuffle` produces a randomly-generated order on each call.

## Sorting: `sorted` and `list.sort`

Python includes two easy ways to sort lists: `sorted` and `list.sort`.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/listsortsorted?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

There are two important differences between these two functions:

* `mylist.sort()` **alters `mylist`** by sorting it. **It does not return anything.**
* `sorted` **returns a sorted copy of the input list**. **`sorted` does not alter `mylist`.**


## Assignment

1. Create a function that simulates a deck of cards **omitting suits**, prints them in sorted order, then prints a shuffled version of the cards.

	* Cards can be represented by integers between 1 and 13. So, each Ace can be represented by the `int` `1`, each 2 by a `2`, each Jack by `11`, each Queen by `12`, and each King by `13`.

	The sorted version of the deck should look like this:

	```python
	>>> print(deck)
	[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
	```

	The shuffled version of the deck should look something like this:

	```python
	>>> print(deck)
	[12, 13, 11, 3, 4, 13, 9, 2, 9, 2, 8, 1, 6, 5, 2, 9, 11, 6, 3, 5, 5, 7, 6, 2, 3, 8, 4, 7, 12, 10, 9, 12, 4, 8, 1, 7, 13, 11, 1, 4, 5, 11, 1, 6, 7, 12, 8, 10, 3, 13, 10, 10]
	```

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Decksortshuffle?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	Save your work in a file called `deck_sort_shuffle.py`.
