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

## Operations

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

## Control Statements

#### for
####  while
####  if

## Indentation

## Data Structures

####  lists
####  tuples
####  sets
####  dictionaries

## Comments!

