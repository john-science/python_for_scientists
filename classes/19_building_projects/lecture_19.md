# Building Python Projects

This lecture does not apply to stand-alone Python scripts. It's not even for small programs with one or two modules. This lecture is for Python projects that have gotten big enough to have several modules and be distributed to several people.

#### Installation

There are many libraries for testing and building Python projects. To keep this lecture from becoming its own course, we only show examples for the most standard tools (Python v2.7 or v3.2 or newer).

## A Build Process

Tests tend to be run automatically during the build process. For that reason, it would be hard to give an introduction to testing without talking about the build process.

There are a lot of different ways to build software, and a lot of different ways to run tests. So we will just touch the most common pathways, which use:

 * [DistUtils](https://docs.python.org/2/library/distutils.html) - The original tool for building and installing Python packages (no support for testing).
 * [setuptools](http://pythonhosted.org/an_example_pypi_project/setuptools.html) - Based on distutils, this is the standard tool for building and installing your Python code. It also allows you to register your code with [PyPi](https://pypi.python.org/pypi).
 * [easy_install](http://pythonhosted.org/setuptools/easy_install.html) - A tool that comes with `setuptools` to help you download, build, and install Python packages.
 * [VirtualEnv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) - The standard tool in Python for keeping the dependencies for different projects on the same machine separate.

### A Simple Example

Let's follow through on the `unittest` example from the last lecture, and test out a build environment on our script: `cube.py`:

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

### The setuptools Example

Let's redo our `unittest` example of `super_math` above, using `setuptools`.

First, we will need to layout our project something like this:

    super_math/
    |-- setup.py
    |-- super_math/
    |   |-- __init__.py
    |   |-- cube.py
    |-- test/
    |   |-- __init__.py
    |   |-- cube_test.py

(Quick Note: Since we are moving `cube_test.py` into a new directory, the import line at the top should now read: `from super_math.cube import cube`.)

Our `setup.py` will look like:

```python
from setuptools import setup

setup(name='super_math',
    version='0.1',
    description='A simple test of unittest.',
    packages=['super_math'],
    test_suite="test",
    zip_safe=False)
```

You can now run these tests on the command line by doing:

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

At this point, go ahead and feel justified if you feel like creating a Python project just got too complicated. All these libraries and tools and config files... Luckily, after you do this once it becomes easy boilerplate. More luckily, so many people have written that boilerplate that you can find many Python project templates online.

My favorite Python project template is Audreyr's [Cookie Cutter](https://github.com/audreyr/cookiecutter-pypackage) on [GitHub](https://www.github.com).

The Cookie Cutter has all kinds of useful tools built-in and laid out, ready for you to use:

 * [setuptools](http://pythonhosted.org/setuptools/) - for building and installation
 * [Sphinx](http://sphinx-doc.org/) - for attractive HTML code documenation
 * [VirtualEnv](http://virtualenv.readthedocs.org/en/latest/) - to keep your project separate from the rest of your computer
 * [TOX](http://tox.readthedocs.org/en/latest/) - to make keeping track of your VirtualEnv and running your tests
 * [GIT](http://www.git-scm.com/doc) - for your code repository

And if you don't want to use any these tools, you can just delete a couple of files from the template. Easy.

## Why Bother?

If you're asking why bother, you're not the first person. The truth is, some people spend too much time worrying about the build processes.

The truth is that the build process can be helpful and well thought out or it can waste a lof of your time.


## Real-World Examples

GitHub is a great place to look for example Python projects. There are thousands of projects using the tools in this lecture. For two simple example Python projects using `unittest`, take a look at two of my other projects on GitHub:

 * [mazelib](https://github.com/theJollySin/mazelib) - A Python algorithm library for creating and solving mazes.
 * [pytextgame](https://github.com/theJollySin/pytextgame) - A cross-platform text-game engine.

## Further Reading

 * [Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/) - A great reference for all facets of building a modern Python project.
 * [Audreyr's Cookie Cutter](https://github.com/audreyr/cookiecutter-pypackage) - Great boilerplate for a Python project.
 * [setuptools installs requires vs requirements](https://packaging.python.org/en/latest/requirements/) - An easy place to get confused, explained.


[Back to Syllabus](../../README.md)

 
 
