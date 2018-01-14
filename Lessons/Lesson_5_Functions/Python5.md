# Python Lesson 5 - Functions (`def`)

[TOC]

## Review of Lesson 4

### String Indexing, Slicing, Concatenating, and `.format`

>You should understand all the code in the following snippet

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/StringReview?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

## Python Functions: `def`

We have seen functions before:

* `len` tells us the **length** of a `list` or `str` variable.
* `print` writes stuff onscreen

Let's create our own functions! We use the `def` keyword to signal that we're defining a function:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions1?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

What happens when we run this code? Seemingly nothing! Why? We have to **call** the function we created to execute the code we used in its definition:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions2?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>




### "**Don't Repeat Yourself**" (the **DRY** Principle)

We have seen how concatenation makes code re-usable. Functions are all about re-usability.

Think about how much code the following function saves us:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions3?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


### Function Arguments and Parameters

What if we want a function to behave differently at different times? We can give a function **arguments** that it will use as **parameters** to perform its functions.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions4?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Note that we were able to call `feet_and_a_half(5)` or `feet_and_a_half('five')` with no errors! That's because our function worked fine with either `int` or `str` input. Python is a language that uses what's called **Duck Typing**, meaning "if the input works, it doesn't matter what **type** it is". The term "Duck Typing" comes from the phrase "if it walks like a duck and quacks like a duck, it's probably a duck".

#### Positional Arguments and Parameters

If a function has multiple parameters, the order the arguments are written in parentheses when you **call** the function is the order they will be matched with parameters in a function definition:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions5positionalarguments?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

But what if our arguments are variables with names - don't they get matched to the correct arguments?

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions5positionalarguments2?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

**NOPE**! The order in which arguments are given is the only thing that affects which argument is assigned to which function parameter:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions5positionalarguments3?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

When a Python function receives arguments, each **argument** takes on the **name** of the **parameter** corresponding to the position in which it was given. Within the function, that parameter has its own variable name. Taking on a different name inside a function versus outside the function is called **scope**.

>The **scope** of a variable is the environment in which its name refers to that variable. So far, we have seen variables **outside** functions, and variables given as arguments to functions, which stand in as the function's paramaters **inside** functions. The word **scope** will come up again and again!


#### Keyword Arguments and Parameters

>What if we want to **name** which argument gets assigned to which parameter?

We can specify which argument gets matched with which function parameter if we know the names of the function parameters.

When we write `a_inside = a_outside` we are saying that the function parameter `a_inside` should be assigned the value of the argument `a_outside`.



<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions5keywordarguments?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Try switching the last line to
	```python
	print_two_things(a_inside=1,b_inside=2)
	```
	Notice that the order doesn't matter!

#### Default Arguments and Parameters

Suppose we want to create a function that prints `10` every time we call it, unless we specify something else? In that case, `10` could be a **default parameter**.


<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions6defaultarguments?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


We can always **override** default function parameters by supplying our own values.

#### Mixture of Positional, Keyword, and Default Arguments

When a function is taking some positional arguments and some keyword arguments, there are a few things to be careful of. Python needs to clearly know which argument should be assigned to which function parameter.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Function6positionalandkeyword?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


**Positional arguments and parameters always come *before* keyword arguments and parameters**.

When you're calling a function, positional arguments and parameters always have to be written before keyword arguments and parameters. When you're defining a function, parameters with default values have to be written before parameters without default values.

THIS DOESN'T WORK:
```python
def print_two_things(a,b=2):
	print("a is: {}".format(a))
	print("b is: {}".format(b))
```

### Functions are Defined Only **Once**

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions7defaultdynamicargument?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

If we give a function a **dynamic** default parameter, meaning one that is generated rather than pre-set, it will be evaluated when the function is defined, not every time the function is called.


### Return Statements: `return`

When we call `len`, we *get something* out of it. We can even assign the output of `len` to a variable: `x = len(y)` and store whatever value `len` produces in a variable. Would `x=print(y)` make sense, though? No, because `print` doesn't **return** anything.

So far each of our functions has done some calculation, then executed a `print` statement. But functions don't have to `print` anything in order to be useful!

If a function includes a `return` statement, then when we call the function, we can store the value of whatever expression follows the keyword `return` in some other variable, and then access it outside the function. This is how we pass values from one "scope" to another.


<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions8return?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

### "Functions are First Class Citizens"

Why does this work?

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions9firstclasscitizens?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

It works because **functions are "first class citizens"**.

Python can interpret `'hello ' + 'dude'` and `5 + 6`, even though `+` is doing very different things in both cases. In the case of `yourfunction = myfunction`, Python is doing slightly more than when we type `x = 5`, but the idea is the same: Python creates a "name" and makes sure it refers to the correct thing, stored somewhere in memory. In this case the correct "thing" is the definition of a function.


### Recursion: Functions Calling Themselves

We saw that a `while` loop executes over and over until some "stopping condition" is met:

```python
counter = 1
while (counter < 10):
	print(counter)
	counter = counter + 1
```

Note that on each iteration we needed to *increase* `counter` by `1` and *test* whether `counter < 10`. If we didn't increase `counter` on each iteration, the loop would never end; if we didn't *test* counter on every iteration, the loop would never end (`while` takes care of that for us).

Another way we can achieve iteration is **recursion**. That is the term we use for *a function calling itself*.

Just like a `while` loop, successful recursion needs a **stopping condition**, and it needs to be met. Otherwise, like an **infinite loop**, we can create **infinite recursion**, which never ends and fails to achieve our goals.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions9recursion?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


## Assignment

1. Create a function that returns the maximum of two numbers.

	```python
	def max(a,b):
		#your code here
	```
	Your code should satisfy the following:
		* `max(1,2)` returns  `2`
		* `max(2,1)` returns `2`
		* `max(2,2)` returns `2`

	Save your work in a file called `max.py`.

2. Factorials! The **factorial** of an integer is the product of all the positive integers less than or equal to that integer:

	* 1!									= 1
	* 2! = 1 * 2					= 2
	* 3! = 1 * 2 * 3			= 6
	* 4! = 1 * 2 * 3 * 4 	= 24
	* n! = 1 * 2 * 3 * ... * (n-1) * n

	Create a recursive function that returns the factorial of a number. It's started for you.

	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Factorial?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


	* `factorial(5)` should return `120`
	* `factorial(6)` should return `720`

	>HINT: You know n! is the product of 1 through n. Similarly, (n-1)! is the product of 1 through (n-1). Another way to think about this is that n! is n times (n-1)!.

	Save your work in a file called `factorials.py`.
