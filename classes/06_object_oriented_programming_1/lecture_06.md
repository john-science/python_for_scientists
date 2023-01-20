# Object-Oriented Programming, Part 1

[Object-Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming) (OOP) means programming with [classes](https://en.wikipedia.org/wiki/Class_%28computer_programming%29). The "class" is a fundamental building block in Python, and used everywhere.

## Table of Contents

1. [The class Keyword](#the-class-keyword)
2. [Classes are Blueprints](#classes-are-blueprints)
3. [self](#self)
4. [init](#__init__)
5. [Methods](#class-methods)
6. [Static Methods](#static-methods)
7. [Python is Built on Classes](#python-is-built-on-classes)
8. [Problem Sets](#problem-sets)
9. [Further Reading](#further-reading)

<br/>

## The `class` Keyword

In Python we use the `class` keyword to create classes in a similar way we use the `def` keyword to create functions. "And what is a class?" you ask.

> A class is a logical grouping of data and functions.


**Fun Fact**: when a "function" is part of a class, we call it a "method".

> Using a class can help you organize your code.

Find a core concept or idea (like a file, a plot, or a database) and make a class out of it. This will help you organize your code and your thoughts. Things that belong to your idea will become variables or methods inside of the class. This will help you keep everything else separate. When thinking about larger amounts of code, you will only have to think about one class at a time.

<br/>

## Classes are Blueprints

> A class is a blueprint for an idea.

First, some jargon. An "object" is a specific instance of a "class". For instance, if I have a "student" class, each "student" would have a few pieces of information attached to it: name, student id, grades, etc. But if you make a particular student named "beth", then we would say "beth is an object of the student class". Or we might say "an object is an instance of a class".

Enough talk, let's look at an example:

```python
class Student:
    '''A Student is a person currently enrolled in this awesome course.
    Students have the following properties:

    Attributes:
        name: A string representing the student's name.
        student_id: An integer given as a unique identifier for the student.
        hw_grades: A list of 10 numbers (0 to 100) representing the student's homework grades.
        test_grades: A list of 2 numbers (0 to 100) representing the student's test grades.
    '''

    def __init__(self, name, sid):
        '''return a Student object, with a name, id, and fresh grades'''
        self.name = name
        self.student_id = sid
        self.hw_grades = [0.0] * 10
        self.test_grades = [0.0, 0.0]

    def set_hw_grade(self, grade, week):
        '''Set the grade for a specific homework'''
        self.hw_grades[week] = grade

    def set_test_grade(self, grade, exam):
        '''Set the grade for a specific test'''
        self.test_grades[exam] = grade

    def calculate_grade(self):
        '''Return the current grade of the student.
        Tests and homeworks are each worth 50%.'''
        average_hw_grade = sum(self.hw_grades) / len(self.hw_grades)
        average_test_grade = sum(self.test_grades) / len(self.test_grades)
        final_grade = (average_hw_grade + average_hw_grade) / 2.0

        return final_grade
```

The code above does not create an "object"; we didn't decide this `student` has a name of `beth` and a student id of `12345789`. The code above just creates a blueprint for a student. The first line `class Student(object):` tells Python that we are going to start defining a class blueprint.

To create a specific `Student` object, we would do something like:

```python
emmy = Student('Emmy Noether', 837195783)
```

Here we create an "object" from the `Student` class, and call it `emmy`. Notice that `'Emmy Noether'` and `837195783` match the inputs (ignore `self` for now) of the `__init__` method in the `Student` class. Where the generic, abstract notion of a `Student` is defined by the class, the details for the particular student `emmy` form an "object".

<br/>

## `self`

What is with that `self` parameter used throughout the `Student` class? It is a reference to the "instance" of that class. For example, let's say we had all these "instances" of the `Student` class:

```python
emmy = Student("Emmy Noether", 837195783)
al = Student("Albert Einstein", 986534568)
issac = Student("Issac Newton", 191739171)
name = "Marie"
```

To help clear up why we use `self`, I have put that string variable `name = "Marie"` alongside the three `Student` objects. How would you retrieve the value of `name`? Easy, you would do something like:

```python
print(name)
```

You've done that before. But let's say you want to retrieve the value of `name` inside the `al` object. You would do:

```python
print(al.name)
```

When we do that, we make clear that we want the value of the `name` variable stored inside the `al` object; not the `emmy` object, and not the global `name = "Marie"`. Well, inside the class itself we also need a way to show we are talking about `al.name = "Albert Einstein"` and not any other `name` variable. To do this, we identify all values associated with the current instance of the class using the `self` keyword.

Just to be clear, let's print all the names above:

```python
>>> emmy.name
'Emmy Noether'
>>> al.name
'Albert Einstein'
>>> issac.name
'Issac Newton'
>>> name
'Marie'
```

<br/>

## `__init__`

What is the deal with that `__init__` in `Student`? When we create a new object by doing something like `emmy = Student("Emmy Noether", 837195783)`, the `__init__` is called, and the code inside is executed to create the initial form of the object.

In this case, the `__init__` method is called and four variables are set: `self.name`, `self.student_id`, `self.hw_grades`, and `self.test_grades`. Two variables are set to the values `"Emmy Noether"` and `837195783` and the other two are given default values. This is the purpose of the `__init__` method; to give the attributes of the object starting values.

<br/>

## Methods

Now let's talk about those `Student` methods: functions inside of the class. Mostly, they look like regular functions, except they are indented to signify they are part of the `Student` class. Also, the first input is `self`:

```python
class Student:
    ...

    def set_hw_grade(self, grade, week):
        '''Set the grade for a specific homework'''
        self.hw_grades[week] = grade
```

The first parameter to this function is `self`, not because you need to pass a `self` variable in, but to signify that this method takes the attributes (`self.name`, `self.student_id`, `self.hw_grades`) from this instance of Student. To set the first homework grade to 99 percent, we would do this:

```python
emmy = Student("Emmy Noether", 837195783)
emmy.set_hw_grade(99.0, 0)
```

We see the `set_hw_grade` method actually only takes two inputs, not three. The `self` input is provided by doing the `emmy.`. Another thing we see is that by using a class method, we have access to all of the class attributes. In this case, that means we can modify the values in the `self.hw_grades` list.

<br/>

## Static Methods

A class method is any function you include in a class and give the `self` parameter to. But what if you want to include a method in a class that is independent of the value of this particular object? These are called "static methods", and here are a couple examples:

```python
class Student:
    ...

    @staticmethod
    def fail_student():
        '''Hilarious print statement'''
        print("You Fail!")

    @staticmethod
    def letter_grade(percent_grade):
        '''return a letter grade from a percentage grade'''
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

Notice that these two new methods defined inside `Student` don't have the `self` in their argument lists. That's because they don't make use of any instance attributes (like `self.name`). Also notice that to tell Python about this fact, we have included the `@staticmethod` [decorator](http://thecodeship.com/patterns/guide-to-python-function-decorators/). This just stops Python from throwing an error when it doesn't see that `self` in the method's argument list.

Why use static methods? Well, it's true, you could have just written these methods without worrying about it:

```python
class Student:

    # ...rest of the class defined as normal

    def fail_student(self):
        '''Hilarious print statement'''
        print("You Fail!")

    def letter_grade(self, percent_grade):
        '''return a letter grade from a percentage grade'''
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

Written like this, these methods would still run. But using the `@staticmethod` decorator has some performance improvements. Also, when you look at a method with the `@staticmethod` decorator on top, you instantly know a lot about it. It will help the next person who looks at your code read and understand what is going on.

<br/>

## Properties

There are lots of other decorators in Python. But a super handy one for OOP is the `@property` decorator. First, let's see an example:

```python
class Celsius:

	def __init__(self, temp=0):
		self._temperature = temp

	@property
	def temp(self):
		return self._temperature

	@temp.setter
	def temp(self, val):
		if val < -273.15:
			raise ValueError(f"In reality, temepratures can't go this low: {val}")

        # sets the temperature
		self._temperature = val
```

Okay, so here we create a simple `Celcius` class. And (for now) it only has one attribute, the temperature. And its private (it starts with an underscore). What the `@property` decorator gets us over the `def temp` method is just a way to return the private temperature value. And that might not seem that valuable. But then we look at the `@temp.setter` decorator which goes along with the `@property` decorator and we can see the _reason_ for all this. 

We don't want people to set the temperature to an impossible value!

So the `@temp.setter` decorator allows us to do error-checking when we "set" and "get" the private `self._temperature` value. This ability to ensure the values of a class are valid can be really helpful. It is a great way to enforce that everything is in a reasonable state, and will work properly.

Let's use our new little toy class:

```python
cel = Celsius();

# using the @temp.setter, under the hood
cel.temp = -270

# using the @property getting, under the hood
print(cel.temp)
```

Great! That worked out! Super easy to use.

But what if we try to do this?

```python
cel.temp = -300
```

Boom! Failure! The program throws a `ValueError`. But that's great. It means that thousands of lines of code later than this, we know the Celcius temperature value we are using is valid. And that confidence in correctness can be game-changing.

<br/>

## Python is Built on Classes

You don't have to go far to find examples of classes being used in Python. We've already seen tons of them: `int`, `float`, `list`, `dict`, `True`, `csv`, the list goes on.

A lot of the features of a `list` start to look like a class immediately. You can create an object from the list class:

```python
>>> lst = list((1,2,3))
>>> lst
[1, 2, 3]
```

And after you create the `lst` object, you can call class methods on that object:

```python
>>> lst.append(-9)
>>> lst
[1, 2, 3, -9]
>>>
>>> lst.sort()
>>> lst
[-9, 1, 2, 3]
>>>
>>> lst.count(1)
1
```

And if you call `help(lst)` the documentation you see starts with `class list(object)` because nearly everything in Python is a class or an object. Object-oriented programming is so important in Python, it's hard to understand the language without it.

<br/>

## Problem Sets

 * [Simple Classes](problem_set_1_try_it_out.md)
 * [init Problems](problem_set_2_init.md)


## Further Reading

 * [Full Example: Using FTP](lecture_06_2_full_example.md)
 * [Python Tutorial: OOP](http://www.python-course.eu/object_oriented_programming.php)
 * [Decorators](http://thecodeship.com/patterns/guide-to-python-function-decorators/)


[Back to Syllabus](../../README.md)
