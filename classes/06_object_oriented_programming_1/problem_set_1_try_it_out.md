# Try It Out

Don't scroll too far down, or you will see the answers.

## Try it Out: Using Simple Classes

### Problem 1 - Instantiating Objects

Instantiate (create an instance of) this class:

    class Plot(object):
    
        def __init__(self, num_pixels_x, num_pixels_y):
            self.pixels_x = num_pixels_x
            self.pixels_y = num_pixels_y

### Solution 1

    plot1 = Plot(600, 400)

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

### Solution 2

    plot2 = Plot(600, 400)
    print(plot2.total_pixels())

### Problem 3 - Accessing Attributes

Print the `pixel_x` attribute from an instance of the `Plot` class above.

### Solution 3

    plot3 = Plot(900, 300)
    print(plot3.pixel_x)

### Problem 4 - Using Objects

Create two instances of `Point` and write a function that finds the distance between them.

    class Point:
    
       def __init__(self, x=0, y=0):
          self.x = x
          self.y = y

### Solution 4

    from math import sqrt
    
    origin = Point()
    point = Point(5, 15)
    
    def distance(pnt1, pnt2):
        '''Find the distance between to Point instances'''
        return sqrt((pnt2.x - pnt1.x)**2 + (pnt2.y - pnt1.y)**2)
    
    print(distance(origin, point))

## Try it Out: Writing Simple Classes

    * Coming Soon
        

[Back to Lecture](lecture_06.md)
