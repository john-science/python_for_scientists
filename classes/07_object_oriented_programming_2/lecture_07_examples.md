# Object-Oriented Programming, Examples

What follows are just some simple examples of OOP in Python.

## Reading Text Files

This is a simple utility class to make reading a text file a tiny bit easier.

    class TextFile(object):
    
        def __init__(self, filepath, ditch_header=False):
            self.filepath = filepath
            self.ditch_header = ditch_header
            self.lines = []
            self.read_text_file()
        
        def read_text_file(self):
            '''read the text file, with or without the first line
            and strip the right end of the file, if necessary'''
            # read the file
            f = open(self.filepath, 'r')
            lines = f.readlines()
            f.close()
    
            # do we want the header row?
            if self.ditch_header:
                start = 1
            else:
                start = 0
            
            # save the files lines as a class attribute
            self.lines = lines[start:]
            # OR self.lines = [l.rstrip() for l in lines[start:]]
        
        def number_of_lines(self):
            '''How many lines are in our file?'''
            return len(self.lines)

Notice that the `__init__` method takes two parameters: `filepath` is the full path of the file we want to read, and `ditch_header` is a boolean to say whether we want to remove the first line of the file or not. Also notice that the `__init__` method calls a method to fill one of it's values.

We have two methods in this class: `read_text_file` reads each line of the text file and saves the results (with or without the header), and `number_of_lines` which returns the number of lines in the file.

Now, let's look at another class. This time we will be reading a CSV file.

    class CSVFile(object):
    
 * Coming Soon


## Making Plots

 * Coming Soon


[Back to Lecture](lecture_07.md)
