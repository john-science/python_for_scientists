# Basic Python Syntax

You gotta start somewhere. Let's try some simple examples. To follow along, start the Python interpreter by typing `python` on the commandline:

    ~$ python

## Variable Definition

Let's try some basic variable definitions.

#### Numbers

    # integers
    x = 1
    three = 3
    fake_id = 18
    
    # floats
    pi = 3.1415926535
    hydrogens_atomic_weight = 1.00794

#### Text

    first_name = "Beth"
    last_name = 'Sanders'
    book_title = "Orion's Belt"
    sentence = 'Never say "I will be back." in a movie.'

#### Booleans

    skynet_rocks = False
    python_is_awesome = True

## Operations

#### Numbers

The Python interpreter can act like a calculator:

    >>> 2 + 2
    4
    >>> 50 - 5 * 6
    20
    >>> 3.0 + 3.0 + 3.0
    9.0
    >>> (50 - 5.0 * 6) / 4
    5.0
    >>> 8 / 5.0
    1.6
    >>> 9 / 7
    1

But you can also do algebra with stored variables:

    >>> x = 20
    >>> x += 1
    >>> x
    21
    >>> y = 7
    >>> x / y
    3
    >>> z = x / y
    >>> z
    3

After a mathematical operation is performed, a variable of a new type is returned:

    >>> 17 / 3     # int / int -> int
    5
    >>> 17 / 3.0   # int / float -> float
    5.666666666666667
    >>> 17 // 3.0  # explicit floor division discards the fractional part
    5.0
    >>> 17 % 3     # the % operator returns the remainder of the division
    2
    >>> 5 * 3 + 2  # result * divisor + remainder
    17

If a variable that has not been assigned is used, Python will throw an error:

    >>> numerator = 34.2
    >>> numerator / denominator
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'denominator' is not defined

#### Text

There are also several basic operations for strings:

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
    6

Above, the `[1]` notation returns element number `1` from the list (start counting with zero in Python). And `len` returns the length of, or number of elements in, the list.

#### Booleans

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

## Types

The above (integers, floats, booleans, and strings) are different `types` of variables. Ignoring strings for the moment, we can imagine one byte of memory. That byte is a series of zeros and ones. But that same byte could hold the data for an integer, a float, or a boolean. It's still just one byte either way.

There are a lot of implementation details here, but that is a solid picture to have in your mind: one byte of memory can be used for any of several different `types` of variables.

## Problem Sets

 * [Practice with Variables](problem_set_1_variables.md)

## Further Reading

 * [Google Ed - Python Strings](https://developers.google.com/edu/python/strings)
 * [Dive Into Python - Native Datatypes](http://www.diveintopython3.net/native-datatypes.html)
 * [An Informal Introduction - Numbers](https://docs.python.org/2/tutorial/introduction.html#numbers)
 * [An Informal Introduction - Strings](https://docs.python.org/2/tutorial/introduction.html#strings)
 * [String Processing](http://www.idiotinside.com/2014/09/04/string-processing-in-python/)


[Back to Syllabus](../../README.md)
