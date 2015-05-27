# Basic OOP

## Using Classes

#### Problem 1 - Instantiating Objects

Instantiate (create an instance of) this class:

    class Plot(object):
    
        def __init__(self, num_pixels_x, num_pixels_y):
            self.pixels_x = num_pixels_x
            self.pixels_y = num_pixels_y

#### Problem 2 - Using Methods

Instantiate this class and run use it's method to calculate the number of pixels in the final plot:

    class Plot(object):
    
        def __init__(self, num_pixels_x, num_pixels_y):
            self.pixels_x = num_pixels_x
            self.pixels_y = num_pixels_y

        def total_pixels(self):
            '''Calculates the total number of pixels in
            the final plot'''
            return self.pixels_x * self.pixels_y

#### Problem 3 - Accessing Attributes

Print the `pixel_x` attribute from an instance of the `Plot` class above.

#### Problem 4 - Using Objects

Create two instances of `Point` and write a function that finds the distance between them.

    class Point:
    
       def __init__(self, x=0, y=0):
          self.x = x
          self.y = y

## Writing Classes

1. Create a class named `RightTriangle`, with an `__init__` method that takes two variables: length of side a, and length of side b. The class also has a variable `hypotenuse`, that is initially undefined.
2. Add a method named `calculate_area` to `RightTriangle` that returns the area of a right triangle.
3. Add a method named `calculate_hypotenuse` to `RightTriangle` that calculates the length of the hypotenuse and saves it to the `hypotenuse` member variable.
4. Add a static method named `to_string` that prints out a phrase like `A right triangle with length 3 and width 4.`.
5. Create a new class named `Rectangle`, with qn `__init__` method that takes two variables: length and width. The class has two methods: one is named `area` and returns the area of the rectangle, and the other is named `is_square` and returns a boolean to say if the Rectangle is square or not.

## Solutions

 * [Basic OOP - Solutions](problem_set_1_solutions.md)

[Back to Lecture](lecture_06.md)
