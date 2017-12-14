## Hi, Eitan,

This will be your first website. This will also be your first time running code from the command line. There are a few things to keep in mind:

1. NEVER delete files from the command line unless they are files you created. If you delete a file that Windows needs, Windows may start malfunctioning.
2. Only use commands that you have learned from me (Zach) or from sources that I have introduced myself.
3. Feel free to ask questions about anything that you don't understand! There is a very good reason why everything is the way it is, and if I don't know, I will do my best to find out for you. If you are with your parents and not me, please ask them to ask me - I will respond to messages from them within a few hours.


## Getting Started with the "Webapp" Project
Before getting started, you have to take care of a few things:

1. Download our project from [the GitHub repository I made](https://github.com/zsiegel92/Eitan_S)
	* Click the green "Clone or download" button and "Download Zip"

2. Navigate to the the folder with the download, "unzip" the .zip file, and go into the folder. These are the commands you will need to navigate using the command line (press <kbd>Enter</kbd> after typing each command):
	* Type `cd` to see what folder you are in.
	* Type `cd [folder name]` to navigate to a specific folder.
	* Type `cd ..` to navigate up one folder (into the condaining folder)
	* Type `ls` to list all the files and folders in the folder you are in.
	* Type `ls -AL` to list all the files and folders in the folder you are in, INCLUDING the hidden folders, which begin with a dot (such as `.env`).

3. When you are in the folder called `webapp`, type the command
            `/venv/Scripts/activate`
This command tells your computer "hey, I'm working on the `webapp` project, so if I install anything, please don't let it affect the rest of my computer."

## Running Python

You are ready to run Python! Your computer's Python installation can run in two important ways:

#### Running Python Code Written in `.py` Files

1. Python can execute Python code, which is written in `.py` files, such as `app.py`. If you write code in a `.py` file called `app.py`, you can tell Python to run __all__ the code with the following command (without typing `>>`):

			>> python app.py

This command tells Python to execute every line of code written in the `app.py` file.

#### Running Python Code in the Interactive Console

2. Python has an "Interactive Console" called the "Python Interactive Console".

	Any Python commands can be executed one at a time by writing them in the command prompt and hitting the <kbd>Enter</kbd> key. This is called a __Read-Evaluate-Print-Loop__ environment, because it "reads" your input, "evaluates" it, "prints" the output, and then "loops" by starting the process over again.


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

