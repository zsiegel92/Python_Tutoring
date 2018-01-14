# Python Lesson 4 - Strings (`str`)

[TOC]

>This lesson contains embedded code snippets! This uses a tool called **repl.it**, and we will use embedded REPL environments frequently from now on. To run any of these code snippets, hit the triangular "play button" in the repl.it window.

>You will still have to use the `python` command in your command prompt for assignments, though.


## Review of Lesson 3

### Loops: `while`

To repeat some command or commands, we can place those commands in a `while` statement. The commands that are **indented** on the line after `while (some condition):` will be executed until `(some condition)` is false. Note that `(some condition)` has to evaluate to either `True` or `False` - that is, it must evaluate to a value with type `bool`.

Example:


<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Print-1-10?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


### Types

We can find out the type of any variable by using the `type` function:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Type-Check?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


>Don't worry about the `.format` commands now. They will make more sense after this lesson.


Here are the types we have seen so far:

| Type Name | Type | Example 1 | Example 2 |
|----------|--------|------------|---|
| Integer | `int` | `x = 5` | `len([1,2,3])`|
| String | `str` | `y = "a`" | `name = 'baba'`
| Boolean | `bool` | `True` | `value = (4 <= 5)` |
| List | `list` | `[1,2,3]` | `["a","b","c"]`|

## Python Strings: `str`

We have seen the Python `str` type, but have not used all of its functionality yet. Here are some things we can do with Strings:

### Concatenation

The `+` operator is assigned to **arithmetic addition** when the expressions on either side of it are numbers (`int` or `float`). When given two `str` variables, however, the `+` operator is assigned to **string concatenation**, which combines two strings by placing them side-by-side.

#### Concatenation is **Exact**

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/String-Concatenation?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>



#### Concatenation Makes Code Re-Usable


<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Concatenation-2?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


>Notice that we were able to exactly re-use the line of code with the `print` statement!

Concatenation is one of the most important jobs most computer programs do. Just like the line of code we re-used, most websites just concatenate in a tiny snippet of data (like `title = "Watch This Cute Panda Eat Bamboo"`) to a bigger webpage.


Imagine how many ways we could use and re-use this code:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Concatenation-3?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


>Notice that the `preferred_pronoun` should be capitalized at the beginning of the last sentence. We will come back to that!

#### Concatenation is Fun

Try your parent's information!

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Complicated-Concatenation?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


### Substrings

We have seen how to combine little snippets into a longer string. How can we **extract** little snippets **from** a longer string?


Python offers intuitive ways to do this, and we will talk about three: **the `in` keyword**, **indexing** and **slicing**. You have seen that a `list` is a Python type that contains other Python variables (eg `x = [1,2,3,'hello']`). The ways we **index** and **slice** substrings of strings will prepare us for working with the `list` data type in an upcoming lesson.

#### The `in` Keyword

```python
>>> name = 'Zach'
>>> print('a' in name)
True
>>> print('b' in name)
False
```

Why did we see `True` and then `False`? Didn't we ask to print "a" and "b"?

The `in` keyword allows us to check whether a string contains a given substring.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/The-in-Keyword?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


We can use `in` to check for more than single-letter substrings:

```python
>>> story = "I love taking the bus! It gives me the freedom to travel around for very little money. Thanks to public resources like the bus, I know that no matter how tough a situation I'm in, I will survive and be able to do my job."
>>> query = "the freedom"
>>> print(query in story)
True
```

#### String Indexing and Slicing

Let's say we wanted to print the first letter of a middle name

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/String-Indexing?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


Great! Why did I have to print `middle_name[0]` and not `middle_name[1]` to get the **first** character of the `str` `"Edmund"`? Try `middle_name[1]` and `middle_name[2]`. Try `middle_name[n]` for all `n` between `0` and `5`.

>What happens when you execute `middle_name[6]`? Why?

Can we access more than a single character using indexing? Yes, and when we do, it is called **slicing**.

```python
>>> middle_name = "Edmund"
>>> print(middle_name[0:3])
Edm
```

When you see `0:3`, you might expect the characters at indices `0`, `1`, `2`, and `3` to be printed. However, we only saw `0`, `1`, and `2`. **Slicing is non-inclusive**, meaning the last index in a slice is not part of that slice.

>Part of why computer scientists like non-inclusive slicing is so that the **length** of a string (or list) is clear. If the first index is `0`, and the last index is `5`, then there are a total of `6` characters in `middle_name`. Looking at `middle_name[0:6]`, we know that (in Math) 6-0=6, so the slice `[0:6]` should have 6 characters, which is all of them. Similarly, `middle_name[1:6]` has 6 - 1 = 5 characters.

We know the last index of `"Edmund"` is `5`, so, since slicing is non-inclusive, we can get the entirety of our string using middle_name[0:6].

### Finding the **Length** of a String: The `len` Keyword

To find the number of characters in a `str` (or the number of elements in a `list`), we can use the `len` function:

```python
>>> print(len("hello"))
5
>>> print(len("Zach"))
4
>>> print(len([1,2,3]))
3
```

Usually, we use `len` to provide a number that will be used as an index. Remember, **the number of characters in a `str` (which `len` tells us) is one greater than the highest index because indexing starts at 0**.

>In a `str` called `mystring`, the last character is `mystring[len(mystring)-1]`.

Here are some uses of `len`:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Indexing-Using-len?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>



| Code | Value | Explanation|
|:-------|:----|:----|
|`category[len(category)-1]` | `"y"` | The last character in a string called `mystring` has index `len(mystring)-1`|
|prices[len(prices)-1] |`700` | The last element of a `list` called `mylist` has index `len(mylist)-1`|
|`names[len(names)-1]`|`"Google Pixl"` | Another `list` - this time a `list` of `str` variables|
|`len(names[len(names)-1])`| `11` | `names[len(names)-1]` is the last element of `names`, which is `"Google Pixl"`. The `len("Google Pixl")` is `11`|
|`names[0][0]` | `"N"` | The element of `names` at index `0` is `"Nokia NK100"`. The character at index `0` in `"Nokia NK100"` is `"N"`|
|`names[len(names)-1][len(names)-1]` | `"l"` | The last character of the last element of `names` is the last letter of `"Google Pixl"`, which is `"l"`|

### Accessing the Last Element: the `[-1]` Shortcut

#### Indexing with `[-1]`

Finding **the last** element of a `list` or character of a `str` is **so** common in python that there is a special shortcut to access it.

Instead of typing `mystring[len(mystring)-1]` or `mylist[len(mylist)-1]` we can just type `mystring[-1]` or `mylist[-1]` to access the last element of a `str` or `list`.

```python
>>> mystring = "Zach"
>>> mylist = ["Zach", "Susan", "Lawrence"]
>>> print(mystring[-1])
h
>>> print(mylist[-1])
Lawrence
```

Notice that the index `-1` gives the exact same result as `len(mystring)-1`.

#### Slicing with `:-1`

We can also use a `-1` in a slice to access **all elements through the final element**.

>Remember that slicing is **non-inclusive**, meaning that a slice ending in `-1` will not include the `-1` element, which is the final element.

```python
>>> myname = "Zachary Edmund Siegel"
>>> print(myname[0:-1])
Zachary Edmund Siege
```
You should see `Zachary Edmund Siege`.

>**Slices can include any negative numbers, which refer to the index of a given number of elements from the end of the list**.

```python
>>> myname = "Zach"
>>> print(myname[-4])
Z
>>> print(myname[1:-2])
a
```

### Splitting Substrings at Delimiters: `str.split` and `str.join`

Usually, we want to think of strings as collections of **tokens** separated by **delimiters**. **Token** is just a fancy way to say "meaningful word".

In English, the most common delimiter is the **space** (`" "`). Sometimes, like in URLs, we use other delimiters, like the **slash** (`"/"`).

In Python, there is a great way to deal with ordered sequences of tokens, or of any data - lists! How can we turn a `str` consisting of tokens separated by delimiters into a `list` consisting of only tokens?

#### Meet `split`!

Every `str` variable in Python carries with it some built-in functionality, like the `split` function.

>The `len` function was usable straight from Python. We can even type `len` <kbd>enter</kbd> and see the output `<built-in function len>` telling us that `len` **is defined**. On the other hand, the `split` function is part of a `str` variable, and we have to "reach inside" the variable to find the definition of `split` by using `.split` after the variable name of a string variable.

Split breaks apart a `str` and gives a `list`:


<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Split?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>



#### Meet `join`

Now, let's say we had a `list` of tokens and a delimiter and wanted to turn them into a `str`. We can do that using `str.join`. Like `split`, `join` is "part of" `str` variables, and cannot be called without one.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/strjoin?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>



#### Combining `split` and `join`


<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Split-and-Join-2?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>



### Formatting Strings: `.format`

We know that we can concatenate diferent `str` variables using the `+` operator, and we can combine tokens in a `list` with a delimiter using `str.join`.

Joining long strings with `+`, though, takes a lot of work, and even makes Python work much harder than it should, believe it or not. Plus, we can't easily concatenate `str` variables to other variables, like `int`s.

>Try `mystring = "hey" + 7`. We get `TypeError: must be str, not int`. And if we try `mystring = 7  "hey"` we get a different error message (butt the same error type, `TypeError`): `TypeError: unsupported operand type(s) for +: 'int' and 'str'`

Just like `str.split`, `str.join`, `str.upper`, and `str.capitalize`, let's think about another useful function contained in variables of type `str`: `str.format`.

In the previous example (about Malia Obama), we had a lot of text concatenated to our variables, but it didn't get its own variable. If we had to use that line `"I want to tell you about my " + relationship + ", " + name.upper() + ` many times, we would be doing more work than we need to in copying and pasting, and furthermore it's hard to read.

#### Formatting with Positional Arguments

If we know which parts of a string we'd want to insert another string into, we can create a string to use as a template, with holes in it ready to be filled by variables, using `format`:

```python
>>> name = "Zach"
>>> "Hi, {}".format(name)
'Hi, Zach'
```

Let's get just a bit more complicated:

```python
>>> myname = "Zach"
>>> friendname = "Samuel"
>>> "Hi, {}! My name is {}".format(friendname, myname)
'Hi, Samuel! My name is Zach'
```


It may not seem like a big deal, but this can save a lot of work. Observe the example from before, and try to understand how to use `format`:


<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/strformat?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


It is easier to read and manage a template without all those `+` operators in the way. Another advantage is that we can format in arguments that aren't of type `str`, like `"I have {} apples".format(5)`. The downside is that we have to remember to give all the data **in the right order**!

#### Formatting with Keyword Arguments

We can also use `format` with **keyword arguments**. The concepts of **arguments** and of keyword arguments will become more clear as soon as we cover functions. For now, just know that you can give arguments in any order, as long as you clearly label which argument means what.




<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/strformat-with-Keyword-Arguments?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


This may seem like a pain right now (why do we need to say `name = name`?!?), but it will become more clear later on, when we talk about **functions**.

#### Formatting with **Format String Literals**

Formatting strings is *such* a common task, that Python includes a special shortcut to do what we have just done: **format string literals**.

We use format string literals by using `f"` or `f'` at the beginning of our string, instead of just `"` or `'`. Any keyword variable names that are already defined will be formatted into the string, and we won't be left with a template, but a fully-formatted string.

You won't be expected to use this, but you can if you want to:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Format-String-Literals?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


### Automatically Upper-Casing and Lower-Casing: `str.upper`, `str.lower`, and `str.capitalize`

Python includes some useful functions to work with textual data. In particular, in English we care about capitalization, and Python can help.

* If we call `"hello".upper()`, the output will be `"HELLO"`. The `upper` function capitalizes every alphabetical character in the string.

* If we call `"HELLO".lower()"`, the output will be `"hello"`. The `lower` function makes every alphabetical character in the string lowercase.

* If we call `"hello".capitalize()`, the output will be `"Hello"`. The `capitalize` function capitalizes the first character in the string if it is alphabetical, and makes lowercase every other alphabetical character.

```python
>>> "hello".upper()
'HELLO'
>>> "hElLo".capitalize()
'Hello'
>>> "HELLO".lower()
'hello'
```


Not every letter can be capitalized, but `upper`, `lower`, and `capitalize` all affect alphabetical characters in a given string. This is very convenient, since **capital and lowercase letters are different characters completely** as far as computers know. Python's built-in functions contain information about the relationships between these characters.

Now we can revisit our "very re-usable" string code from earlier:

```python
>>> name = "Malia Obama"
>>> preferred_pronoun = "she"
>>> relationship = "classmate"
>>> role = "smartest person ever"
>>> place_of_employment = "my school"
>>> hobby = "build model figurines"
>>> future_role = "president...of NASA"
>>> print("I want to tell you about my " + relationship + ", " + name.upper() + ". " + preferred_pronoun.capitalize() + " is the " + role + " at " + place_of_employment + ". " + preferred_pronoun.capitalize() + " loves to " + hobby + ", and, someday, " + preferred_pronoun + " will be " + future_role + "!")
I want to tell you about my classmate, MALIA OBAMA. She is the smartest person ever at my school. She loves to build model figurines, and, someday, she will be president...of NASA!
```

Now we've fixed the capitalization of the first letters of the first words of sentences. Also, the `name` is made entirely uppercase, just for fun.

>The `len` function was usable straight from Python. We can even type `len` <kbd>enter</kbd> and see the output `<built-in function len>` telling us that `len` **is defined**. On the other hand, the `split`, `join`, `upper`, and `capitalize` functions are part of a `str` variable. More on that later.

### Line Breaks in Python: The **Newline** Character `\n`

When we press <kbd>enter</kbd> in the Python Interactive Shell, our command executes. When we type <kbd>enter</kbd> in a script (a `.py` file), we start typing our next command. So, how do we insert a **line break** in a Python string?

If we include the characters `\n` in a Python string, they will be interpreted as a single character, namely the **newline** character, which gives a line break.

```python
>>> print("\n\nMy name is Zach\nAnd I love typing.\nI love to pack\nLots of words on my screen.\n\n")


My name is Zach
And I love typing.
I love to pack
Lots of words on my screen.


>>>
```

Each time there's a `\n` character, Python prints a line break. This is an extremely useful character.

>**HTML also has a newline character**. In HTML, to send text to the next line, you have to use the `<br>` tag. A `.html` file is kind of like a big string ready to be formatted and printed. More on that later!

## Assignment

Create a template of a poem, print the poem with variables **for each of three people you know**. The poem must satisfy these requirements:

* **Obtain values from the people themselves by asking them**. For example, if one of your variables was `role`, you would ask someone "What is your role? It's for a poem." At least one variable for each person must be obtained this way. The others you can fill in yourself if possible.
* **Use at least five variables** that are each different for each person
* Your poem must have **at least four lines**. Use newline characters (`\n`) to accomplish this.
* **Use `str.format`** with either positional arguments (and `{}`) or keyword arguments (and `{variable_name}`)
* Save the code in a file called `poem.py`. **When you execute the code in this file using `python poem.py`, the poems should all print**. Nothing should print except the poems.
* **Be nice!** This should be fun for you and everyone who is part of your poems. Otherwise, they won't be part of your poems next time, and that won't be fun.
* **The poem does not have to make perfect sense!!** This is poetry, not science. However, they should make some sense and adhere to English grammar as much as possible.
* **HAVE FUN**


A sufficient file `poem_example.py` is in the `/code` folder of this repository. Run it using `python poem_example.py`. The same code can be run in here:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Poem-Example?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

