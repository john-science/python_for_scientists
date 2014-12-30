# Object-Oriented Programming, Part 1

Object-Oriented Programming (OOP) is programming that uses "classes". The "class" is a fundamental building block in Python. The standard libraries all use classes, as do nearly all popular Python programs.

### The `class` Keyword

In Python we use the `class` keyword to create classes in the same way we use the `def` keyword to create functions. And what is a class? A class is a logical grouping of data and functions. Fun fact, when a function is part of a class, we call it a method.

What do we mean by "logical grouping"? Well, a class can contain any data or functions (methods) we want. But Rather than just throwing random things together into a "class", we try to create classes where there is a logical connection between things. Many times, classes are based on objects in the real world (like `Refinery` or `Wildfire`). Other times, classes are based on concepts in our system, like `LinePlot` or `MeteorologyDatabase`.

Classes are an abstraction technique; a way of thinking about programs. When used wisely, creating a class will make your programs easier to reason about and understand. The core ideas will be separated into classes and all related data will be kept together.

### Classes are Blueprints

A class is a blueprint of an idea. For instance, you might have a class for a `student`, but there might be many "objects" made from that `student` class. Each object would represent a `student` with different identifying information: `name`, `student_id`, `homework_grades`, `test_grades`. So, while `john` might be an "object" it is an "instance" of the class `student`.

Let us look at an example.

    class Student(object):
        '''A Student is a person currently enrolled in this awesome course.
        Students have the following properties:
      
        Attributes:
          name: A string representing the students name.
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

The first line `class Student(object)` does *not* create a new class. All the code above does is create the *blueprint* for a student object. To actually create a `Student` object, we need to use the `__init__` method above, giving it two values (ignoring `self`, which we will get to next).

To create an object, we would do something like: `emmy = Student('Emmy Noether', 837195783)`. All this says is that we want to create an "instance" of the `Student` class, where the student has the name "Emmy Noether" and she has the student id "837195783".

The `emmy` object is a realized version of the `Student` class. It takes the generic, abstract notion of a "Student" and fills in the specifics. There is still only one `Student` class, even if we created dozens of different instances.

### `self`

Okay, what is with that `self` parameter spread throughout the `Student` class? What is it? It is a reference to the "instance" of that object. For example, let's say we had all these "instances" of the `Student` class:

    emmy = Student("Emmy Noether", 837195783)
    al = Student("Albert Einstein", 986534568)
    issac = Student("Issac Newton", 191739171)
    
    name = "Marie"

Notice I also have the variable `name` in the code for some reason. Now, what if I want to print Emmy's full name? Well, I would do `emmy.name`. And the `self` variable inside the `Student` class allows me to reference the `name` attribute of the `emmy` instance, instead of returning the `name` of the `al` instance, or the `name = "Marie"` global variable I defined later.

In short `self` is the way to tell Python you want to address something about the specific instance of the class involved.

### `__init__`

Okay, what is the deal with that `__init__` in `Student`? When we create a new object by doing something like `emmy = Student("Emmy Noether", 837195783)`, the `__init__` is called, and the code inside is executed to create the initial form of the (mutable) object.

In this case, the `__init__` method is called, and four variables are set: `self.name`, `self.student_id`, `self.hw_grades`, and `self.test_grades`. Two variables are set to the values `"Emmy Noether"` and `837195783` and the other two are given default values. This is the purpose of the `__init__` method; to give the attributes of the object starting values.

### Instance Attributes

This brings us to an important piece of jargon: "instance attributes". The "instance" of the `Student` class `emmy` has four "attributes": `self.name`, `self.student_id`, `self.hw_grades`, and `self.test_grades`. These "attributes" are attributes of the class, yes. But since they have specific values in the `emmy` instance, they are called "instance attributes".

This is not meant to be confusing, there are just two things to understand. First, the difference between an object, or an "instance" of a class. And second, the "attributes" are the values/data stored inside of an object.

### Static Methods

Classes (and their objects) have more than just attributes. They also have methods. (Remember, any function inside a class is called a "method".) A typical method will make use of the instance attributes, like `def calculate_grade(self)` defined above. However, what if you want to include a method inside a class that is independent of the values of the object? These are called "static methods", and here are a couple examples:

    class Student(object):
    
        # rest of the class defined as normal
        
        @staticmethod
        def fail_student():
            '''Hilarious print statement'''
            print "You Fail!"
        
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

Notice that these two new methods defined inside `Student` don't have the `self` included in their argument lists. That's because they don't make use of any instance attributes, like `self.name`. Also notice, that to tell Python about this fact, we have included the `@staticmethod` [decorator](http://thecodeship.com/patterns/guide-to-python-function-decorators/). This just stops Python from throwing an error when it doesn't see that `self` in the method's argument list.

So why use static methods? Why bother with the static method decorator?  Well, it's true, you could have just written these methods without worrying about that:

    class Student(object):
    
        # rest of the class defined as normal

        def fail_student(self):
            '''Hilarious print statement'''
            print "You Fail!"

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

Written like this, these methods would still run. But using the `@staticmethod` decorator has some performance improvements. It will make your code faster to use this when you can. Also, when you look at a method with the `@staticmethod` decorator on top, you instantly know a lot about it. It will help the next person who looks at your code read and understand what is going on.

[Back to Syllabus](../../README.md)
