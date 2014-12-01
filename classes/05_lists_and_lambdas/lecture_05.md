# Lists and Lambdas

## Lambdas

A `lambda` is just an unnamed function:

    def check_is_even(n):
        return n % 2 == 0
    
    lambda n: n % 2 == 0

But these `anonymous functions` are often really handy. You can pass around like variables (Python 2.2 and newer).

Let us try to print the even numbers in the Fibonacci Sequence the usual way:

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

Well, these look pretty similar. But now let's say we want to print the odd numbers in the Fibonacci Sequence. We would have to write a whole new method `print_odd_numbers`. And if we wanted to print numbers divisible by 3, the same thing. But with the `print_some_numbers` method, all we have to do is define one new (short) lambda predicate function. This keeps us having to repeat ourselves. As you can imagine, if `print_some_numbers` was very long, you could save yourself a lot of typing and repitition.

This is a major principle in Python:

> DRY = Don't Repeat Yourself

## Map, Reduce, Filter

In theory, scientists and engineers might want to do almost anything with a long list of data. In practice, there are only a few general things we do with lists: apply a function to each member of a list, sum or reduce a whole list to one number, or select just some elements from a list. There are some real fast, easy-to-use tools built right into Python to do just these things.

### Map

Let's say we want to take a list of numbers and create another list, by applying some function to each member of the list. That's a pretty general goal, and something you might want to do a lot:

    >>> map(lambda n: n * n, range(5))
    [0, 1, 4, 9, 16]

All we did there was apply a squaring function (`lambda` function) to each element of a list from zero to four. Let's try a more realistic example. Let's say we want to do a unit conversion on a long list of values:

    >>> temps_fahrenheit = [0.0, 32.0, 72.0, 98.6, 212.0]
    >>> f2c = lambda t: (5.0 / 9.0 ) * (t - 32.0)
    >>> temps_celcius = map(f2c, temps_fahrenheit)
    >>> temps_celcius
    [-17.777777777777779, 0.0, 22.222222222222221, 37.0, 100.0]

### Reduce

    >>> reduce(lambda a,d: a + d, range(5), 0)
    10

### Filter

    >>> filter(lambda n: n % 2 == 0, range(5))
    [0, 2, 4]

## List Comprehensions

    >>> [i*i for i in range(5)]
    [0, 1, 4, 9, 16]

[Back to Syllabus](../../README.md)
