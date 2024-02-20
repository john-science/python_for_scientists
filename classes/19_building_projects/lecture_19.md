# Laying out a New Python Project

At some point, you will want to build a real "Python project". That is, you will want to write Python code that other people can `import` or install. It will be several Python files workign together.

In this lecture, we will work through an example of how to layout a Python project. We will not attempt to show _every_ possible approach, but our example should be a good paradigm to start with for most projects.

Our whole project will only have one Python file, but these same tools would work even if we had thousands of Python files.

## A Build Process

There are a lot of different ways to build software, and a lot of different ways to run tests. But we have to pick something:

 * [setuptools](http://pythonhosted.org/an_example_pypi_project/setuptools.html) - This is still the standard tool for building and installing Python code.
 * [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html) - This is the standard Python tool to run unit tests.

### A Simple Example

You will find a full copy of the example project we built in this lecture [here](gradebook/). Play around with it.

Let's follow through on the `unittest` example from the [testing lecture](../17_testing_projects/lecture_17.md), and test out a build environment on our file: `student.py`:

```python
class Student:
    """A Student is a person currently enrolled in this awesome course."""

    def __init__(self, name, sid):
        """Return a Student object, with a name, id, and fresh grades."""
        self.name = name
        self.student_id = sid
        self.hw_grades = [0.0] * 10
        self.test_grades = [0.0, 0.0]

    def set_hw_grade(self, grade, week):
        """Set the grade for a specific homework."""
        self.hw_grades[week] = grade

    def set_test_grade(self, grade, exam):
        """Set the grade for a specific test."""
        self.test_grades[exam] = grade

    def calculate_grade(self):
        """
        Return the current grade of the student.

        (Tests and homeworks are each worth 50%.)
        """
        average_hw_grade = sum(self.hw_grades) / len(self.hw_grades)
        average_test_grade = sum(self.test_grades) / len(self.test_grades)
        final_grade = (average_hw_grade + average_test_grade) / 2.0

        return final_grade

    @staticmethod
    def letter_grade(percent_grade):
        """Return a letter grade from a percentage grade."""
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

It would be hard to give an introduction to laying out a Python project without mentioning testing.

So, while we're at it, let's copy over `test_student.py`:

```python
import unittest
from gradebook.student import Student

class TestStudent(unittest.TestCase):

    def test_no_grades(self):
        """Test that the constructor works, and that calculate_grade works when there are no grades."""
        charles = Student("Charlie Brown", 12345)
        self.assertEqual(charles.calculate_grade(), 0.0)

    def test_perfect_grades(self):
        """Test that this works for students with perfect grades."""
        emmy = Student("Emmy Noether", 14152)

        # set all of the grades to perfect
        emmy.set_test_grade(100.0, 0)
        emmy.set_test_grade(100.0, 1)
        for i in range(10):
            emmy.set_hw_grade(100.0, i)

        self.assertEqual(emmy.calculate_grade(), 100.0)

    def test_better_than_perfect_grades(self):
        """Test that this works for students with extra credit."""
        emmy = Student("Emmy Noether", 14152)

        # set all of the grades to perfect
        emmy.set_test_grade(100.0, 0)
        emmy.set_test_grade(110.0, 1)
        for i in range(10):
            emmy.set_hw_grade(100.0, i)

        final_grade = emmy.calculate_grade()
        self.assertEqual(final_grade, 102.5)
        self.assertEqual(Student.letter_grade(final_grade), 'A')
```

### The Project Layout

First, we will need to layout our project something like this:

    gradebook/
    |-- pyproject.toml
    |-- gradebook/
    |   |-- __init__.py
    |   |-- student.py
    |   |-- test/
    |       |-- __init__.py
    |       |-- test_student.py

Those `__unit__.py` files are emtpy. They tell Python that a directory contains Python code. Any directory underneath `gradebook/` that has a `__init__.py` file will be included in your package.

Obviously, our codebase inside `gradebook/` could be much more complicated. For instance, we might have many, many `*.py` files in various folder/directories. But we're just trying to make this example easy to parse.

> NOTE: We moved `test_student.py` into a new directory, which is why the the import line at the top reads: `from gradebook.student import Student`. This is the only change from the [Unit Testing lecture](../17_testing_projects/lecture_17.md).)

### The pyproject.toml file

The `pyproject.toml` file is a place to centralize _all kinds_ of things you might want to do with your Python project:

* Building it
* Deploying it
* Managing dependencies
* Managing what version you are on
* Managing licenses
* Managaing linting
* Managing testing

The `pyproject.toml` file in our project will be very short. But it will give us some flavor of what these files can look like.

Our `pyproject.toml` will look like:

```toml
[build-system]
requires = ["setuptools>=61.2"]
build-backend = "setuptools.build_meta"

[project]
name = "gradebook"
version = "2.0.0"

[project.optional-dependencies]
test = ["pytest"]

[tool.setuptools.packages]
find = {}
```

For a full guide to the `pyproject.toml` file and packaging Python projects, see [the official documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/).


### Installing with Pip

The typical way that you wil install Python code is to first create a [VirtualEnvironment](../22_virtualenv/lecture_2.md) and then use `pip`. On the command-line, from the same directory as your `pyproject.toml` file run:

    pip install -e .

That line will install our package in our local env (hopefuly a VirtualEnv), by looking at the code in these folders. But it will also go online and grab any depenencies we have. (A dependency is someone else's code, that your code needs to work.)

In this case, we didn't define any dependencies, except for testing, so if we want to install our code AND all the extra things we will need to run our tests, we would run this on the command-line:

    pip install -e .[test]

Because of the `test = ["pytest"]` in our `pyproject.toml` file, running that command will install our code _plus_ the `pytest` library which we will use to run our tests.


### Running the Unit Tests

As above, to run our tests, we will type this at the command-line:

    pip install -e .[test]

And then we can run the tests from the command-line by running:

    pytest gradebook

And, if your tests pass, you will get something like this:

```bash
λ pytest gradebook
=================== test session starts ===================
...
collected 3 items

gradebook\test\test_student.py ...                   [100%]

==================== 3 passed in 0.01s ====================
```

Success!


## Further Reading

Okay, "designing software" is a big topic. As is "tools to build Python projects". But, honestly, these are the basics. And the official docs have a huge amount of detail if you're interested:

 * [Official Python Packaging Homepage](https://packaging.python.org/en/latest/)
 * [Official Python Packaging Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
 * [Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/) - A great reference for all facets of building a modern Python project.


[Back to Syllabus](../../README.md)
