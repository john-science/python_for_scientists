# Functions and Modules

## Simple Functions

Write a function named:

1. `product` that takes in two numbers and returns their product.
2. `absolute` that takes in a number and returns its absolute value.
3. `sum_up_to` that takes in an integer and adds all of the positve integers from zero to the input.
4. `list_average` that takes an input `list` of numbers and uses a `for` loop to return the average.
5. `odd_filter` that takes a `list` of integers and returns a list containing only the odd numbers.
6. `make_square_dict` that takes in an integer `n` and returns a dictionary where the keys are the numbers `1` through `n` and the values are the square of the key.
7. `list_to_set` that takes in a `list` of values and returns a `set` of those values.
8. `not_in` that takes in a `list` and returns `True` if the value *isn't* in the list.
9. `triple_union` that takes in three sets and returns the union of all three.
10. `get_sorted_keys` that takes in a dictionary and returns a sorted list of its keys.
11. `hey_you` that prints "Hello, X!" (keywordd default value of X is "World").
12. `print_divisible` that takes aa `list` of integers and prints all that are evenly divided by X (default value 2).
13. `extend_set` that takes a set and extends it by another set (whose default value is the empty set).

## Modules

Create a Python module called:

1. `hey_jude.py` that includes the function `hey_you` from problem #11 above, and calls it from a `main` function with the `X` value of `'Jude'`.
2. `list_to_set.py` that includes the function `list_to_set` from problem #7. In the `main` function, convert this list into a set, and print the results before and after: `pi = [1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9]`.
3. `sixty_minutes.py` that includes the function `triple_union` from problem #9 above. Print these three sets and their union: `twos = set([2, 4, 6, 10, 12])`, `threes = set([3, 6, 12])`, and `fours = set([4, 12])`.
4. `coincidence.py` that includes the function `product` from problem #1 above. In the `main` function set `a` equal to `2` and `b` equal to `497`. Print the value of `product(a, b)`, and also print the value of the sum of `a` and `b`. Notice anything strange?
5. `sorted_squares.py` that includes the functions `make_square_dict` and `get_sorted_keys` from problems #6 and #10 above. In the `main` function, create a square dictionary from 1 to 20. Print the keys of that dictionary. Then use `get_sorted_keys` to print the keys in order.

## Importing

Create a Python module called:

1. `roll_the_dice.py` that uses `from random import randint` to print the result of a random dice roll (print 1 through 6 randomly from the `main` function).
2. `set_theory.py` that imports `triple_union` from `sixty_minutes.py` and `list_to_set` from `list_to_set.py`. In the `main` function, convert these threee lists into sets and print their union: `six = range(1, 7)`, `evens = range(2, 13, 2)`, and `thirds = range(3, 13, 3)`.

XKCD is always relevant:

![XKCD is always relevant](http://imgs.xkcd.com/comics/random_number.png)

## Solutions

* [Functions - Solutions](problem_set_1_solutions.md)


[Back to Lecture](lecture_03.md)
