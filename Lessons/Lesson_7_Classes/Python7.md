# Python Lesson 7 - Object Classes (`class`)


## Review of Lesson 6

### Lists, Iteration, and Input

>You should understand all the code in the following snippet


## Python Classes: `class`

In Python, we have considered the following concepts:

* **Variables**, each of which has a *type*
	* We create variables just by declaring a variable name and assigning it using the assignment operator `=`
	* Example:
		```python
		>>> x=5
		>>> type(x)
		<class 'int'>
		```
* **Functions**, which are also variables (*First Class Citizens*)
	* We create functions by using the `def` keyword
	* Example:
		```python
		>>> def my_function(a,b):
		...     print("a is: {}, b is: {}".format(a,b))
		...     return a + b
		...
		>>> print("returned value is: {}".format(my_function(1,2)))
		a is: 1, b is: 2
		returned value is: 3
		>>>
		>>> type(my_function)
		<class 'function'>
		```




## Assignment

1. Do some stuff

	Save your work in a file called `max.py`.
