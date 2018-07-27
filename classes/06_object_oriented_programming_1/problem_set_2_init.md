# Be Careful When you init

## Describing the Problem

When creating a new class, you can create potentially invalid states for your objects. For example:

    class Rectangle:
    
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

    class Rectangle:
    
      def __init__(self, x, y):
        self.length_of_x_side = x
        self.length_of_y_side = y

#### Problem 1

Fix the problem with this object initialization:
    
    class Student:
    
        def __init__(self):
            self.first_name = None
            self.last_name = None
        
        def print_full_name(self):
            print(' '.join([self.first_name, self.last_name]))

#### Problem 2

Fix the problem with this object initialization:

    class Student:
    
        def __init__(self, first, last):
            self.first_name = first
            self.last_name = last
        
        def average_grade(self):
            '''Salculate the average grade from the student's
            list of grades. (This is the student's total grade.)
            '''
            return sum(self.grades) / len(self.grades)

#### Problem 3

Create a valid `__init__` method for this class.

    class GPSLocation:
    
        def print_location(self):
            '''A simple print statement, to describe the exact
            GPS location in human terms.
            '''
            print('This GPS location is at a lat/lon of: ' + \
                  str(self.lat) + '/' + str(self.lon) + \
                  'degrees and at an elevation of : '  + \
                  str(self.elevation) + ' meters.')

#### Problem 4

Create an initializing method for this class:

    class Species:
        '''This class is meant to help classify various
        endangered species.'''

        @staticmethod
        def conservation_status_string(n):
            '''Returns the IUCN description for the conservation
            status of a species, given a simple number representing
            that status.'''
            if n == -2:
                return "Not Evaluated"
            elif n == -1:
                return "Data Deficient"
            elif n == 0:
                return "Least Concern"
            elif n == 1:
                return "Not Threatened"
            elif n == 2:
                return "Vulnerable"
            elif n == 3:
                return "Endangered"
            elif n == 4:
                return "Critically Endangered"
            elif n == 5:
                return "Extinct in the Wild"
            elif n == 6:
                return "Extinct"
    
            return "Status Unknown"
    
        def get_status(self):
            '''Based on the status number in this object, returns
            the IUCN string for the conservation status of the species.
            '''
            return Species.conservation_status_string(self.status)
    
        def info(self):
            '''Returns a nice string, describing the species and its 
            conservation status. For instance:
            Elephant Seal (Mirounga angustirostris). Least Concern
            Kakapo (Strigops habroptilus). Critically Endangered
            '''
            full_name_text = self.common_name + "  (" + self.scientific_name + ")."
            
            return full_name_text + "  " + self.get_status()

## Solutions
 * [Problem Set 2 - Solutions](problem_set_2_solutions.md)


[Back to Lecture](lecture_06.md)
