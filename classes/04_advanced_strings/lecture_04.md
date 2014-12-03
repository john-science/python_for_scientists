# Advanced Strings

## String Operations

Python has a nice variety of tools to do commonly-desired things to strings.

#### `lower`, `upper`, `capitalize` do what you'd think:

    >>> "funKY tOwn".capitalize()
    'Funky town'
    >>> "funky tOwn".lower()
    'funky town'
    >>> "funky tOwn".ooper()
    'FUNKY TOWN'

#### `split` splits a string using another string:

    >>> "funKY tOwn".split()
    ['funKY', 'tOwn']
    >>> "funKY tOwn".capitalize().split()
    ['Funky', 'town']
    >>> [x.capitalize() for x in "funKY tOwn".split()]
    ['Funky', 'Town']
    >>> "I want to take you to, funKY tOwn".split("u")
    ['I want to take yo', ' to, f', 'nKY tOwn']
    >>> "I want to take you to, funKY tOwn".split("you")
    ['I want to take ', ' to, funKY tOwn']

Notice that by default, `split` uses spaces to split the string.

#### `strip`, `join`, `replace` are also super usefule:

    >>> csv_string = 'Dog,Cat,Spam,Defenestrate,1, 3.1415 \n\t'
    >>> csv_string.strip()
    'Dog,Cat,Spam,Defenestrate,1, 3.1415'
    >>> clean_list = [x.strip() for x in csv_string.split(",")]
    >>> clean_list
    ['Dog', 'Cat', 'Spam', 'Defenestrate', '1', '3.1415']
    
#### `join` allows you to combine a list of strings into one:

    >>> print ",".join(clean_list)
    'Dog,Cat,Spam,Defenestrate,1,3.1415'
    >>> print "\t".join(clean_list)
    Dog! Cat! Spam!
    Defenestrate!1! 3.1415

#### `replace` strings in strings with other strings

    >>> csv_string = 'Dog,Cat,Spam,Defenestrate,1, 3.1415 \n\t'
    >>> alt_csv = csv_string.strip().replace(' ','')
    >>> alt_csv
    'Dog,Cat,Spam,Defenestrate,1,3.1415'
    >>> print csv_string.strip().replace(' ','').replace(',','\t')
    Dog! Cat! Spam!
    Defenestrate!1! 3.1415

#### `find` searches for a substring, and returns the index of the first found:

    >>> s = 'My Funny Valentine'
    >>> s.find("y")
    1
    >>> s.find("y",2)
    7
    >>> s[s.find("Funny"):]
    'Funny Valentine'
    >>> s.find("z")
    -1
    >>> ss = [s,"Argentine","American","Quarentine"]
    >>> for thestring in ss:
            if thestring.find("tine") != -1:
                print "'" + str(thestring) + "' contains 'tine'."
    'My Funny Valentine' contains 'tine'.
    'Argentine' contains 'tine'.
    'Quarentine' contains 'tine'.

#### `str` casts a variable to a string format, where available:

    >>> str(3)
    '3'
    >>> str(3.14)
    '3.14'
    >>> str(True)
    'True'
    >>> str(type(3.14))
    "<type 'float'>"
    >>> str(True and False)
    'False'
    >>> str(1 + 2 + 3 + 4 + 5.0)
    '15.0'

Not everything can be converted using `str()`, only classes which have a `__str__` method. (We'll see more about classes later.)

## Reading and Writing Text Files

`open`

## Reading and Writing CSV Files

`import csv`


[Back to Syllabus](../../README.md)
