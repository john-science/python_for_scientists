# Cython - a pxd example

### The Disclaimer

Cython is a big topic. It would take 4-8 lectures to cover it completely. So we won't be doing that. But it would also be a disservice to skip it entirely. The approach we will take here is to show *one example* of how to use Cython. This is not, by any means, the only way to use Cython. This is just one approach.

This lecture shows some examples of how to speed up pre-existing Python code using Cython. The approach we will take is to add a `*.pxd` file for each `*.py` file, and juggle the new Cython build process.

Again, this is not the only way to use Cython, but a common and useful one.

### Making Python Faster

The major goal behind Cython is to make Python code faster. Python is a great language, but it is not as fast as older, simpler languages, like C or Fortran.

How Cython accomplishes this speed increase is to apply some aspects of the C language (in which Python is written) to Python. In particular, Cython applies the  [type system](https://en.wikipedia.org/wiki/Type_system) from the [C programming language](https://en.wikipedia.org/wiki/C_(programming_language)) to Python. If you are not familiar with [C](https://en.wikipedia.org/wiki/C_(programming_language)), [Fortran](https://en.wikipedia.org/wiki/Fortran), or some other [strongly-typed language](https://en.wikipedia.org/wiki/Strong_and_weak_typing), this will all seem a little magical to you. These are good languages, and worth learning, but outside the scope of this course.


### Installation

For Linux and Mac, the installation is merely a single line of `apt-get`.

#### Anaconda

Consider installing [Anaconda](http://docs.continuum.io/anaconda/install.html) instead. Anaconda is Python packaged with hundreds of tools and libraries that you will want (This includes Cython and nearly everything else we use in this course.)


## The Example Python Script - Finding Primes

We need a piece of Python code to try and speed up. For our example, we will chose a simple function that finds prime numbers.

#### Wait, Wait... What's a Prime Again?

A [prime number](https://en.wikipedia.org/wiki/Prime_number) is a number that is only divided by itself and 1.  For instance, `3`, `5`, and `7` are prime, but `2`, `6`, and `15` are not.

#### Finding Primes

For our example function, we will find prime numbers using the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). Basically, the process is: we take all the numbers up to N and assume they are prime. Then we remove all the ones divisible by each prime as we find then. So, go through the list and remove everything divisible by 2. Then everything divisble by 3. Four is already gone, so then we remove everything divisible by 5. And so on. What's left when we get through the list are only the prime numbers.

Here is our Sieve. Our first, naive version isn't very fast, so this is our starting place:

```python
def sieve_naive(n):
    """ The Sieve of Eratosthenes - first pass
    """
    # Python indexes start at zero
    m = n + 1

    # make a list of for all numbers up to n, initially all prime
    numbers = [True for i in range(m)]

    # go through and remove all numbers that are a multiple of the others
    for i in range(2, n + 1):
      if numbers[i]:
        for j in range(i * i, m, i):
          numbers[j] = False

    # what is left are primes
    primes = []
    for i in range(2, m):
      if numbers[i]:
        primes.append(i)

    return primes
```

It's probably okay if this is not immediately obvious to you, but learning to read code is important, so go through it line-by-line and figure out what it's doing.

We can run the code and find primes below a certain upper limit:

```python
>>> sieve_naive(10)
[2, 3, 5, 7]

>>> sieve_naive(100)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

Okay, remember our mantra:

> Make it work, make it right, make it fast

Based on the order of those, we are good. It works and it outputs the correct prime numbers like it is supposed to. Good. Now we can finally worry about making our Python code fast(er).

Step 1 to making our code faster is timing it, to see how long it takes to run. That way we have a benchmark to compare any future modifications to:

```python
max_prime = 100000

start = time()
sieve_naive(max_prime)
print('{0} seconds'.format(time() - start))
 
 # 0.026287317276000977 seconds
```

## Making it Faster without Cython

First things first, we don't actually need Cython to make Python code faster. There are a lot of choices we can make that can improve the performance. We will break these choices into two categories: knowing Python better and knowing your subject matter better.

### Python Tricks

The first way we can improve any piece of Python code is to use the tools provided in the Python language to make small tweaks to the code. The the better you know the Python language, the more of these kinds of performance improvements you will be able to find.

For instance, in the `sieve_naive` function above we use this line to create a list of `True` values of size `m`:

```python
numbers = [True for i in range(m)]
```

But it turns out that list comprehensions are so powerful they are not optimal for generating really simple lists like this. It would be much faster to use a function that does nothing but create uniform lists:

```python
numbers = [True] * m
```

### Math Tricks

The second major way we can improve Python performance is with math. That is, the better you know the problem you are trying to solve, the more you can conceptually optimize it.

For instance, in our `naive` function above, we iterated from 1 to N to remove all the prime numbers in the range:

```python
for i in range(2, n + 1):
```

But, if you think about it for a second, we only have to iterate from 1 to the square root of N, because this number times itself is N, and anything bigger than that can't be a prime factor of N (considering we have already knocked out all the lower primes. So, knowing something about math means we can simplify our iterator to:

```python
for i in range(2, int(n**0.5 + 1)):
```

### Testing our performance

We have made two performance-improving changes above, yielding our new function to find primes:

```python
def sieve_decent(n):
    """ The Sieve of Eratosthenes:
        a couple small speed improvements
    """
    # Python indexes start at zero
    m = n + 1

    # make a list of for all numbers up to n, initially all prime
    numbers = [True] * m  # NOTE: faster due to Python magic

    # go through and remove all numbers that are a multiple of the others
    for i in range(2, int(n**0.5 + 1)):  # NOTE: faster due to basic math
      if numbers[i]:
        for j in range(i * i, m, i):
          numbers[j] = False

    # what is left are primes
    primes = []
    for i in range(2, m):
      if numbers[i]:
        primes.append(i)

    return primes
```

Again, we should time our function to see how we did:


```python
max_prime = 100000

start = time()
sieve_decent(max_prime)
print('{0} seconds'.format(time() - start))
 
 # 0.015769004821777344 seconds
```

Not bad! Without using Cython at all we managed to improve our peformance by 42%!

We will do even better below, but it is important to remember that Cython isn't the only way to improve your performance.


## Cythonizing Script

The first move to Cythonizing our little script is to pull out all the heavy lifting and place it in a separate file that we can Cythonize. First, we will put the `sieves` functions into a file `sieves.py` that looks like this:

```python
def sieve(n):
    """ The Sieve of Eratosthenes
    """
    # Python indexes start at zero
    m = n + 1

    # make a list of for all numbers up to n, initially all prime
    numbers = [True] * m  # NOTE: faster due to Python magic

    # go through and remove all numbers that are a multiple of the others
    for i in range(2, int(n**0.5 + 1)):  # NOTE: faster due to basic math
      if numbers[i]:
        for j in range(i * i, m, i):
          numbers[j] = False

    # what is left are primes
    primes = []
    for i in range(2, m):
      if numbers[i]:
        primes.append(i)

    return primes
```

But none of the unimportant glue code really needs to be Cythonized. So we will create a helper script called `finding_primes.py` that looks like this:

```python
from time import time
from sieves import sieve


def main():
    max_prime = 100000

    print("\nA decent pass at the Sieve of Eratosthenes, in Cython:")
    start = time()
    sieve(max_prime)
    print('{0} seconds'.format(time() - start))


if __name__ == '__main__':
    main()
```

Okay, obviously we haven't done any Cythonizing yet, but let's just do a quick check to see that our performance hasn't changed.

    $ python finding_primes.py
    A decent pass at the Sieve of Eratosthenes, in Cython:
    0.015347957611083984 seconds

Good, we got back our original performance. 

Now, in the same folder we are going to create our new Cython file `sieves.pxd`, which will look like this:

```python
cimport cython

@cython.locals(m=cython.int, i=cython.int, j=cython.int, numbers=list, primes=list)
cpdef list sieve(int n)
```

Two things will tell the Cython compiler what this file is. First, we called it `sieves.pxd` and put it in the same folder as `sieves.py`. Second is that little `cimport cython` at the top of the file.

Notice this the `pxd` file appears to declare the same function (`sieve(n)`) that we have in `sieves.py`. This new declaration looks broadly like our Python version except it has type information everywhere. 

Above, type the inputs and outputs of a function, which we don't usually do in Python.

* We have `sieve(int n)` rather than just `sieve(n)`, so we are forcing the function input to be an `int`.
* We have `def list sieve()` rather than just `def sieve()`, so we are forcing the function output to be a `list`.

We are also adding that strange `@cython.locals()` decorator to the function, to force all the variables internal to the function to have certain types as well:

* `m=cython.int` - forces the type so Cython can optimize statements like `m = n + 1`
* `i=cython.int` - forces types so Cython can optimize things like `for i in range(2, m):`
* `j=cython.int` - again, forcing types for loop indexing
* `numbers=list` - we want to create a `list` like `numbers = [True] * m`
* `primes=list` - This gets returned, so it needs to match the functions return type.

Finally, notice that the function has that `cpdef` at the beginning, instead of the normal Python `def`. Cython has a few options:

* `def` - Normal Python function, no Cython optimization.
* `cdef` - A fully C-like Cython function. This can only be called from other Cython function, not pure Python code.
* `cpdef` - A middle-ground function that is optimized by Cython, but can still be called by vanilla Python code.

Since our calling script (`finding_primes.py`) is a vanilla Python script, we needed to declare our Cythonize `sieves()` function as `cpdef`.


## Compiling and Running Your Script

Okay, we have defined our Python code, our Cython code, and we are ready to run it. Now we just need to compile our Cython code down to C and convert it to something Python will understand. Luckily, there are lots of Python tools to automate this process. We will use `distutils` because it's a community standard and worth seeing.

In the same folder we have been working in we will create a file called `setup.py` and put this in it:

```python
from setuptools import setup, find_packages
from setuptools.command.install import install
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
from glob import glob


EXT_MODULES = [Extension(p[:-4], [p, p[:-2] + 'y'], extra_compile_args=["-w"])
               for p in glob('*.pxd')]


# do the actual setup / install
setup(cmdclass={'install': install, 'build_ext': build_ext},
      name='finding_primes',
      packages=find_packages(),
      ext_modules=cythonize(EXT_MODULES, force=True))
```

Okay, now we have a directory with the following files all laid out:

* finding_primes.py
* sieves.py
* sieves.pxd
* setup.py

FINALLY, we can compile our Cython code from the command line by running this command:

    python setup.py build_ext --inplace

After you do that you will see a couple new files pop up:

* `sieves.c` - The C code generated from our Python code. Usually long and hard to read. But fast!
* `sieves.cpython-36m-x86_64-linux-gnu.so` - Or something named vaguely like that. This `.so` file is a compiled Cython library that Python can understand.

### Let's Try it!

Okay, it has taken us a while to get here, let's run our new code and see how we did:

    $ python finding_primes.py 
    A decent pass at the Sieve of Eratosthenes, in Cython:    
    0.005792379379272461 seconds

Success! All we had to do was conver the code to Cython and it ran 5 times faster than our original version, and three times faster than our optimized Python code!


## Can you do better?

Can you make the Cython code above even faster? Try it!

After the initial, cheap, speed improvements provided by Cython, a lot more performance boosts can be had. For instance, our function still takes `int n` and not `cython.int n`. We still have two lists instead of two `np.array` objects. At this point, we typically take a look at each part of the code and see if we can tweak it to behave more like Pure C and less like Python. There is never a guaranteed way to improve the speed of your code. Though chances are the more you play around, the faster you will be able to make your code.

Also, the better you know the C language the faster this process will be.

One trick is to make a change, compile your Cython and see how many lines there are in the resultant `.c` file. *Probably* fewer lines will mean faster code.


## In Conclusion

> What did we learn?

1. We learned that the first thing we can do to improve the performance of our Python code is to look at the Python code. Look for Python tricks and math tricks to make you code faster.
2. We also learned to create `.pxd` files to improve our code's performance without ever touching our Python code.
3. We learned how to setup those `.pxd` files.
4. And we learned how to use `distutils` to compile and Cython code into a Python-ready library.
5. Finally, we learned there is a certain amount of guess-and-check in what changes you can make to Python/Cython code to improve its performance.

> If Python makes writing code fast. Cython can make the code you write fast.


## A Quick Note

There are lots of other ways to use Cython to improve your code performance. This was just one example approach that seemed short enough to explain in a limited time.


## Example Scripts

If you want to try this out for yourself, the above examples (with Cython build scripts) are included in this class:

* [pure Python example](finding_primes/pure_python)
* [Cython example](finding_primes/cython)


## Further Reading

 * [Cython language basics](http://docs.cython.org/en/latest/src/reference/language_basics.html) - A great reference, but kind of boring to read end-to-end.
 * [SciPy Con Cython tutorial](https://conference.scipy.org/proceedings/SciPy2009/paper_1/full_text.pdf) - PDF tutorial about Cython. In depth and complete.
 

[Back to Syllabus](../../README.md)
