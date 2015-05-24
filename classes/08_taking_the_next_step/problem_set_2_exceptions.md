## Exceptions

All of the functions have a failure mode that you need to fix by adding at least one Exception.

For a full list of Python's built-in Exceptions, look at the public documentation:

 * [Python 2](https://docs.python.org/2/library/exceptions.html)
 * [Python 3](https://docs.python.org/3/library/exceptions.html)

#### 1. This function returns the fraction of two numbers. But what happens when the denominator is zero?

    def calc_fraction(num, denom):
        '''calculate the fraction of two numbers'''
        return num / demon

#### 2. This function reads in the lines of a file. But what if that file doesn't exist?

    def read_lines(filepath):
        '''simply read in the lines of a text file'''
        f = open(filepath, 'r')
        lines = f.readlines()
        f.close()

#### 3. This function tries to read a value from a dictionary based on a key. But if that key isn't found, we want to return the number zero.

    def read_from_dict(d, key):
        '''read a value from a dictionary,
        based on a key,
        return zero if key is not found.'''
        return d[key]

#### 4. This function calculates the ratio of two numbers. But there are a couple of issues. What if the denominator is zero? Also, what if the values given to the number aren't numbers?

    def calc_ratio(num, denom):
        '''Find the ratio of two numbers'''
        # Note, even if the input numbers are integers, we want
        # the result as a decimal.
        ratio = float(num) / denom
        return ratio

#### 5. This function is meant to help read in a CSV file, it takes in a single line (a string) and returns a tiny dictionary. Use exceptions to catch at least two ways this function might fail.

    def parse_csv_line(line):
        '''This fuction reads a string (line from a CSV file)
        and returns a custom dictionary. The CSV line looks like,
        student,attendance score,hw1 grade,hw2 grade,hw3 grade,exam grade
        Albert Schweitzer,1.00,95,89,27,82
        Frank B. Kellogg,0.975,85,73,25,98
        '''
        line_split = line.strip().split(',')
        student name = line_split[0]
        average_hw = (float(line_split[2]) + float(line_split[3]) + float(line_split[4])) / 3.0
        exam = float(line_split[5])

        d = {}
        d[line_split[0]] = {'average_hw': average_hw, 'final_exam': exam}
        
        return d
        
#### 6. This function is meant to average the percentage score of three homework grades. If any of the grades are below zero or above 100 percent, we need to raise an exception.

    def average_grades(grade1, grade2, grade3):
        '''return the avearge of three homework grades'''
        total = grade1 + grade2 + grade3
        return (total / 3.0)

## Solutions

 * [Exceptions - Solutions](problem_set_2_solutions.md)

[Back to Lecture](lecture_08.md)
