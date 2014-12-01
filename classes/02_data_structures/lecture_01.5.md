# Data Structures

Whether designing a huge program or a short script, it is important to choose your data structures appropriately. Following the "batteries included" philosophy, Python has several handy data structures built right in.

####  lists

This is the collection of data most commonly used in Python. Lists are what they seem: a list of values. Each value is numbered, starting with zero. You can remove values from a list or add values to the end. The elements of the list don't even need to be the same type:

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
    >>> my_list[-2:]
    [4444, 55555]

You can also modify lists in a wide variety of convenient ways:

    >>> list1 = [1, 2, 3]
    >>> list2 = [4, 5, 6]
    >>> list1 + list 2
    [1, 2, 3, 4, 5, 6]
    >>> list1.append(9)
    >>> list1
    [1, 2, 3, 9]
    >>> len(list1)  # strictly speaking, this isn't modifying the list
    4
    >>> list2.reverse()
    >>> list2
    [6, 5, 4]

If you want to learn more about what kinds of functionality are built into Python for lists (or anything else, for that matter), simply type `help` in the interpreter:

    >>> help(list1)

####  tuples

Tuples are just like lists, but you can't change their values. Again, each value is numbered starting from zero. As an example, the days of the week:

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

####  sets

A set is a bit like a list, except every value in a set is unique. If you had an empty set of numbers and you added the number `3` a million times, the set would still just be `(3)`. Sets are designed to preserve this uniqueness when you add a new element.

You can define a new set and add some values:

    >>> tolkein = set()
    >>> tolkein.add('orc')
    >>> tolkein.add('goblin')
    >>> tolkein.add('troll')
    >>> tolkein.add('dragon')
    >>> tolkein.add('orc')
    >>> tolkein.add('orc')
    >>> tolkein.add('orc')
    >>> tolkein
    set(['orc', 'goblin', 'troll', 'dragon'])

And you can remove values from a set:

    >>> tolkein.remove('dragon')
    >>> tolkein
    set(['orc', 'goblin', 'troll'])

And perform various other operations:

    >>> len(tolkein)
    3
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

Set theory is a whole field in mathematics. But the basics of set theory, as they apply to computer science are easy to understand. For more information, just look on Wikipedia for: [sets](http://en.wikipedia.org/wiki/Set_%28abstract_data_type%29), [subset](http://en.wikipedia.org/wiki/Subset), [superset](http://en.wikipedia.org/wiki/Subset), [union](https://en.wikipedia.org/wiki/Union_%28set_theory%29), and [intersection](https://en.wikipedia.org/wiki/Intersection_%28set_theory%29).

####  dictionaries

Dictionaries are similar to what their name suggests - a dictionary. In a dictionary, you have an 'index' of words, and for each of them a definition. In Python, the word is called a 'key', and the definition a 'value'. The values in a dictionary aren't numbered - they aren't in any specific order, either - the key does the same thing. (Each key must be unique, though!) You can add, remove, and modify the values in dictionaries.

Creating a dictionary is much like anything else, but you use curly brace (`{`, `}`) to define a collection as dictionary and a colon (`:`) to define a key/value pair:

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
