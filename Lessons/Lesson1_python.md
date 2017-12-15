# Lesson 1: Python


## Running Python

You are ready to run Python! Your computer's Python installation can run in two important ways:

### 1. Running Python Code Written in `.py` Files

Python can execute Python code, which is written in `.py` files, such as `app.py`. If you write code in a `.py` file called `app.py`, you can tell Python to run __all__ the code with the following command (without typing `>>`):

			>> python app.py

This command tells Python to execute every line of code written in the `app.py` file. Try running this command and, if there are no error messages, navigate to [localhost](localhost:5000).

### 2. Running Python Code in the Interactive Console

Python has an "Interactive Console" called the "Python Interactive Console".

Any Python commands can be executed one at a time by writing them in the command prompt and hitting the <kbd>Enter</kbd> key. This is called a __Read-Evaluate-Print-Loop (REPL)__ environment, because it "reads" your input, "evaluates" it, "prints" the output, and then "loops" by starting the process over again.


__Type `python` to start the Python interactive console.__ Then try the following Python commands:

* `x=5` to create a variable named `x` with the value `5`.
	* `x = 5` will also work. Spaces (made with the <kbd>spacebar</kbd>) are known as __whitespace__, and are generally ignored by Python.
* `print(x)` to print the value of `x`
	* `x` (on its own) is another way to say `print(x)`, but this only works in the interactive shell.
* `print(x+1)`
	* `x+1` (on its own) will also work.
* `y = "Eitan"`
	* (why did we need quotes around `Eitan` but not around the number `5`?)
* `z = "Zach"`
* `w = y`
* `print(y + z)`
	* How is this different from `print(x + 1)`? How is it the same?
* `print(y + " " + z)`




## First Python Script

Create a file called __loops.py__ and open it in your favorite text editor (SublimeText is reccommended).

In this file, add the following code:

	x = 5
	print(x)

Now, navigate to the folder containing this file and type in your command line

	python loops.py

You should see the following output:

		>> 5

