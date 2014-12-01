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

> DRY = Don't Repeat Yourself.

## Map, Reduce, Filter



### Map



### Reduce



### Filter



## List Comprehensions



[Back to Syllabus](../../README.md)
