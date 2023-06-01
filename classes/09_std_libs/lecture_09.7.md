# Decorators

Python decorators are a little piece of [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) that will finish off our understanding of the Python language syntax.


## What is a Decorator?

A "decorator" is a wrapper you define around a function or classs in Python. A decorator might allow you to modify the inputs or outputs of a function. A decorator might allow you to wrap different functions with the same error / validity checking logic.

We will have to look at some examples, but decorators are a great way to write logic to "wrap around" other logic.  It's a useful and powerful idea, once you have used it a couple of times.


## Toy Examples

Theory is great. But let's stop being vague and show some real (if toy) examples of building our own decorators. THEN we can talk about what they are in more detail.


### Time a Method

Let's say you want to time a function (here our function will just wait one second, but imagine it's more interesting):

```python
import time

def wait_one_sec():
    time.sleep(1)

t = time.time()
wait_one_sec()
print(time.time() - t)
```

If you run this code, you'll get something _juuuust_ over one second:

```bash
λ python decorators.py
1.0148913860321045
```

So, great. It worked. But now you might want to time a second function, and a third. And this might be something you want to do ALL the time. Well, remember the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle: Don't Repeat Yourself. It's bad practice when writing code to copy/paste all over the place.

Happily, Python provides us a handy tool for this: decorators.

```python
import time

def time_it(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print(time.time() - t)
        return res

    return wrapper


@time_it
def wait_one_sec():
    time.sleep(1)


wait_one_sec()
```

The `time_it()` function above is really the exciting part here. It takes in any function (`func`), and returns a "wrapper". The word "wrapper" was chosen because we are still calling the `func` function, but we are doing some stuff before and after it. So we say we are "wrapping" one piece of code with other logic.

With the `time_it()` function returning a wrapper function, and that allows us to do `@time_it` before our method. This `@` syntactic sugar is how we _apply_ our wrapper to our function.  (This also works for classes.)

#### What did we learn?

> A decorator is a special function that takes in any function and returns a wrapper function. Then we can use the `@` syntax to apply our decorator to a function.


### Validate the Inputs

Let's say you have a lot of code with physically-meaningful numbers: masses, volumes, temperatures in Kelvin. For scientists and engineers this is a _really_ common situation (it happens to me all the time). But what you probably don't want to do is clutter your code with a million "check this number is positive":

```python
def some_math(a, b, c=0, d=0):
    assert a >= 0
    assert b >= 0
    assert c >= 0
    assert d >= 0
    return (c + d) / (a + b)
```

That code is certainly easy to read and understand. It's simple. That's all good. But it also violates our [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle. And just imagine if these checks were on hundreds of functions!

Now, this may not be ideal in the wild, but let's build a toy example to solve this problem:

```python
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            assert arg >= 0

        for val in kwargs.values():
            assert val >= 0

        return func(*args, **kwargs)

    return wrapper


@validate_positive
def some_math(a, b, c=0, d=0):
    return (c + d) / (a + b)


some_math(1, 2, 3, 4)  # passes
some_math(1, 0, 1, 0)  # passes
some_math(1, 2, 3, -4)  # fails
```


## Standard Library Examples

Python decoartors are super helpful, and as such you will find them _all over_ the standard libraries, and in many third-party libraries. You'll find a good list [here](https://github.com/lord63/awesome-python-decorator).


### staticmethod

One of the original uses of decorators in Python is the `@staticmethod`, which identifies a method on a class that doesn't need access to the `self` object:

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grade = 100.0

    def getName(self):
        return self.name

    @staticmethod
    def get_letter_grade(num):
        if num >= 90:
            return "A"
        elif num >= 80:
            return "B"
        elif num >= 70:
            return "C"
        elif num >= 60:
            return "D"
        else:
            return "F"
```


### property

A more recent, but super helpufl tool is Python's `@proprety` system, which allows you to create Java-like setters and getters for class attributes in ARMI:

```python
class Student:
    def __init__(self, name):
        self.name = name
        self._grades = [100.0, 95.0]

    @property
    def grade(self):
        return sum(self._grades) / len(self._grades)

    @grade.setter
    def grade(self, value):
        assert value >= 0.0
        assert value <= 100.0
        self._grades.append(value)
```

And there are just [so many more examples](https://github.com/lord63/awesome-python-decorator) of Python decorators.


## Further Reading

 * [Geeks for Geeks](https://www.geeksforgeeks.org/decorators-in-python/)
 * [Python Basics](https://pythonbasics.org/decorators/)
 * [Programiz](https://www.programiz.com/python-programming/decorator)
 * [Python decorator list: std libs and found in the wild](https://github.com/lord63/awesome-python-decorator)

[Back to Syllabus](../../README.md)
