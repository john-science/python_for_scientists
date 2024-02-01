# Unit Testing

Today we're going to begin the big conversation of testing code. This lecture does not apply to stand-alone Python scripts, or even small programs with one or two modules. The bigger a program gets, the more important testing becomes.

#### Installation

In today's lecture we will cover two testing frameworks: `unittest` and `pytest`.
The `unittest` framework is included with python, and no additional work is required if python is already installed.
The `pytest` framework is widely availble with `pip`, `conda`, or virtually any other python package manager.


## Unit Tests

A [developer's mantra](http://c2.com/cgi/wiki?MakeItWorkMakeItRightMakeItFast):

    Make it work.
    Make it right.
    Make it fast.

Today we'll talk about that second thing: let's make sure our code is *right* (that it produces the desired outputs). And the only way to know if your code is *right* is to test it.

#### Different Types of Software Tests

Without getting too pedantic, there are generally three kinds of [software testing](https://en.wikipedia.org/wiki/Software_testing):

 * [Unit Tests](https://en.wikipedia.org/wiki/Unit_testing) - Testing each piece of your code on the smallest level (functions and methods).
 * [Integration Tests](https://en.wikipedia.org/wiki/Integration_testing) - Testing the connections between different pieces of your code.
 * [System Tests](https://en.wikipedia.org/wiki/System_testing) - Full end-to-end testing of your software as whole.

As your project gets larger, the items lower on this list become more important. But everything starts with unit tests.

So today we will just focus on unit tests.

#### Why Unit Test?

Unit Tests will answer several questions, that become more important as the size of your code base and your user base increase:

 * Does every single function or method produce the results I want for typical inputs?
 * What about for edge cases?
 * When I make a change to the code, how can I be sure I didn't break something elsewhere in the code?

A logical follow-up question will be:

 * How can I automate this process, so testing code doesn't take up all my time?

#### Unit Testing Frameworks

Software testing is an increasingly big topic, and there are a lot of good tools out there to help you test your software. Perhaps five of the most popular tools in Python are:

 * [unittest](http://pythontesting.net/framework/unittest/unittest-introduction/) - in the Python standard library
 * [mock](http://www.voidspace.org.uk/python/mock/) - A  way to test untestable code, and a great way to keep your code and your tests maintainable
 * [nose](http://pythontesting.net/framework/nose/nose-introduction) - built as an extension to unittest
 * [pytest](https://docs.pytest.org/en/8.0.x/) - Simple, easy-to-use, unit testing library.
 * [tox](http://tox.readthedocs.org/en/latest/) - VirtualEnv management tool that acts as a wrapper for your other unit testing libraries

For a nice discussion on the differences between the first three unit testing frameworks, see [this](http://pythontesting.net/podcast/pytest-vs-unittest-vs-nose-pt002/) article over at [pythontesting.net](http://pythontesting.net).

Again, there are lots of good testing tools out there. In this lecture we will first present `unittest`, because it is part of the Python standard library. A brief introduction to `pytest` will follow because it is a popular alternative to `unittest`.

#### A Simple Example

To use `unittest`, we'll put the `Student` class from our object-oriented lecture into a file called `student.py`:

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
            return "A"
        elif percent_grade >= 80.0:
            return "B"
        elif percent_grade >= 70.0:
            return "C"
        elif percent_grade >= 60.0:
            return "D"
        else:
            return "F"
```

Now we will create a file called `test_student.py` in the same folder and filling in a couple of basic tests.

```python
import unittest

from student import Student


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


if __name__ == '__main__':
    unittest.main()
```

Okay, so we have some unit tests. Let's try and unpack all of that.

First things first, if you want a unit test, just subclass `unittest.TestCase`, that brings with it all the architecture you need to automate your testing. Also, notice that we added `unittest.main()` to the main block. That means we can now call this script from the command line to run all the tests. That's handy!

There is a little magic happening here. Any method whose name starts with "test" is a unit test. That is, `TestCase` handles finding all methods with these names and running them as tests. You can put other helper methods in this class and they won't be run as unit tests. This is *super handy*, but also falls into the realm of invisible magic so don't code like this yourself.

Basically, in each "test" method, you will see that we use the `Student` class, and then test it's output. In both of the tests above `assertEqual` is the meat of the test. It will throw an error if if arguments are not equal. There are several [other assert methods](https://docs.python.org/2/library/unittest.html#unittest.TestCase) built-into `TestCase`:

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

Now, since the `test_student.py` has a `main` function at the bottom of it, we can run the test on the command line:

    > python test_student.py
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

To get more detailed output, we can use the `-v` flag:

    OK
    > python test_student.py -v
    test_no_grades (__main__.TestStudent)
    Test that the constructor works, and that calculate_grade works when there are no grades ... ok
    test_perfect_grades (__main__.TestStudent)
    Test that this works for students with perfect grades ... ok
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s
    OK

Here we get nice, human-friendly results for each of our tests. We have a unit test for our code and can execute it. That's really all you *need*. But on a larger project you will collect a lot of these testing modules, and you won't want to run them all by hand. As it happens, `unittest` has self-discovery functionality built-in so you can execute all your tests at once.

Let us say that both of the above modules are in the same directory (/python_class/). We can run all the `unittest` tests at once by doing:

    > python -m unittest discover python_class
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

Or, again, more verbosely:

    > python -m unittest discover -v python_class

That's it! Rinse and repeat and you can test all the Python you ever write.

#### More Practice

Let's add some more tests to `TestStudent`.

```python
class TestStudent(unittest.TestCase):
    # ...as before

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
        self.assertEqual(Student.letter_grade(final_grade), "A")
```

And we run the test again:

    $ py test_student.py
    F..
    ======================================================================
    FAIL: test_better_than_perfect_grades (__main__.TestStudent)
    Test that this works for students with extra credit
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "test_student.py", line 36, in test_better_than_perfect_grades
        self.assertEqual(Student.letter_grade(final_grade), 'A')
    AssertionError: 'B' != 'A'
    - B
    + A
    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s
    FAILED (failures=1)

Oops. Wait. What? 102.5% final grade is a B? What?

Okay, it turns out this line in `letter_grade` is the culprit:

```python
if percent_grade >= 90.0 and percent_grade <= 100.0:
```

Grades over 100% are excluded from being As! Okay, we can fix that by changing the code:

```python
if percent_grade >= 90.0:
```

And now are unit tests run great again:

    $ py test_student.py
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s
    OK

We might want to write a lot more unit tests for the `Student` class, actually. We could do this to ensure that even when someone changes little things in the code, the functionality we want still persists:

* Entering a homework grade for homework #11 should throw an error.
* A student with 100% on the tests and 0% on the homeworks should get a 50% in the class.
* A student with 0% on the tests and 100% on the homeworks should get a 50% in the class.
* A student with a 69.9% should get a D.
* A student with a 79.9% should get a C.
* A student with a 90.0001% should get an A.

We might also use unit tests to help us make important design decisions:

* Can students get negative grades?
* If a student is within 0.1% of getting a higher final grade... can't we just round up?
* If we want to drop the lowest homework grade... how does that effect our code?

Try writing unit tests for all of the above. See what happens!

## Good Unit Tests and Testable Code

Some code is more testable than others. If you write code that calls an external executable, or calls out to the internet for information, your code _might_ be fine, but testing your code will be slow (if your executable takes more than 1ms to run) or flaky (internet connections aren't guaranteed).

This leads us to an important idea in software testing: "mocking". When you write a unit test, you want to test the smallest possible piece of your code (say, one small function/method or even just part of one). But software is often heavily inter-connected or (as suggested above), your code makes a call out to something external. In all these cases, we can insert some "mocked" code that fakes an external interface to the small part of code we are testing.

### Example: Getting the world population from Wikipedia

For our example, we're going to write a little piece of code that scrapes a Wikipedia page and gets the world's total population. (As a side note, this code is a bad idea, but we are only concerned with testing here.)

The simple version of this code would be:

```python
import requests

CSV_PATH = "world_pop.csv"
WIKI_POP_URL = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

def get_world_pop(url=WIKI_POP_URL, csv_path=CSV_PATH):
    pops = get_world_pop_wikipedia(url)
    return sum_values(pops)
```

As you can see, our straw-man code goes two Wikipedia, scrapes some data (population by country) and then returns the sum.

In detail, let's put this code in `world_pop.py`:

```python
import requests

WIKI_POP_URL = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

def get_world_pop(url=WIKI_POP_URL, csv_path=CSV_PATH):
    """Get the world population from Wikipedia."""
    pops = get_world_pop_wikipedia(url)
    return sum_values(pops)

def get_world_pop_wikipedia(url):
    """NOTE: This is a terrible way to parse HTML. Use BeautifulSoup."""
    r = requests.get(url)
    rows = str(r.content).split("<table")[1].split("table>")[0].split("<tr")[2:-1]

    pops = {}
    for row in rows:
        country = row.split("<td")[1].split("</a>")[0].split(">")[-1]
        pop = int(row.split("<td")[5].split("<")[0].split(">")[1].replace(",",""))
        pops[country] = pop
    
    return pops

def sum_values(dct):
    """Return the sum of all the values in a dictionary."""
    if len(dct):
        return sum(dct.values())
    else:
        return 0
```

Okay, now that we have the above code (which worked in early 2023), we can write a simple test (in `test_world_pop.py`):

```python
import unittest
import world_pop

class TestWorldPop(unittest.TestCase):
    def test_sum_values(self):
        # Test Case: empty dict
        d = {}
        self.assertEqual(world_pop.sum_values(d), 0)

        # Test Case: mixed integers and floats
        d = {"a": 1, "b": 2.2}
        self.assertEqual(world_pop.sum_values(d), 3.2)

        # Test Case: large set of values
        d = {str(i): i for i in range(100)}
        self.assertEqual(world_pop.sum_values(d), 4950)

if __name__ == "__main__":
    unittest.main()
```

Here, we have only tested one of the three functions in `world_pop.py`, of course. We could imagine writing a test of the whole system:

```python
    def test_world_pop_end2end(self):
        self.assertEqual(world_pop.get_world_pop(), 7975105156)
```

But the above test, I argue strongly, is horrible.  For several reasons:

* Wikipedia WILL update this page regularly, so the exact number here will change.
* Wikipedia might change the URL to this page. Or the exact contents of this page might change.
* This test fails if you don't have internet access.
* **More importantly**, this test doesn't just test our code, we are doing a lot of work to run our external sources.
  * This means the test will run in several seconds, instead of milliseconds.
  * But the greater concern is test maintainability, and not just run time.

Finally, with all this "world pop" background, we can talk about "mocking". In this case, what we would LOVE to do is fake (mock) the internet call to Wikipedia, and just have a set unit test tool return some default/known HTML to us. And then our test will only TEST our code, and we are no longer call out to the internet.

Such a test might look like:

```python
import unittest
from unittest.mock import MagicMock, patch
import world_pop

EX_HTML = """<!DOCTYPE html><html><head></head><body><table>
<thead><th></th><th>Country</th><th>region</th><th>subregion</th><th>pop1</th><th>pop2</th><th>Change</th></thead><tr></tr>
<tr>::before<td><a>Aba</a></td><td>Asia</td><td>East Asia</td><td>400</td><td>401</td><td>+0.25%</td></tr>
<tr>::before<td><a>Bac</a></td><td>Asia</td><td>East Asia</td><td>100</td><td>101</td><td>+1.0%</td></tr>
<tr></tr></table></body></html>"""

class TestWorldPop(unittest.TestCase):
    # other tests...
    @patch('world_pop.requests')
    def test_world_pop_end2end(self, mock_requests):
        # mock the response return value of the get() method
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = EX_HTML
        mock_requests.get.return_value = mock_response

        # check that the code returns the test value from test HTML
        self.assertEqual(world_pop.get_world_pop(), 502)

if __name__ == "__main__":
    unittest.main()
```

First, you can ignore the `EX_HTML` above, we just hard code some test/sample/example HTML data that matches what we expect to see on Wikipedia. Of course, for brevity, we only include two countries (and 502 people here), instead of ALL countries.

More importantly, see that we have used `unittest.mock.patch` to NOT really call `requests.get()` but replace that code with a `MagicMock` that returns the data we want. This is the crux we need to understand to build fast, maintainabe tests. And mocking allows us to easily write tests for code that would otherwise _seem_ untestable.

## Pytest

[Pytest](https://docs.pytest.org/en/8.0.x/) is a popular alternative to unittest.
One nice feature is that tests that have been written with the unittest framework can already be run with pytest.
For example, the file `test_student.py` can be run on the command line as follows:

    > pytest test_student.py
    ============================= test session starts ==============================
    platform <platform info>
    rootdir: <path to rootdir>
    collected 3 items

    test_student.py ...                                                      [100%]

    ============================== 3 passed in 0.00s ===============================


Some advantages that pytest has over unittest is that it enables more pythonic ways to write unit tests, and it has many [helpful plugins](https://docs.pytest.org/en/8.0.x/reference/plugin_list.html#plugin-list).
There are two python projects worth mentioning that are compatible with pytest are [hypothesis](https://hypothesis.readthedocs.io/en/latest/) and [pytest-dependency](https://pypi.org/project/pytest-dependency/).

For more information on how to get started with pytest checkout the [Get Started](https://docs.pytest.org/en/8.0.x/getting-started.html#get-started) page for a basic introduction.
For a more indepth introduction [this two hour tutorial](https://www.youtube.com/watch?v=LX2ksGYXJ80) covers pytest in scientific computing applications.


## Why Bother?

If you're asking why bother, you're not the first person. But most teams lose a lot of time and energy because their code isn't tested enough.

The truth is also that every software company in the world tests their code. As projects get bigger, not every single person committing code to the project will understand every function/class in the project.

Well-tested code tends to be less buggy. And the tests can save people time.


## Real-World Examples

GitHub is a great place to look for example Python projects. There are thousands of projects using the tools in this lecture. For two simple example Python projects using `setuptools`, take a look at two of my other projects on GitHub:

 * [mazelib](https://github.com/john-science/mazelib) - A Python algorithm library for creating and solving mazes.
 * [pytextgame](https://github.com/john-science/pytextgame) - A cross-platform text-game engine.


## Further Reading

 * [Testing Your Code](http://docs.python-guide.org/en/latest/writing/tests/) - From the wonderful people over at Hitchhiker's Guide to Python
 * [PyTesting.net](http://pythontesting.net/) - People who really care about this topic.
 * [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)


[Back to Syllabus](../../README.md)
