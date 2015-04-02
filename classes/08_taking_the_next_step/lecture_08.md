# Taking the Next Step

All the material in this course so far was just too define "the rules" of Python. But writing good code means more than just knowing the rules that define a language. You can teach a six-year-old the rules to chess, but that doesn't make them a Grand Master. A lot of knowledge, skill, and practice are needed to earn that title. The rest of this class will be devoted to taking the next step beyond basic syntax.

## Writting Better Code

The most important thing is always that your code works. Obviously. But some software is better than others. Good code creates *less* work for you, not *more*.

**Good code is easy to use, easy to understand, and easy to modify.**

In this lecture we will introduce the methods and tools needed to write better code.

## Style

#### The Counter Example

Imagine you are reading though someone else's code and you come across this function:

    def F(n):
      if n==0:    return 0
      elif n ==1:
       return 1
      else:return F(n-1)+F(n- 2)

What does it do? This method has a subtle bug, can you find it?

#### PEP8

Here is the exact same function, but following the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/):

    def fibonacci(n):
        '''Returns the n-th term in the Fibonacci Sequence'''
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

It has comments, so you immediately know exactly what it does. The regular 4-space tabs make it easy to compare the if-statements. And now that you fully grasped what the function does, you can start testing it with various values to see how it behaves. The bug: the method fails when passed a negative number.

To make your code readable you have to be extremely consistent about your spaces, naming conventions, comments, etcetera. If you want to spend the time to develop all of your own conventions, and stick to them stoically, great. Good for you. The rest of the world will use the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/).

## Comments

> You are what you comment.

If someone else has to look at your code, and there are no comments, you are wasting their time. They might spend minutes or hours trying to figure out a detail they could have understood in a second if there were a comment.

Code that isn't commented well is destined to be thrown away. But first people might get angry with you.

The [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/) has lots of good notes on how to comment your code. The basic comment is the `#`:

    # find the factorial of N
    result = 1  # integer
    for i in xrange(2, N+1):
        result *= i

The `#` can be used at the start or the end of a line of code. Everything after the `#` is a comment, not code. And we have already seen the `'''` and `"""` comments in our [Functions and Modules](classes/03_functions_and_modules/lecture_03.md) lecture.

## Exceptions

#### Example: fixing `fibonacci`

There are several ways to fix any problem. But for learning purposes, let's fix the `fibonacci` function above by raising an `Exception`.

An `Exception` is a Python class designed to halt the current program politely when an error occurs and return a string so the user can know what the problem is. You have already seen many Exceptions in Python. Every time we make a bone-headed mistake Python returns an `Error`, which is just a type of `Exception`:

    >>> 4 / 'a'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for /: 'int' and 'str'

In the case above, `TypeError` subclasses `Error` which subclasses `Exception`.



#### More kinds of exceptions

 * Coming Soon

#### Creating your own exceptions

 * Coming Soon

## Code Organization

Be smart when choosing between functions and classes in your code.

#### Example: A good time to use functions

 * Coming Soon: small, independent pieces

#### Example: A good time to use classes

 * Coming Soon: too many arguments

#### Example: Another good time to use classes

 * Coming Soon: lots of global variables

#### Example: Are you going to be `import`ed?

 * Coming Soon: be careful what you put in `main`

## Code Repositories

Software works best when it is shared. Software shared between multiple people, developed and improved by everyone becomes easier to understand, easier to use, easier to update, and better.

The best way to share code is via a code repository. This is a central place where we can store code, save different versions, make updates, and track changes. If you're not using a code repository, your scripts and programs are just little text files on your computer, waiting to be forgotten.

The two most popular code repositories are Git and SVN. Both are good, and have their advantages. If you are comfortable with the command line, Git is easier to use. If you want to use your mouse, SVN is probably easier. If you have very small or very large projects, Git is probably the way to go.

## The Git Primer

I have already written a short introduction to Git, it is on GitHub [here](https://gist.github.com/theJollySin/7a2ee80c05d073996d16).

## GitHub

As you may have already noticed, this class is being stored and displayed using [GitHub](https://help.github.com/articles/set-up-git/), which is just a nice web interface for a Git repository.

 * Coming Soon: a link to how to creat your own repo or github

## Further Reading

 * [After Hours Tutorial](http://www.afterhoursprogramming.com/tutorial/Python/Exceptions/)
 * [Python Documentation](https://docs.python.org/2/tutorial/errors.html)

[Back to Syllabus](../../README.md)
