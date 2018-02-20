# Python Lesson 12 - Challenges

[All Lessons](https://zsiegel92.github.io/Eitan_S/)

[TOC]

## Randomly Choosing, Avoiding Forbidden Elements

Achashverosh, the King of Persia, wants to randomly choose his next viceroy (his second-in-command). He asks his wife Esther to pick for him by drawing a name from a hat. She is able to do this in private, though, so nobody will see if she puts a name back into the hat.

She decides that if she draws `'Haman'`, she will put it back into the hat. Here is her algorithm:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Randomforbidden1?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Run this a few times. What names do you get?

When she uses this method, though, she still winds up with `'Haman'`! She realizes that she drew `'Haman'`, put it back in the hat, and then, unfortunately, drew `'Haman'` again!

She decides on a new method:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Randomforbidden2?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Run this a few times. What names do you get?

This ensures that she will draw a name, over and over, until it is NOT `'Haman'`. Whew.

>Note that `picked == 'Haman'` may never be true, depending on the first call to `random.choice`. That means the *body* of the `while` loop may never execute. That's just fine.



## Assignments

1. **Avoid forbidden choices.** You go to the movies with your friends Daniel and Sarah. There are 5 movies playing: 'Black Panther', 'Peter Rabbit', 'Jumanji', 'The Post', and 'The Shape of Water'.

	You want to see 'Black Panther', but Daniel wants to see 'Peter Rabbit', and Sarah wants to see 'Jumanji'.

	You ask your dad to randomly choose a movie for you. He chooses 'The Post' (ugh, dads!). Now nobody is happy! Sarah and Daniel say together, "Nobody wants to see boring movies like 'The Post' and 'The Shape of Water'"!

	Create a function that does the following:

	* Randomly chooses a movie from the list `movies = ['Black Panther', 'Peter Rabbit', 'Jumanji', 'The Post', 'The Shape of Water']`
	* Chooses again (over and over) as long as the choice is in `boring_movies = ['The Post', 'The Shape of Water']`

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Randomforbiddenassignment?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	For the snippet on repl.it or save in a file called `forbidden_elements.py`.

2. **Create a random name.** A valid name on planet Zulu has four characters, the first and third of which are consonants, and the second and fourth of which are vowels.

	Examples of valid names include:

	* Boxa
	* Veru
	* Heha
	* Yiyi
	* Xuxe

	Create a program that randomly creates valid names from planet Zulu. You can use the lists `vowels` and `letters` to accomplish this goal.

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Randomname?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	>Note that the lowercase letters can be obtained `chr(i)` for `i` between `97` and `123` (all keyboard characters can be found between `33` and `126`).

3. **Find the maximum.** In Mathematics, a very useful concept is that of a **set**. "In mathematics, a set is a collection of distinct objects" -[Wikipedia (Set)](https://en.wikipedia.org/wiki/Set_(mathematics)).

	A mathematical set containing the numbers \\(1, 2,\\) and \\(3\\) can be written \\(\\{1,2,3\\}\\).

	Unlike a Python `list`, elements of a mathematical *set* are not in any order and repeated elements are considered the same element. That is, the set \\(\\{1,2,3\\}\\) is the same as the set \\(\\{3,2,1\\}\\), which is the same as the set \\(\\{1,1,2,2,3,3\\}\\).

	For a given set, the **maximum** is the greatest element of the set. The maximum of \\(\\{3,2,1\\}\\) is \\(3\\).

	**Create a function called `maximum_element` that returns the maximum element of a `list` of `int` variables**.

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Setmaximum?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	>Remember that to iterate through the elements of a list, we can use a `while` loop or a `for` loop:
		```python
		my_list = [1,2,3,4]
		i = 0
		while i < len(my_list):
			print(my_list[i])
			i += 1
		```
		or
		```python
		my_list = [1,2,3,4]
		for thing in my_list:
			print(thing)
		```















