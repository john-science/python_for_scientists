# Basic OOP

## Using Simple Classes

#### Solution 1 - Instantiating Objects

    plot1 = Plot(600, 400)

#### Solution 2 - Using Methods

    plot2 = Plot(600, 400)
    print(plot2.total_pixels())

#### Solution 3 - Accessing Attributes

    plot3 = Plot(900, 300)
    print(plot3.pixel_x)

#### Solution 4 - Using Objects

    from math import sqrt
    
    origin = Point()
    point = Point(5, 15)
    
    def distance(pnt1, pnt2):
        '''Find the distance between to Point instances'''
        return sqrt((pnt2.x - pnt1.x)**2 + (pnt2.y - pnt1.y)**2)
    
    print(distance(origin, point))

## Writing Simple Classes

#### 1. Create a class named `RightTriangle`, with an `__init__` method that takes two variables: length of side a, and length of side b. The class also has a variable `hypotenuse`, that is initially undefined.

    class RightTriangle:
    
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.hypotenuse = None

#### 2. Add a method named `calculate_area` to `RightTriangle` that returns the area of a right triangle.

    class RightTriangle:
    
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.hypotenuse = None

        def calculate_area(self):
            '''calculate the area of the triangle'''
            return self.a * self.b / 2.0
    

#### 3. Add a method named `calculate_hypotenuse` to `RightTriangle` that calculates the length of the hypotenuse and saves it to the `hypotenuse` member variable.

    from math import sqrt

    class RightTriangle:
    
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.hypotenuse = None

        def calculate_area(self):
            '''calculate the area of the triangle'''
            return self.a * self.b / 2.0

        def calculate_hypotenuse(self):
            '''calculates the length of the hypotenuse,
            and saves it a member variable'''
            self.hypotenuse = sqrt(self.a * self.a + self.b * self.b)
            

#### 4. Add a static method named `to_string` that takes two numbers, that represent the lengths of the sides of a right triangle, andprints out a phrase like `A right triangle with length 3 and width 4.`.

    from math import sqrt

    class RightTriangle:
    
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.hypotenuse = None

        def calculate_area(self):
            '''calculate the area of the triangle'''
            return self.a * self.b / 2.0

        def calculate_hypotenuse(self):
            '''calculates the length of the hypotenuse,
            and saves it a member variable'''
            self.hypotenuse = sqrt(self.a * self.a + self.b * self.b)

        @staticmethod
        def to_string(length_a, length_b):
            '''print out a description of a right triangle,
            based on the lengths of two non-hypotenuse sides'''
            print('A right triangle with length ' + str(length_a) + ' and width ' + str(length_b) + '.')

#### 5. Create a new class named `Rectangle`, with a constructor that takes two variables: length and width. The class has two methods: one is named `area` and returns the area of the rectangle, and the other is named `is_square` and returns a boolean to say if the Rectangle is square or not.

    class Rectangle:
    
        def __init__(self, length, width):
            self.length = length
            self.width = width
        
        def area(self):
            '''calculates the area of the rectangle'''
            return self.length * self.width
        
        def is_square(self):
            '''a rectangle is a square if all its sides
            are the same length'''
            return self.length == self.width
    

[Back to Problem Set](problem_set_1_try_it_out.md)
