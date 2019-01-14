# Data Structures

A "data structure" is a way to organize data in a computer. In the first lecture, we looked at the simplest data structure, a single primitive `type`: integers, floats, strings, and booleans. But if you're using a computer to solve a problem, chances are you have many pieces of data that are inter-related to each other in some way. Python has four standard data structures that you will find useful when organizing your data: lists, dictionaries, tuples, and sets.

###  lists

This is the most frequently used data structure in Python. Lists are what they sound like: a sequental collection of values. Each value is numbered, starting with zero. You can retrieve these numbered values or modify them. And the values don't even need to be the same type:

```python
new_list = []                         # empty list
my_list = [1, 2, 3]
my_other_list = [1, 2.2222, 'three']
```

You can select elements from a list just like we selected elments from strings in the first class:

```python
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
```

You can also modify and interact with lists in a wide variety of convenient ways:

```python
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
```

It turns out that if you want to add items to a list, `.append()` is the fastest way. And if you want to remove elements from a list `.pop()` is the fastest way. Though `.pop()` only removes the last element from the list, so it is not always helpful:

```python
>>> blue_box = ['S', 'I', 'D', 'R', 'A', 'T']
>>> blue_box.pop()
'T'
>>> blue_box.pop()
'A'
>>> blue_box.pop()
'R'
>>> print(blue_box)
['S', 'I', 'D']
```

###  dictionaries

Dictionaries in Python are similar to dictionaries in real life. They both have keys matched with a value. A real world key is a word and the value is a definition. In Python, a dictionary has a set of "keys" (keys can be simple things like numbers and strings) and each key has a related "value". The value could be almost anything. You can add, remove, and modify both keys and values in dictionaries.

You can create an empty dictionary with just the curly braces:

```python
d = {}
```

And you use colons define a key/value pair:

```python
gdp = {'USA': 16244600, 'China': 8358400, 'Japan': 5960180, 'Ghana': 40711, 'Samoa': 681}
```

To retreive a value from a dictionary, simply supply the related key:

```python
>>> gdp['Samoa']
681
```

Notice, that since we pull values out of the dictionary by using a single key, that means that all the keys in the dictionary have to be unique. Otherwise, Python wouldn't know which `'Samoa'` you were talking about.

However, if that key doesn't exist, Python will throw an error:

```python
>>> gdp['Czechoslovakia']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Czechoslovakia'
```

To add a new key/value pair to an existing dictionary, just asign the new value:

```python
gdp['Germany'] = 3425956
```

You can also delete an element from a dictionary:

```python
del gdp['Japan']
```

To retreive all the keys or values from a dictionary (Python 3.x):

```python
>>> gdp.keys()
dict_keys(['USA', 'Germany', 'China', 'Samoa', 'Ghana'])
>>> gdp.values()
dict_keys([16244600, 8358400, 40711, 681, 3425956])
```

**NOTE**: It is important to know that when you retreive all of the keys or values from a dictionary in this way, they will not be ordered. Do not expect that you can predict what *order* these keys or values come out in.


###  tuples

Tuples are just like lists, but you can't change their values (they are "immutable"). Again, each value is numbered starting from zero. As an example, the days of the week:

```python
dow = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
```

You can access elements of a tuple, just like it was a list:

```python
>>> dow[1]
'Tuesday'
>>> dow[1:3]
('Tuesday', 'Wednesday')
```

But you can't modify the tuple:

```python
>>> dow[0] = 'Friday'  # In your dreams.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Of course, you can create and empty tuple, by doing this:

```python
empty = ()
```

But I find that I don't do this much, as now I have an empty tuple that I can't modify. So... what good does it do me?


###  sets

Imagine we want to know every country that the students in this class were born in. If we went through each student and asked them where they were born, we would probably get the response "United States" several times. But that's not quite what we want. We want a short list with each country just written once. There is a standard Python data structure for this called a "set".

First, let's create an empty set:

```python
>>> class1 = set()
```

Now, let's add some elements to it:

```python
>>> class1.add('United States')
>>> class1.add('China')
>>> class1.add('United States')
>>> class1.add('Japan')
>>> class1.add('France')
>>> class1.add('China')
>>> class1.add('United States')
>>> class1.add('Columbia')
```

And let's print the set:

```python
>>> class1
set(['Japan', 'United States', 'China', 'Columbia', 'France'])
```

And we can remove an element from a set:

```python
>>> class1.remove('Japan')
>>> class1
set(['United States', 'China', 'Columbia', 'France'])
```

The picture to have in your mind, is that [sets](http://en.wikipedia.org/wiki/Set_%28abstract_data_type%29) are like [Venn diagrams](https://en.wikipedia.org/wiki/Venn_diagram). Two different sets might overlap a little or a lot. And we can consider their [union](https://en.wikipedia.org/wiki/Union_%28set_theory%29), [intersection](https://en.wikipedia.org/wiki/Intersection_%28set_theory%29), or if one is a [subset](http://en.wikipedia.org/wiki/Subset) of another. All of these general ideas about sets can be computed inside Python:

```python
>>> class2 = set(['Icleand', 'United States'])
>>> class1.union(class2)
set(['United States', 'China', 'Columbia', 'France', 'Iceland'])
>>> johanna = set(['Icleand'])
>>> johanna.issubset(class2)  # determine if one set is a subset of another
True
>>> class2.issuperset(johanna)  # determine if one set is a superset of another
True
>>> johanna.intersection(class2)  # find the intersection of two sets
set(['Icleand'])
```

### Helper Methods

Each of the data structures above have methods built in to help you do things you'll frequently want to do. We can actually use some of these helper methods to draw a strong parallel between the structures.

#### Looping

We can use `for` with `in` to loop through any of the four data structures above:

```python
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
for country in class1:
    print(country)
```

#### Length

You can find the number of items in each data structure in the same way:

```python
# list
len(my_list)

# dict
len(gdp)

# tuple
len(dow)

# set
len(class1)
```

Notice that `len` of a dictionary only returns the number of keys, it doesn't say anything about the number of values in the dictionary. It is the same for all four data structures, actually. If you have a list of lists, using `len` will only tell you the number of outermost elements. Make some lists of lists, or lists of sets, and try this out.

#### in

You can also test to see if something is in each of these data structures using the keyword `in` (which is somewhat different outside a `for` loop:

```python
# list
>>> 22 in my_list
True

# dict
>>> 'Japan' in gdp
False

# tuple
>>> 'Monday' in dow
True

# set
>>> 'Columbia' in class1
True
```

#### For More Info

If you want to learn more about what kinds of functionality are built into Python for any of the structures above, simply type `help` in the interpreter:

```python
>>> help(my_list)
>>> help(gdp)
>>> help(dow)
>>> help(class1)
```

## Problem Sets

 * [Basic Data Structures](problem_set_1_data_structures.md)

## Further Reading

 * [Google Ed - lists and using them](https://developers.google.com/edu/python/lists)
 * [An Informal Introduction - Lists](https://docs.python.org/2/tutorial/introduction.html#lists)
 * [Python Tutorial: Sets](http://www.python-course.eu/sets_frozensets.php)
 * [Python Tutorial: Lists, Tuples, and Slicing](http://www.python-course.eu/sequential_data_types.php)
 * [i-Programmer: Dictionaries](http://www.i-programmer.info/programming/python/3990-the-python-dictionary.html)


[Back to Syllabus](../../README.md)
