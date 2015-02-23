# Be Careful When you init

As usual, when doing the problems don't scroll down too far or you will see the answers.

## Describing the Problem

When creating a new class, you can create potentially invalid states for your objects. For example:

    class Rectangle(object):
    
      def __init__(self, length_of_x_side):
        self.length_of_x_side = length_of_x_side
        self.length_of_y_side = None
      
      def get_area(self):
        '''calculates the area of the rectangle'''
        return self.length_of_x_side * self.length_of_y_side

So, if you create a new `Rectangle` and try to find an area, you will get an error:

    >>> r = Rectangle(5)
    >>> r.get_area()
    TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'

Now, this is easily fixable:

    >>> r = Rectangle(5)
    >>> r.length_y_side = 14
    >>> r.get_area()
    70

But it is still a problem that when we set up the `Rectangle` object using the `__init__` method. This is the concern we will focus on in this problem set. The standard solution to this problem is to demand all important data is present when the object is created:

    class Rectangle(object):
    
      def __init__(self, x, y):
        self.length_of_x_side = x
        self.length_of_y_side = y

## Problem 1

Fix the problem with this object initialization:
    
    class Student(object):
    
        def __init__(self):
            self.first_name = None
            self.last_name = None
        
        def print_full_name(self):
            print(' '.join([self.first_name, self.last_name]))

## Solution 1

    class Student(object):
    
        def __init__(self, first, last):
            self.first_name = first
            self.last_name = last

# Problem 2

Fix the problem with this object initialization:

    class Student(object):
    
        def __init__(self, first, last):
            self.first_name = first
            self.last_name = last
        
        def average_grade(self):
            '''Salculate the average grade from the student's
            list of grades. (This is the student's total grade.)
            '''
            return sum(self.grades) / len(self.grades)

## Solution 2

    class Student(object):
    
        def __init__(self, first, last, grades):
            self.first_name = first
            self.last_name = last
            self.grades = grades  # or possibly self.grades = []
        
        def average_grade(self):
            '''Salculate the average grade from the student's
            list of grades. (This is the student's total grade.)
            '''
            return sum(self.grades) / len(self.grades)

[Back to Lecture](lecture_06.md)
