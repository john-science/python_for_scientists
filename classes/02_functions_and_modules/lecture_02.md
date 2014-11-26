# Functions and Modules

## Functions

A function is a handy way to encasuplate a piece of logic that needs to be passed around or performed repeatedly.

    def say_hi():
        print('Hi!')

#### Scope

Python has it’s own local variables list. `x` is not modified globally.

    >>> def numop(x,y):
    x *= 3.14
    return x + y
    >>> x = 1
    >>> print numop(x,3)
    6.14
    >>> print x
    1

## Modules

#### Imports

Try:

    import this

## main()

### How to execute Python code

#### Interpretter

#### Execute Bytecode


[Back to Syllabus](../../README.md)
