## Exceptions

#### 1. This function returns the fraction of two numbers. But what happens when the denominator is zero?

    def calc_fraction(num, denom):
        """calculate the fraction of two numbers"""
        if denom == 0.0:
            raise Exception("Cannot divide by zero.")

        return num / demon

#### 2. This function reads in the lines of a file. But what if that file doesn't exist?

This is the easy way:

    def read_lines(filepath):
        """simply read in the lines of a text file"""
        try:
            f = open(filepath, "r")
        except:
            print("File not found")
            return None
        lines = f.readlines()
        f.close()

But it is better to be as specific as possible when catching errors. The idea is that you might accidentally trap errors that you didn't predict, and your code won't be able to handle such errors. In this case, you would be better off only catching the 'file not found' type of exception. You would do that by only catching the `IOError` exceptions:

    def read_lines(filepath):
        """simply read in the lines of a text file"""
        try:
            f = open(filepath, "r")
        except IOError as e:
            print(f"File not found: {e}")
            return None
        lines = f.readlines()
        f.close()

#### 3. This function tries to read a value from a dictionary based on a key. But if that key isn't found, we want to return the number zero.

The same as problem number 2, this is the easy way:

    def read_from_dict(d, key):
        """read a value from a dictionary,
        based on a key,
        return zero if key is not found.
        """
        try:
            value = d[key]
        except:
            value = 0

        return value

But this is a better way:

    def read_from_dict(d, key):
        """read a value from a dictionary,
        based on a key,
        return zero if key is not found.
        """
        try:
            value = d[key]
        except KeyError as e:
            value = 0

        return value

#### 4. This function calculates the ratio of two numbers. But there are a couple of issues. What if the denominator is zero? Also, what if the values given to the inputs aren't numbers?

The easy way:

    def calc_ratio(num, denom):
        """Find the ratio of two numbers"""
        # Note, even if the input numbers are integers, we want
        # the result as a decimal.
        if denom == 0:
            raise Exception("Cannot divide by zero.")
        elif not num in (int, long, float, complex):
            raise Exception("The numerator must be a number.")
        elif not denom in (int, long, float, complex):
            raise Exception("The denominator must be a number.")
        
        ratio = float(num) / denom
        return ratio

A better way:

    def calc_ratio(num, denom):
        """Find the ratio of two numbers"""
        # Note, even if the input numbers are integers, we want
        # the result as a decimal.
        if denom == 0:
            raise ValueError("Cannot divide by zero.")
        elif not isinstance(num, (int, long, float, complex))
            raise TypeError("The numerator must be a number.")
        elif not isinstance(denom, (int, long, float, complex))
            raise TypeError("The denominator must be a number.")
        
        ratio = float(num) / denom
        return ratio

Along with more specific Exceptions, the above solution uses `isinstance`. This is just a convenient way to check the type of a variable.

#### 5. This function is meant to help read in a CSV file, it takes in a single line (a string) and returns a tiny dictionary. Use exceptions to catch at least two ways this function might fail.

The easy way:

    def parse_csv_line(line):
        """This fuction reads a string (line from a CSV file)
        and returns a custom dictionary. The CSV line looks like,
        student,attendance score,hw1 grade,hw2 grade,hw3 grade,exam grade
        Albert Schweitzer,1.00,95,89,27,82
        Frank B. Kellogg,0.975,85,73,25,98
        """
        line_split = line.strip().split(",")
        student name = line_split[0]
        try:
            average_hw = (float(line_split[2]) + float(line_split[3]) + float(line_split[4])) / 3.0
        except Exception:
            print("The CSV homework columns are invalid.")
            return {}
        try:
            exam = float(line_split[5])
        except IndexError as ie:
            print("The CSV exam columns are invalid.")
            return {}

        d = {}
        d[line_split[0]] = {"average_hw": average_hw, "final_exam": exam}
        
        return d

A better way:

    def parse_csv_line(line):
        """This fuction reads a string (line from a CSV file)
        and returns a custom dictionary. The CSV line looks like,
        student,attendance score,hw1 grade,hw2 grade,hw3 grade,exam grade
        Albert Schweitzer,1.00,95,89,27,82
        Frank B. Kellogg,0.975,85,73,25,98
        """
        line_split = line.strip().split(",")
        student name = line_split[0]
        try:
            average_hw = (float(line_split[2]) + float(line_split[3]) + float(line_split[4])) / 3.0
            exam = float(line_split[5])
        except ValueError as ve:
            print("The CSV column contains text, and not a number.")
            return {}
        except IndexError as ie:
            print("The CSV line does not contain enough columns.")
            return {}

        d = {}
        d[line_split[0]] = {"average_hw": average_hw, "final_exam": exam}
        
        return d

Notice that the empty dictionary `{}` is returned here. Depending on the surrounding code, it might be better to simply `exit()` the program. I'll leave this to your discretion.
        
#### 6. This function is meant to average the percentage score of three homework grades. If any of the grades are below zero or above 100 percent, we need to raise an exception.

The easy way:

    def average_grades(grade1, grade2, grade3):
        """return the avearge of three homework grades"""
        if grade1 < 0 or grade2 < 0 or grade3 < 0:
            raise Exception("Grades cannot be below zero.")
        elif grade1 > 100 or grade2 > 100 or grade3 > 100:
            raise Exception("Grades cannot be above one hundred.")
        
        total = grade1 + grade2 + grade3
        return (total / 3.0)

A better way:

    def average_grades(grade1, grade2, grade3):
        """Return the avearge of three homework grades."""
        if grade1 < 0 or grade2 < 0 or grade3 < 0:
            raise ValueError("Grades cannot be below zero.")
        elif grade1 > 100 or grade2 > 100 or grade3 > 100:
            raise ValueError("Grades cannot be above one hundred.")
        
        total = grade1 + grade2 + grade3
        return (total / 3.0)


[Back to Problem Set](problem_set_2_exceptions.md)
