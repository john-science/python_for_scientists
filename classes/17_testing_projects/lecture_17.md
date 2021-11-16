# Unit Testing

Today we're going to begin the big conversation of testing code. This lecture does not apply to stand-alone Python scripts, or even small programs with one or two modules. The bigger a program gets, the more important testing becomes.

#### Installation

None! Everything we talk about today is part of the Python standard library.

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
 * [nose](http://pythontesting.net/framework/nose/nose-introduction)/ - built as an extension to unittest
 * [pytest](http://pythontesting.net/framework/pytest/pytest-introduction/) - Simple, easy-to-use, unit testing library
 * [mock](http://www.voidspace.org.uk/python/mock/) - A Java-style testing framework that allows you to replace components of your code with "mock" components with known results.
 * [tox](http://tox.readthedocs.org/en/latest/) - VirtualEnv management tool that acts as a wrapper for your other unit testing libraries

For a nice discussion on the differences between the first three unit testing frameworks, see [this](http://pythontesting.net/podcast/pytest-vs-unittest-vs-nose-pt002/) article over at [pythontesting.net](http://pythontesting.net).

Again, there are lots of good testing tools out there. In this lecture we will use `unittest`, just because it is part of the Python standard library.

#### A Simple Example

To use `unittest`, we'll put the `Student` class from our object-oriented lecture into a file called `student.py`:

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
        if percent_grade >= 90.0 and percent_grade <= 100.0:
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

Now we will create a file called `student_test.py` in the same folder and filling in a couple of basic tests.

```python
import unittest
from student import Student


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

Now, since the `student_test.py` has a `main` function at the bottom of it, we can run the test on the command line:

    > python student_test.py
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

To get more detailed output, we can use the `-v` flag:

    OK
    > python student_test.py -v
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

That's it! Rince and repeat and you can test all the Python you ever write.

#### More Practice

Let's add some more tests to `TestStudent`.

```python
class TestStudent(unittest.TestCase):
    # ...as before

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
```

And we run the test again:

    $ py student_test.py
    F..
    ======================================================================
    FAIL: test_better_than_perfect_grades (__main__.TestStudent)
    Test that this works for students with extra credit
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "student_test.py", line 36, in test_better_than_perfect_grades
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

    $ py student_test.py
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


## Why Bother?

If you're asking why bother, you're not the first person. The truth is, some people spend too much time worrying about the testing.

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
