# Python Lesson 8 - Input and Challenges

[TOC]

## Input: `input()`

There are some functions that we can always access: `len`, `type`,

## Assignment

1. Create a `cat` class and a `human` class. Give both classes a field called `happiness`. Create dynamic methods in the `cat` class called `snuggle` and `scratch` that take a `human` parameter. Create dynamic methods in the `human` class called `snuggle` and `scold` that take a `cat` parameter.

	After calling `snuggle` from either class, the `happiness` field of both the `human` and the `cat` instance involved should increase by 1. After calling `scratch` and `scold`, the happiness field of both the `human` and the `cat` instance involved should decrease by 1.

	Your script should create two `Human` instances and two `Cat` instances. They should `snuggle`, `scold`, and `scratch` each other and at the end, both `Human` instances should have `happiness` equal to `0`, but one `Cat` should have `happiness` equal to `2`, and one should have `happiness` equal to `-2`.


	<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/Classhumancat?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

	Save your work in a file called `humans_and_cats.py` or fork the repl.it script above.
