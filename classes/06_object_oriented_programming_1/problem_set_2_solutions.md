# Be Careful When you init

## Solution 1

    class Student(object):
    
        def __init__(self, first, last):
            self.first_name = first
            self.last_name = last

## Solution 2

    class Student(object):
    
        def __init__(self, first, last, grades):
            self.first_name = first
            self.last_name = last
            self.grades = grades  # or possibly self.grades = []
        
        def average_grade(self):
            '''Salculate the average grade from the student's
            list of grades. (This is the student's total grade.)
            '''
            return sum(self.grades) / len(self.grades)

## Solution 3

    class GPSLocation(object):
    
        def __init__(self, lat, lon, elevation):
            self.lat = lat
            self.lon = lon
            self.elevation = elevation

## Solution 4

    class Species(object):
    
        def __init__(self, com, sci, status):
            self.common_name = com
            self.scientific_name = sci
            self.status = int(status)


[Back to the Problem Set](problem_set_2_init.md)
