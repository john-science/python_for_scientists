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

Step 1 to making our code faster is timing it, to see how long it takes to run. That way we have a benchmark to compare any future modifications to:

```python
max_prime = 100000

start = time()
sieve_naive(max_prime)
print('{0} seconds'.format(time() - start))
 
 # 0.026287317276000977 seconds
```

## Making it Faster without Cython

First things first, we don't actually need Cython to make Python code faster. There are a lot of smart choices we can make that can improve the performance. We will break these choices into two categories: knowing Python better and knowing your subject matter better.

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
