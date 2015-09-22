# Testing Python Projects

First, a quick note: this lecture is not for single Python scripts. It's not even for small programs with one or two modules. This lecture is for Python projects that have gotten big enough to have several modules and get distributed to several people.

#### Installation

There are many libraries for testing and building Python projects. To keep this lecture from becoming its own course, we will select some of the most standard tools and ignore the rest.

## Unit Tests

A [developer's mantra](http://c2.com/cgi/wiki?MakeItWorkMakeItRightMakeItFast):

    Make it work.
    Make it right.
    Make it fast.

Today we'll talk about that second thing: let's make sure our code is *right*. By *right* we mean producing the desired outputs. And the only way to know if your code is "right" is to test it.

#### Different Types of Software Tests

Without getting too pedantic, there are generally three kinds of [software testing](https://en.wikipedia.org/wiki/Software_testing):

 * [Unit Tests](https://en.wikipedia.org/wiki/Unit_testing) - Testing each piece of your code on the smallest level (functions and methods).
 * [Integration Tests](https://en.wikipedia.org/wiki/Integration_testing) - Testing the connections between different pieces of your code.
 * [System Tests](https://en.wikipedia.org/wiki/System_testing) - Full end-to-end testing of your software as whole.

As your project gets larger, the items lower on this list become more important. But everything starts with unit testing. If you don't know if and how the smallest pieces of your code is working, larger-scale tests will be less useful.

#### Why Unit Test?

Unit Tests will answer several questions, that become more important as the size of your code base and your user base increase:

 * Does every single function or method produce the results I want for typical inputs?
 * What about for edge cases?
 * Every time I make a change to the code, how can I check that I didn't break something else?

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

    def cube(x):
        '''An unnecessary function to find the
        cube of a number.
        '''
        return x**3

Now, let's write the module `test_cube.py`:

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

Notice `setUp()` can be used to load any information you want into the `TestCube` class. This can be handy if you need a more complex input for your function/method. You can instantiate a class from another part of your project, mock up a lot of fake data, or even create a temporary database for testing.

Also notice that `assertEqual`, it is the meat of the test. It will throw an error if if arguments are not equal. There are [many other](https://docs.python.org/2/library/unittest.html#unittest.TestCase) assert methods built-into `TestCase`:

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

Now, since the `test_cube.py` has a `main` function at the bottom of it, we can run the test on the command line:

    > python test_cube.py
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

To get more detailed output, we can use the `-v` flag:

    OK
    > python test_cube.py -v
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

## The Build Process

Tests tend to be run automatically during the build process. For that reason, it would be hard to give an introduction to testing without talking about the build process.

There are a lot of tools in the Python ecosystem for helping you handle all the facets of building and distributing your code. The most standard (and useful) tools you'll want to know about are:

 * [DistUtils](https://docs.python.org/2/library/distutils.html) - The original tool for building and installing Python packages (no support for testing).
 * [setuptools](http://pythonhosted.org/an_example_pypi_project/setuptools.html) - Based on distutils, this is the standard tool for building and installing your Python code. It also allows you to register your code with [PyPi](https://pypi.python.org/pypi).
 * [easy_install](http://pythonhosted.org/setuptools/easy_install.html) - A tool that comes with `setuptools` to help you download, build, and install Python packages.
 * [VirtualEnv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) - The standard tool in Python for keeping the dependencies for different projects on the same machine separate.

### The setuptools Example

Let's redo our `unittest` example of `super_math` above, using `setuptools`.

First, we will need to layout our project something like this:

    super_math/
    |-- setup.py
    |-- super_math/
    |   |-- __init__.py
    |   |-- cube.py
    |-- tests/
    |   |-- __init__.py
    |   |-- test_cube.py

(Quick Note: Since we are moving `test_cube.py` into a new directory, the import line at the top should now read: `from super_math.cube import cube`.)

Our setup.py will look like:

    import os
    import sys
    import unittest
    from setuptools import setup, find_packages
    from setuptools.command.test import test
    
    class DiscoverTest(test):
    
        def finalize_options(self):
            test.finalize_options(self)
            self.test_args = []
            self.test_suite = True
    
        def run_tests(self):
            # get setup.py directory and then tests directory
            setup_file = sys.modules['__main__'].__file__
            setup_dir = os.path.abspath(os.path.dirname(setup_file))
            test_dir = os.path.join(setup_dir, 'tests')
    
            # use the default shared TestLoader instance
            test_loader = unittest.defaultTestLoader
    
            # use the basic test runner that outputs to sys.stderr
            test_runner = unittest.TextTestRunner()
    
            # automatically discover all tests
            # NOTE: only works for python 2.7 and later
            test_suite = test_loader.discover(test_dir)
    
            # run the test suite
            test_runner.run(test_suite)
    
    setup(
        name='super_math2',
        version='0.0.1',
        description="A Simple setuptools Test",
        cmdclass={'test': DiscoverTest}
    )

Now, all you really need is the `setup` function in that script. The `DiscoverTest` is my own personal convenience (found on [this]() StackOverflow post) used to run all of your unit tests simply by typing this on the command line:

    python setup.py test

And, if your tests pass, you will get something like this:

    $ python setup.py test
    running test
    running egg_info
    writing super_math.egg-info/PKG-INFO
    writing top-level names to super_math.egg-info/top_level.txt
    writing dependency_links to super_math.egg-info/dependency_links.txt
    reading manifest file 'super_math.egg-info/SOURCES.txt'
    writing manifest file 'super_math.egg-info/SOURCES.txt'
    running build_ext
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s
    
    OK

If there are errors, you will get a lot more information about the tests that ran. The `DiscoverTest` class hides the results of passing tests.

### Installing with SetupTools

We saw that we can use `python setup.py test` to test our code using `setuptools`. But now that we have a working `setup.py`, we can perform a lot of different build steps.

We can build our project:

    python setup.py build

We can clean a previous build:

    python setup.py clean

We can build a source distribution (tar ball, zip file, exe, etc..):

    python setup.py sdist

We can install our project to the local Python on our computer:

    python setup.py install

And [a lot more](http://pythonhosted.org/an_example_pypi_project/setuptools.html#using-setup-py).

### The Cookie Cutter

At this point, go ahead and feel justified if you feel like creating a Python project just got too complicated. All these libraries and tools and config files... Luckily, after you do this once it becomes easy boilerplate. More luckily, so many people have written that boilerplate that you can just download Python project templates online.

My favorite Python project template is Audreyr's [Cookie Cutter](https://github.com/audreyr/cookiecutter-pypackage) over on [GitHub](https://www.github.com).

The Cookie Cutter has all kinds of useful tools built-in and laid out, ready for you to use:

 * [setuptools](http://pythonhosted.org/setuptools/) - for building and installation
 * [Sphinx](http://sphinx-doc.org/) - for nice, HTML code documenation
 * [VirtualEnv](http://virtualenv.readthedocs.org/en/latest/) - to keep your project separate from the rest of your computer
 * [TOX](http://tox.readthedocs.org/en/latest/) - to make keeping track of your VirtualEnv and running your tests
 * [GIT](http://www.git-scm.com/doc) - for your code repository

And if you don't want to use any these tools, you can just delete a couple of files from the template. Easy.

## Why Bother?

If you're asking why bother, you're not the first person. The truth is, some people spend too much time worrying about the whole testing and building processes.

The truth is also that every software company in the world tests their code. As projects get bigger (both in lines of code and in number of developers) it becomes impossible that everyone will be able to keep every part of the project in their minds at all times. People are busy.

Well-tested code tends to be less buggy. And its bugs tend to get found faster.

## Further Reading

 * [Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/) - A great reference for all facets of building a modern Python project.
 * [Audreyr's Cookie Cutter](https://github.com/audreyr/cookiecutter-pypackage)
 * [Testing Your Code](http://docs.python-guide.org/en/latest/writing/tests/) - From the wonderful people over at Hitchhiker's Guide to Python
 * [PyTesting.net](http://pythontesting.net/)
 * [setuptools installs requires vs requirements](https://packaging.python.org/en/latest/requirements/) - An easy place to get confused, explained.


[Back to Syllabus](../../README.md)
