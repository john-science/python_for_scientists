# Object-Oriented Programming, Examples

What follows are just some simple examples of OOP in Python.

## Reading Text Files

This is a simple utility class to make reading a text file a tiny bit easier.

```python
class TextFile:

    def __init__(self, filepath, ditch_header=False):
        self.filepath = filepath
        self.ditch_header = ditch_header
        self.lines = []
        self.read_file()
    
    def read_file(self):
        """Read the text file, with or without the first line
        and strip the right end of the file, if necessary."""
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
        self.lines = [line.rstrip() for line in lines[start:]]
    
    def number_of_lines(self):
        """How many lines are in our file?"""
        return len(self.lines)
```

Notice that the `__init__` method takes two parameters: `filepath` is the full path of the file we want to read, and `ditch_header` is a boolean to say whether we want to remove the first line of the file or not. Also notice that the `__init__` method calls a method to fill one of it's values.

We have two methods in this class: `read_file` reads each line of the text file and saves the results (with or without the header), and `number_of_lines` which returns the number of lines in the file.

Here is an example of how we might use the class:

```python
>>> tf = TextFile('/path/to/some/fancy_file.txt')
>>> print(tf.number_of_lines())
12345
```

The power of this class is that I've done all of the work of reading my text file into an array in one line (`tf = TextFile('my_file.txt')`). I can now access the line (`tf.lines`) and do whatever processing I need to do, and ignore all the details about how to read the file.

Now, let's look at another class. This time we will be reading a CSV file.

```python
class CSVFile:

    def __init__(self, filepath):
        self.filepath = filepath
        self.lines = []
        self.header = []
        self.read_file()
    
    def read_file(self):
        '''read the csv file, with or without the first line
        and strip the right end of the file, if necessary'''
        # read the file
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        
        # save off the CSV header
        self.header = lines[0].rstrip().split(',')
        
        # save the files lines as a class attribute
        self.lines = [line.rstrip().split(',') for line in lines[1:]]
    
    def number_of_lines(self):
        '''How many lines are in our file?'''
        return len(self.lines)
    
    def number_of_columns(self):
        '''How many columns are in our CSV file?'''
        return len(self.lines[0])
```

As usual, we see that reading a CSV file is a lot like reading a text file. Our `__init__` method is very similar, except it doesn't take a `ditch_header` parameter, and includes a `header` value. The `read_file` method is really similar, but we use `split(',')` to create lists instead of strings for each line. Also, we added a `number_of_columns` method, which returns the number of columns in our CSV file.

If we had an appropriate file, we could use it by doing:

```python
>>> csv = CSVFile('local/path/to/my/file.csv')
>>> print(csv.number_of_columns())
6789
```

Both `TextFile` and `CSVFile` above are fine as is. But they share a lot of code and ideas (because CSV files are just a type of text file). And it would be nice if we didn't have to repeat ourselves, so maybe both of these classes should subclass the same abstract class:

```python
from abc import ABC, abstractmethod

class AbstractTextFile(ABC):
    
    def __init__(self, filepath, ditch_header):
        self.filepath = filepath
        self.ditch_header = ditch_header
        self.lines = []
        self.read_file()

    @abstractmethod
    def read_file(self):
        pass
        
    def number_of_lines(self):
        '''How many lines are in our file?'''
        return len(self.lines)
```

Again, we can not instantiate an abstract class:

```python
>>> atf = AbstractTextFile('my_file.txt', True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class AbstractTextFile with abstract methods get_area
```

Now we can re-write `TextFile` using our new abstract class:

```python
class TextFile(AbstractTextFile):

    def __init__(self, filepath, ditch_header=False):
        AbstractTextFile.__init__(filepath, ditch_header)
    
    def read_file(self):
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
        self.lines = [line.rstrip() for line in lines[start:]]
```

Even though `TextFile` is now based on an abstract class, we don't change how we would use it:

```python
>>> tf = TextFile('/path/to/some/fancy_file.txt')
>>> print(tf.number_of_lines())
12345
```

We can also re-write our `CSVFile` class using the same abstract base class:

```python
class CSVFile(AbstractTextFile):

    def __init__(self, filepath):
        AbstractTextFile.__init__(filepath, True)
        self.header = []
    
    def read_file(self):
        """Read the csv file, with or without the first line
        and strip the right end of the file, if necessary."""
        # read the file
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        
        # save off the CSV header
        self.header = lines[0].rstrip().split(',')
        
        # save the files lines as a class attribute
        self.lines = [line.rstrip().split(',') for line in lines[1:]]
    
    def number_of_columns(self):
        """How many columns are in our CSV file?"""
        return len(self.lines[0])
```
        
Now we have two classes, `TextFile` and `CSVFile`, based on the same abstract class `AbstractTextFile`. There is some shared code and functionality in the abstract class `AbstractTextFile`. But since CSV files are special text files, we have some differences there that we need to express. The goal of using this abstract class is to express the similarity between our two subclasses.

Abstract classes are particularly useful if you don't just have two classes in your code, but many. You can organize your thoughts around all of the things you need to think about. And when you need to remember something, you have a solid frame of reference for the current piece of the puzzle.


[Back to Lecture](lecture_07.md)
