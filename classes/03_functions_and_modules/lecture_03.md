# Functions and Modules

## Functions

#### Defining a Function

A function is a handy way to encasuplate a piece of logic that needs to be performed repeatedly or made more portable.

    def say_hi():
        print('Hi!')

The structure of a function definition is:

    def FUNCTION_NAME(arg1, arg2, ..., kw1=v1, kw2=v2, ...):
        '''EXPLANATION OF WHAT THE FUNCTION DOES'''
        FUNCTION_BODY

The `argX` above are function arguments, and they are required (the order is important). The `kwX` above are keywords, but they are optional (the order is unimportant; the valuess are defaults).

Function names can be almost anything, but they have a few restrictions:

- contain only numbers, letters, underscores
- do not start with a number
- are not the same name as a built-in function (like `print`)

Notice also that every function should have a short 1 to 5 line comment block, describing what it does. This helps you remember anything tricky about the function when you come back to it next year. And it also helps speed along the process of reading your code for anyone else that works with it.

#### Example Functions

Let's look at some simple example functions. First, we'll create a trivial function to add a couple numbers:

    >>> def addnums(x, y):
            '''Add two numbers'''
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
            '''Add two numbers, with a default value of
            two for the second number.
            '''
            return x + y
    >>> addnums(3)
    5
    >>> addnums(3, y=3)
    6
    >>> addnums(3, 3)
    6
    >>> addnums(3, 3, 3)
    TypeError: addnums() takes at most 2 arguments (3 given)
    >>> addnums("oops")
    TypeError: cannot concatenate 'str' and 'int' objects

Here we see a few valid was to call the `addnums` function, and a couple invalid ones. Take some time and make sure each of these cases makes sense to you.

#### Scope

The [scope](https://en.wikipedia.org/wiki/Scope_%28computer_science%29) of a variable is where the name of that variable is accessable from. Inside a function, Python keeps a local variables list. Below, `pi` is not modified globally, and so printing it inside and outside of the function yields two different results:

    >>> pi = 1.0
    >>> def set_pi():
            '''set and print the value of pi'''
            pi = 3.1415926
            print(pi)
    >>> set_pi()
    3.1415926
    >>> print(pi)
    1.0

If we want to set the global `pi` variable inside a function, we need to access it using the `global` keyword:

    >>> pi = 1.0
    >>> def set_pi():
            '''set and print the value of pi'''
            global pi
            pi = 3.1415926
            print(pi)
    >>> set_pi()
    3.1415926
    >>> print(pi)
    3.1415926


## Modules

You can write all of your Python code in the interpreter. But when you quit the interpreter, all of your work lost. Frequently, this is perfectly okay. But another option is to write all of your Python code into a text file, and run that text file directly from the commandline. As your programs get longer, you may want to break the code into multiple files for easier maintenance. You can also have one handy function shared between multiple files, saving repetition.

> Any file ending in .py is treated as a module by Python.

A module is an organized unit of Python code. Every Python file has its own global variable `scope`, so you can name your variables and functions there whatever you want without conflicting with other modules.

#### Imports

Back in the interpreter, let's try importing the `numop1` function from our new module:

    >>> import super_happy_fun_nums
    >>> super_happy_fun_nums.numop1(2, 3, 2, greetings=None)
    10
    >>> numop1(2, 3, 2, greetings=None)
    NameError: name 'numop1' is not defined

Above we can see that the function `numop1` is defined in the `scope` of the `super_happy_fun_nums` module. If we want to use the function a little more easily, we could import it as:

    >>> from super_happy_fun_nums import numop1
    >>> numop1(2, 3, 2, greetings=None)
    10

You can even rename things `as` you import them:

    >>> from super_happy_fun_nums import numop1 as number_op
    >>> number_op(2, 3, 2, greetings=None)
    10

If there are multiple functions in the module, you can import them all at the same time:

    >>> from super_happy_fun_nums import *
    >>> numop1(2, 3, 2, greetings=None)
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

There are a few ways to execute Python code.

#### Interpretter

The method we've already seen for executing Python code is by using the Python interpreter. This is a great way to do a small amount of work, make a quick plot, or test out code you are writing. But, as we've already discussed, it is limited in that you can't reuse the code later.

#### Executing Modules as Scripts

Let's write a the simplest possible Python script, and call it `hello.py`:

    print("Hello, World!")

To run this script from the commandline, we simply do:

    python hello.py

BUT, this code is hard to import from another file. To make your code more portable, let's create a new file called `hello_function.py`:

    def hello():
        '''Prints the standard Hello World example'''
        print("Hello, World!")
    
    if __name__ == '__main__':
        hello()

Now, when you run this script from the commandline, you get the same result as before. But, now you can import this function from another file, and call it there:

    from hello import hello
    
    hello()

What we have learned about here is the Python `main` method. This is a handy way to turn your Python script into an executable program, but still allow your code to be reused later.

    > Resuing code is better than copy/pasting code.

Finally, let's try one more example. Let's look back at our `super_happy_fun_nums` script. Let's say we want to run it from the commandline by just passing it a single number:

    python super_happy_fun_nums.py 1
    python super_happy_fun_nums.py 42
    python super_happy_fun_nums.py <arguments>

To do so, we will create a custom `main` method:

    if __name__ == "__main__":
        import sys
        print(numop1(int(sys.argv[1]), 3, 2, greetings=None))

or:

    import sys
    
    def main():
        print(numop1(int(sys.argv[1]), 3, 2, greetings=None))
        
    if __name__ == "__main__":
        main()

With either one of the above options, we can now execute the script and execute the `numop1` method we wrote:

    $ python super_happy_fun_nums.py 2
    10

If the module is imported, the code is not run:

    >>> import super_happy_fun_nums
    >>>

The take-away message here is there are several ways to write, store, and execute Python code. You should choose among these based on how much you might want to reuse this code later. If you just want to use Python as a simple calculate: write your code in the interpreter and be done with it. If you might ever want to run the code again, put it into a text file with a `.py` extension. And if you understand your code well enough to break it into logical pieces that might be useful again one day, separate your code into functions, and call them with a `main` method.


#### Documentation

**Documentation**: Just the right thing to do and Python makes it dead simple.

![docstrings](../../resources/glorious_docstrings.png)

**Docstring**: the first unassigned string in a function (or class, method, program, etc.). Here is a nice example of a helpful docstring for the function `numop1`:

    def numop1(x,y,multiplier=1.0,greetings="Thank you for your inquiry."):
        """
            Purpose: does a simple operation on two numbers.

            Input: We expect x,y are numbers multiplier is also a number
            (a float is preferred) and is optional.
            It defaults to 1.0. You can also specify a small greeting as a string.

            Output: return x + y times the multiplier
        """
        if greetings is not None:
            print(greetings)
            return (x + y)*multiplier

If we copy the Python code for `numop1` into a file, say `super_happy_fun_nums.py`, we can go to the command line and type `pydoc -w super_happy_fun_nums` and you will create a nicely-formmated HTML file with all the documentation for the functions in that file:

![docstrings](../../resources/docstring_screencap.png)


## Problem Sets

 * [Basic Functions](problem_set_1_basic_functions.md)

## Further Reading

 * [Python Tutorial: Functions](http://www.python-course.eu/functions.php)
 * [Special Topic: Underscores in Python](http://shahriar.svbtle.com/underscores-in-python)


[Back to Syllabus](../../README.md)
