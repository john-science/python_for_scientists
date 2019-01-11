# Basic Python Syntax

You gotta start somewhere. Let's try some simple examples. To follow along, start the Python interpreter by typing `python` on the commandline:

    ~$ python

## Variable Definition

Let's try some basic variable definitions.

#### Numbers

```python
# integers
x = 1
three = 3
fake_id = 18

# decimals (floats)
pi = 3.1415926535
hydrogens_atomic_weight = 1.00794
```

#### Text (Strings)

```python
first_name = "Beth"
last_name = 'Sanders'
book_title = "Orion's Belt"
sentence = 'Never say "I will be back." in a movie.'
```

Notice here that you can use `'` or `"` to enclose a character string. And this has the added bonus of including either `'` or `"` in the `string` easier. But what if you have to include both in the `string`? Use the escape character:

```python
book_title = 'Orion\'s Belt'
```

#### Booleans

```python
skynet_rocks = False
python_is_awesome = True
```

## Operations

#### Numbers

The Python interpreter can act like a calculator:

```python
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
1.2857142857142858
```

NOTE: If you are running Python 3.x you will see the above behavior for division. But if you are running Python 2.x you will see that division of integers always returns an integer:

```python
>>> # In Python 2.x
>>> 9 / 7
1
```

But you can also do algebra (math with variables):

```python
>>> x = 20
>>> x += 1
>>> x
21
>>> y = 7
>>> x / y
3
>>> z = x / y
>>> z
3.0
```

After a mathematical operation is performed, a variable of a new type is returned:

```python
>>> 17.0 / 3.0  # float / float -> float
5.666666666666667
>>> 15 / 3      # int / int -> float
5.0
>>> 15 / 3.0    # int / float -> float
5.0
>>> 15.0 / 3    # float / int -> float
5.0
>>> 17 / 3.0    # int / float -> float
5.666666666666667
>>> 17 / 3      # int / int -> float
5.666666666666667
```

But if you try to use a variable that has not been assigned a value, Python will throw an error:

```python
>>> numerator = 34.2
>>> numerator / denominator
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'denominator' is not defined
```

#### Text

There are also several basic operations for strings. For instance, you can add two strings:

```python
>>> s1 = "Hello "
>>> s2 = "World"
>>>
>>> s1 + s2
"Hello World"
```

You can also retrive a single letter from a string. Notice, in Python we always start counting from zero, not one:

```python
>>> s1[0]
'H'
>>> s1[1]
'e'
```

You can also get the last character in a string, if that's easier:

```python
>>> s2[-1]
'd'
>>> s2[-2]
'l'
```

Less common, but you can even multiply a string:

```python
>>> 3 * 'un' + 'ium'
'unununium'
```

A really, really useful tool is the ability to be able to take a `slice` of a string. Notice, the first number is inclusive, but the last number isn't:

```python
>>> s2[1:3]
'or'
>>> s1[0:4]
'Hell'
>>> s1[:4]
'Hell'
>>> s2[1:5]
'orld'
>>> s2[1:999]  # error automatically surpressed!
'orld'
>>> s2[1:]
'orld'
```

Another really useful tool is `len`, which calculates the number of characters in a string:

```python
>>> len(s1)
6
>>> len(s2)
5
```

#### Booleans

Finally, the basic operations for boolean logic are similar to those in other langauges:

```python
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
```

(**NOTE**: In a pinch, you can replace `True` and `False` with the numbers `1` and `0`.)

There are some basic comparison operators that act on numbers and return boolean values, these are called `predicates`:

```python
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
```

## Types

The above (integers, floats, booleans, and strings) are different `types` of variables. Ignoring strings for the moment, we can imagine one byte of memory. That byte is a series of zeros and ones. But that same byte could hold the data for an integer, a float, or a boolean. It's still just one byte either way.

There are a lot of implementation details here, but that is a useful picture to have in your mind: one byte of memory can be used to hold any of several different `types` of variables.

As you are learning and exploring the Python language, you might find it interesting to use the `type` command to learn about a variable:

```python
>>> i = 42
>>> type(i)
<type 'int'>
>>>
>>> pi = 3.14159265358979
>>> type(pi)
<type 'float'>
>>>
>>> s = 'Hello, World!'
>>> type(s)
<type 'str'>
>>>
>>> type(True)
<type 'bool'>
```

## Help

You can do a `type` on basically everything in Python. For instance, if you do a `type(s)` as above you get `str`. You can then do a `help(str)` and you will get the whole string help menu (which is extensive):

Help on class str in module builtins:

```python
class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
...
```

If you are new to Python, the `help()` function is a great place to start when you have questions.  Of course, Google also works, but this is faster and you don't have to wade through a bunch of unhelpful links.


## Problem Sets

 * [Practice with Variables](problem_set_1_variables.md)

## Further Reading

 * [Google Ed - Python Strings](https://developers.google.com/edu/python/strings)
 * [Dive Into Python - Native Datatypes](http://www.diveintopython3.net/native-datatypes.html)
 * [An Informal Introduction - Numbers](https://docs.python.org/2/tutorial/introduction.html#numbers)
 * [An Informal Introduction - Strings](https://docs.python.org/2/tutorial/introduction.html#strings)
 * [String Processing](http://www.idiotinside.com/2014/09/04/string-processing-in-python/)


[Back to Syllabus](../../README.md)
