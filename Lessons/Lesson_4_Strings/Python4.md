# Python Lesson 4 - Strings (`str`)

## Review of Lesson 3

### Loops: `while`

To repeat some command or commands, we can place those commands in a `while` statement. The commands that are **indented** on the line after `while (some condition):` will be executed until `(some condition)` is false. Note that `(some condition)` has to evaluate to either `True` or `False` - that is, it must evaluate to a value with type `bool`.

Example:

```python
x = 0
while(x < 10):
	print(x)
	x = x + 1
```

will output

```python
0
1
2
3
4
5
6
7
8
9
```

### Types

We can find out the type of any variable by using the `type` function:

```python
x= 'hello'
type(x)
```
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

##### Concatenation is **Exact**

```python
x = "hey"
y = "my friend"
print(x + y)
```
You should see the output

```python
heymy friend
```
Oops - no space! Try this:

```python
print(x + " " + y)
```
That's more like it.

##### Concatenation Makes Code Re-Usable


```python
relationship = "friend"
action = "high-five"
print("You are my " + relationship + " and I can't wait to " + action + " you!")

relationship = "enemy"
action = "pour water on"
print("You are my " + relationship + " and I can't wait to " + action + " you!")
```
>Notice that we were able to re-use the line of code with the `print` statement!

Concatenation is one of the most important jobs most computer programs do. Just like the line of code we re-used, most websites just concatenate in a tiny snippet of data (like `title = "Watch This Cute Panda Eat Bamboo"`) to a bigger webpage.


Imagine how many ways we could use and re-use this code:

```python
name = "Malia Obama"
preferred_pronoun = "she"
relationship = "classmate"
role = "smartest person ever"
place_of_employment = "my school"
hobby = "build model figurines"
future_role = "president...of NASA"
print("I want to tell you about my " + relationship + ", " + name + ". " + preferred_pronoun + " is the " + role + " at " + place_of_employment + ". " + preferred_pronoun + " loves to " + hobby + ", and, someday, " + preferred_pronoun + " will be " + future_role + "!")
```

>Notice that the `preferred_pronoun` should be capitalized at the beginning of the last sentence. We will come back to that!

##### Concatenation is Fun

Try your parent's information!

```python
name = "[parent's name]"
preferred_pronoun = "[parent's preferred pronoun, like "he" or "she" or "they"]"
relationship = "parent [or 'father' or 'mother']"
role = "[their job, or skill, or just 'best parent ever']"
place_of_employment = "[where they do their work, or 'my home']"
hobby = "[their hobby]"
future_role = "very happy to see me become a computer scientist"
print("I want to tell you about my " + relationship + ", " + name + ". " + preferred_pronoun + " is the " + role + " at " + place_of_employment + ". " + preferred_pronoun + " loves to " + hobby + ", and, someday, " + preferred_pronoun + " will be " + future_role + "!")
```

Here's some input that tells you about my Dad:

```python3
name = "Lawrence Siegel"
preferred_pronoun = "he"
relationship = "Dad"
role = "psychiatrist"
place_of_employment = "New York's public mental health services"
hobby = "bike ride"
future_role = "even more proud of me than he is now"
```

### Substrings

We have seen how to combine little snippets into a longer string. How can we **extract** little snippets **from** a longer string?


Python offers intuitive ways to do this, and we will talk about three: **the `in` keyword**, **indexing** and **slicing**. You have seen that a `list` is a Python type that contains other Python variables (eg `x = [1,2,3,'hello']`). The ways we **index** and **slice** substrings of strings will prepare us for working with the `list` data type in an upcoming lesson.

##### The `in` Keyword

```python
name = 'Zach'
print('a' in name)
print('b' in name)
```

Why did we see `True` and then `False`? Didn't we ask to print "a" and "b"?

The `in` keyword allows us to check whether a string contains a given substring.

```python
name = "Zach"
if "a" in name:
	print("Your name contains an 'a'!")
elif "b" in name:
	print("Your name does not contain an 'a', but it contains a 'b'!")
else:
	print("Your name does not contain an 'a' or a 'b'!")
```

Try that with `name = "ben"` and `name = "Doris"`.

We can use `in` to check for more than single-letter substrings:

```python
story = "I love taking the bus! It gives me the freedom to travel around for very little money. Thanks to public resources like the bus, I know that no matter how tough a situation I'm in, I will survive and be able to do my job."
query = "the freedom"
print(query in story)
```

##### String Indexing and Slicing

Let's say we wanted to print the first letter of a middle name

```python
first_name = "Zach"
middle_name = "Edmund"
last_name = "Siegel"
print(first_name + " " + middle_name[0] + " " + last_name)
```

Great! Why did I have to print `middle_name[0]` and not `middle_name[1]` to get the **first** character of the `str` `"Edmund"`? Try `middle_name[1]` and `middle_name[2]`. Try `middle_name[n]` for all `n` between `0` and `5`.

>What happens when you execute `middle_name[6]`? Why?

Can we access more than a single character using indexing? Yes, and when we do, it is called **slicing**.

```python
middle_name = "Edmund"
print(middle_name[0:3])
```

When you see `0:3`, you might expect the characters at indices `0`, `1`, `2`, and `3` to be printed. However, we only saw `0`, `1`, and `2`. **Slicing is non-inclusive**, meaning the last index in a slice is not part of that slice.

>Part of why computer scientists like non-inclusive slicing is so that the **length** of a string (or list) is clear. If the first index is `0`, and the last index is `5`, then there are a total of `6` characters in `middle_name`. Looking at `middle_name[0:6]`, we know that (in Math) 6-0=6, so the slice `[0:6]` should have 6 characters, which is all of them. Similarly, `middle_name[1:6]` has 6 - 1 = 5 characters.

We know the last index of `"Edmund"` is `5`, so, since slicing is non-inclusive, we can get the entirety of our string using middle_name[0:6].

### Finding the **Length** of a String: The `len` Keyword

To find the number of characters in a `str` (or the number of elements in a `list`), we can use the `len` function:

```python
print(len("hello"))
print(len("Zach"))
print(len([1,2,3]))
```

Usually, we use `len` to provide a number that will be used as an index. Remember, **the number of characters in a `str` (which `len` tells us) is one greater than the highest index because indexing starts at 0**.

>In a `str` called `mystring`, the last character is `mystring[len(mystring)-1]`.

Here are some uses of `len`. Suppose we first created the variables `category`, `prices` and `names`:

```python
category = "phones"
prices = [100, 200, 1000, 600, 700]
names = ["Nokia NK100", "LG vx1100", "iPhone X", "iPhone 7", "Google Pixl"]
```

| Code | Value | Explanation|
|:-------|:----|:----|
|`category[len(category)-1]` | `"y"` | The last character in a string called `mystring` has index `len(mystring)-1`|
|prices[len(prices)-1] |`700` | The last element of a `list` called `mylist` has index `len(mylist)-1`|
|`names[len(names)-1]`|`"Google Pixl"` | Another `list` - this time a `list` of `str` variables|
|`len(names[len(names)-1])`| `11` | `names[len(names)-1]` is the last element of `names`, which is `"Google Pixl"`. The `len("Google Pixl")` is `11`|
|`names[0][0]` | `"N"` | The element of `names` at index `0` is `"Nokia NK100"`. The character at index `0` in `"Nokia NK100"` is `"N"`|
|`names[len(names)-1][len(names)-1]` | `"l"` | The last character of the last element of `names` is the last letter of `"Google Pixl"`, which is `"l"`|

### Accessing the Last Element: the `[-1]` Shortcut

##### Indexing with `[-1]`

Finding **the last** element of a `list` or character of a `str` is **so** common in python that there is a special shortcut to access it.

Instead of typing `mystring[len(mystring)-1]` or `mylist[len(mylist)-1]` we can just type `mystring[-1]` or `mylist[-1]` to access the last element of a `str` or `list`.

```python
mystring = "Zach"
mylist = ["Zach", "Susan", "Lawrence"]
print(mystring[-1])
print(mylist[-1])
```

Notice that the index `-1` gives the exact same result as `len(mystring)-1`.

##### Slicing with `:-1`

We can also use a `-1` in a slice to access **all elements through the final element**.

>Remember that slicing is **non-inclusive**, meaning that a slice ending in `-1` will not include the `-1` element, which is the final element.

```python
myname = "Zachary Edmund Siegel"
print(myname[0:-1])
```
You should see `Zachary Edmund Siege`.

In fact, **slices can include any negative numbers, which refer to the index of a given number of elements from the end of the list**.

```python
myname = "Zach"
print(myname[-4])
print(myname[1:-2])
```

### Splitting Substrings at Delimiters: `str.split` and `str.join`

Usually, we want to think of strings as collections of **tokens** separated by **delimiters**. **Token** is just a fancy way to say "meaningful word".

In English, the most common delimiter is the **space** (`" "`). Sometimes, like in URLs, we use other delimiters, like the **slash** (`"/"`).

In Python, there is a great way to deal with ordered sequences of tokens, or of any data - lists! How can we turn a `str` consisting of tokens separated by delimiters into a `list` consisting of only tokens?

##### Meet `split`!

Every `str` variable in Python carries with it some built-in functionality, like the `split` function.

>The `len` function was usable straight from Python. We can even type `len` <kbd>enter</kbd> and see the output `<built-in function len>` telling us that `len` **is defined**. On the other hand, the `split` function is part of a `str` variable, and we have to "reach inside" the variable to find the definition of `split` by using `.split` after the variable name of a string variable.


The input:

```python
"hello, my name is Zach, and I love coffee and chocolate.".split(" ")
```
outputs

```python
['hello,', 'my', 'name', 'is', 'Zach,', 'and', 'I', 'love', 'coffee', 'and', 'chocolate.']
```

##### Meet `join`

Now, let's say we had a `list` of tokens and a delimiter and wanted to turn them into a `str`. We can do that using `str.join`. Like `split`, `join` is "part of" `str` variables, and cannot be called without one.

```python
" ".join(['hello,', 'my', 'name', 'is', 'Zach'])
```
outputs `'hello, my name is Zach'`


##### Combining `split` and `join`

Observe the following:

```python
" ".join("google.com/I/love/bananas/so/much!".split("/"))
```

Using `list` slicing, we can extract just the arguments of a URL without a domain:

```python
" ".join("google.com/I/love/bananas/so/much!".split("/"))
```


### Automatically Upper-Casing: `str.upper` and `str.capitalize`

Python includes some useful functions to work with textual data. In particular, in English we care about capitalization, and Python can help.

* If we call `"hello".upper()`, the output will be `"HELLO"`. The `upper` function capitalizes every alphabetical character in the string.

* If we call `"hello".capitalize()`, the output will be `"Hello"`. The `capitalize` function capitalizes the first character in the string if it is alphabetical (otherwise, it does nothing).

Not every letter can be capitalized, but `upper` and `capitalize` both can affect alphabetical characters in a given string. This is very convenient, since **capital and lowercase letters are different characters completely** as far as computers know. Python's built-in functions contain information about the relationships between these characters.

Now we can revisit our "very re-usable" string code from earlier:

```python
name = "Malia Obama"
preferred_pronoun = "she"
relationship = "classmate"
role = "smartest person ever"
place_of_employment = "my school"
hobby = "build model figurines"
future_role = "president...of NASA"
print("I want to tell you about my " + relationship + ", " + name.upper() + ". " + preferred_pronoun.capitalize() + " is the " + role + " at " + place_of_employment + ". " + preferred_pronoun.capitalize() + " loves to " + hobby + ", and, someday, " + preferred_pronoun + " will be " + future_role + "!")
```

Now we've fixed the capitalization of the first letters of the first words of sentences. Also, the `name` is made entirely uppercase, just for fun.

>The `len` function was usable straight from Python. We can even type `len` <kbd>enter</kbd> and see the output `<built-in function len>` telling us that `len` **is defined**. On the other hand, the `split`, `join`, `upper`, and `capitalize` functions are part of a `str` variable. More on that later.


### Formatting Strings: `.format`

We know that we can concatenate diferent `str` variables using the `+` operator, and we can combine tokens in a `list` with a delimiter using `str.join`.

Joining long strings with `+`, though, takes a lot of work, and even makes Python work much harder than it should, believe it or not.

Just like `str.split`, `str.join`, `str.upper`, and `str.capitalize`, let's think about another useful function contained in variables of type `str`: `str.format`.

In the previous example (about Malia Obama), we had a lot of text concatenated to our variables, but it didn't get its own variable. If we had to use that line `"I want to tell you about my " + relationship + ", " + name.upper() + ` many times, we would be doing more work than we need to in copying and pasting, and furthermore it's hard to read.

##### Formatting with Positional Arguments

If we know which parts of a string we'd want to insert another string, we can create a string to use as a template, with holes in it ready to be filled by variables, using `format`:

```python
name = "Zach"
"Hi, {}".format(name)
```

It may not seem like a big deal, but this can save a lot of work. Observe the example from before, and try to understand how to use `format`:

```python
name = "Malia Obama"
preferred_pronoun = "she"
relationship = "classmate"
role = "smartest person ever"
place_of_employment = "my school"
hobby = "build model figurines"
future_role = "president...of NASA"

template = "I want to tell you about my {}, {}. {} is the {} at {}. {} loves to {}, and, someday, {} will be {}!"

print(template.format(relationship,name.upper(),preferred_pronoun.capitalize(),role,place_of_employment,preferred_pronoun.capitalize(),hobby,preferred_pronoun,future_role))
```

It is easier to read and manage a template without all those `+` operators in the way. The downside is that we have to remember to give all the data **in the right order**!

##### Formatting with Keyword Arguments

We can also use `format` with **keyword arguments**. The concepts of **arguments** and of keyword arguments will become more clear as soon as we cover functions. For now, just know that you can give arguments in any order, as long as you clearly label which argument means what.


```python
name = "Malia Obama"
preferred_pronoun = "she"
relationship = "classmate"
role = "very smart person"
hobby = "build model figurines"

template = "I want to tell you about my {relationship}, {name}. {name} is a {role}, but {preferred_pronoun} really loves to {hobby}. {preferred_pronoun} is one of my favorite people in the world, because {preferred_pronoun} is kind."

print(template.format(name=name,relationship=relationship, role=role,preferred_pronoun=preferred_pronoun,hobby=hobby))
```

This may seem like a pain right now (why do we need to say `name = name`?!?), but it will become more clear later on, when we talk about **functions**.

##### Formatting with **Format String Literals**

Formatting strings is *such* a common task, that Python includes a special shortcut to do what we have just done: **format string literals**.

We use format string literals by using `f"` or `f'` at the beginning of our string, instead of just `"` or `'`. Any keyword variable names that are already defined will be formatted into the string, and we won't be left with a template, but a fully-formatted string.

You won't be expected to use this, but you can if you want to:

```python
name = "Zach"
pronoun = "he"
occupation = "tutor"
hobby = "running"
print(f"{name} works as a {occupation}. {pronoun} loves {hobby}.")
```

### Line Breaks in Python: The **Newline** Character `\n`

When we press <kbd>enter</kbd> in the Python Interactive Shell, our command executes. When we type <kbd>enter</kbd> in a script (a `.py` file), we start typing our next command. So, how do we insert a **line break** in a Python string?

If we include the characters `\n` in a Python string, they will be interpreted as a single character, namely the **newline** character, which gives a line break.

```python
print("\n\nMy name is Zach\nAnd I love typing.\nI love to pack\nLots of words on my screen.\n\n")
```

Each time there's a `\n` character, Python prints a line break. This is an extremely useful character.

>**HTML also has a newline character**. In HTML, to send text to the next line, you have to use the `<br>` tag. A `.html` file is kind of like a big string ready to be formatted and printed. More on that later!

## Assignment

1. Create a template of a poem, print the poem with variables **for each of three people you know**. The poem must satisfy these requirements:
	* **Obtain values from the people themselves by asking them**. For example, if one of your variables was `role`, you would ask someone "What is your role? It's for a poem." At least one variable for each person must be obtained this way. The others you can fill in yourself if possible.
	* **Use at least five variables** that are each different for each person
	* Your poem must have **at least four lines**. Use newline characters (`\n`) to accomplish this.
	* **Use `str.format`** with either positional arguments (and `{}`) or keyword arguments (and `{variable_name}`)
	* Save the code in a file called `poem.py`. **When you execute the code in this file using `python poem.py`, the poems should all print**. Nothing should print except the poems.
	* **Be nice!** This should be fun for you and everyone who is part of your poems. Otherwise, they won't be part of your poems next time, and that won't be fun.

	A sufficient file `poem_example.py` is in the `/code` folder of this repository. Run it using `python poem_example.py`.


