# Basic OOP

## Try it Out: Using Simple Classes

### Solution 1 - Instantiating Objects

    plot1 = Plot(600, 400)

### Solution 2 - Using Methods

    plot2 = Plot(600, 400)
    print(plot2.total_pixels())

### Solution 3 - Accessing Attributes

    plot3 = Plot(900, 300)
    print(plot3.pixel_x)

### Solution 4 - Using Objects

    from math import sqrt
    
    origin = Point()
    point = Point(5, 15)
    
    def distance(pnt1, pnt2):
        '''Find the distance between to Point instances'''
        return sqrt((pnt2.x - pnt1.x)**2 + (pnt2.y - pnt1.y)**2)
    
    print(distance(origin, point))

## Try it Out: Writing Simple Classes

    * Coming Soon
        

[Back to Problem Set](problem_set_1_try_it_out.md)
