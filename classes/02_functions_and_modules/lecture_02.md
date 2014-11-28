# Functions and Modules

## Functions

#### Defining a Function

A function is a handy way to encasuplate a piece of logic that needs to be performed repeatedly or made more portable.

    def say_hi():
        print('Hi!')

The structure of a function definition is:

    def FUNCTION_NAME(arg1, arg2, ..., kw1=v1, kw2=v2, ...):
        FUNCTION_BODY

The `argX` above are function arguments, and they are required (the order is important). The `kwX` above are keywords, but they are optional (the order is unimportant; the valuess are defaults).

Function names can be almost anything, but they have a few restrictions:

- contain only numbers, letters, underscores
- do not start with a number
- are not the same name as a built-in function (like `print`)

#### Example Functions

Let's look at some simple example functions. First, we'll create a trivial function to add a couple numbers:

    >>> def addnums(x, y):
        return x + y

And now let's use the function:

    >>> addnums(2, 3)
    5
    >>> addnums("a", "b")  # Wait, what?
    ab
    >>> addnums("cat", 23232)
    TypeError: cannot concatenate 'str' and 'int' objects

What we see is that the function works as expected for numbers, but since Python is a *dynamic* language, it doesn't stop you from trying to add a `string` and an `integer`. Of course, you can't add these, so a type error is thrown. This is part of the Python "we're all consenting adults" philosophy; you are trusted to know what you're doing.

Let's see that same example with key word arguments:

    >>> def addnums(x, y=2):
        return x + y
    >>> addnums(3)
    5
    >>> addnums(3, y=3)
    6
    >>> addnums("oops")
    TypeError: cannot concatenate 'str' and 'int' objects

#### Scope

The [scope](https://en.wikipedia.org/wiki/Scope_%28computer_science%29) of a variable is where the name of that variable is accessable from. Inside a function, Python keeps a local variables list. Below, `x` is not modified globally, so its scope is just inside the `times_pi` function:

    >>> def times_pi(x, y):
        x *= 3.14
        return x + y
    >>> x = 1
    >>> print(times_pi(x, 3))
    6.14
    >>> print(x)
    1

#### Documentation

**Documentation**: Just the right thing to do and Python makes it dead simple.

![docstrings](../../resources/glorious_docstrings.png)

**Docstring**: The first unassigned string in a function (or class, method, program, etc.). Here is a nice example of a helpful docstring for the function `numop1`:

    def numop1(x,y,multiplier=1.0,greetings="Thank you for your inquiry."):
        """
            Purpose: does a simple operation on two numbers.\n
            Input: We expect x,y are numbers multiplier is also a number
            
            (a float is preferred) and is optional.
            It defaults to 1.0. You can also specify a small greeting as a string.\n
            Output: return x + y times the multiplier
        """
        if greetings is not None:
            print(greetings)
            return (x + y)*multiplier

If we copy the Python code for `numop1` into a file, say `super_happy_fun_nums.py`, we can go to the command line and type `pydoc -w super_happy_fun_nums` and you will create a nicely-formmated HTML file with all the documentation for the functions in that file:

![docstrings](../../resources/docstring_screencap.png)

## Modules

Up until the docstring example above, you could have done all of the work for this class in the interpreter. But when you quit the interpreter, all of the variables and functions you have defined are lost. Another option is to write all of your Python code into a text file, and run that text file directly from the commandline. As your programs get longer, you may want to break the code into multiple files for easier maintenance. You can also have one handy function shared between multiple files, saving repetition.

> Any file ending in .py is treated as a module by Python.

A module is an organized unit of Python code. Easy Python file has it's own global variable `scope`, so you can name your variables and functions there whatever you want without conflicting with other modules.

#### Imports

Back in the interpreter, let's try importing the `numop1` function from our new module:

    >>> import super_happy_fun_nums
    >>> super_happy_fun_nums.numop1(2,3,2,greetings=None)
    10
    >>> numop1(2,3,2,greetings=None)
    NameError: name 'numop1' is not defined

Above we can see that the function `numop1` is defined in the `scope` of the `super_happy_fun_nums` module. If we want to use the function a little more easily, we could import it as:

    >>> from super_happy_fun_nums import numop1
    >>> numop1(2,3,2,greetings=None)
    10
    >>> super_happy_fun_nums.numop1(2,3,2,greetings=None)
    NameError: name 'numop1' is not defined

You can even rename things `as` you import them:

    >>> from super_happy_fun_nums import numop1 as number_op
    >>> number_op(2,3,2,greetings=None)
    10

The Python moto is "batteries included", because there are many handy modules built right into Python to help you do various things. For instance, the standard math library:

    >>> import math
    >>> math.sqrt(4.00)
    2.0
    >>> math.trunc(3.14159265358979)
    3
    >>> math.floor(3.14159265358979)
    3.0
    >>> math.sin(0.0)
    0.0

Some other libraries that you will find very useful:

    import os, sys, gzip, zlib, timeit, urllib2, datetime, random, shutil

Try this:

    import this

## How to execute Python code

#### Interpretter

#### Execute Bytecode

main()

[Back to Syllabus](../../README.md)
