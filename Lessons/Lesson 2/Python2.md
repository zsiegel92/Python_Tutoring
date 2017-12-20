# Python Lesson 2

## Running Python

#### Running Python Scripts (`something.py`)

Use `cd` and `dir` to navigate to the folder containing a Python file with the `.py` extension. Type `python filename.py` to execute all the Python commands in the `.py` file.

#### Running the Python Interactive Console (REPL)

Type `python` <kbd>enter</kbd> from the command prompt at any time to open the Python Interactive Console, which will **R**ead **E**valuate **P**rint and **L**oop as you provide commands.

## Lesson 1: `if`, `while`, and Variable Types

Open the Python Interactive Console by typing `python`<kbd>enter</kbd> in the command prompt.

Create a variable named `x` storing the value `5`. Then, print the variable.

```python
x = 5
print(x)
```

Now, change the value of `x` and print the new value.

```python
x = 'hello'
print(x)
```

Wouldn't you say that the value `'hello'` and the value `5` are fundamentally different? That's because they have different **type**. Check the type of `x` with the following assignments:

```python
x = 5
print(type(x))
```
```python
x = 'hello'
print(type(x))
```
```python
x = [1,2,3]
print(type(x))
```
```python
x = 1.5
print(type(x))
```

