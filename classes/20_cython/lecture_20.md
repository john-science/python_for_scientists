# Cython - a pxd example

### The Disclaimer

Okay, first things first. Cython is a big topic. It would take 6-9 lectures to cover it completely. So we won't be doing that. But it would also be a dis-service to skip the topic entirely. The approach we will take here is to show *one example of how to use Cython*. This is not, by any means, the only way to use Cython. This is just one approach.

This lecture shows an example of how to speed up pre-existing code using Cython, without changing the code itself. You just add an extra `*.pxd` file for each `*.py` file, and deal with the new Cython build process.

Again, this is not the only way to use Cython, but it is a simple example.

### Making Python Faster

The major goal behind Cython is to make your Python code faster. Python is a great language, but it is not as fast as older, simpler languages like C or Fortran.

How Cython accomplishes this speed increase is to apply some aspects of the C language (which Python is written in) to Python. In particular, Cython applies the  [type system](https://en.wikipedia.org/wiki/Type_system) from the [C programming language](https://en.wikipedia.org/wiki/C_(programming_language)) to Python. If you are not familiar with [C](https://en.wikipedia.org/wiki/C_(programming_language)), [Fortran](https://en.wikipedia.org/wiki/Fortran), or some other [strongly-typed language](https://en.wikipedia.org/wiki/Strong_and_weak_typing), this will all seem a little magical to you. These are good languages, and worth learning, but outside the scope of this course.


#### Installation

For Linux and Mac, the installation is merely a single line of `apt-get`.

#### Anaconda

Consider installing [Anaconda](http://docs.continuum.io/anaconda/install.html) instead. Anaconda is Python packaged with hundreds of tools and libraries that you will want (This includes matplotlib and everything else we will use in this course.)


## The Example Python Script - Finding Primes

TODO: What are primes again?

TODO: Show the Example

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
