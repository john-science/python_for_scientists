# Lambda and Looping

The real goal of this lecture is introduce `map`, `filter`, and `reduce`. But before you can use these great tools, you will have to understand two things: `lambda` and `yield`.

## Lambda

The `lambda` keyword creates a function, but doesn't give it a name. Here we create a simple function that tests if a number is even, and a lambda statement that does the same thing:

```python
def check_is_even(n):
    return n % 2 == 0

lambda n: n % 2 == 0
```

These [anonymous functions](https://en.wikipedia.org/wiki/Anonymous_function) can be really handy. You can pass them around like variables (Python 2.2 and newer).

Here is another compare-and-contrast example between a regular function (`f`) and a lambda function (`g`):

```python
>>> def f (x):
...     return x**2
... 
>>> print(f(8))
64
>>> g = lambda x: x**2
>>> 
>>> print(g(8))
64
```

As you can see, `f()` and `g()` do the same thing and can be used in similar ways.

 * **Note**: The lambda definition does not include a `return` statement -- it always contains a single expression which is then returned.

Let's print the even numbers in the Fibonacci Sequence (the usual way):

```python
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

def print_even_numbers(lst):
    for element in lst:
        if element % 2 == 0:
            print(element)

print_even_numbers(fibonacci)
```

Now let's do the same thing, using a lambda funciton:

```python
is_even = lambda n: n % 2 == 0

def print_some_numbers(lst, predicate):
    for element in lst:
        if predicate(element):
            print(element)

print_some_numbers(fibonacci, is_even)
```

Well, those approaches look pretty similar. But what if we want to print the odd numbers in the Fibonacci Sequence? We would have to write a whole new method `print_odd_numbers`. And if we wanted to print numbers divisible by 3, again we'd need to write a whole new function. But with the `print_some_numbers` method, all we have to do is define one new (short) lambda predicate function. (A predicate function returns `True` or `False`.) This keeps us having to repeat ourselves. If `print_some_numbers` was very long, you could save a lot of repitition.

```python
is_odd = lambda n: n % 2 == 1
divisible_by_three = lambda n: n % 3 == 0

print_some_numbers(fibonacci, is_odd)
print_some_numbers(fibonacci, divisible_by_three)
```

This is a major principle in Python:

> DRY = Don't Repeat Yourself


## Yield

#### What is an Iterator?

Let us take a look at a wonderful built-in Python function, `range`:

```python
>>> range(5)
range(0, 5)
>>> type(range(5))
<class 'range'>
```

In the older version of Python, `range(5)` simply created a list of integers from zero to four. But in Python 3, `range` creates an [iterator](https://en.wikipedia.org/wiki/Iterator) from zero to four.  What's an iterator? Think of it as a function that will create all the values you need, but not until you ask for them.

For instance, imagine you tried to make a list from zero to `1000000000000000000000`. Well, that list would take up more memory than you (probably) have on your computer, right? But if you ask me for the 14th element in that list I immediately know it is `13`, so why bother keeping the whole thing in memory, when you can just get the one element you want WHEN you want it? Iterators let you do this. They are built into Python 3 everywhere, and they are a great performance-enhancing tool.

But if you *really* want a list, you can just change your iterator to a list by using the built-in `list` function:

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
```

#### Creating your own Iterators

The [yield](http://pythontips.com/2013/09/29/the-python-yield-keyword-explained/) keyword in Python is used to create [iterators](https://en.wikipedia.org/wiki/Iterator). Before jumping into using these tools, let's take a look at a stupid example of why we want them. Suppose we define a stupid function:

```python
def sum_odd_even(N):
    total = 0
    for i in list(range(N)):
        if i % 2 == 0:
            total += i
        else:
            total -= i
    return total

>>> sum_odd_even(1000)  # took way less than a second
-500
>>> sum_odd_even(10000)  # took way less than a second
-5000
>>> sum_odd_even(10000000)  # took way ~1 second
-500000
>>> sum_odd_even(1000000000)  # took so long I gave up and quit
```

#### Using Yield

That `range` in Python v3 is great, but what if we want to create our own iterators? That's where `yield` comes in. You use `yield` inside of a loop to return a sequence of values from a function (or method). This is something like `return` in normal functions, but `return` only provides a value once. Let's try to replace our stupid function above with one that uses an iterator:

```python
def sum_odd_even_iterator(N):
    i = 0
    while i < N:
        if i % 2 == 0:
            yield i
        else:
            yield -i
        i += 1

def sum_odd_even(N):
    total = 0
    for i in sum_odd_even_iterator(N):
        total += i
    return total
```


## Map and Filter

In theory we could do anything with our data. But in practice, what we do with a `list` of data frequently falls into a few basic categories: apply a function to each member of a list, sum or reduce a whole list to one number, or select some elements from a list. Python has three handy tools built in to speed those processes up: `map`, `reduce`, and `filter`.

### Map

Let's say we want to take a `list` of numbers and create another list, by applying some function to each member of the original list. That's a pretty generic goal, and can be accomplished using `map` along with a `lambda` function:

```python
>>> map(lambda n: n * n, range(5))
<map object at 0x7fed22b304e0>
```

Notice here that `map` returns an iterator, just like `range`. Of course, we can still use `list` to convert that to a list if we want to take a look at it:

```python
>>> list(map(lambda n: n * n, range(5)))
[0, 1, 4, 9, 16]
```

All we did there was apply a squaring function (a `lambda` function) to each element of a list from zero to four. Let's try a more realistic example. Let's say we want to do a unit conversion on a long list of values:

```python
>>> temps_fahrenheit = [0.0, 32.0, 72.0, 98.6, 212.0]  # pretend this is much longer
>>> f2c = lambda t: (5.0 / 9.0 ) * (t - 32.0)          # Fahrenheit to Celcius
>>> temps_celcius = map(f2c, temps_fahrenheit)
>>> list(temps_celcius)
[-17.777777777777779, 0.0, 22.222222222222221, 37.0, 100.0]
```

One more example. Let's split a sentence into a list of words and create a final list with the length of each word:

```python
>>> sentence = 'It is raining cats and dogs'
>>> words = sentence.split()
>>> words
['It', 'is', 'raining', 'cats', 'and', 'dogs']
>>> 
>>> lengths = map(lambda word: len(word), words)
>>> list(lengths)
[2, 2, 7, 4, 3, 4]
```

Of course, we could even do this on a single line:

```python
>>> list(map(lambda w: len(w), 'It is raining cats and dogs'.split()))
[2, 2, 7, 4, 3, 4]
```

All of the above examples create `lambda` expresssions only take one variable as input. But `lambda` expressions can take multiple variables:

```python
>>> f = lambda a, b, c: (a + b) / c
>>> f(4, 8, 2)
6.0
>>> f(1, 98, 3)
33.0
```


### Filter

You will want to use a `filter` whenever you need to take a subset of a long list of data points. As a simple example, let's find all the even numbers under 21:

```python
>>> filter(lambda n: n % 2 == 0, range(21))
<filter object at 0x7fed22b304e0>
>>> list(filter(lambda n: n % 2 == 0, range(21)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

Of course, we could re-write this defining the predicate separately:

```python
>>> is_even = lambda n: n % 2 == 0
>>> list(filter(is_even, range(21)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

We could even make our own function, that filters the positive integers up to some value, and returns a list:

```python
>>> def filter_integers(predicate, max):
...     return list(filter(predicate, range(max)))
... 
>>> 
>>> filter_integers(is_even, 21)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

This may seem like more work, but now we have a lot of flexibility to filter numbers:

```python
>>> is_odd = lambda i: i % 2 == 1
>>> filter_integers(is_odd, 22)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
>>> 
>>> less_than_10 = lambda i: i < 10
>>> filter_integers(less_than_10, 999999)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```


## List Comprehensions

As a secondary goal for todays grab-bag of a lecture, let's talk about some other ways we can loop over lists/data: [list comprenhension](https://en.wikipedia.org/wiki/List_comprehension).

Here we take a list of integers and create a list of their squares using the list comprehension `[EXPRESSION for X in LIST]` syntax:

```python
>>> [i*i for i in range(5)]
[0, 1, 4, 9, 16]
```

By adding an `if` into the `list comprenhension`, we can create a `filter` statement:

```python
>>> string = "The answer is... 42."
>>> numbers = [x for x in string if x.isdigit()]
>>> print(numbers)
>>> ['4', '2']
```

We can even make the predicate (`if` statement) more complex. Here we find all numbers: above 30, less than 100, and evenly divisible by 21:

```python
>>> [i for i in range(100) if i > 30 and i % 21 == 0]
[42, 63, 84]
```


## Dictionary Comprehensions

Lastly, in Python 2.6 and newer, we can use dictionary comprehensions. Dictionary comprehensions look like list comprensions, but we use `dict()` instead of `[]`. In this example we create a dictionary where the key is a letter and the value is the number of times that letter appears in the given string:

```python
>>> word = 'droog'
>>> dict((item, word.count(item)) for item in set(word))
{'o': 2, 'r': 1, 'd': 1, 'g': 1}
```

Well, that string was pretty short, let's try a longer one:

```python
>>> sentence = 'The quick brown fox jumps over the lazy dog'
>>> dict((item, sentence.count(item)) for item in set(sentence))
{' ': 8, 'T': 1, 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 3, 'f': 1,
 'g': 1, 'h': 2, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1,
 'o': 4, 'p': 1, 'q': 1, 'r': 2, 's': 1, 't': 1, 'u': 2, 'v': 1,
 'w': 1, x': 1, 'y': 1, ''z': 1}
```

This is a really easy tool to use. Let's create a dictionary where the keys are words in a list and the values are the length of those words:

```python
>>> sentence = ['The', 'spice', 'is', 'life.']
>>> dict((word, len(word)) for word in sentence)
{'life.': 5, 'The': 3, 'is': 2, 'spice': 5}
```

And dictionary comprehensions can make creating a dictionary much easier, using a list of tuples:

```python
>>> days = [(0, 'Mon'), (1, 'Tue'), (2, 'Wed'), (3, 'Thu'), (4, 'Fri'), (5, 'Sat'), (6, 'Sun')]
>>> dict(tup for tup in days)
{0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
```

Another handy tool, frequently used along side dictionary comprehension, is the `zip` function. It takes two or more lists and creates lists of tuples:

```python
>>> zip(['a', 'b', 'c'], range(3))
[('a', 0), ('b', 1), ('c', 2)]
>>> 
>>> zip(range(4), range(4, 8), range(8, 12))
[(0, 4, 8), (1, 5, 9), (2, 6, 10), (3, 7, 11)]
```

Rewriting the day-of-week example using the `zip` function:

```python
>>> dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
>>> days = zip(range(7), dow)
>>> days
[(0, 'Mon'), (1, 'Tue'), (2, 'Wed'), (3, 'Thu'), (4, 'Fri'), (5, 'Sat'), (6, 'Sun')]
>>> dict(days)
{0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
```

Which we would usually just write in two lines:

```python
>>> dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
>>> dict(zip(range(7), dow))
{0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
```

## What did all of this have in common?

What *was* this lecture? What did all of these disparate topics have in common? Looping. You really only *need* for-loops and while-loops. But you will write them so often it's good to have optiions. This lecture gives you loads of new options for your work-hourse control flows.


## Problem Sets

 * [Map and Filter](problem_set_1_map_reduce_filter.md)
 * [Comprehensions](problem_set_2_comprehensions.md)

## Further Reading

 * [Origins of Python's Functional Features](http://python-history.blogspot.com/2009/04/origins-of-pythons-functional-features.html) - Post by Guido van Rossum
 * [Dictionary Comprehensions and Zip](http://www.bogotobogo.com/python/python_dictionary_comprehension_with_zip_from_list.php)
 * [Python Tutorial: Map and Filter](http://www.python-course.eu/lambda.php)
 * [Python Tutorial: List Comprehension](http://www.python-course.eu/list_comprehension.php)


[Back to Syllabus](../../README.md)
