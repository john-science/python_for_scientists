# Object-Oriented Programming, Part 2

This lecture continues outlining the basics of OOP in Python that was started [here](../06_object_oriented_programming_1/lecture_06.md).

## Table of Contents

1. [Inheritance](#inheritance)
2. [Abstract Classes](#abstract-classes)
3. [Multilevel Inheritance](#multilevel-inheritance)
3. [Multiple Inheritance](#multiple-inheritance)
4. [Be Warned](#be-warned)
5. [More Examples](#more-examples)
6. [Problem Sets](#problem-sets)
7. [Further Reading](#further-reading)

<br/>

## Inheritance

Inheritance is taking the abstractions we create with Classes one step further.

Imagine we have different classes for various kinds of shapes: `Rectangle`, `Triangle`, `Octohedron`, and so on. Instead of just creating a class for `Rectangle` and a class for `Triangle`, we make the logical leap that both of these are polygons and thus have some things in common. So we create a `Polygon` class for our other shapes to inherit from.

Let's see some concrete examples:

```python
class Polygon:

    def __init__(self, n):
        self.number_of_sides = n

    def print_num_sides(self):
        '''A quick, informational print statement.'''
        print(f'There are {self.number_of_sides} sides.')

class Rectangle(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 4)
        self.lengths_of_sides = lengths_of_sides  # list of two numbers

    def get_area(self):
        '''Return the area of the rectangle: length x width.'''
        x, y = self.lengths_of_sides
        return x * y

class Triangle(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 3)
        self.lengths_of_sides = lengths_of_sides  # list of three numbers

    def get_area(self):
        '''Return the area of the triangle using the semi-perimeter method.'''
        a, b, c = self.lengths_of_sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
```

There are a few things to notice here. First of all, the `Polygon` class is very simple. In the class signatures for `Triangle` and `Rectangle` we actually reference the `Polygon` class. Then in the `__init__` methods for each `Triangle` and `Rectangle` class we reference the `Polygon` `__init__` method, so that when we create a `Triangle` class, we are also initializing the attributes of a `Polygon` class, and including it's methods.

We can create an instance of `Polygon` by doing:

```python
>>> p = Polygon(9)
>>> p.print_num_sides()
There are 9 sides.
```

And if we create a `Triangle`, we can call both the methods in `Triangle` and those in `Polygon`:

```python
>>> tri = Triangle([3, 4, 5])
>>> print(tri.get_area())
6.0
>>> tri.print_num_sides()
3
```

We have created a connection between the idea of a triangle and the idea of a polygon. We say that "Triangle inherits from Polygon". We have set up a conceptual connection such that everything in `Polygon` should appear in `Triangle`. And we use this connection in code to help us think about the logic of our situation. The goal is to create relationships in code that miror the real world we are trying to mimic. This will make OOP powerful, and make it a lot easier for humans (like you) to think and reason about the code.

<br/>

## Abstract Classes

You may have noticed a chance to improve the `Polygon` example above. Both the `Triangle` and `Rectangle` examples above have a `get_area()` method. Wouldn't it be nice if we could include that in `Polygon` somehow? But the problem is that you calculate the area of triangles and rectangles differently, so we can't just write the equation directly in `Polygon`. This is where abstract classes come into play.

What we do when we define an [abstract class](https://en.wikipedia.org/wiki/Class_%28computer_programming%29#Abstract_and_concrete) is we create the blueprint of all the classes that will inherit from it (the [subclasses](http://en.wikipedia.org/wiki/Inheritance_%28object-oriented_programming%29#Subclasses_and_superclasses)). And we let those subclasses fill in the details (like how to calculate their area).

We could modify the example above to make `Polygon` an abstract class:

```python
from abc import ABC, abstractmethod

class Polygon(ABC):

    def __init__(self, n):
        self.number_of_sides = n

    def print_num_sides(self):
        print(f'There are {self.number_of_sides} sides.')

    @abstractmethod
    def get_area(self):
        pass
```

Here we have imported the Python standard library `abc` to create an "abstract base class". We subclass `ABC` to define it as an abstract class. And every abstract method we mark with the `@abstractmethod` decorator. This marks the method as not being implemented, so a subclass has to fill it in later.

An abstract base class cannot be created directly, so we can no longer create a generic `Polygon`:

```python
>>> p = Polygon(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Polygon with abstract methods get_area
```

And in order to implement a subclass of `Polygon`, it must provide an implementation of all of the abstract methods, like `get_area`:

```python
>>> class Circle(Polygon):
>>>     def __init__(self):
>>>         Polygon.__init__(self, 1)
>>>
>>> c = Circle()
TypeError: Can't instantiate abstract class Circle with abstract methods get_area
```

But as long as the subclass implements all the abstract methods, we can create an instance of it just like we would any other class:

```python
>>> t = Triangle([3.0, 4.0, 5.0])
>>> print(t.number_of_sides())
3
```

What we did by making `Polygon` abstract is create a more complete blueprint for `Triangle` and `Rectangle`, that includes the idea (but not the implementation) that every polygon has an area. This can be useful in organizing our thoughts in code. If at some point in the distant future we want to add a `Heptadecagon` class, we would have the abstract blueprint in `Polygon` to remind us we need to write a `get_area()` method.

<br/>

## Multilevel Inheritance

Starting with the examples above, imagine we want to create a `Square` class. Now, we could do this by inheriting directly from our abstract `Polygon` class as before:

```python
class Square(Polygon):

    def __init__(self, lengths_of_side):
        Polygon.__init__(self, 4)
        self.lengths_of_sides = [lengths_of_side]  # list of two numbers

    def get_area(self):
        '''Return the area of the rectangle: length x width.'''
        x = self.lengths_of_sides[0]
        return x * x
```

But this misses out on a key idea from basic geometry: squares are just a special type of rectangle. So perhaps it would be better if `Square` inherited from `Rectangle`:

```python
class Square(Rectangle):

    def __init__(self, side):
        Rectangle.__init__(self, [side, side])
```

Not only does recognizing something basic about our system help organize our thoughts, it makes the code much shorter.

We still create an instance of `Square` in the usual way:

```python
>>> s = Square(7.0)
>>> print(s.number_of_sides)
4
```

In the language of OOP, we could describe the above classes in a few ways:

 * `Square` inherits from `Rectangle`, which in turn inherits from `Polygon`.
 * `Square` is a subclass of `Rectangle`, which is a subclass of `Polygon`.
 * `Polygon` is a superclass of `Rectangle`, which is a superclass of `Square`.

Okay, there's some jargon here. But the jargon itself is not as important as the relationship between these classes. Multilevel Inheritance is a powerful abstraction tool, giving us a huge amount of flexibilty to organize our thoughts and thus our code. Multilevel Inheritance is also super common in OOP codebases. Especially in Python and Java, people who write one class tend to think of more and more things to do with them, and [Multilevel Inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)#Types) will just happen.

<br/>

## Multiple Inheritance

What we have above is a straight line of inheritance.  `Square` -> `Rectangle` -> `Polygon`.  But Python also supports [Multiple Inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)#Types), where a single class inherits things from two or more other classes.  Let's see a simple example:

```python
class Class1:
    def m(self):
        print("In Class1") 
        
class Class2(Class1):
    def m(self):
        print("In Class2")
  
class Class3:
    def x(self):
        print("In Class3")  
         
class Class4(Class2, Class3):
    pass
```

Here our `Class4` inherits from `Class2` AND `Class3`. (`Class4` could have other methods and attributes, I'm just trying to keep it simple.) 

What would happen if we asked for `Class4.x()`? How about `Class4.m()`?  Let's try it!

```python
c4 = Class4()
c4.m()  # prints: "In Class 2"
c4.x()  # prints: "In Class 3"
```

Okay, since only `Class3` has an `.x()` method, that one is easy. `Class4` gets the `Class3` `.x()` method. But that `c4.m()` is trickier. That comes from `Class2`, because `Class2` overrides that method from `Class1`.

<br/>


### Be Warned

So maybe you can tell that Multilevel / Multiple Inheritance are really powerful. But hopefully you can also tell that they can lead to a lot of complexity. And that's an important thing to consider in OOP:

> Only add layers of abstraction in your classes if it simplifies things. Code that is too abstracted is hard to understand and work with.

## More Examples

The two object-oriented programming classes have been quite short. There is not a lot of code to learn here, just a few new ideas. If you haven't seen OOP before, it might be useful to look at some more examples:

 * [OOP Examples](lecture_07_examples.md)


## Problem Sets

 * [Inheritance](problem_set_1_interheritance.md)


## Further Reading

 * [Python Tutorial: Inheritance](http://www.python-course.eu/inheritance_example.php)
 * [Learn Python the Hard Way: Inheritance vs Composition](http://learnpythonthehardway.org/book/ex44.html)
 * [Python Inheritance Intro](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)
 * [Dave On Code: Abstract Classes](http://www.daveoncode.com/2014/10/07/abstract-classes-in-python-using-abc-module/)
 * [Module of the Week: abc](http://pymotw.com/2/abc/)
 * [Multilevel & Multiple Inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)#Types)


[Back to Syllabus](../../README.md)
