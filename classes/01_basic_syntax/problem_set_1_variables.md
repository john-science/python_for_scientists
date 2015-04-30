# Problem Set for Python Variable Definitions

## The Python Calculator

> Python has integers and floats, but not doubles.

    # What do you expect?
    print(6 - 2)

    # Now what do you expect?
    print(6 - 2.4)
    # Why did that happen?

Python stores floats as their byte representation so they are limited by the same 16-bit issues as most other languages.

    # What do you expect?
    4 / 2
    # Now what do you expect?
    5 / 2
    # Why did that happen?
    
    # What do you expect here?
    5.0 / 2

Because Python is a dynamic language, it has to determine the `type` of a variable on the fly. So in the case of `5 / 2`, the Python interpreter determines that both variables are integers, and therefore decides the operator is `integer division`. But in the case of `5.0 / 2`, one of the variables is a `float`, so Python is clever enough to give you a float as output, to preserve the greatest amount of information.

    # Have you seen the `modulo` operator before?
    3 % 2
    4 % 2
    5 % 2
    6 % 2

We can also assign these same mathematical values to variables:

    print(3.085e18 * 1e6)  # this is a Megaparsec in units of cm!
    
    t = 1.0                # declare a variable t (time)
    accel = 9.8            # acceleration in units of m/s^2
    
    # distance travelled in time t seconds is 1/2 a*t**2
    dist = 0.5 * accel * t * t
    # this is the distance in meters
    print(dist)

Python also has `long` and `complex` number types:

    2L
    2L + 2
    4L
    2L / 2
    2L / 2.0
    complex(1, 2)
    1 + 2j
    1 + 2j - 2j

## Boolean Relationships

There are several basic boolean operators to know:

    dist < 10
    dist <= 4.9
    dist < (10 + 2j)
    dist < -2.0
    dist != 3.1415

If you have ever worked in another programming language, it almost certainly had variations on all of these. However, in Python, we can natively compare almost any type of variable. And each variable type has a `False` equivalent:

    0 == False
    not False
    0.0 == False
    not (10.0 - 10.0)
    not -1
    not 3.1415
    x = None    # None is something special. Not true or false
    None == False
    None == True
    False or True

## Variable Types

Every variable in Python has a type. Try the following type tests:

    type(1)
    x = 2
    type(x)
    type(2) == type(1)
    type(True)
    type(type(1))
    type(pow)

We can also test whether something is a certain type with `isinstance()`:

    isinstance(1, int)
    isinstance("spam", str)
    isinstance(1.212, int)

## Python Strings

Strings are a sequence of characters

 * They can be indexed and sliced up as if they were an array.
 * You can glue strings together with `+` signs.

Strings are immutable (unlike in C), so you cannot change a string in place (this isn't so bad).

Strings can be formatted and compared.
    
    x = "spam"
    print(type(x))
    print("hello!\n...my sire.")
    "wah?!" == 'wah?!'
    print("'wah?!' said the student")
    print("\"wah?!\" said the student")

Backslashes `\` start special (escape) characters:

 * `\n` = newline (`\r` = return)
 * `\t` = tab
 * `\a` = bell

String literals are defined with double quotes or quotes. The outermost quote type cannot be used inside the string (unless it's escaped with a backslash).

Triple quotes are real useful for multiple line strings:

    y = '''Four score and seven minutes ago,
        you folks all learned some basic mathy stuff with Python
        and boy were you blown away!'''
    print(y)

Try out these basic string operations:

    s = "spam"
    e = "eggs"
    print(s + e)
    print(s + " and " + e)
    print("green " + e + " and\n " + s)
    print(s * 3 + e)
    print("*" * 50)
    "spam" < "zoo"
    "s" < "spam"

The above operations use overloaded operators (`<`, `*`, `+`, etc), that you are more used to seeing with numbers and booleans. Most of these you will find very handy and use often, once you know about them. (`batteries included`).

Of course, the fundamental way to do with a string in Python is as a list of characters, starting with an index of zero:

    s = "spam"
    len(s)
    len("eggs\n")
    len('')
    s[0]
    s[-1]

You can also use these indexes to grab sub-strings:

    s[0:1]    # get every character between 0 and 1
    s[1:4]    # get every character between 1 and 4 
    s[-2:-1]  # an index of `-1` is the last character in the string
    s[0:100]  # this does not throw an error
    s[1:]     # python runs the index to the end
    s[:2]     # python runs the index to the beginning
    s[::-1]   # print it out backwards

That last item, where we printed the string backwards is actually really powerful. Say, for instance, we only want to print every other character in a string:

    >>> alpha = 'abcdefghijklmnop'
    >>> alpha[::2]
    'acegikmo'

Or we could print every third character in the string, starting with the fourth character:

    >>> alpha[3::3]
    'dgjmp'

Slicing strings with one and two colons in Python gives the developer (you) a lot of flexibility. Try playing around with this, and get used to it.

Another really powerful string tool in Python is `find`. Try out these examples and see if you can determine how `find` works and what it does:

alpha = 'abcdefghijklmnop'
alpha.find('d')
alpha.find('jk')
alpha.find('x')
alpha[alpha.find('fg')::2]

[Back to Lecture 1](lecture_01.md)
