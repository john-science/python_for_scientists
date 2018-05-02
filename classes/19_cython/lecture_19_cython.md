# Cython

Writing code in Python is fast. But running Python code isn't as fast as, say, C code. Wouldn't it be nice if Python were faster? Enter Cython.

Cython is two things:

* a way to add C-like types to Python code, to improve performance
* a way to compile Cython code to C, so it can be compiled as an extension module

Cython also provides parallel processing options that are not available in normal Python code.


## Installation

Consider installing [Anaconda](http://docs.continuum.io/anaconda/install.html). It will come packaged with Cython, but also a ton of other really great Python libraries.


## Compiling and Running Cython

There are several ways to compile Cython code so it can be run by Python. Cython can be compiled:

 * separately by build tools like `distutils`
 * by hand using the `cython` commandline tool
 * automatically at import time with `pyximport`
 * and run interactively from iPython's `%%cython` magic

### Using distutils

This is probably the best option. And the only one I really use in practice.

The most common Python build tool is `distutils`. This tool that lets people to build and install your Python projet using the ubiquitous `python setup.py install` from the command line.  If you want to add some Cython to your Python project, write one or more modules optionally using the Cython syntax, and change the extension of your files from `.py` to `.pyx`. Then add these lines to your setup.py:

    from distutils.core import setup
    from Cython.build import cythonize
    ...
    setup(ext_modules=cythonize('example.pyx'))

The whole process can get more complicated, but that's the core of it and a good place to start.

### Compile using Cython import

How do you compile Cython code by hand? Why, by using the `cython` command, obviously!

    $ cython example.pyx

But wait! Are there a ton of obscure flags to learn to customize your compillation? You bet there are!

A typical workflow to compile Cython code into a Python extension module will look something like:

    $ CFLAGS=$(python-config --cflags)
    $ LDFLAGS=$(python-config --ldflags)
    $ cython example.pyx                      # creates example.c
    $ gcc -c fib.c $(CFLAGS)                  # creates example.o
    $ gcc fib.o -o fib.so -shared ${LDFLAGS}  # creates example.so
    $ rm example.c example.o                  # cleanup

Of course, once you have designed commandlines to compile your Cython project, you can throw these into Bash, Batch, Make, or CMake scripts. Or whatever build tools you use.

### Using pyximport

One possible way to speed up your Python code is to import your modules as if they were Cython modules using `pyximport`. Which you can do easily by putting this at the top of your calling modules:

    import pyximport
    pyximport.install()

### iPython Magic

Okay, I never do this, but it is an option. During an iPython session you just have to initalize Cython "magic":

    %load_ext cythonmagic

And then you can write Cython code directly into your session:

    %%cython
    def fib(int n):
        cdef int i
        cdef double a = 0.0, b = 0.0
        for i in range(n):
            a, b = a+b, a
        return a


## Cython Syntax

TODO


## Extension Types

TODO


## Organizing Cython Code

TODO


## Wrapping C in Cython

TODO


## Wrapping C++ in Cython

TODO


## Profiling Cython

TODO


## NumPy and MemoryViews

TODO


## Parallel Programming

TODO


## Further Reading

 * [Cython - O'Reilly textbook](https://www.amazon.com/Cython-Programmers-Kurt-W-Smith/dp/1491901551/ref=sr_1_1?ie=UTF8&qid=1523792400&sr=8-1&keywords=cython+o%27reilly) - A good intro text
 

[Back to Syllabus](../../README.md)
