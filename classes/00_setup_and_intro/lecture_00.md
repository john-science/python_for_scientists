# Setup and Introduction

## How to install Python?

Python should be easy to install on basically all home computers and laptops. There are many different versions and flavors of Python. This class will be built around Python v2.7, but you will probably be fine using anything above Python v2.5.

The installation procedure depends on what operating system you have installed. As always, [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/) has a great description of how to install for the three different operating systems.

 * [Windows](http://docs.python-guide.org/en/latest/starting/install/win/)
 * [Mac OS X](http://docs.python-guide.org/en/latest/starting/install/osx/)
 * [Linux](http://docs.python-guide.org/en/latest/starting/install/linux/)

(NOTE: The above guide also explains how to install SetupTools, Pip, and VirtualEnv. While these are great tools worth learning, and I highly encourage it, they are not necessary for this course.)

## What is Python?

Python is a [high-level](https://en.wikipedia.org/wiki/High-level_programming_language), [interpretted](https://en.wikipedia.org/wiki/Interpreted_language), [dynamically-typed](https://en.wikipedia.org/wiki/Dynamic_programming_language) computer programming language whose goal appears to be to make code as easy to write as possible. The Python programming language is [free](http://www.howtogeek.com/howto/31717/what-do-the-phrases-free-speech-vs.-free-beer-really-mean/) and [open-source](https://en.wikipedia.org/wiki/Open_source#Computer_software).

### Comparing Python to other languages

To understand Python it is probably best to consider how Python differs from other programming languages. This is a good chance to explain those esoteric terms used above.

#### High-Level

A low-level language is one designed directly for a computer's hardware. It is not human readable, and details the exact calculations to be performed by the computer to the smallest detail. A high-level language is meant to abstract away the inner workings of a computer and make code easily readable by humans.

![high-level language diagram](http://blog.malwarebytes.org/wp-content/uploads/2012/09/FlowDiagram2.png)

There are several layers of languages in the above pyramid. If you've ever worked with C or Fortran, those languages are somewhere in the middle. They are human readable, but deal with the specifics of a computer's hardware all the time (pointers, allocating and freeing memory, stack overflows). It would be worth your time to look up each of the above terms or languages on Wikipedia.

#### Interpretted

If you've ever written Fortran or C code, you will remember having to "compile" your code. This is the process of taking your text file and turning it into an executable that can be run as a program. This final executable is a series of commands that the computer will understand when executed.

But you don't have to compile Python code. The Python programming language comes with an interpreter, that will read directly from your text file on the fly and executes commands as it finds them. This means you never have to compile, but it also means you can type commands into the Python interpreter and they will be executed as you go:

    john@neutrino:~$ python
    Python 2.6.6 (r266:84292, Jan 22 2014, 09:42:36) 
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> def fib(n):
    >>>     a, b = 0, 1
    >>>     while a < n:
    >>>         print(a, end=' ')
    >>>         a, b = b, a+b
    >>>     print()
    >>> fib(1000)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

You can try out the Python interpreter online, by going to [Python.org](https://www.python.org/) and clicking "Launch Interpreter" at the top.

Of course, you can still write Python scripts, or "modules", as text files and execute those from the command line, a bit like they were executables (but more like Shell scripts if you ever used Linux):

    john@neutrino:~$ python my_awesome_script.py

#### Dynamically Typed

In most programming languages, when you define a variable `x`, you have to tell the computer what "[type](https://en.wikipedia.org/wiki/Data_type)" that variable will be: integer, decimal, letter, string, array, list of strings, table, plot, whatever. But the Python interpreter is designed to figure out what the type of the variable is, from context.

If you have seen another programming language before, the comparison becomes interesting in what you, as the programmer, *don't* have to do:

**In Java**:

    int three = 3;
    int six = 2 * three;

**In C**:

    int three = 3;
    int six = 2 * three;

**In Fortran**:

    integer three,six
    three = 3
    six = 2 * three

**In Python**:

    three = 3
    six = 2 * three

Python is smart enough to figure out what type your variables are, without you telling it. This is valid Python code:

    name = "Jesse Owens"
    height = 180
    height = 180.5
    weight = 75.5
    year = 1936
    gold_medals = ["long jump", "100m sprint", "long jump", "200m sprint", "4x100m sprint relay"]

#### Batteries Included

That's the Python motto. The author of the first version of Python, [Guido von Rossom](http://en.wikipedia.org/wiki/Benevolent_dictator_for_life), has started a culture in the Python community that code should be easy to use. To that end, Python comes with a large collection of [standard libraries](https://en.wikipedia.org/wiki/Standard_library). Python comes with a wide range of tools to do the sorts of things that people frequently want to do with a computer programming language: complex math, random numbers, calendars, dates and times, dealing with *.zip files, communicating over the internet with HTTP, reading CSV files, you name it.

## Why Python?

> You'll never find a programming language that frees you from the burden of clarifying your ideas.

![the well](http://imgs.xkcd.com/comics/well_2.png)

Every programming language has syntax, rules you have to learn. But Python has a lot of traction right now with scientists and engineers. The rules are easy enough to learn that you can focus on what really matters. And after a few years of that traction there are a lot of libraries and tools written just for scientists and engineers. And that's really what Python brings to the table, a load of handy tools designed right for you.

## How to make the most of this class

> The best way to learn is by doing. And the best way to remember what you learn is by doing it a lot.

Write code. Don't use Excel or a calculator for that little thing that needs to get done at work, write it in Python. Do it in the interpreter. Try out the latest thing you've learned about. Make sure and practice what you learn about between lectures.
