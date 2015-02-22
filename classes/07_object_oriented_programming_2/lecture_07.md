# Object-Oriented Programming, Part 2

## Inheritance

Inheritance is taking the abstractions we create with Objects one step further. Instead of just creating a class for `Rectangle` and a class for `Triangle`, we make the logical leap that both of these are polygons and will have many things in common. So we create a `Polygon` class and have each `Rectangle` and `Triangle` inherit many of it's properties from the Polygon.

Let's see some concrete examples:

    class Polygon(object):
    
        def __init__(self, n):
            self.number_of_sides = n
        
        def print_num_sides(self):
            print('There are ' + str(self.number_of_sides) + 'sides.')
    
    class Triangle(Polygon):
    
        def __init__(self, lengths_of_sides):
            Polygon.__init__(self, 3)
            self.lengths_of_sides = lengths_of_sides  # list of three numbers
        
        def get_area(self):
            '''return the area of the triangle using the semi-perimeter method'''
            a, b, c = self.lengths_of_sides
            
            # calculate the semi-perimeter
            s = (a + b + c) / 2
            return (s*(s-a)*(s-b)*(s-c)) ** 0.5
    
    class Rectangle(Polygon):
    
        def __init__(self, lenghts_of_sides):
            Polygon.__init__(self, 4)
            self.lengths_of_sides = lengths_of_sides  # list of two numbers
        
        def get_area(self):
            '''return the area of the rectangle: length x width'''
            x, y = self.lenghts_of_sides
            return x * y

There are a few things to notice here. First of all, the `Polygon` class is very simple, used primarily to organize our thoughts on what a polygon is. Then in the class signatures for `Triangle` and `Rectangle` we actually reference the `Polygon` class. Then in the `__init__` methods for each `Triangle` and `Rectangle` class we reference the `Polygon` `__init__` method, so that when we create a `Triangle` class, we are also initializing the attributes of a `Polygon` class, and including it's methods.

Now if we create a `Triangle`, we can call both the methods in `Triangle` and those in `Polygon`:

    >>> tri = Triangle([3, 4, 5])
    >>> print(tri.get_area())
    6.0
    >>> print(tri.print_num_sides())
    3

What we have done is create a connection between the ideas of a triangle and a rectangle by having them both "inherit" from the `Polygon` class. This also means that both method classes share the `print_num_sides` method, but we didn't have to write it twice: DRY.

So that is what inheritance is in OOP. It is adding another layer of abstraction to the ideas in our code. And from that layer of abstraction we can reason more generally about the functionality of the separate components  of software we are creating.

## Abstract Classes

You may have noticed a chance to improve the `Polygon` example above. Both the `Triangle` and `Rectangle` examples above have a `get_area()` method. Wouldn't it be nice if we could include that in `Polygon` somehow? But the problem is that the implementation details of how you calculate the area of a triangle and rectangle differ. So we can't just write the method directly into `Polygon`. This is where abstract classes come into play.

What we do when we define an [abstract class](https://en.wikipedia.org/wiki/Class_%28computer_programming%29#Abstract_and_concrete) is we create the blueprint of all the classes that will inherit from it (the [subclasses](http://en.wikipedia.org/wiki/Inheritance_%28object-oriented_programming%29#Subclasses_and_superclasses)). And we let those subclasses give the details (like how to calculate their area).

In the example above we can modify `Polygon` to become an abstract class:

    import abc

    class Polygon(object):
        __metaclass__ = abc.ABCMeta
    
        def __init__(self, n):
            self.number_of_sides = n
        
        def print_num_sides(self):
            print('There are ' + str(self.number_of_sides) + 'sides.')
            
        @abc.abstractmethod
        def get_area(self):
            pass

Here we have imported the Python standard library `abc` to create an abstract class. We use the `__metaclass__ = abc.ABCMeta` statement to define it as an abstract class. And every abstract method we mark with the `@abc.abstractmethod` decorator. This marks the method as not being implemented. Every subclass of `Polygon` must now give an implementation of the `get_area` method, or Python will throw an error:

    >>> class Circle(Polygon)
    >>> __metaclass__ = abc.ABCMeta
    >>> def __init__(self):
    >>>         self.number_of_sides = 1
    >>> 
    >>> c = Circle()
    TypeError: Can't instantiate abstract class Circle with abstract methods get_area

What we did by making `Polygon` abstract is create a more complete blueprint for `Triangle` and `Rectangle`, that includes the idea (if not the implementation) that every polygon has an area. This can be useful in organizing our thoughts on code. If at some point in the distant future we want to add a `Rhombus` class, we would have the abstract blueprint in `Polygon` to remind us we need a `get_area` method.

## Multiple Inheritance

There is one more really major topic we need to cover in OOP before we can move on. Starting with the examples above, imagine we want to create a `Square` class. Now, we could do this be inheriting directly from our abstract `Polygon` class as before:

    class Square(Polygon):
    
        def __init__(self, lenghts_of_side):
            Polygon.__init__(self, 4)
            self.lengths_of_sides = [lengths_of_side]  # list of two numbers
        
        def get_area(self):
            '''return the area of the rectangle: length x width'''
            x = self.lenghts_of_sides[0]
            return x * x

But this misses out on a key idea from basic geometry: squares are just a special type of rectangle. So perhaps it would be better if `Square` inherited directly from `Rectangle`:


    class Square(Rectangle):
    
        def __init__(self, side):
            Rectangle.__init__(self, 4, [side, side])

Not only does recognizing this basic fact about our system help organize our thoughts, it makes the code much shorter.

In the language of OOP, we could describe the above classes in a few ways:

 * Square inherits from Rectangle, which in turn inherits from Polygon.
 * Square is a subclass of Rectangle, which is a subclass of Polygon.
 * Polygon is a superclass of Rectangle, which is a superclass of Square.

The jargon itself is not as important as the relationship between these classes. Multiple inheritance is a powerful abstraction tool, giving us a huge amount of flexibilty to organize our thoughts and thus our code.

## The Warning

Be warned. The above example of `Square` seems reasonable enough. But using multiple inhertance comes with a danger. You can create classes with subclasses of subclasses of subclasses of subclasses of subclasses of subclasses so deep that you can no longer keep the whole chain of inheritance easily in mind. At some level deep down the rabbit hole adding another layer of abstraction begins to add more complexity than it removes. At what point that happens is entirely up to you.

## Problem Sets

 * Coming Soon

## Further Reading

 * [Python Tutorial: Inheritance](http://www.python-course.eu/inheritance_example.php)


[Back to Syllabus](../../README.md)
