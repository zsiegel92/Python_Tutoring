# Python Lesson 7 - Object Classes (`class`)

[All Lessons](https://zsiegel92.github.io/Eitan_S/)

[TOC]

## Review of Lesson 6

### Lists, Iteration

You should understand all the code in the following snippet

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/ListsReview?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


If you don't understand **for loops**, **`append`**, **`join`**, or **string multiplication**, please refer to [**Lesson 6**](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_6_Lists/Python6.html).


## Python Classes: `class`

In Python, we have seen variables of several **types**:

* **Variables**, each of which has a *type*
	* We create variables just by declaring a variable name and assigning it using the assignment operator `=`
	* Example: `int` variables
		```python
		>>> x=5
		>>> type(x)
		<class 'int'>
		```
	* Example: *functions are variables* with a **type**
		```python
		>>> def my_function(a,b):
		...     return a + b
		...
		>>> type(my_function)
		<class 'function'>
		```

**What if we want to create *our own `type`* of variable?**

We can define a new type of variable using the `class` keyword:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Class?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Note that we the variables we created have type `Dog`!

We have created a new **class** called `Dog`. The variables we created, like all Python variables, are **objects** of type `Dog`, which just means that all Python variables come from some `class` definition, which the `type` function tells us about.

### Initializing Object Variables by "Calling" the Class

When we create `int` or `str` variables, we just write `x = 5` or `x = 'hey'`. When we typed `my_dog = Dog()`, why did we need the `()`?

The answer is that `int` and `str` variables are so common that Python has special ways of dealing with them. However, the ability to create your own variable types is the  defining feature of **Object-Oriented Programming**, which is what we do in Python.

Normally, when we define a **class**, *we get a freebie function with the same name as the class, which **returns** a variable whose **type** is the class name*.

If we want to create a `Dog` object variable, we can call the function `Dog()` (which takes no arguments).

We can create custom initialization behavior by defining a function called `__init__`. More on that later.

### Object Variables: Fields

Notice that our class definition included some variables:

```python
class Dog:
	number_legs = 4
	number_eyes = 2
	smell = "good"
```

We were able to access these by creating a `Dog` variable `my_dog = Dog()`, and then using a `.` such as `my_dog.number_legs` (returned `4`).

Variables that are "part of" an object variable are called the object's **fields**.

Once we create an object, *we can change its fields*.

```python
class Dog:
	number_legs = 4
your_dog = Dog()
your_dog.number_legs = 3
print(your_dog.number_legs) # prints 3
```

Incredibly, we can also access fields that aren't associated with a `Dog` *variable*, but are associated with the `Dog` *class*:

```python
>>> class Dog:
...     number_legs = 4
...
>>> print(Dog.number_legs)
4
```

### Object Functions: Methods and `self`

We can give objects their own functions, just like we can give them their own variables. These are called **object methods**.

Just like **object fields**, **object methods** can be associated with object variables, which we call ***instances** of an object* (like `my_dog.bark()` and `your_dog.bark()`), or they can be associated with the class itself (like `Dog.bark()`).

*Fields and methods associated with a **class** (and not an **instance**) are called **static**.*

*Fields and methods associated with an **instance** of an object are called **instance methods** and **instance fields** (sometimes **dynamic methods** and **dynamic fields**).*

In this snippet, there is a **static method** called `static_bark` and an **instance method** called `instance_bark`.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Classmethods?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

**What is with the `self` parameter in `instance_bark`?** We didn't use the parameter `self` in the function `instance_bark`, and we didn't provide an argument `self` when we called `my_dog.instance_bark()`. For now, just think of the `self` parameter as a way to tell Python that this method can only be called from an **instance** of the `Dog` object, rather than that **class** `Dog`.

### Accessing the Fields of an Instance of an Object

#### Accessing Fields Inside Object Methods: `self`

We've seen that we can create `Dog` instances, and each instance can have different **fields** (like `number_legs`). We can give `Dog` an **instance method** to tell us about itself:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Classinstancevariablesself?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Notice that when we accessed the `smell` field from *outside* the class `Dog`, we used `my_dog.smell`, but when we accessed it from *inside* the class `Dog` (in `smart_bark`) we used `self.smell`. That's because **`self` refers to the object instance**.

#### Accessing Fields Outside the Class Definition

We have already talked about the **scope** of variables *inside* and *outside* functions (sometimes those can be called **global scope** and **local scope**).

Similarly, each object instance gets its own **scope**.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Classinstancevariablesexternal?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

We were able to create a variable `my_dog.breed` even though the `Dog` object has no field called `breed`. In the **scope** of the **object instance** `mydog`, we created a variable called `breed`. This becomes an **object field** of `mydog`, but not of `Dog` variables elsewhere.

If we try to access a field that an object instance does not have, like `your_dog.breed`, we get an `AttributeError`.

#### Dynamic Fields vs Static Fields

We know how to access **static** fields (associated with a **class**) and **dynamic fields** (associated with an **instance**), but if we change these fields, which one takes precedence?

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Classinstanceclasscollission?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Notice that we changed `my_dog.smell` as though `smell` were a **dynamic field**, but then we changed `Dog.smell` as though `smell` were a **static field**. When we changed `Dog.smell`, somehow the instance field `yourdog.smell` was changed along with it!

***Question**:* When we changed `Dog.smell`, why didn't `my_dog.smell` get changed as well?

***Answer**:* When we alter a dynamic field, the field we altered on an object instance replaces the class field, and we can no longer access the class field. If we leave the instance's fields alone, they refer to the class's fields.

Sometimes this becomes confusing, so define your classes with care.

### Objects Interact with Each Other

Consider two `Dog` instances getting in a fight. How would we simulate this? Observe:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Classobjectsinteracting?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>



## Assignment

1. Create a `cat` class and a `human` class. Give both classes a field called `happiness`. Create dynamic methods in the `cat` class called `snuggle` and `scratch` that take a `human` parameter. Create dynamic methods in the `human` class called `snuggle` and `scold` that take a `cat` parameter.

	After calling `snuggle` from either class, the `happiness` field of both the `human` and the `cat` instance involved should increase by 1. After calling `scratch` and `scold`, the happiness field of both the `human` and the `cat` instance involved should decrease by 1.

	Your script should create two `Human` instances and two `Cat` instances. They should `snuggle`, `scold`, and `scratch` each other and at the end, both `Human` instances should have `happiness` equal to `0`, but one `Cat` should have `happiness` equal to `2`, and one should have `happiness` equal to `-2`.


	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Classhumancat?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	Save your work in a file called `humans_and_cats.py` or fork the repl.it script above.
