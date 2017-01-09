# Lambda and Looping Faster

The goal of this lecture is to show you `map`, `filter`, and `reduce`. But before you can use these great tools, you will have to understand a couple of things first: `lambda` and `yield`.

## Lambda

The `lambda` keyword creates a function, but doesn't give it a name. Here we create a simple function that tests if a number is even, and a lambda statement that does the same thing:

    def check_is_even(n):
        return n % 2 == 0
    
    lambda n: n % 2 == 0

These [anonymous functions](https://en.wikipedia.org/wiki/Anonymous_function) can be really handy. You can pass them around like variables (Python 2.2 and newer).

Here is another compare-and-contrast example between a regular function (`f`) and a lambda function (`g`):

    >>> def f (x):
    ...     return x**2
    ... 
    >>> print(f(8))
    64
    >>> g = lambda x: x**2
    >>> 
    >>> print(g(8))
    64

As you can see, `f()` and `g()` do the same thing and can be used in similar ways.

 * **Note**: The lambda definition does not include a `return` statement -- it always contains a single expression which is then returned.

Let's print the even numbers in the Fibonacci Sequence (the usual way):

    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    
    def print_even_numbers(lst)
        for element in lst:
            if element % 2 == 0:
                print(element)
    
    print_even_numbers(fibonacci)

Now let's do the same thing, using a lambda funciton:

    is_even = lambda n: n % 2 == 0
    
    def print_some_numbers(lst, predicate):
        for element in lst:
            if predicate(element):
                print(element)
    
    print_some_numbers(fibonacci, is_even)

Well, those approaches look pretty similar. But what if we want to print the odd numbers in the Fibonacci Sequence? We would have to write a whole new method `print_odd_numbers`. And if we wanted to print numbers divisible by 3, again we'd need to write a whole new function. But with the `print_some_numbers` method, all we have to do is define one new (short) lambda predicate function. This keeps us having to repeat ourselves. If `print_some_numbers` was very long, you could save a lot of repitition.

    is_odd = lambda n: n % 2 == 1
    divisible_by_three = lambda n: n % 3 == 0
    
    print_some_numbers(fibonacci, is_odd)
    print_some_numbers(fibonacci, divisible_by_three)

This is a major principle in Python:

> DRY = Don't Repeat Yourself

## Yield

#### What is an Iterator?

The [yield](http://pythontips.com/2013/09/29/the-python-yield-keyword-explained/) keyword in Python is used to create [iterators](https://en.wikipedia.org/wiki/Iterator) for looping. Before jumping into using these tools, let's take a look at a stupid example of why we want them. In Python v2.x we will define a function:

    def sum_odd_even(N):
        total = 0
        for i in range(N):
            if i % 2 == 0:
                total += i
            else:
                total -= i
        return total

    >>> sum_odd_even(1000)  # took way less than a second
    -500
    >>> sum_odd_even(10000)  # took way less than a second
    -5000
    >>> sum_odd_even(1000000)  # took way ~1 second
    -500000
    >>> sum_odd_even(10000000)  # took so long I gave up and quit

We could write the above function much smarter, but let's ignore that for now. The important thing is that when I did the final `sum_odd_even(10000000)` it took over 10 seconds and I got bored and gave up. Now, that is partly because we are adding 10 million numbers, but part of the problem is that when I saw `range(10000000)` I am creating a 10-million item list. This takes ~10MB of memory. Imagine if the list was 10 billion. You'd (probably) run out of memory.

Wouldn't it be nice if we could save all that memory and make this (stupid) loop faster? Well, it turns out you can, by using `xrange` instead of `range` (Python 2.x):

    def sum_odd_even(N):
        total = 0
        for i in xrange(N):
            if i % 2 == 0:
                total += i
            else:
                total -= i
        return total

    >>> sum_odd_even(1000)  # took less than a second
    -500
    >>> sum_odd_even(10000)  # took less than a second
    -5000
    >>> sum_odd_even(1000000)  # took less than 1 second
    -500000
    >>> sum_odd_even(10000000)  # took less than 1 second
    -5000000

That little `x` sure seems to be pretty magical. What's the difference? Well, hopefully by now you've gotten used to looking for help with the interpretter:

    >>> type(range(10))
    <type 'list'>
    >>> type(xrange(10))
    <type 'xrange'>
    >>> help(xrange)

    class xrange(object)
     |  xrange([start,] stop[, step]) -> xrange object
     |  
     |  Like range(), but instead of returning a list, returns an object that
     |  generates the numbers in the range on demand.  For looping, this is 
     |  slightly faster than range() and more memory efficient.

What `xrange()` does is produce only one number at a time. So, instead of having to keep the entire list `range(1000000000)` in memory, we just get the first item of the list returned to us, then the second, then the third, and so on. A function that returns a sequence that you only get one item of at a time is called an [iterator](https://en.wikipedia.org/wiki/Iterator#Python).

**Python 2 vs 3:** This is a major difference between Python v2.x and Python v3.x. In Python v2, `range()` returns a list, but there is no `xrange` in Python v3 because in Python v3 `range` returns an iterator instead of a list.

#### Using Yield

That `xrange` in Python v2 sure is great, but what if we want to create our own iterators? That's where `yield` comes in. You use `yield` inside of a loop to return a sequence of values from a function (or method). This is something like `return` in normal functions, but `return` only provides a value once. Let's try to replace our stupid function above with one that uses an iterator:

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

#### Python v3 Concerns

But wait, you say, all of that is great but sometimes you use `range` because you want an actual list. Not to worry, you can always convert an iterator to a list:

    >>> range(5)        # Python v3.x
    range(5)
    >>> list(range(5))  # Python v3.x
    [0, 1, 2, 3, 4]
    
    >>> sum_odd_even_iterator(10)
    <generator object sum_odd_even_iterator at 0x7f5680143410>
    >>> list(sum_odd_even_iterator(10))
    [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]

## Map, Reduce, Filter

In theory we could do anything with our data. But in practice, what we do with a `list` of data frequently falls into a few basic categories: apply a function to each member of a list, sum or reduce a whole list to one number, or select some elements from a list. Python has three handy tools built in to speed those processes up: `map`, `reduce`, and `filter`.

### Map

Let's say we want to take a `list` of numbers and create another list, by applying some function to each member of the original list. That's a pretty generic goal, and can be accomplished using `map` along with a `lambda` function:

    >>> map(lambda n: n * n, range(5))
    [0, 1, 4, 9, 16]

All we did there was apply a squaring function (a `lambda` function) to each element of a list from zero to four. Let's try a more realistic example. Let's say we want to do a unit conversion on a long list of values:

    >>> temps_fahrenheit = [0.0, 32.0, 72.0, 98.6, 212.0]  # pretend this is much longer
    >>> f2c = lambda t: (5.0 / 9.0 ) * (t - 32.0)          # Fahrenheit to Celcius
    >>> temps_celcius = map(f2c, temps_fahrenheit)
    >>> temps_celcius
    [-17.777777777777779, 0.0, 22.222222222222221, 37.0, 100.0]

One more example. Let's split a sentence into a list of words and create a final list with the length of each word:

    >>> sentence = 'It is raining cats and dogs'
    >>> words = sentence.split()
    >>> words
    ['It', 'is', 'raining', 'cats', 'and', 'dogs']
    >>> 
    >>> lengths = map(lambda word: len(word), words)
    >>> lengths
    [2, 2, 7, 4, 3, 4]

Of course, we could even do this on a single line:

    >>> map(lambda w: len(w), 'It is raining cats and dogs'.split())
    [2, 2, 7, 4, 3, 4]

All of the above examples create `lambda` expresssions only take one variable as input. But `lambda` expressions can take multiple variables:

    >>> f = lambda a, b, c: (a + b) / c
    >>> f(4, 8, 2)
    6
    >>> f(1, 98, 3)
    33

#### Python v3

This is one place where Python v2 and v3 differ. In Python v2, `map` returns a list:

    >>> map(lambda a: a, [1, 2, 3])
    [1, 2, 3]

But in Python v3.x, `map` returns an iterator:

    >>> map(lambda a: a, [1, 2, 3])
    <generator object map at 0x7f5680143410>

### Filter

You will want to use a `filter` whenever you need to take a subset of a long list of data points. As a simple example, let's find all the even numbers under 21:

    >>> filter(lambda n: n % 2 == 0, range(21))
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

Of course, we could re-write this defining the predicate separately:

    >>> is_even = lambda n: n % 2 == 0
    >>> filter(is_even, range(21))
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

We could even make our own function, that filters the positive integers up to some value:

    >>> def filter_integers(predicate, max):
    ...     return filter(predicate, range(max))
    ... 
    >>> 
    >>> filter_integers(is_even, 21)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

This may seem like more work, but now we have a lot of flexibility to filter numbers:

    >>> is_odd = lambda i: i % 2 == 1
    >>> filter_integers(is_odd, 22)
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    >>> 
    >>> less_than_10 = lambda i: i < 10
    >>> filter_integers(less_than_10, 999999)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#### Python v3

This is another place where Python v2 and v3 differ. In Python v2, `filter` returns a list:

    >>> filter(lambda a: a > 3, range(5))
    [4]

But in Python v3.x, `filter` returns an iterator:

    >>> filter(lambda a: a > 3, range(5))
    <generator object map at 0x7f5680143410>

### Reduce

Reduce is special, in that it takes a list and creates a single element. For instance, if we wanted to sum the integers below 1337:

    >>> reduce(lambda a,b: a + b, range(1337), 0)
    893116

We know that the lambda expression above takes two variables and adds them.  But what two elements are being added? Reduce takes a list and a single value, in this case `range(1337)` and `0`. Each element in `range(1337)` is added to the running total that starts with a value of `0`. We could use a different starting value:

    >>> reduce(lambda a,d: a + d, range(1337), 2)
    893118

Of course, `map`, `filter`, and `reduce` work with more than just numbers:

    >>> words = ['Time', 'is', 'an', 'illusion.', 'Lunchtime', 'doubly', 'so.']
    >>> make_sentence = lambda a,b: a + ' ' + b
    >>> reduce(make_sentence, words, '')
    ' Time is an illusion. Lunchtime doubly so.'

#### Python v3

Note that the `reduce` function doesn't exist in Python v3. [Guido](https://en.wikipedia.org/wiki/Guido_van_Rossum) suggests you just [use a normal loop](http://www.artima.com/weblogs/viewpost.jsp?thread=98196) instead.

## List Comprehensions

If want to create a list from another list, `map` isn't the only option. You can use a [list comprenhension](https://en.wikipedia.org/wiki/List_comprehension).

Here we take a list of integers and create a list of their squares using the list comprehension `[EXPRESSION for X in LIST]` syntax:

    >>> [i*i for i in range(5)]
    [0, 1, 4, 9, 16]

By adding an `if` into the `list comprenhension`, we can create a `filter` statement:

    >>> string = "The answer is... 42."
    >>> numbers = [x for x in string if x.isdigit()]
    >>> print(numbers)
    >>> ['4', '2']

We can even make the predicate (`if` statement) more complex. Here we find all numbers: above 30, less than 100, and evenly divisible by 21:

    >>> [i for i in xrange(100) if i > 30 and i % 21 == 0]
    [42, 63, 84]

#### Python v3

Please note, that in Python v2.x list comprehensions return lists, but in Python v3.x they return iterators.

## Dictionary Comprehensions

Lastly, in Python 2.6 and newer, we can use dictionary comprehensions. Dictionary comprehensions look like list comprensions, but we use `dict()` instead of `[]`. In this example we create a dictionary where the key is a letter and the value is the number of times that letter appears in the given string:

    >>> word = 'droog'
    >>> dict((item, word.count(item)) for item in set(word))
    {'o': 2, 'r': 1, 'd': 1, 'g': 1}

Well, that string was pretty short, let's try a longer one:

    >>> sentence = 'The quick brown fox jumps over the lazy dog'
    >>> dict((item, sentence.count(item)) for item in set(sentence))
    {' ': 8, 'T': 1, 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 3, 'f': 1,
     'g': 1, 'h': 2, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1,
     'o': 4, 'p': 1, 'q': 1, 'r': 2, 's': 1, 't': 1, 'u': 2, 'v': 1,
     'w': 1, x': 1, 'y': 1, ''z': 1}

This is a really easy tool to use. Let's create a dictionary where the keys are words in a list and the values are the length of those words:

    >>> sentence = ['The', 'spice', 'is', 'life.']
    >>> dict((word, len(word)) for word in sentence)
    {'life.': 5, 'The': 3, 'is': 2, 'spice': 5}

And dictionary comprehensions can make creating a dictionary much easier, using a list of tuples:

    >>> days = [(0, 'Mon'), (1, 'Tue'), (2, 'Wed'), (3, 'Thu'), (4, 'Fri'), (5, 'Sat'), (6, 'Sun')]
    >>> dict(tup for tup in days)
    {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

Another handy tool, frequently used along side dictionary comprehension, is the `zip` function. It takes two or more lists and creates lists of tuples:

    >>> zip(['a', 'b', 'c'], range(3))
    [('a', 0), ('b', 1), ('c', 2)]
    >>> 
    >>> zip(range(4), range(4, 8), range(8, 12))
    [(0, 4, 8), (1, 5, 9), (2, 6, 10), (3, 7, 11)]

Rewriting the day-of-week example using the `zip` function:

    >>> dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    >>> days = zip(range(7), dow)
    >>> days
    [(0, 'Mon'), (1, 'Tue'), (2, 'Wed'), (3, 'Thu'), (4, 'Fri'), (5, 'Sat'), (6, 'Sun')]
    >>> dict(days)
    {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

Which we would usually just write in two lines:

    >>> dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    >>> dict(zip(range(7), dow))
    {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

#### Python v3

Again, in Python v2.x dictionary comprehensions return lists, but in Python v3.x they return iterators.

## Problem Sets

 * [Map, Reduce, Filter](problem_set_1_map_reduce_filter.md)
 * [Comprehensions](problem_set_2_comprehensions.md)

## Further Reading

 * [Origins of Python's Functional Features](http://python-history.blogspot.com/2009/04/origins-of-pythons-functional-features.html) - Post by Guido van Rossum
 * [Dictionary Comprehensions and Zip](http://www.bogotobogo.com/python/python_dictionary_comprehension_with_zip_from_list.php)
 * [Python Tutorial: Map, Reduce, Filter](http://www.python-course.eu/lambda.php)
 * [Python Tutorial: List Comprehension](http://www.python-course.eu/list_comprehension.php)


[Back to Syllabus](../../README.md)
