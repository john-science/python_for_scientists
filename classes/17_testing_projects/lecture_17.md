# Testing Python Projects

First, a quick note: this lecture is not for single Python scripts. It's not even for small programs with one or two scripts. This lecture only applies to Python projects that have gotten big enough to have several modules and be distributed to other people.

#### Installation

There are many libraries for testing and building Python projects, but in this lecture we will focus on those that come standard with Python. No extra installations required.

## Unit Tests

A [developer's mantra](http://c2.com/cgi/wiki?MakeItWorkMakeItRightMakeItFast):

    Make it work.
    Make it right.
    Make it fast.

Today we'll talk about that second thing: let's make sure our code is "right". By "right" we mean producing the desired outputs given all inputs. The only way to know if your code is "right" is to test it.

#### Different Types of Software Tests

Without getting too pedantic, there are generally three kinds of [software testing](https://en.wikipedia.org/wiki/Software_testing):

 * [Unit Tests](https://en.wikipedia.org/wiki/Unit_testing) - Testing each piece of your code on the smallest level (functions and methods).
 * [Integration Tests](https://en.wikipedia.org/wiki/Integration_testing) - Testing the connections between different pieces of your code.
 * [System Tests](https://en.wikipedia.org/wiki/System_testing) - Full end-to-end testing of your software as whole.

As your project gets larger, the items lower on this list become more important. But everything starts with unit testing. If you don't know if and how the smallest pieces of your code is working, larger-scale tests will have very little meaning.

#### Why Unit Test?

Unit Tests will answer several questions for you, that become more important as the size of your code base and your user base increase:

 * Does every single function or method produce the results I want for typical inputs?
 * What about for edge cases?
 * Every time I make a change to the code, how can I re-test the entire code base to make sure nothing broke?

Of course, the next question on your mind will immediately be:

 * How can I automate this whole process, so it doesn't take up all my time?

#### Unit Testing Libraries



## The Build Process

 * Coming Soon

## Documentation

 * Coming Soon

## Designing a Python Project

 * Coming Soon

#### The Cookie Cutter

 * Coming Soon

[Cookie Cutter](https://github.com/audreyr/cookiecutter-pypackage)

## Why Bother?

 * Coming Soon

## Further Reading

 * [Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/) - A great reference for all facets of building a modern Python project.
 * [Audreyr's Cookie Cutter](https://github.com/audreyr/cookiecutter-pypackage)


[Back to Syllabus](../../README.md)
