# Data Structures

A "data structure" is a way to organize data and store it in a computer. In the first class we only saw individual `type`s of data: integers, floats, strings, and booleans. But if you're using a computer to solve a problem, chances are you have many pieces of data that are related to each other in some way. Python has four standard data structures to that you will find useful when organizing your data: lists, dictionaries, tuples, and sets.

###  lists

This is the most commonly-used way to collect your data in Python. Lists are what they seem: a sequental collection of values. Each value is numbered, starting with zero. You can retrieve these number values or modify them. The elements of the list don't even need to be the same type:

    new_list = []
    my_list = [1, 2, 3]
    my_other_list = [1, 2.2222, 'three']

You can select elements from an array in almost arbitrary fashion:

    >>> my_list = [1, 22, 333, 4444, 55555]
    >>> my_list[0]
    1
    >>> my_list[2]
    333
    >>> my_list[1:3]  # this is called a slice
    [22, 333]
    >>> my_list[-1]
    55555
    >>> my_list[-2:]  # just like a string!
    [4444, 55555]

You can also modify and interact with lists in a wide variety of convenient ways:

    >>> list1 = [1, 2, 3]
    >>> list2 = [4, 5, 6]
    >>> list1 + list 2
    [1, 2, 3, 4, 5, 6]
    >>> list1.append(9)
    >>> list1
    [1, 2, 3, 9]
    >>> list2.reverse()
    >>> list2
    [6, 5, 4]

###  dictionaries

Dictionaries in Python are similar to dictionaries in real life. They both have keys matched with a value. A real world key is a word and the value is a definition. In Python, a dictionary has a set of "keys" (keys can be simple things like numbers and strings) and each key has a related "value". The value could be something simple, like an integer, or more complicated like a list or another dictionary. You can add, remove, and modify both keys and values in dictionaries.

You can create an empty dictionary with just the curly braces:

    d = {}

And you use colons define a key/value pair:

    gdp = {'USA': 16244600, 'China': 8358400, 'Japan': 5960180, 'Ghana': 40711, 'Samoa': 681}

To retreive a value from a dictionary, simply supply the related key:

    >>> gdp['Samoa']
    681

However, if that key doesn't exist, Python will throw an error:

    >>> gdp['Czechoslovakia']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'Czechoslovakia'

To add a new key/value pair to an existing dictionary, just asign the new value:

    gdp['Germany'] = 3425956

You can also delete an element from a dictionary:

    del gdp['Japan']

To retreive all the keys or values from a dictionary:

    >>> gdp.keys()
    ['USA', 'Germany', 'China', 'Samoa', 'Ghana']
    >>> gdp.values()
    [16244600, 8358400, 40711, 681, 3425956]

**NOTE**: It is important to know that when you retreive all of the keys or values from a dictionary in this way, they will not be ordered. Do not expect that you can predict what *order* these keys or values come out in.

###  tuples

Tuples are just like lists, but you can't change their values (they are "immutable"). Again, each value is numbered starting from zero. As an example, the days of the week:

    dow = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

You can access elements of a tuple, just like it was a list:

    >>> dow[1]
    'Tuesday'
    >>> dow[1:3]
    ('Tuesday', 'Wednesday')

But you can't modify the tuple:

    >>> dow[0] = 'Friday'  # In your dreams.
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

Of course, you can create and empty tuple, by doing this:

    empty = ()

But I find that I don't do this much, as now I have an empty tuple that I can't modify. So... what good does it do me?

###  sets

Imagine we want to know every county that the students in this class were born in. If we went through each student and asked them where they were born, we would probably get the response "United States" several times. But that's not quite what we want. We want a short list with each country just written once. There is a standard Python data structure for this called a "set".

First, let's create an empty set:

    >>> tolkein = set()

Now, let's add some elements to it:

    >>> tolkein.add('orc')
    >>> tolkein.add('goblin')
    >>> tolkein.add('troll')
    >>> tolkein.add('dragon')
    >>> tolkein.add('orc')
    >>> tolkein.add('orc')
    >>> tolkein.add('orc')

And let's print the set:

    >>> tolkein
    set(['orc', 'goblin', 'troll', 'dragon'])

And we can remove an element from a set:

    >>> tolkein.remove('dragon')
    >>> tolkein
    set(['orc', 'goblin', 'troll'])

The picture to have in your mind, is that [sets](http://en.wikipedia.org/wiki/Set_%28abstract_data_type%29) are like [Venn diagrams](https://en.wikipedia.org/wiki/Venn_diagram). Two different sets might overlap a little or a lot. And we can consider their [union](https://en.wikipedia.org/wiki/Union_%28set_theory%29), [intersection](https://en.wikipedia.org/wiki/Intersection_%28set_theory%29), or if one is a [subset](http://en.wikipedia.org/wiki/Subset) of another. All of these general ideas about sets can be computed inside Python:

    >>> tolk2 = set(['elf', 'dwarf'])
    >>> tolkein.union(tolk2)
    set(['orc', 'goblin', 'troll', 'elf', 'dwarf'])
    >>> elf = set(['elf'])
    >>> elf.issubset(tolk2)  # determine if one set is a subset of another
    True
    >>> tolk2.issuperset(elf)  # determine if one set is a superset of another
    True
    >>> elf.intersection(tolk2)  # find the intersection of two sets
    set(['elf'])

### Helper Methods

Each of the data structures above have methods built in to help you do things you'll commonly want to do. We can actually use some of these helper methods to draw a strong parallel between the structures.

#### Looping

We can use `for` with `in` to loop through any of the four data structures above:

    # list
    for item in my_list:
        print(item)
    
    # dict
    for key in gdp:
        print(key)
        print(gdp[key])
    
    # tuple
    for day in dow:
        print(day)
    
    # set
    for creature in tolkein:
        print(creature)

#### Length

You can find the number of items in each data structure in the same way:

    # list
    len(my_list)
    
    # dict
    len(gdp)
    
    # tuple
    len(dow)
    
    # set
    len(tolkein)

Notice that `len` of a dictionary only returns the number of keys, it doesn't say anything about the number of values in the dictionary. It is the same for all four data structures, actually. If you have a list of lists, using `len` will only tell you the number of outermost elements. Make some lists of lists, or lists of sets, and try this out.

#### in

You can also test to see if something is in each of these data structures using the keyword `in` (which is somewhat different outside a `for` loop:

    # list
    >>> 2 in my_list
    True
    
    # dict
    >>> 'Japan' in gdp
    False
    
    # tuple
    >>> 'Monday' in dow
    True
    
    # set
    >>> 'troll' in tolkein
    True

#### For More Info

If you want to learn more about what kinds of functionality are built into Python for any of the structures above, simply type `help` in the interpreter:

    >>> help(my_list)
    >>> help(gdp)
    >>> help(dow)
    >>> help(tolkein)

## Problem Sets

 * [Basic Data Structures](problem_set_1_data_structures.md)

## Further Reading

 * [Google Ed - lists and using them](https://developers.google.com/edu/python/lists)
 * [An Informal Introduction - Lists](https://docs.python.org/2/tutorial/introduction.html#lists)
 * [Python Tutorial: Sets](http://www.python-course.eu/sets_frozensets.php)
 * [Python Tutorial: Lists, Tuples, and Slicing](http://www.python-course.eu/sequential_data_types.php)


[Back to Syllabus](../../README.md)
