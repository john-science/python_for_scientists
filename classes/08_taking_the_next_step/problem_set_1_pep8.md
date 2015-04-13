# PEP8 & Code Choices

All of the "problems" in this set are just examples of poorly formatted Python. Just reformat them, as best you can, to match the [PEP8 standards](https://www.python.org/dev/peps/pep-0008/). Some of the examples are not PEP8 formatting, but just examples of code that is bad far other reasons.

Don't scroll down too far, or you'll see the solutions.

## Reformat the Code

Just reformat the given code. If there are things here that you didn't know about, that's fine. You learned something. No one is grading you, who cares?

### One Statement Per Line

#### Example Code

Reformat this code to meet PEP8 standards:

    print 'one'; print "two"
    
    if x == 1: print 'one'
    
    if x >= 2 and derivative(f(y)) < 0:
        print('something')

#### Solution (Reformatted Code)

    print('one')
    print('two')
    
    if x == 1:
        print('one')
    
    x_is_big = x >= 200
    slope_is_negative = derivative(f(x)) < 0;
    
    if x_is_big and slope_is_negative:
        print('something')

### Crazy Conditionals

#### Example Code

    if thing == True:
        print('True!')
    
    if thing == None:
        print('thing is None!')

#### Solution (Reformatted Code)

What if the value of `thing` is `False`? And while we're at it, why would you ever write `if thing == True`? Isn't that just the same as `if thing`? And let's connect all of these `if` statements in the standard way:

    if thing:
        print('thing is truthy!')
    elif not thing:
        print('thing is falsey!')
    elif thing is None:
        print('thing is None!')

### Searching in a Dictionary

#### Example Code

    tardis = dict()
    tardis['doctor'] = 'who'

    if tardis.has_key('master'):
        print('Run!')

#### Solution (Reformatted Code)

The major problem with the above example code is that the `has_key` function has been deprecated. It is now preferable to use `in` for Python 2.x and 3.x.

Also, that `dict()` there is technically find. But don't be fancy.

    tardis = {}
    tardis['doctor'] = 'who'

    if 'master' in tardis:
        print('Run!')

### Finding Elements in a Dictionary

#### Example Code

    d = {'XKCD': 'stick'}
    
    if d.has_key('Garfield'):
        print(d['Garfield'])
    else:
        print('default_value')

#### Solution (Reformatted Code)

Again, we see the old `has_key` function used. Ick. But also this is a prime example of using the dictionary method `get`. This will allow you to return a default value if the key you are looking for in the dictionary does not exist.

    d = {'XKCD': 'stick'}
    
    # These are examples of how to safely retrieve values from dictionaries
    print(d.get('XKCD', 'default_value'))       # prints 'stick'
    print(d.get('Garfield', 'default_value')')  # prints 'default_value'

    # Or you can do an explicit test first
    if 'Garfield' in d:
        print('fat_cat')
    else:
        print('default_value')

### Iterative Loops

#### Example Code (Python versions 1.x and 2.x.)

    for i in range(100000):
        some_crazy_function(i)

#### Solution (Reformatted Code)

The problem with the above example is the `range` keyword. It will create an actual array in memory of 100,000 numbers. This might be okay, but if this happens a lot, you are suddenly wasting a lot of time and memory. If you instead use `xrange`, you are creating an [iterator](https://wiki.python.org/moin/Iterator) that will generate one number at a time. This will be faster can conserve memory.

    for i in xrange(100000):
        some_crazy_function(i)

*Fun Fact:* This is such an important standard that the old `range` has been entirely replaced with `xrange` in Python 3.x.

### Reading Text Files

#### Example Code

Imagine you are reading a very simple (2 column) CSV file that is several million lines long. And you want to load that data (somehow specially, let's ignore the details) into a big database.

    f = open('/path/to/my_file.csv', 'r')
    d = {}
    
    for line in f.readlines():
        line_list = line.strip().split(',')
        if d.has_key(line_list[0]):
            d[line_list[0]] += float(line_list[1])
        else:
            d[line_list[0]] = float(line_list[1])

#### Solution (Reformatted Code)

Okay, the major problem here is `f.readlines()`. Much like `range`, this will load the entire CSV file into memory. But we says this files is millions of lines long. And, okay, this file only has two columns. But what if it had more, that's potentiall a lot to read into memory. Using `xreadlines()` generates an iterator, that will only read one line at a time. So you will only have one line at a time in memory. Much better.

    f = open('/path/to/my_file.csv', 'r')
    d = {}
    
    for line in f.xreadlines():
        line_list = line.strip().split(',')
        if line_list[0] not in d:
            d[line_list[0]] = 0.0
        d[line_list[0]] += float(line_list[1])

    f.close()

*NOTE:* Python is pretty good at this, but just go ahead and `.close()` every file you open. Worst case scenario, at least the person reading your code knows you're done with that file.

### Importing

#### Example Code

    import sys, os

#### Solution (Reformatted Code)

Keep each `import` on a separate line. And most people keep them in alphabetical order, because things easier to find when you start to get a lot of imports.

    import os
    import sys

### Naming Things

#### Example Code

    class parallel_universe(object):
    
        def __init__(self):
            self.EvilSpock = True
        
        def MirrorMirror(self):
            # do something
    
    universeOne = parallel_universe()

#### Solution (Reformatted Code)

Class names should be `CamelCase`.
Function and Method names should be `underscore_case`.
Variable and Attribute names should be `underscore_case`.

    class ParallelUniverse(object):
    
        def __init__(self):
            self.evil_spock = True
        
        def mirror_mirror(self):
            # do something
        
    universe_one = ParallelUniverse()

### Mystery Example 1

#### Example Code

This function returns all the Fibonacci numbers below n. Fix it up.

    def Fib(n):
        resultList = []
        a, b = 0,1
        while b <n:
              resultList.append(b)
              a, b = b, a+b
        return resultList
    
    F100 = Fib(100)
    print F100

#### Solution (Reformatted Code)

    def fibonacci_list(n):
        '''Returns all of the Fibonacci Numbers below n'''
        result_list = []
        a = 0
        b = 1
        while b < n:
            result_list.append(b)
            temp = a
            a = b
            b += temp
        return result_list
    
    first_100 = fibonacci_list(100)
    print(first_100)


## Further Reading

Some of the examples above originated in these two websites:
    
 * [Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/writing/style/)
 * [Google Code](https://code.google.com/p/soc/wiki/PythonStyleGuide)
