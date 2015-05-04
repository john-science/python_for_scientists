# Python Functions - Solutions

## Simple Functions

    # 1. return the product of two numbers
    def product(num1, num2):
        '''return the product of two numbers'''
        return num1 * num2
        
    # 2. returns the absolute value of a number
    def absolute_value(num):
        '''returns the absolute value of a number'''
        if n < 0.0:
            return (-1.0 * num)
        else:
            return num
            
    # 2, cheating, using built-in functions
    def absolute_value(num):
        '''returns the absolute value of a number'''
        return abs(num)
        
    # 3. takes in a number and adds all of the positve number from zero to the input
    def sum_from_zero(number):
        '''adds all the positive number from zero to the input'''
        if number <= 0:
            # the input was wrong
            return 0
        
        # this will calculate the sum, even if the input number is a float
        sum = 0
        i = 1
        while i <= number:
            sum += 1
        
        return sum
    
    # 4. uses `from random import randint` to return the result of a random dice roll
    def fair_dice_roll():
        '''produces a number 1 through 6,
        just like a dice roll
        '''
        from random import randint
        return randint(1, 6)

XKCD is always relevant:

![XKCD is always relevant](http://imgs.xkcd.com/comics/random_number.png)
    
    # 5. takes an input list of numbers and returns the average
    def average(lst):
        '''averages a list of numbers'''
        sum = 0
        for val in lst:
            sum += val
        
        return sum / len(lst)
    
    # 5, cheating, using built-in functions
    def average(lst):
        '''averages a list of numbers'''
        return sum(lst) / len(avg)
        
    # 6. takes in a list of integers and returns a list containing only the odd numbers
    def odd_list_maker(lst):
        '''Input: a list of integers
        Output: a unique, minimal list of just the odd integers
        '''
        # I need to ensure uniqueness, so I use a set
        odds = set()
        for val in lst:
            if val % 2 == 1:
                odds.add(val)
        
        # need to return a list, so I type cast
        return list(odds)

## Keyword Arguments

    # 1. Print "Hello, X!", where the default value of X is "World".
    def greeting(X="World"):
        '''Print "Hello, X!" with a default X of "World"'''
        print("Hello, " + X + "!")
    
    # 2. Given a list of integers, return all that are evenly divided by X (default value 2).
    def modulo_filter(lst, X=2):
        '''return the subset of a list that shares a common denominator'''
        new_lst = []
        for val in lst:
            if val % X == 0:
                new_lst.append(val)
        
        return new_lst
    
    # 3. Extend a set of values (default empty set), by another set.
    def extend_set(new_set, old_set=set()):
        '''extend one set by another'''
        for s in new_set:
            old_set.add(s)
        
        return old_set
    
    
## Nested Functions
    
    def fibonacci(n):
        def recursion():
            return fibonacci(n-1) + fibonacci(n-2)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return recursion()
    
    >>> map(fibonacci, range(10))
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


[Back to Problem Set](problem_set_1_basic_functions.md)
