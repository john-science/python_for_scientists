# Object-Oriented Programming, Part 1

[Object-Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming) (OOP) means programming with [classes](https://en.wikipedia.org/wiki/Class_%28computer_programming%29). The "class" is a fundamental building block in Python. All of Python's standard libraries use classes, as do nearly all popular Python programs.

### The `class` Keyword

In Python we use the `class` keyword to create classes in a similar way we use the `def` keyword to create functions. "And what is a class?" you ask. A class is a logical grouping of data and functions.

**Fun Fact**: when a "function" is part of a class, we call it a "method".

What do we mean by "logical grouping"? Well, a class can contain any data or functions (methods) we want. But rather than just throwing random things together into a "class", we try to create classes where there is a logical connection between things. For instance, classes are often based on physical things (like students, beers, refineries, or wildfires). Other times, classes are based more abstract concepts, like line plots or meteorological databases.

Classes are an abstraction technique. They help us organize groups of things that are logically connected. In this way the help us organize and reason about large amounts of code. If all the core ideas in a program are separated into classes, we can think about one class at a time and how it interacts with another class. This saves us from having to think about all the details our code at the same time.

### Classes are Blueprints

A class is a blueprint of an idea. For instance, you might have a class for a `student`, but there might be many "objects" made from that `student` class. Each object would represent a `student` with different identifying information: `name`, `student_id`, `homework_grades`, `test_grades`. So, while `john` might be an "object" it is an "instance" of the class `student`.

Enough talk, let's look at some examples:

    class Student(object):
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
            final_grade = (average_hw_grade + average_homework_grade) / 2.0
            
            return final_grade

The first line `class Student(object)` does *not* create a new class. All the code above does is create the *blueprint* for a student object. To actually create a `Student` object, we need to use the `__init__` method above, giving it two values (ignoring `self`, which we will get to).

To create an object, we would do something like: `emmy = Student('Emmy Noether', 837195783)`. All this says is that we want to create an "instance" of the `Student` class, where the student has the name `Emmy Noether` and she has the student id `837195783`.

The `emmy` object is a realized version of the `Student` class. It takes the generic, abstract notion of a "Student" and fills in the specifics. There is still only one `Student` class, even if we created dozens of different students.

### `self`

Okay, what is with that `self` parameter used throughout the `Student` class? It is a reference to the "instance" of that object. For example, let's say we had all these "instances" of the `Student` class:

    emmy = Student("Emmy Noether", 837195783)
    al = Student("Albert Einstein", 986534568)
    issac = Student("Issac Newton", 191739171)
    name = "Marie"

To help clear up why we use `self`, I have put that string variable `name = "Marie"` alongside the three `Student` objects. How would you retrieve the value of `name`? Easy, you would do something like:

    print(name)

You've done this before. But let's say we want to retrieve the value of `name` inside the `al` object. Well, we would do:

    print(al.name)

When we do that, we make clear that we want the value of the `name` variable stored inside the `al` object; not the `emmy` object, and not the global `name = "Marie"`. Well, inside the class itself we also need a way to show we are talking about `al.name = "Albert Einstein"` and not any other `name` variable. To do this, we identify all values associated with the current instance of the class using the `self` keyword.

### `__init__`

Okay, what is the deal with that `__init__` in `Student`? When we create a new object by doing something like `emmy = Student("Emmy Noether", 837195783)`, the `__init__` is called, and the code inside is executed to create the initial form of the (mutable) object.

In this case, the `__init__` method is called and four variables are set: `self.name`, `self.student_id`, `self.hw_grades`, and `self.test_grades`. Two variables are set to the values `"Emmy Noether"` and `837195783` and the other two are given default values. This is the purpose of the `__init__` method; to give the attributes of the object starting values.

### Instance Attributes

This brings us to an important piece of jargon: "instance attributes". The "instance" of the `Student` class `emmy` has four "attributes": `self.name`, `self.student_id`, `self.hw_grades`, and `self.test_grades`. These "attributes" are attributes of the class, yes. But since they have specific values in the `emmy` instance, they are called "instance attributes".

This is not meant to be confusing, there are just two things to understand. First, the difference between an object, or an "instance" of a class. And second, the "attributes" are the values/data stored inside of an object.

### Class Methods

 * Coming Soon

### Static Methods

Classes (and their objects) have more than just attributes. They also have methods. (Remember, any function inside a class is called a "method".) A typical method will make use of the instance attributes, like `def calculate_grade(self)` defined above. However, what if you want to include a method inside a class that is independent of the values of the object? These are called "static methods", and here are a couple examples:

    class Student(object):
    
        # rest of the class defined as before
        
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

Notice that these two new methods defined inside `Student` don't have the `self` included in their argument lists. That's because they don't make use of any instance attributes (like `self.name`). Also notice that to tell Python about this fact, we have included the `@staticmethod` [decorator](http://thecodeship.com/patterns/guide-to-python-function-decorators/). This just stops Python from throwing an error when it doesn't see that `self` in the method's argument list.

So why use static methods? Why bother with the static method decorator?  Well, it's true, you could have just written these methods without worrying about that:

    class Student(object):
    
        # rest of the class defined as normal

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

Written like this, these methods would still run. But using the `@staticmethod` decorator has some performance improvements. Also, when you look at a method with the `@staticmethod` decorator on top, you instantly know a lot about it. It will help the next person who looks at your code read and understand what is going on.

## Problem Sets

 * [Full Example: Using FTP](lecture_06_2_full_example.md)
 * [Simple Classes](problem_set_1_try_it_out.md)
 * [init Problems](problem_set_2_init.md)

## Further Reading

 * [Python Tutorial: OOP](http://www.python-course.eu/object_oriented_programming.php)
 * [Decorators](http://thecodeship.com/patterns/guide-to-python-function-decorators/)


[Back to Syllabus](../../README.md)
