# Functions and Modules

## Functions

#### Defining a Function

A function is a handy way to encasuplate a piece of logic that needs to be passed around or performed repeatedly.

    def say_hi():
        print('Hi!')

The structure of a function definition is:

    def FUNCTION_NAME(arg1, arg2, ..., kw1=v1, kw2=v2, ...):
        FUNCTION_BODY

The `argX` abve are arguments required (the order is important). The `kwX` above are keywords optional (sequence unimportant; valuess are defaults).

You can name a function anything you want as long as it:

- contains only numbers, letters, underscore
- does not start with a number
- is not the same name as a built-in function (like `print`)

#### Example Functions

Let's look at some simple example functions. First, we'll create a trivial function to add a couple numbers:

    >>> def addnums(x, y):
        return x + y
    >>> addnums(2, 3)
    5
    >>> print(addnums("a", "b")  # Wait, what?)
    ab
    >>> print(addnums("cat", 23232))
    TypeError: cannot concatenate 'str' and 'int' objects

What we see here is that the function works as expected for numbers, but since Python is a *dynamic* language, it doesn't stop you from trying to add a `string` and an `integer`. Of course, you can't add these, so a type error is thrown. This is part of the Python "we're all consenting adults" philosophy; you are trusted to know what you're doing.

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

The [scope](https://en.wikipedia.org/wiki/Scope_%28computer_science%29) of a variable is where the name of that variable is accessable from. Inside a function, Python keeps a local variables list. Below, `x` is not modified globally.

    >>> def numop(x,y):
        x *= 3.14
        return x + y
    >>> x = 1
    >>> print numop(x,3)
    6.14
    >>> print x
    1

#### Documentation

**Documentation**: Just the Right thing to Do and Python makes it dead simple.

**Docstring**: the first unassigned string in a function (or class, method, program, etc.).

    def numop1(x,y,multiplier=1.0,greetings="Thank you for your inquiry."):
        """ numop1 -- this does a simple operation on two numbers.
        We expect x,y are numbers and return x + y times the multiplier
        multiplier is also a number (a float is preferred) and is optional.
        It defaults to 1.0.
        You can also specify a small greeting as a string. """
        if greetings is not None:
            print(greetings)
        return (x + y) * multiplier

## Modules

#### Imports

Try:

    import this

## main()

### How to execute Python code

#### Interpretter

#### Execute Bytecode


[Back to Syllabus](../../README.md)
