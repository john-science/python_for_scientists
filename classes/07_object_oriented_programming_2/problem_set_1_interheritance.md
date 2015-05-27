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

## Problems

1. Define a class `Polygon` that is a subclass of `Shape`, but not abstract because the method `is_3d` returns `False`.
2. Define a class `Polyhedron` this is a subclass of `Shape`, but not abstract because the method `is_3d` return `True`.
3. Define a class `Cube` that is a subclass of `Polyhedron`, where the `__init__` method only takes one variable: `side_length`.  This class has one method, `calculate_volume`, that multiples the the `self.side_length` by itself three times.
4. Define a class `Retangle` that is a subclass of `Polygon`, where `self.number_of_sides` is set equal to 4. But the `__init__` method takes two more variables: `length` and `width`. This will have a method `calculate_area` that will find the area of the rectangle.
5. Define a class `Square` that is a subclass of `Rectangle`, where the `__init__` method only takes one variable (`length`). This will also have a method `calculate_area`, that overrides the method from `Rectangle`.

## Solutions

 * [Inheritance - Solutions](problem_set_1_solutions.md)

[Back to Lecture](lecture_07.md)
