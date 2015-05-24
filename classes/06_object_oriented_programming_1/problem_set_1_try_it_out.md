# Basic OOP - Try It Out

## Try it Out: Using Simple Classes

### Problem 1 - Instantiating Objects

Instantiate (create an instance of) this class:

    class Plot(object):
    
        def __init__(self, num_pixels_x, num_pixels_y):
            self.pixels_x = num_pixels_x
            self.pixels_y = num_pixels_y

### Problem 2 - Using Methods

Instantiate this class and run use it's method to calculate the number of pixels in the final plot:

    class Plot(object):
    
        def __init__(self, num_pixels_x, num_pixels_y):
            self.pixels_x = num_pixels_x
            self.pixels_y = num_pixels_y

        def total_pixels(self):
            '''Calculates the total number of pixels in
            the final plot'''
            return self.pixels_x * self.pixels_y

### Problem 3 - Accessing Attributes

Print the `pixel_x` attribute from an instance of the `Plot` class above.

### Problem 4 - Using Objects

Create two instances of `Point` and write a function that finds the distance between them.

    class Point:
    
       def __init__(self, x=0, y=0):
          self.x = x
          self.y = y

### Try it Out: Writing Simple Classes

    * Coming Soon

## Solutions

 * [Basic OOP - Solutions](problem_set_1_solutions.md)

[Back to Lecture](lecture_06.md)
