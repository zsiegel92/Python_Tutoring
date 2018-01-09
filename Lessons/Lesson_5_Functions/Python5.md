# Python Lesson 5 - Functions (`def`)


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


#### Positional Arguments

If a function has multiple parameters, the order the arguments are written in parentheses when you **call** the function is the order they will be matched with parameters in a function definition:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions5positionalarguments?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

But what if our arguments are variables with names - don't they get matched to the correct arguments?

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions5positionalarguments2?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

**NOPE**! But what if we want that behavior?


#### Keyword Arguments

We can specify which argument gets matched with which function parameter if we know the names of the function parameters.

When we write `a_inside = a_outside` we are saying that the function parameter `a_inside` should be assigned the value of the argument `a_outside`.



<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Functions5keywordarguments?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Try switching the last line to
	```python
	print_two_things(a_inside=1,b_inside=2)
	```
	Notice that the order doesn't matter!

#### Default Arguments

### Return Statements













## Assignment

Create a template of a poem, print the poem with variables **for each of three people you know**. The poem must satisfy these requirements:

* **Obtain values from the people themselves by asking them**. For example, if one of your variables was `role`, you would ask someone "What is your role? It's for a poem." At least one variable for each person must be obtained this way. The others you can fill in yourself if possible.
* **Use at least five variables** that are each different for each person


A sufficient file `poem_example.py` is in the `/code` folder of this repository. Run it using `python poem_example.py`. The same code can be run in here:
