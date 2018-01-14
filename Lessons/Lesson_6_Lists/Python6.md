# Python Lesson 6 - Lists, Syntactic Sugar, Casting, and Mutability


## Review of Lesson 5

### Functions: `def`, `return`, Parameters and Arguments

>You should understand all the code in the following snippet

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functionsreview?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


## Python's **Syntactic Sugar**

The words and phrases that make the structure of a language is called its **syntax**. English evolved over thousands of years, whereas [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) was created in 1991. English **syntax** *came to be accepted* over time as people started to use words and phrases. Python's **syntax** is *designed* by programmers who decide how Python code should be executed by a computer.

>[Wikipedia gives a definition](https://en.wikipedia.org/wiki/Syntax_(programming_languages)) of **syntax**: "the syntax of a computer language is the set of rules that defines the combinations of symbols that are considered to be a correctly structured document or fragment in that language."

The syntax that is acepted in spoken languages and designed in computer languages often is *easy and convenient*. There is no real *need* for contractions like "gonna", "wanna", and "I'd", but they're great, and save us lots of time; many spoken languages have contractions.

*Designed languages also have shortcuts, and we call those **syntactic sugar**.* Like sugar, they're not really necessary for survival, but we like them.

Much of this lesson is about how to use Python's **syntactic sugar**, so be prepared for some time-saving shortcuts!

### Python's **Syntactic Sugar** We've Already Covered

* Suppose `mylist` is `[1,2,3,4]`. We know `len(mylist)` will be `4`, so we can access the last element using `mylist[len(mylist)]`. So we don't really need the ability to access the last element using `mylist[-1]`, but it's much clearer. ***That's syntactic sugar.***
* When we concatenate `"my " + "friend"` we are "adding" words, which is *not* something people think about in everyday life. We could achieve the same thing using `.format` as so:
	```python
	>>> "{} {}".format("my","friend")
	'my friend'
	```
	but using the `+` operator for concatenation is often much easier to read, so Python's designers decided that that syntax is valid. ***That's syntactic sugar.***

### Some New **Syntactic Sugar** in Python

#### **Incrementing** and **Decrementing**: `+=` and `-=` Operators

When we write `while` loops, we usually start with a counter
```python
mylist = [1,2,3,4]
i = 0
while i < len(mylist):
	print(mylist[i])
	i = i + 1
```

When we write `i = i + 1`, we are **incrementing** our counter. It is also common to **decrement** a counter by subtracting a constant.

Python has shortcuts for incrementing and decrementing:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/incrementshortcut?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Explanation:

|Statement (Syntactic Sugar)|Equivalent Statement|Explanation|
|----|-----|-----|
|`x+=5`| `x = x + 5` | `+=` is the **increment** operator also called the **Add AND** operator|
|`x-=5` | `x = x - 5` | `-=` is the **decrement** operator also called the **Subtract AND** operator|
|`x*=5` | `x = x * 5` | `*=` is the **Multiply AND** operator|
|`x/=5` | `x = x / 5` | `\=` is the **Divide AND** operator|



## Python `list` Variables

We have seen Python `list` variables:

```python
>>> a = [1,2,3]
>>> print(a)
[1, 2, 3]
>>> type(a)
<class 'list'>
```

We know how to declare lists, and even how to access elements of lists, but not much more.

### Indexing and Slicing

The following snippet should all make sense to you:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Listsindexingslicing?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


Note that if we try to access list elements that do not exist, we get an `IndexError`:

```python
>>> a = [1,2,3]
>>> print(a[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

Even if we attempt to assign values to non-existing indices, we get an `IndexError`:

```python
>>> a = [1,2,3]
>>> a[3] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
```

### Appending and Extending: `.append`, `.extend`, and Concatenation Using the `+` Operator

We seem to get an `IndexError` when we try to access list indices that do not exist. So: *can we change the length of a list*? Yes.

The `.append` function takes one argument, which it makes into the last element of a list:

>We have seen `str` functions like `.format` that have to be called from a `str` variable (like `"hello {}".format("friend")`). We will learn more about **object methods** soon.

```python
>>> a = [1,2,3]
>>> a.append(4)
>>> print(a)
[1, 2, 3, 4]
```

The `.extend` function takes one argument, *which has to be a `list`*, whose elements it adds onto the end of a list:

```python
>>> a = [1,2,3]
>>> a.extend([4,5,6])
>>> print(a)
[1, 2, 3, 4, 5, 6]
```

We have seen that we can **concatenat** `str` variables using the `+` operator. We can do the same with `list` variables:

```python
>>> a = [1,2,3] + [4,5,6]
>>> print(a)
[1, 2, 3, 4, 5, 6]
```

Be careful about the difference between `append` and `extend`!

```python
>>> x = [1,2,3]
>>> y = [4,5,6]
>>> x.append(y)
>>> print(x)
[1, 2, 3, [4, 5, 6]]
```

Now a `list` is an element of a `list`! This isn't a problem if it's intentional.


### Automatically Creating a List Using `while`

We can combine our knowledge of `while` loops with `append` to automatically create long lists!

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Listswhileiteration?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Note the use of `+=` in these examples! We will use that operator from now on.

### **For** Loops: `for`

We have seen how to loop using `while`, and we always have to create a counter, which we increment on each loop iteration. Python has the keyword `for`, which allows us to access each element in a data structure:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Listsaccessingfor?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

The line `for thing in mylist:` assures that the indented code is executed once for each element of `mylist`, and on each iteration an element of `mylist` is assigned to the variable `thing`.

>The `for` loop syntax is definitely **syntactic sugar**, but it is extremely common and useful!

### List "Multiplication" (more **syntactic sugar**)

Suppose we want a list that repeats the same values over and over. We can achieve this very easily using the `*` operator in Python:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Listsmultiplication?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

We can even use the `*=` operators:

```python
>>> mylist = [1,2,3,4]
>>> mylist *= 4
>>> print(mylist)
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
```

### Strings are Like Lists!

Note all the similarities between `list` variables and `str` variables:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Listslikestrings?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


### Two-Dimensional Lists

We have seen that we can create `list` variables that contain `list` variables.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Lists2dimensions?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

In this case, `x[0]` is the list `[0,1,2]`, so `x[0][0]` is the first element of that list, which is `0`!

*Note that each `list` variable contained inside a `list` variable does not have to have the same **length***. However, if they each have the same length, we can create a nice grid:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Lists2dimensions2grid?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Note that we needed to print one row at a time (which we achieved using `for`) in order to see our grid!

## Type Casting

Often there's an obvious way that we would want to "convert" a variable of one **type** to a variable of another **type**. In computer science, we call this **casting**.

It's fairly intuitive, but pay close attention to the following examples:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Casting?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Most variables in Python are defined using a `class` definition (Lesson 7). When we call `str(7)`, Python calls the `__init__` method in the `class` definition of `str`. That method **initializes** a `str` variable, and has instructions on how to do so using an argument of type `int`. We are not "converting" so much as defining a new variable using another variable as a parameter!


## Mutability of Data Types

Some data types are **mutable**, which means that Python can edit them in the computer's memory. Other data types are **immutable**, which means Python cannot make changes to them without destroying them and creating a new version.

In Python, `str` and `int` variables are **immutable** but `list` variables are **mutable**.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Mutability?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


>In general, objects are mutable, but **primitive data types** are immutable. These are limited to `int` and `str` values.

When we use `extend` or `+` to concatenate two `list` variables, the values from one list are copied to the other, and they are no longer part of the same variable:

```python
>>> list1 = [1,2,3]
>>> list2 = []
>>> list2.extend(list1)
>>> print(list2)
[1, 2, 3]
>>> list1[0]=5
>>> print(list1)
[5, 2, 3]
>>> print(list2)
[1, 2, 3]
```

>Note that values in `list2` are not changed when we *mutate* `list1` because values were *copied* by the `extend` command, and `list2` no longer accesses the same values as `list1`.

## Assignment

1. Define a function called `flatten` that takes one parameter that is a `list` variable that contains only `list` variables and returns a `list` variable containing all the elements of all the `list` variables making up the input.

	* `flatten([[1,2],[3,4],[5,6]])` should return `[1,2,3,4,5,6]`
	* `flatten([[1],[2],[3]])` should return `[1,2,3]`
	* `flatten([[1],[2,3],[4,5,6]])` should return `[1,2,3,4,5,6]`

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Listflatten?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	Save your work in a file called `flatten.py` **or** fork the *repl.it* snippet above and do your work in repl.it.

2. Define a function called `square_grid` that takes one parameter that is an `int` variable that determines the side length of a square 2-dimensional `list` containing all asterisks.

	The `pretty_print` function has been provided for you to print your "square grids" (2-dimensional `list` variables).

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Listssquaregrid?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	The output displayed on screen should match the following:

	* `pretty_print(square_grid(5))` should output
	```python
	['*','*','*','*','*']
	['*','*','*','*','*']
	['*','*','*','*','*']
	['*','*','*','*','*']
	['*','*','*','*','*']
	```

	>**HINT**: Remember that `[1,2,3]*3` returns `[1, 2, 3, 1, 2, 3, 1, 2, 3]` (see the **List "Multiplication"** section). Also note that `['*']*5` returns `['*', '*', '*', '*', '*']`.

	Save your work in a file called `square_list.py` **or** fork the *repl.it* snippet above and do your work in repl.it.

3. Define a function called `square_grid` that takes one parameter that is an `int` variable that determines the side length of a square 2-dimensional `str` containing all asterisks.

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Listsstringsquaregrid?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	The output of `print(square_grid(20))` should be:
	```python
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	********************
	```

	>**HINT**: Remember that `'*'*5` returns `'*****'` (see the **Strings are Like Lists!** section).
	>**HINT**: Remember that the `'\n'` character sequence is a "line break".
	```python
	>>> print('hey\nmy\nfriend')
	hey
	my
	friend
	```
	more specifically,
	```python
	>>> print('***' + '\n' + '***' + '\n' + '***' + '\n')
	***
	***
	***

	```

	Save your work in a file called `square_string.py` **or** fork the *repl.it* snippet above and do your work in repl.it.


3. Define a function called `square_grid` that takes **two** parameters. The first parameter should determine the size of the square (as in **Assignment 2**) and the second parameter should be a `str` that determines the symbol for the grid. The second parameter should have the default value `'*'`.

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Listsstringsquaregridsymbol?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	The output described in the snippet should be achieved.

	The function should be almost identical to the function in **Assignment 2**, except `symbol` should be used in place of `'*'`.

	Save your work in a file called `square_symbol.py` **or** fork the *repl.it* snippet above and do your work in repl.it.
