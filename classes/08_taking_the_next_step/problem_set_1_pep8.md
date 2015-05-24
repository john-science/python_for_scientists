# PEP8 & Style

All of the "problems" in this set are just examples of poorly formatted Python. Just reformat them, as best you can, to match the [PEP8 standards](https://www.python.org/dev/peps/pep-0008/). Some of the examples are not PEP8 formatting, but just examples of code that is bad far other reasons.

## Reformat the Code

Just reformat the given code. If there are things here that you didn't know about, that's fine. You learned something. No one is grading you, who cares?

### One Statement Per Line

Reformat this code to meet PEP8 standards:

    print 'one'; print "two"
    
    if x == 1: print 'one'
    
    if x >= 2 and derivative(f(y)) < 0:
        print('something')

### Crazy Conditionals

    if thing == True:
        print('True!')
    
    if thing == None:
        print('thing is None!')

### Searching in a Dictionary

    tardis = dict()
    tardis['doctor'] = 'who'

    if tardis.has_key('master'):
        print('Run!')

### Finding Elements in a Dictionary

    d = {'XKCD': 'stick'}
    
    if d.has_key('Garfield'):
        print(d['Garfield'])
    else:
        print('default_value')

### Iterative Loops

    for i in range(100000):
        some_crazy_function(i)

### Reading Text Files

Imagine you are reading a very simple (2 column) CSV file that is several million lines long. And you want to load that data (somehow specially, let's ignore the details) into a big database.

    f = open('/path/to/my_file.csv', 'r')
    d = {}
    
    for line in f.readlines():
        line_list = line.strip().split(',')
        if d.has_key(line_list[0]):
            d[line_list[0]] += float(line_list[1])
        else:
            d[line_list[0]] = float(line_list[1])

### Importing

    import sys, os

### Naming Things

    class parallel_universe(object):
    
        def __init__(self):
            self.EvilSpock = True
        
        def MirrorMirror(self):
            # do something
    
    universeOne = parallel_universe()

### Save Your Indents

    for littleList in someBigList:
        if littleList[0]:
            if littleList[1] == 'Spock':
                if littleList[2] == 'fire':
                    print('Spock! Fire the torpedos!')
                else:
                    print('Runaway!')
            else:
                if littleList[2] == 'fire':
                    print('Sulu! Fire the torpedos!')
                else:
                    print('Runaway!')

### Mystery Example 1

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

### Mystery Example 2

    # d is some big dictionary of craziness
    # a is some big list of string
    
    for i in len(d.keys()):
        someFunction(i, d[i])
    
    for j in range(len(a)):
        print('Value number ' + str(j) + ' is: ' + a[j])

### Mystery Example 3

    import numpy, matplotlib
    
    try:
        f = open('/path/to/some_file.txt', 'r')
    except:
        print('Failed to open file: /path/to/some_file.txt')
        exit()
    
    for Line in f.readlines():
        plotThingsUsingMatplotlib(Line)

### Mystery Example 4

    s={};c={}
    for i in range(1e7):
     if(i%3==0):s[i]=i*i;if(i%y)==0:c[i]=i*i*i

## Solutions

 * [PEP8 - Solutions](problem_set_1_solutions.md)

## Further Reading

Some of the examples above originated in these two websites:
    
 * [Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/writing/style/)
 * [Google Code](https://code.google.com/p/soc/wiki/PythonStyleGuide)

[Back to Lecture](lecture_08.md)
