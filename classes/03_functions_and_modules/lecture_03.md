# Functions and Modules

## Functions

#### Defining a Function

A function is a handy way to encasuplate a piece of logic that needs to be used again by you or your friends.

Here we use the `def` keyword to *define* a function named `say_hi`, that prints `Hi!` to the screen.

```python
>>> def say_hi():
...     print('Hi!')
...
>>> say_hi()
Hi!
```

The structure of a function definition is:

```python
def FUNCTION_NAME(arg1, arg2, ..., kw1=v1, kw2=v2, ...):
    '''EXPLANATION OF WHAT THE FUNCTION DOES'''
    FUNCTION_BODY
```

The `arg1` above are function arguments, and if a function has arguments, then the user must give a value for those arguments when calling the function. And the order of arguments is important.

The `kw1` above are keywords, but they are optional because a default value `v1` will be provided for each keyword. Since keywords have names, the order of the keywords isn't important.

Function names can be almost anything, but they have a few restrictions:

- contain only numbers, letters, underscores
- do not start with a number
- are not the same name as a built-in function (like `print`, `list`, `exit`)

Notice also that every function should have a short 1-to-5 line comment block describing what it does. This speeds up reading your code, for you and everyone else.

#### Example Functions

Let's look at some simple example functions. First, we'll create a trivial function to add a couple numbers:

```python
>>> def addnums(x, y):
...     '''Add two numbers'''
...     return x + y
```

And now let's use the function:

```python
>>> addnums(2, 3)
5
>>> addnums("a", "b")  # Wait, what?
ab
>>> addnums("cat", 23232)
TypeError: cannot concatenate 'str' and 'int' objects
```

What we see is that the function works as expected for numbers, but since Python is a *dynamic* language, it doesn't stop you from trying to add a `string` and an `integer`. Of course, you can't add these, so a type error is thrown. This is part of the Python "we're all consenting adults" philosophy; you are trusted to know what you're doing.

Let's see that same example with key word arguments:

```python
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
```

Here we see a few valid was to call the `addnums` function, and a couple invalid ones. Take some time and make sure each of these cases makes sense to you.

#### Scope

The [scope](https://en.wikipedia.org/wiki/Scope_%28computer_science%29) of a variable is where the name of that variable is accessable from. Inside a function, Python keeps a local variables list. Below, `pi` is not modified globally, and so printing it inside and outside of the function yields two different results:

```python
>>> pi = 1.0
>>> def set_pi():
        '''set and print the value of pi'''
        pi = 3.1415926
        print(pi)
>>> set_pi()
3.1415926
>>> print(pi)
1.0
```

#### Documentation

**Documentation**: Just the right thing to do and Python makes it dead simple.

![docstrings](../../resources/glorious_docstrings.png)

**Docstring**: the first unassigned string in a function (or class, method, program, etc.).

Here is a nice example of a helpful docstring for the function `numop1`:

```python
def numop1(x, y, multiplier=1.0, greetings="Thank you for your inquiry."):
    """
        Purpose: does a simple operation on two numbers.

        Input: We expect x,y are numbers. multiplier is also a number
        (a float is preferred) and is optional.
        It defaults to 1.0. You can also specify a small greeting as a string.

        Output: return x + y times the multiplier
    """
    if greetings is not None:
        print(greetings)
        return (x + y) * multiplier
```

Let's write our first Python script as a stand-alone file. Leave the interpreter and create a file `super_happy_fun_nums.py`. Copy the above `numop1` function into that file, save and close. Then, go to the command line and run the following command:

    pydoc -w super_happy_fun_nums

This will generate a nicely-formmated HTML file with all the documentation for the functions in that file:

![docstrings](../../resources/docstring_screencap.png)

## Your First Python Module

Let's take another look at the file we created above: `super_happy_fun_nums.py`.

This is an example of a Python module. That is, instead of writing our Python code into the interpreter, we placed it into a text file. Certainly, you *can* write all of your Python code in the interpreter. But when you quit the interpreter, all of your work is lost.

> Any file ending in .py is treated as a module by Python.

A module is an organized unit of Python code. Every Python file has its own global variable `scope`, so you can name your variables and functions there whatever you want without conflicting with other modules.

## Using Your First Module

Let's try to use the `numop1` code we have saved in the `super_happy_fun_nums.py` module.

You will need to be on the commandline to do this. First, navigate to the directory that contains `super_happy_fun_nums.py`. Next, open up the Python intepreter by typing "python" on the commandline:

    $ python
    Python 3.6.1 |Anaconda 4.4.0 (64-bit)| (default, May 11 2017, 13:09:58) 
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Now, let's import and use `numop1`:

```python
>>> from super_happy_fun_nums import numop1
>>> numop1(5, 7)
Thank you for your inquiry.
12.0
>>> numop1(2, 4, multiplier=2.5, greetings="Yo.")
Yo
15.0
```

Let's recap. We wrote a Python function into a file with the `*.py` extension. That extension allowed the Python intepreter to know that there was importable Python code to be found. We then used `"from FILENAME import THING"` to import the Python code into the intepreter and use it.

The ability to store off Python code in a module and use that code with different values is huge. This is a big step towards making Python useful to you in your every day work.

## Executing Your First Python Program

A Python program consists of one (or more) modules that are executable from the commandline. To run a Python program, just use the word `python` and then the name of the file:

    $ python super_happy_fun_nums.py

If you try that line above, you will see that...

Nothing happens.

Well, that's anti-climatic.

But, after all, the function `numop1` above doesn't *do* anything until you pass it at least one number, which we didn't do. So what did you expect to happen?


#### main

It turns out, to create turn a Python module into an executable program, you need to add two things. The first is a `main` function that does something:

```python
def main():
    print('Hello, World!')
```

Second, you need to add these two lines:

```python
if __name__ == '__main__':
    main()
```

If you do the above, your file will now look like:

```python
def main():
    '''Classic First Program'''
    print('Hello, World!')


def numop1(x,y,multiplier=1.0,greetings="Thank you for your inquiry."):
    """
        Purpose: does a simple operation on two numbers.

        Input: We expect x,y are numbers. multiplier is also a number
        (a float is preferred) and is optional.
        It defaults to 1.0. You can also specify a small greeting as a string.

        Output: return x + y times the multiplier
    """
    if greetings is not None:
        print(greetings)
        return (x + y) * multiplier


if __name__ == '__main__':
    main()
```

**NOTE**: Within a function we might leave a single blank line here and there. But I put the standard *two* blank lines between functions. This just makes it easier to read the code.

Okay, let's run our new script!

    $ python super_happy_fun_nums.py
    Hello, World!

Awesome, we just made our first Python program! But... wait, what about `numop1`? Well, we didn't call that function in the `main` function, so we didn't use it. That seems silly. So let's change the main method to:

```python
def main():
    '''Just printing some silly tests'''
    print(numop1(2, 2))
    print(numop1(3, 3, multiplier=3.3))
    print(numop1(4, 4, multiplier=4, greetings='(4 + 4) * 4:'))
```

Let's run our program again:

    $ python super_happy_fun_nums.py
    Thank you for your inquiry.
    4.0
    Thank you for your inquiry.
    19.799999999999997
    (4 + 4) * 4:
    32

NOW we have a real program. It has a `main` function, so we can execute it from the commandline. It includes other functions that we use in `main`. We have even commented our functions. This little file could serve as a blueprint for a lot of the Python work you do from now on.


## Importing From Your Module

Earlier, we imported `numop1` into the Python interpreter by doing:

    >>> from super_happy_fun_nums import numop1

If we had more than one function in `super_happy_fun_nums.py`, we could import both in one of a couple ways:

    >>> from super_happy_fun_nums import numop1, numop2
    >>> from super_happy_fun_nums import *

A different way to import is to just import the whole module:

    >>> import super_happy_fun_nums
    
Then, when you want to use `numop1`, you have to qualify it with the module name:

    >>> super_happy_fun_nums.numop1(2, 2)

So, you have options. Design your code to make it as convenient as possible for the user.


## Importing In Your Module

If you created another Python module and called it `testing_imports.py`, you could use all of the same imports as we did in the interpreter above, to import `numop1` from `super_happy_fun_nums` (as long as `testing_imports` and `super_happy_fun_nums` are still in the same folder):

```python
# this is a new file: testing_imports.py

from super_happy_fun_nums import numop1

def main():
    print(numop1(2, 2))

if __name__ == '__main__':
    main()
```

Now we can share code between different Python modules. That'll come in handy.


## Import Python Standard Libraries

The Python moto is "batteries included". That means Python comes with all kinds of libraries (modules) built it to do a lot of things you'll want to do. We will cover some of these in more detail in a few weeks. But for now it's just good to know they exist.

#### math

An obvious first library for a scientist / engineer to know about is the [math](https://docs.python.org/2/library/math.html) library:

```python
>>> import math
>>> math.sqrt(4.00)
2.0
>>> math.sin(0.0)
0.0
>>> math.log(1)
0.0
>>> math.pi
3.141592653589793
```

Once you `import math`, you can do `help(math)` to learn what options are availble. Similarly, you can also do `help(math.sqrt)` to learn more about something specific. If you have a question, just ask Python.

#### Just for Fun

The `math` library above is just the tip of the standard library iceberg. Python has all kinds of libraries built in:

 * [datetime](https://docs.python.org/3/library/datetime.html) - tools for dealing with dates and times
 * [gzip](https://docs.python.org/3/library/gzip.html) - tools for gzipping and un-gzipping files
 * [random](https://docs.python.org/3/library/random.html) - tools for generating pseudo-random numbers
 * [os](https://docs.python.org/3/library/os.html) - tools creating directories, checking if files exist, etc
 * [sys](https://docs.python.org/3/library/sys.html) - add commandline arguments to your programs
 * [urllib2](https://docs.python.org/3/library/urllib2.html) - tools for dealing with HTTP communications over the internet

For a full list of the Python standard libraries check [here](https://docs.python.org/3/library/).

Try this one:

```python
import this
```


## Wrap-Up

Today we learned about three things that will be useful in our daily work:

1. **Functions**: a way to encapsulate code and save it for later.
2. **Modules**: a way to save Python code into a ".py" file. Further, if you include a `main` function, you create an executable Python program.
3. **Imports**: We can now share our code between modules, and make use of Python's built-in standard libraries.


## Problem Sets

 * [Functions and Modules](problem_set_1_functions_modules.md)

## Further Reading

 * [Python Tutorial: Functions](http://www.python-course.eu/functions.php)
 * [Special Topic: Underscores in Python](http://shahriar.svbtle.com/underscores-in-python)


[Back to Syllabus](../../README.md)
