# Python Lesson 4 - Strings

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
hobby = "invent amazing things for everyone to see"
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

Here's the information I'd input to tell you about my Dad:

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



