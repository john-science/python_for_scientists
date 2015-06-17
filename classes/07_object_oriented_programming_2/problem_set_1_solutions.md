# Inheritance

To start this problem set off, we will define the following abstract class:

    from abc import ABCMeta,abstractmethod
    
    class Shape(object):
        __metaclass__ = ABCMeta
    
        def __init__(self, n):
            self.number_of_sides = n

        @abstractmethod
        def is_3d(self):
            pass

## Solutions

#### 1. Define a class `Polygon` that is a subclass of `Shape`, but not abstract because the method `is_3d` returns `False`.

    class Polygon(Shape):

        def __init__(self, n):
            Shape.__init__(self, n)

        def is_3d(self):
            return False

#### 2. Define a class `Polyhedron` this is a subclass of `Shape`, but not abstract because the method `is_3d` return `True`.

    class Polyhedron(Shape):

        def __init__(self, n):
            Shape.__init__(self, n)

        def is_3d(self):
            return True

#### 3. Define a class `Cube` that is a subclass of `Polyhedron`, where the `__init__` method only takes one variable: `side_length`.  This class has one method, `calculate_volume`, that multiples the the `self.side_length` by itself three times.

    class Cube(Polyhedron):

        def __init__(self, side_length):
            Polyhedron.__init__(self, 6)
            self.side_length = side_length

        def calculate_volume(self):
            '''return the volume of this cube'''
            return self.side_length ** 3

#### 4. Define a class `Rectangle` that is a subclass of `Polygon`, where `self.number_of_sides` is set equal to 4. But the `__init__` method takes two more variables: `length` and `width`. This will have a method `calculate_area` that will find the area of the rectangle.

    class Rectangle(Polygon):
    
        def __init__(self, length, width):
            Polygon.__init__(self, 4)
            self.length = length
            self.width = width
        
        def calculate_area(self):
            '''return the area of a rectangle
            that has a given length and width'''
            return self.length * self.width

#### 5. Define a class `Square` that is a subclass of `Rectangle`, where the `__init__` method only takes one variable (`length`). This will also have a method `calculate_area`, that overrides the method from `Rectangle`.

    def Square(Rectangle):
    
        def __init__(self, length):
            Rectangle.__init__(self, length, length)
        
        def calculate_area(self):
            '''return the area of a rectangle
            that has a given length and width'''
            return self.length * self.length

#### 6. Define a static method `diagonal_length` on `Square`, that takes the length of one side of a square and returns the length of the diagonal of that square.

    from math import sqrt

    def Square(Rectangle):
    
        def __init__(self, length):
            Rectangle.__init__(self, length, length)
        
        def calculate_area(self):
            '''return the area of a rectangle
            that has a given length and width'''
            return self.length * self.length
        
        @staticmethod
        def diagonal_length(length):
            '''returns the length of the diagonal
            of this square'''
            return sqrt(2) * length


[Back to Problem Set](problem_set_1_interheritance.md)
