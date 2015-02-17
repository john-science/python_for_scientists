# Lists and Lambdas

## Lambdas

The `lambda` keywork just creates unnamed function:

    def check_is_even(n):
        return n % 2 == 0
    
    lambda n: n % 2 == 0

But these `anonymous functions` are often really handy. You can pass them around like variables (Python 2.2 and newer).

This piece of code shows the difference between a normal function definition (`f`) and a lambda function (`g`):

    >>> def f (x): return x**2
    ... 
    >>> print f(8)
    64
    >>> 
    >>> g = lambda x: x**2
    >>> 
    >>> print g(8)
    64

As you can see, `f()` and `g()` do exactly the same and can be used in the same ways. Note that the lambda definition does not include a `return` statement -- it always contains an expression which is returned. Also note that you can put a lambda definition anywhere a function is expected, and you don't have to assign it to a variable at all. 

Let us try to print the even numbers in the Fibonacci Sequence (the usual way):

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

Well, those approaches look pretty similar. But now let's say we want to print the odd numbers in the Fibonacci Sequence. We would have to write a whole new method `print_odd_numbers`. And if we wanted to print numbers divisible by 3, the same thing. But with the `print_some_numbers` method, all we have to do is define one new (short) lambda predicate function. This keeps us having to repeat ourselves. As you can imagine, if `print_some_numbers` was very long, you could save yourself a lot of typing and repitition.

This is a major principle in Python:

> DRY = Don't Repeat Yourself

## Map, Reduce, Filter

In theory, scientists and engineers might want to do almost anything with a long list of data. In practice, there are only a few general things we do with lists: apply a function to each member of a list, sum or reduce a whole list to one number, or select just some elements from a list. Python has some handy tools built right in to do each of these.

### Map

Let's say we want to take a list of numbers and create another list, by applying some function to each member of the list. That's a pretty general goal, and something you might want to do a lot:

    >>> map(lambda n: n * n, range(5))
    [0, 1, 4, 9, 16]

All we did there was apply a squaring function (a `lambda` function) to each element of a list from zero to four. Let's try a more realistic example. Let's say we want to do a unit conversion on a long list of values:

    >>> temps_fahrenheit = [0.0, 32.0, 72.0, 98.6, 212.0]
    >>> f2c = lambda t: (5.0 / 9.0 ) * (t - 32.0)
    >>> temps_celcius = map(f2c, temps_fahrenheit)
    >>> temps_celcius
    [-17.777777777777779, 0.0, 22.222222222222221, 37.0, 100.0]

One more example. Let's split a sentence into a list of words and create a final list with the length of each word:

    >>> sentence = 'It is raining cats and dogs'
    >>> words = sentence.split()
    >>> print words
    ['It', 'is', 'raining', 'cats', 'and', 'dogs']
    >>> 
    >>> lengths = map(lambda word: len(word), words)
    >>> print lengths
    [2, 2, 7, 4, 3, 4]

Of course, we could even do this on a single line:

    >>> print map(lambda w: len(w), 'It is raining cats and dogs'.split())
    [2, 2, 7, 4, 3, 4]

All of the above examples create `lambda` expresssions that only take one variable as input. But, `lambda` expressions can take multiple variables:

    >>> f = lambda a, b, c: (a + b) / c
    >>> f(4, 8, 2)
    6
    >>> f(1, 98, 3)
    33

### Filter

You will want to use a `filter` whenever you need to take a subset of a long list of data points. As a simple example, let's find all the even numbers under 5:

    >>> filter(lambda n: n % 2 == 0, range(5))
    [0, 2, 4]

Of course, we could re-write this defining the predicate separately:

    >>> is_even = lambda n: n % 2 == 0
    >>> filter(is_even, range(5))
    [0, 2, 4]

We could even make our own function, that filters the positive integers up to some value:

    >>> def filter_integers(predicate, max):
    ...     return filter(predicate, range(max))
    ... 
    >>> 
    >>> filter_integers(is_even, 5)
    [0, 2, 4]

This may seem like more work, but now we have a lot of flexibility to filter numbers:

    >>> is_odd = lambda i: i % 2 == 1
    >>> filter_integers(is_odd, 22)
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    >>> 
    >>> less_than_10 = lambda i: i < 10
    >>> filter_integers(less_than_10, 999999)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

These examples may seem overly simple, but the important idea is that code that is designed to smartly pass around lambda expressions can be shorter and more flexible.

### Reduce

Reduce is somewhat special, it takes a list and creates a single element. For instance, if we wanted to sum the integers below 5:

    >>> reduce(lambda a,d: a + d, range(5), 0)
    10

Remembering what the `range` function does, the line above could also be written:

    reduce(lambda a,d: a + d, [0, 1, 2, 3, 4], 0)

We know that the lambda expression above takes two variables and adds them.  But what two elements are being added? Reduce takes a list and a single value, in this case `range(5)` and `0`. Each element in `range(5)` is added to the running total that starts with a value of `0`. We could use a different starting value:

    >>> reduce(lambda a,d: a + d, range(5), 2)
    12

Of course, `map`, `reduce`, and `filter` work with more than just numbers:

    >>> words = ['Time', 'is', 'an', 'illusion.', 'Lunchtime', 'doubly', 'so.']
    >>> make_sentence = lambda a,b: a + ' ' + b
    >>> reduce(make_sentence, words, '')
    ' Time is an illusion. Lunchtime doubly so.'

## List Comprehensions

If want to create a list from another list, there is another option than using `map`. You can use a `list comprenhension`. In this example, we take a list of integers and create another list of their squares:

    >>> [i*i for i in range(5)]
    [0, 1, 4, 9, 16]

By adding an `if` into the `list comprenhension`, we can create a `filter` statement:

    >>> string = "The answer is... 42."
    >>> numbers = [x for x in string if x.isdigit()]
    >>> print numbers
    >>> ['4', '2']

We can even make the predicate (`if` statement) more complex. Here we fine all numbers: above 30, less than 100, and evenly divisible by 42:

    >>> [i for i in xrange(100) if i > 30 and i % 21 == 0]
    [42, 63, 84]

## Dictionary Comprehensions

Lastly, in Python 2.7 and newer there are even dictionary comprehensions:

    >>> word = 'droog'
    >>> dict((item, word.count(item)) for item in set(word))
    {'o': 2, 'r': 1, 'd': 1, 'g': 1}

This is a really easy tool to use:

    >>> sentence = ['The', 'spice', 'is', 'life.']
    >>> dict((word, len(word)) for word in sentence)
    {'life.': 5, 'The': 3, 'is': 2, 'spice': 5}

And can make creating a dictionary much easier:

    >>> days = [(0, 'Mon'), (1, 'Tue'), (2, 'Wed'), (3, 'Thu'), (4, 'Fri'), (5, 'Sat'), (6, 'Sun')]
    >>> dict(tup for tup in days)
    {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

Another handy tool, frequently used along side dictionary comprehension, is the `zip` function:

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
    >>> dict(tup for tup in days)
    {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}


[Problem Sets]

 * [Map, Reduce, Filter](problem_set_1_map_reduce_filter.md)


[Back to Syllabus](../../README.md)
