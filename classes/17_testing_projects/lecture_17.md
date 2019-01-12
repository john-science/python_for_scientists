# Testing Python Projects

This lecture does not apply to stand-alone Python scripts. It's not even for small programs with one or two modules. This lecture is for Python projects that have gotten big enough to have several modules and be distributed to several people.

#### Installation

There are many libraries for testing Python projects. To keep this lecture from becoming its own course, we only show examples using `unittest`, which is the standar libraries (Python v2.7 or v3.2 or newer).

## Unit Tests

A [developer's mantra](http://c2.com/cgi/wiki?MakeItWorkMakeItRightMakeItFast):

    Make it work.
    Make it right.
    Make it fast.

Today we'll talk about that second thing: let's make sure our code is *right* (producing the desired outputs). And the only way to know if your code is *right* is to test it.

#### Different Types of Software Tests

Without getting too pedantic, there are generally three kinds of [software testing](https://en.wikipedia.org/wiki/Software_testing):

 * [Unit Tests](https://en.wikipedia.org/wiki/Unit_testing) - Testing each piece of your code on the smallest level (functions and methods).
 * [Integration Tests](https://en.wikipedia.org/wiki/Integration_testing) - Testing the connections between different pieces of your code.
 * [System Tests](https://en.wikipedia.org/wiki/System_testing) - Full end-to-end testing of your software as whole.

As your project gets larger, the items lower on this list become more important. But everything starts with unit tests.

#### Why Unit Test?

Unit Tests will answer several questions, that become more important as the size of your code base and your user base increase:

 * Does every single function or method produce the results I want for typical inputs?
 * What about for edge cases?
 * When I make a change to the code, how can I be sure I didn't break something elsewhere in the code?

A logical follow-up question will be:

 * How can I automate this process, so it doesn't take up all my time?

#### Unit Testing Frameworks

Software testing is an increasingly big topic, and there are a lot of good tools out there to help you test your software. Perhaps five of the most popular tools in Python are:

 * [unittest](http://pythontesting.net/framework/unittest/unittest-introduction/) - Python standard library unit testing tool
 * [nose](http://pythontesting.net/framework/nose/nose-introduction)/ - Built as an extension to unittest, to make it easier.
 * [pytest](http://pythontesting.net/framework/pytest/pytest-introduction/) - Simple, easy-to-use, unit testing library
 * [mock](http://www.voidspace.org.uk/python/mock/) - A Java-style testing framework that allows you to replace components of your code with "mock" components with known results.
 * [tox](http://tox.readthedocs.org/en/latest/) - VirtualEnv management tool that acts as a wrapper for your other unit testing libraries

For a nice discussion on the differences between the first three unit testing frameworks, see [this](http://pythontesting.net/podcast/pytest-vs-unittest-vs-nose-pt002/) article over at [pythontesting.net](http://pythontesting.net).

Again, there are lots of good testing tools out there. In this lecture we will use `unittest`, because it is part of the Python standard library.

#### A Simple Example

To use `unittest`, we'll first need a simple module (`cube.py`):

```python
def cube(x):
    '''An unnecessary function to find the
    cube of a number.
    '''
    return x**3
```

Now, let's write the module `cube_test.py`:

```python
import unittest
from cube import cube

class TestCube(unittest.TestCase):

    def setUp(self):
        pass

    def test_number_4(self):
        self.assertEqual(cube(4), 64)

    def test_negative_one(self):
        self.assertEqual(cube(-1), -1)

if __name__ == '__main__':
    unittest.main()
```

Notice `setUp()` can be used to load any information you want into the `TestCube` class. This can be handy if you need a more complex input for your function/method. You can instantiate a class from another part of your project, mock up a lot of fake data, or even create a temporary database for testing.

Also notice `assertEqual` is the meat of the test. It will throw an error if if arguments are not equal. There are several [other assert methods](https://docs.python.org/2/library/unittest.html#unittest.TestCase) built-into `TestCase`:

| Method | Checks that |
| ------ | ----------- |
| assertEqual(a, b) | a == b |
| assertNotEqual(a, b) | a != b  |
| assertTrue(x) | bool(x) is True  |
| assertFalse(x) | bool(x) is False  |
| assertIs(a, b) | a is b |
| assertIsNot(a, b) | a is not b |
| assertIsNone(x) | x is None |
| assertIsNotNone(x) | x is not None |
| assertIn(a, b) | a in b |
| assertNotIn(a, b) | a not in b |
| assertIsInstance(a, b) | isinstance(a, b) |
| assertNotIsInstance(a, b) | not isinstance(a, b) |

#### Running the Simple Example

Now, since the `cube_test.py` has a `main` function at the bottom of it, we can run the test on the command line:

    > python cube_test.py
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

To get more detailed output, we can use the `-v` flag:

    OK
    > python cube_test.py -v
    test_number_4 (__main__.TestCube) ... ok
    test_negative_one (__main__.TestCube) ... ok
     
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s
     
    OK

Here we get nice, human-friendly results for each of our tests. We have a unit test for our code and can execute it. That's really all you *need*. But on a larger project you will collect a lot of these testing modules, and you won't want to run them all by hand. As it happens, `unittest` has self-discovery functionality built-in so you can execute all your tests at once.

Let us say that both of the above modules are in the same directory (/super_math/). We can run all the `unittest` tests at once by doing:

    > python -m unittest discover super_math
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

Or, again, more verbosely:

    OK
    > python -m unittest discover -v super_math
    test_number_4 (test_cube_unittest.TestCube) ... ok
    test_negative_one (test_cube_unittest.TestCube) ... ok
     
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s
     
    OK

That's it! Rince and repeat and you can test all the Python you ever write.

## Why Bother?

If you're asking why bother, you're not the first person. The truth is, some people spend too much time worrying about the testing processes.

The truth is also that every software company in the world tests their code. As projects get bigger, not every single person committing code to the project will understand every function/class in the project.

Well-tested code tends to be less buggy. And the tests can save people time.

## Real-World Examples

GitHub is a great place to look for example Python projects. There are thousands of projects using the tools in this lecture. For two simple example Python projects using `setuptools`, take a look at two of my other projects on GitHub:

 * [mazelib](https://github.com/theJollySin/mazelib) - A Python algorithm library for creating and solving mazes.
 * [pytextgame](https://github.com/theJollySin/pytextgame) - A cross-platform text-game engine.

## Further Reading

 * [Testing Your Code](http://docs.python-guide.org/en/latest/writing/tests/) - From the wonderful people over at Hitchhiker's Guide to Python
 * [PyTesting.net](http://pythontesting.net/) - People who really care about this topic.
 * [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)


[Back to Syllabus](../../README.md)
