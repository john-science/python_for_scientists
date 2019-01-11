# Cython - a pxd example

### The Disclaimer

Cython is a big topic. It would take 4-8 lectures to cover it completely. So we won't be doing that. But it would also be a disservice to skip it entirely. The approach we will take here is to show *one example of how to use Cython*. This is not, by any means, the only way to use Cython. This is just one approach.

This lecture shows some examples of how to speed up pre-existing Python code using Cython. The approach we will take is to add a `*.pxd` file for each `*.py` file, and juggle the new Cython build process.

Again, this is not the only way to use Cython, but a common and useful one.

### Making Python Faster

The major goal behind Cython is to make Python code faster. Python is a great language, but it is not as fast as older, simpler languages, like C or Fortran.

How Cython accomplishes this speed increase is to apply some aspects of the C language (in which Python is written) to Python. In particular, Cython applies the  [type system](https://en.wikipedia.org/wiki/Type_system) from the [C programming language](https://en.wikipedia.org/wiki/C_(programming_language)) to Python. If you are not familiar with [C](https://en.wikipedia.org/wiki/C_(programming_language)), [Fortran](https://en.wikipedia.org/wiki/Fortran), or some other [strongly-typed language](https://en.wikipedia.org/wiki/Strong_and_weak_typing), this will all seem a little magical to you. These are good languages, and worth learning, but outside the scope of this course.


### Installation

For Linux and Mac, the installation is merely a single line of `apt-get`.

#### Anaconda

Consider installing [Anaconda](http://docs.continuum.io/anaconda/install.html) instead. Anaconda is Python packaged with hundreds of tools and libraries that you will want (This includes matplotlib and everything else we will use in this course.)


## The Example Python Script - Finding Primes

We need a piece of Python code to try and speed up with Cython. For our example, we will chose a simple function to find prime numbers.

#### Wait, Wait, What's a Prime Again?

A [prime number](https://en.wikipedia.org/wiki/Prime_number) is a number that is only divided by itself and 1.  For instance, `3`, `5`, and `7` are prime, but `2`, `6`, and `8` are not.

#### Finding Primes

For our example function, we will find prime numbers using the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). Basically, the process is we take all the numbers up to N and assume they are prime. Then we remove all the ones divisible by each prime as we find then. So, go through the list and remove everything divisible by 2. Then everything divisble by 3. Four is already gone, so then we remove everything divisible by 5. And so on. What's left when we get through the list are only the prime numbers.

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


## Making it Faster without Python

### Python Tricks

TODO


### Math Tricks

TODO


## Cythonizing Script

TODO


## Compiling and Running Your Script

TODO


## We can do even better!

TODO


## In Conclusion

TODO: What did we learn?


## Other Approaches

TODO


## Further Reading

 * [todo](https://duck.com) - TODO

[Back to Syllabus](../../README.md)
