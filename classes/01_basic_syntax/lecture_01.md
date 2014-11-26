# Basic Python Syntax

You gotta start somewhere. Let's try some simple commands. Start the interpreter and follow along.

## Variable Definition

Let's try some basic variable definitions.

### Numbers

    # integers
    x = 1
    three = 3
    fake_id = 18
    
    # floats
    pi = 3.1415926535
    hydrogens_atomic_weight = 1.00794

### Text

    first_name = "Beth"
    last_name = 'Sanders'
    book_title = "Orion's Belt"
    sentence = 'Never say "I will be back." in a movie.'

### Booleans

    its_friday = False
    python_is_awesome = True

## Operations

### Numbers

The Python interpreter can act just like a calculator:

    >>> 2 + 2
    4
    >>> 50 - 5 * 6
    20
    >>> (50 - 5.0 * 6) / 4
    5.0
    >>> 8 / 5.0
    1.6

Or you can do math with stored variables:

    >>> x = 20
    >>> x += 1
    >>> x
    21
    >>> y = 7
    >>> y / x
    3
    >>> z = y / x

After a mathematical operation is performed, a variable of a new type is returned:

    >>> 17 / 3  # int / int -> int
    5
    >>> 17 / 3.0  # int / float -> float
    5.666666666666667
    >>> 17 // 3.0  # explicit floor division discards the fractional part
    5.0
    >>> 17 % 3  # the % operator returns the remainder of the division
    2
    >>> 5 * 3 + 2  # result * divisor + remainder
    17

If a variable that has not been assigned is used, Python will throw an error:

    >>> numerator = 34.2
    >>> numerator / denominator
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'denominator' is not defined

### Text

There are also basic operations for strings:

    >>> s1 = "Hello "
    >>> s2 = "World"
    >>> s1 + s2
    "Hello World"
    >>> s1[0]
    'H'
    >>> s1[1]
    'e'
    >>> s2[-1]
    'd'
    >>> s2[-2]
    'l'
    >>> 3 * 'un' + 'ium'
    'unununium'
    >>> s2[1:3]
    'or'
    >>> len(s1)
    5

### Booleans

Finally, the basic operations for boolean logic are similar to those in other langauges:

    >>> a = True
    >>> b = False
    >>> a and b
    False
    >>> a or b
    True
    >>> not a
    False
    >>> a and not b
    True
    >>> 1 and True
    True
    >>> 0 and False
    0

(**NOTE**: In a pinch, you can replace `True` and `False` with the numbers `1` and `0`.)

There are some basic comparison operators that act on numbers and return boolean values, these are called `predicates`:

    >>> 1 < 2
    True
    >>> 7 > 99
    False
    >>> 314 <= 9
    False
    >>> 7 >= 7
    True
    >>> 3 == 3.0
    True
    >>> 8 != 9.1234
    True
    
    

## Data Structures

When designing a huge program or a short script, it is important to choose your data structure appropriately. Following the "batteries included" philosophy, Python has several handy data structures built right in.

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

## Control Statements

#### for loops

Basically, a `for` loop just does something for every value in a list. For instance:

    new_list = [1950, 'There Will Come Soft Rains', 'Ray Bradbury', 2026]
    
    for element in new_list:
        print(element)

Try that out yourself and see, when the loop executes, it runs through all of the values in the list mentioned after `in`. It then puts them into `element`, and executes through the loop, each time with `element` being worth something different. Let's write another example, printing the square of the odd numbers from `1` to `10`:

    for number in range(1, 11, 2):
        print(number * number)

We also just learned about the `range` function. The `range` function produces a list, given: `start`, `end`, and `step` value2, though the `step` value is optional. For instance:

    >>> range(1, 5, 2)
    [1, 3]
    >>> range(1, 5)
    [1, 2, 3, 4]
    >>> range(1, 30, 7)
    [1, 8, 15, 22, 29]

(**NOTE**: As you can see above, the `start` value is *inclusive* and the `end` value is *exclusive*.)

#### while loops

A `while` loop does something until its main condition is no longer met:

    a = 0
    while a < 10:
        a = a + 1
        print(a)

The above loop will print the numbers `0` through `10` and then comparison between `a` and `10` will be no longer true, and the loop will terminate. You can also create more complicated predicates for the while loop:

    n = 15
    while n > 0 and n < 30:
        n -= 3  # this is the same as `n = n - 3`
        print(n)

The above loop will print the numbers 15, 12, 9, 6, 3 and then the complicated predicate will no longer be true, and the loop will terminate.

Unlike your typical `for` loop, `while` loops leave open an interesting possibility. What if the predicate is *never* true?

    >>> n = 7.0
    >>> while n > 0:
    ...     n += 0.5
    ... 

This is called an `infinte loop`, because it would never terminate on its own. This is, obviously, not a good thing.

#### if statements

In order to write useful programs, we almost always need the ability to check conditions and change the behavior of the program accordingly. Conditional statements give us this ability. The simplest form is the if statement, which has the genaral form:

    if PREDICATE:
        BODY STATEMENTS

In this case, only if the predicate is true is the body of the statement executed. For example:

    food = 'spam'
    
    if food == 'spam':
        print('Ummmm, my favorite!')
        print('I feel like saying it 100 times...')
        print(100 * (food + '! '))

Above is the basic `if` statement. You will use these to control the flow of the program. But what if you want to execute a different block of code if the predicate isn't satisfied? Well, you could do this:

    food = 'spam'
    
    if food == 'spam':
        print('Joy!')
    
    if food != 'spam':
        print('Sadness...')

But the above logic is *so* common, and needed so often, that Python provides a shortcut:

    if food == 'spam':
        print('Ummmm, my favorite!')
    else:
        print("No, I won't have it. I want spam!")

There is another option, what if you want to have several different conditionals chained together, to execute one of many different blocks of code, based on various predicates? That is the purpose of the `elif` symbol:

    if food == 'spam':
        print('Ummmm, my favorite!')
    elif food == 'spam and eggs':
        print('Acceptable. I can pick out the eggs.')
    elif food == 'spam and bacon':
        print('Acceptable. I can pick out the bacon.')
    else:
        print("No, I won't have it. I want spam!")

Lastly, the `else` symbol is always optional:

    if food == 'spam':
        print('Ummmm, my favorite!')
    elif food == 'spam and eggs':
        print('Acceptable. I can pick out the eggs.')

## Indentation

Did you notice in the `for` and `while` loops above how the content *inside* the loop was indented? That indentation is how Python decides what logic is contained within a loop, function, or class (more on those later). Unlike in other languages you might have seen, the indentation *really* matters in Python.

`White Space` is very important in Python.

![white space](http://imgs.xkcd.com/comics/python.png)

Here is an example of a correctly (though confusingly) indented piece of Python code:

    if n == 0:
     return 0
    elif n == 1:
          return 1
    else:
      return (n - 1) + (n - 2)

The following example shows various indentation errors:

        if n == 0:               # error: first line indented
    return 0                     # error: not indented
    elif n == 1:
          return 1
     else:                       # error: inconsistent dedent
       return (n - 1) + (n - 2)

In the end, the only way to make your code correct *and* readable is to be consistent with your indents. Do the same thing every time. The standard is four space per indent:

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (n - 1) + (n - 2)

## Comments!

> You are what you comment.

If you write code and there are no comments and no documentation, the code doesn't exist. No one will want to touch it, and they won't be able to understand it if they do.

    # this is the first comment
    spam = 1  # and this is the second comment
              # ... and now a third!
    text = "# This is not a comment because it's inside quotes."
    
    """This is an especially long comment,
    that takes up two lines."""
    '''This is another especially long comment,
    that takes up multiple
    lines.
    '''

[Back to Syllabus](../../README.md)
