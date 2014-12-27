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



### Instance Attributes



### Static vs Class Methods




[Back to Syllabus](../../README.md)
