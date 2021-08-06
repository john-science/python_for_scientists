# Building Python Projects with Setuptools

This lecture does not apply to stand-alone Python scripts. It's not even for small programs with one or two modules. This lecture is for Python projects that have gotten big enough to have several modules and be distributed to several people.

#### Installation

There are many libraries for testing and building Python projects. To keep this lecture from becoming its own course, we only show examples for the most standard tools (Python v2.7 or v3.2 or newer).

## A Build Process

Tests tend to be run automatically during the build process. For that reason, it would be hard to give an introduction to testing without talking about the build process.

There are a lot of different ways to build software, and a lot of different ways to run tests. So we will just touch the most command, and central, tools to building Python code:

 * [setuptools](http://pythonhosted.org/an_example_pypi_project/setuptools.html) - Based on distutils, this is the standard tool for building and installing your Python code. It also allows you to register your code with [PyPi](https://pypi.python.org/pypi).
 * [unittest](https://docs.python.org/3/library/unittest.html) - which we have already covered in a [different lecture](../17_testing_projects/lecture_17.md)

### A Simple Example

You will find a full copy of the example project we built in this lecture [here](gradebook/). Play around with it.

Let's follow through on the `unittest` example from the [last lecture](../17_testing_projects/lecture_17.md), and test out a build environment on our script: `student.py`:

```python
class Student:
    ''' A Student is a person currently enrolled in this awesome course. '''

    def __init__(self, name, sid):
        ''' return a Student object, with a name, id, and fresh grades '''
        self.name = name
        self.student_id = sid
        self.hw_grades = [0.0] * 10
        self.test_grades = [0.0, 0.0]

    def set_hw_grade(self, grade, week):
        ''' Set the grade for a specific homework '''
        self.hw_grades[week] = grade

    def set_test_grade(self, grade, exam):
        ''' Set the grade for a specific test '''
        self.test_grades[exam] = grade

    def calculate_grade(self):
        ''' Return the current grade of the student.
            Tests and homeworks are each worth 50%.
        '''
        average_hw_grade = sum(self.hw_grades) / len(self.hw_grades)
        average_test_grade = sum(self.test_grades) / len(self.test_grades)
        final_grade = (average_hw_grade + average_test_grade) / 2.0

        return final_grade

    @staticmethod
    def letter_grade(percent_grade):
        ''' return a letter grade from a percentage grade '''
        if percent_grade >= 90.0:
            return 'A'
        elif percent_grade >= 80.0:
            return 'B'
        elif percent_grade >= 70.0:
            return 'C'
        elif percent_grade >= 60.0:
            return 'D'
        else:
            return 'F'
```

While we're at it, let's copy over `student_test.py`:

```python
import unittest
from gradebook.student import Student

class TestStudent(unittest.TestCase):

    def test_no_grades(self):
        ''' Test that the constructor works, and that calculate_grade works when there are no grades '''
        charles = Student("Charlie Brown", 12345)
        self.assertEqual(charles.calculate_grade(), 0.0)

    def test_perfect_grades(self):
        ''' Test that this works for students with perfect grades '''
        emmy = Student("Emmy Noether", 14152)

        # set all of the grades to perfect
        emmy.set_test_grade(100.0, 0)
        emmy.set_test_grade(100.0, 1)
        for i in range(10):
            emmy.set_hw_grade(100.0, i)

        self.assertEqual(emmy.calculate_grade(), 100.0)

    def test_better_than_perfect_grades(self):
        ''' Test that this works for students with extra credit '''
        emmy = Student("Emmy Noether", 14152)

        # set all of the grades to perfect
        emmy.set_test_grade(100.0, 0)
        emmy.set_test_grade(110.0, 1)
        for i in range(10):
            emmy.set_hw_grade(100.0, i)

        final_grade = emmy.calculate_grade()
        self.assertEqual(final_grade, 102.5)
        self.assertEqual(Student.letter_grade(final_grade), 'A')

if __name__ == '__main__':
    unittest.main()
```

### The setuptools Example

Let's redo our `unittest` example of `gradebook` above, using `setuptools`.

First, we will need to layout our project something like this:

    gradebook/
    |-- setup.py
    |-- gradebook/
    |   |-- __init__.py
    |   |-- student.py
    |-- test/
    |   |-- __init__.py
    |   |-- student_test.py

(**Quick Note**: We moved `student_test.py` into a new directory, which is why the the import line at the top reads: `from gradebook.student import Student`. This is the only change from the [Unit Testing lecture](../17_testing_projects/lecture_17.md).)

Our `setup.py` will look like:

```python
from setuptools import setup

setup(name='gradebook',
      version='1.0',
      description='A simple test of setup.py and unittest.',
      packages=['gradebook'],
      test_suite="test",
      zip_safe=False)
```

You can now run these tests on the command line by doing:

    python setup.py test

And, if your tests pass, you will get something like this:

    running test
    running egg_info
    creating gradebook.egg-info
    writing gradebook.egg-info/PKG-INFO
    writing dependency_links to gradebook.egg-info/dependency_links.txt
    writing top-level names to gradebook.egg-info/top_level.txt
    writing manifest file 'gradebook.egg-info/SOURCES.txt'
    reading manifest file 'gradebook.egg-info/SOURCES.txt'
    writing manifest file 'gradebook.egg-info/SOURCES.txt'
    running build_ext
    test_better_than_perfect_grades (test.student_test.TestStudent)
    Test that this works for students with extra credit ... ok
    test_no_grades (test.student_test.TestStudent)
    Test that the constructor works, and that calculate_grade works when there are no grades ... ok
    test_perfect_grades (test.student_test.TestStudent)
    Test that this works for students with perfect grades ... ok

    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    OK


### Installing with SetupTools

We saw that we can use `python setup.py test` to test our code using `setuptools`. But now that we have a working `setup.py`, we can perform a lot of different build steps.

We can install our project to the system Python on our computer:

    python setup.py install

We can build our project (so it can only be imported locally):

    python setup.py build

We can clean a previous build:

    python setup.py clean

We can build a source distribution (tar ball, zip file, exe, etc..):

    python setup.py sdist

And [a lot more](http://pythonhosted.org/an_example_pypi_project/setuptools.html#using-setup-py).


### The Cookie Cutter

Okay, you can go a long way with just the basics above. But you may have some special needs that you will need more special tools to solve. Or maybe you just want to use the same boilerplate setup.py and project build tools al the time.

Luckily, so many people have written that boilerplate that you can find many Python project templates online. Just copy/paste their project and it has all the tools you want in place and working. And you can get back to the business of actually writing your code.

My favorite Python project template is [Audreyr's Cookie Cutter](https://github.com/audreyr/cookiecutter-pypackage) on GitHub.

The Cookie Cutter has all kinds of useful tools built-in and laid out, ready for you to use:

 * [setuptools](http://pythonhosted.org/setuptools/) - for building and installation
 * [Sphinx](http://sphinx-doc.org/) - for attractive HTML code documenation
 * [VirtualEnv](http://virtualenv.readthedocs.org/en/latest/) - to keep your project separate from the rest of your computer
 * [TOX](http://tox.readthedocs.org/en/latest/) - to make keeping track of your VirtualEnv and running your tests
 * [GIT](http://www.git-scm.com/doc) - for your code repository

And if you don't want to use any these tools, you can just delete a couple of files from the template. Easy.


## Why Bother?

Using `distutils` and a `setup.py` file helps other people install your code. It is how most people drive their unit tests. And if you're a Cython user, it's how most people compile their code. As projects grow in complexity and more people use them, you will find more and more reasons to have a smooth build process.


## Real-World Examples

You will find a full copy of the example project we built in this lecture [here](gradebook/). Play around with it.

GitHub is a great place to look for example Python projects. There are thousands of projects using the tools in this lecture. For two simple example Python projects using `unittest`, take a look at two of my other projects on GitHub:

 * [mazelib](https://github.com/john-science/mazelib) - A Python algorithm library for creating and solving mazes.
 * [pytextgame](https://github.com/john-science/pytextgame) - A cross-platform text-game engine.


## Further Reading

 * [Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/) - A great reference for all facets of building a modern Python project.
 * [Audreyr's Cookie Cutter](https://github.com/audreyr/cookiecutter-pypackage) - Great boilerplate for a Python project.
 * [setuptools installs requires vs requirements](https://packaging.python.org/en/latest/requirements/) - An easy place to get confused, explained.


[Back to Syllabus](../../README.md)
