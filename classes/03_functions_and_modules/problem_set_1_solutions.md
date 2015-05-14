# Python Functions - Solutions

## Simple Functions

Write a simple function that:

#### 1. takes in two numbers and returns their product.

    def product(num1, num2):
        '''return the product of two numbers'''
        return num1 * num2
        
#### 2. takes in a numbers and returns its absolute value.

    def absolute_value(num):
        '''returns the absolute value of a number'''
        if n < 0.0:
            return (-1.0 * num)
        else:
            return num
            
#### 2. cheating, using built-in functions
    def absolute_value(num):
        '''returns the absolute value of a number'''
        return abs(num)
        
#### 3. takes in a postive integer and adds all of the positve integers from zero to the input.

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
    
#### 4. takes no input, but uses `from random import randint` to return the result of a random dice roll.

    def fair_dice_roll():
        '''produces a number 1 through 6,
        just like a dice roll
        '''
        from random import randint
        return randint(1, 6)

XKCD is always relevant:

![XKCD is always relevant](http://imgs.xkcd.com/comics/random_number.png)
    
#### 5. takes an input `list` of numbers and returns the average.

    def average(lst):
        '''averages a list of numbers'''
        sum = 0
        for val in lst:
            sum += val
        
        return sum / len(lst)
    
#### 5. cheating, using built-in functions

    def average(lst):
        '''averages a list of numbers'''
        return sum(lst) / len(avg)
        
#### 6. takes a `list` of integers and returns a list containing only the odd numbers.

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

#### 7. takes in an integer `n` and returns a dictionary where the keys are the numbers `1` through `n` and the values are the square of the key.

    def square_dict(n):
        '''Input: a positive integer n
        Output: a dictionary where keys are 1 through n
                and values are the square of the keys
        '''
        d = {}
        
        for i in range(1, n + 1):
            d[i] = i * i
        
        return d

#### 8. takes in a `list` of values and returns a `set` of those values.

    def list_to_set(lst):
        '''Input: a list
        Output: a set version of that list
        '''
        return set(lst)

#### 8. If you want to do this the hard way, this is how sets are made.

    def list_to_set(lst):
        '''Input: a list
        Output: a set version of that list
        '''
        s = set()
        
        for item in lst:
            if item not in s:  # notice the use of "not in"
                s.add(item)
        
        return s

#### 9. takes in a `list` and a value and returns `True` if the value *isn't* in the list, and `False` otherwise (call your function `not_in`).

    def not_in(lst, value):
        '''Input: a list and any value
        Output: returns True if value ISN'T in the list,
                and False otherwise.
        '''
        if value in lst:
            return False
        else:
            return True

#### 10. takes in three sets and returns the union of all three.

    def triple_union(set1, set2, set3):
        '''Input: three sets
        Output: the union of all three sets
        '''
        return set1.union(set2).union(set3)

#### 11. takes in a dictionary and returns a sorted list of its keys.

    def sorted_keys(d):
        '''Input: any dictionary
        Output: a sorted list of the input dicts keys
        '''
        return sorted(d.keys())

## Keyword Arguments

#### 1. Print "Hello, X!", where the default value of X is "World".

    def greeting(X="World"):
        '''Print "Hello, X!" with a default X of "World"'''
        print("Hello, " + X + "!")
    
#### 2. Given a list of integers, return all that are evenly divided by X (default value 2).

    def modulo_filter(lst, X=2):
        '''return the subset of a list that shares a common denominator'''
        new_lst = []
        for val in lst:
            if val % X == 0:
                new_lst.append(val)
        
        return new_lst
    
#### 3. Extend a set of values (default empty set), by another set.

    def extend_set(new_set, old_set=set()):
        '''extend one set by another'''
        for s in new_set:
            old_set.add(s)
        
        return old_set



[Back to Problem Set](problem_set_1_basic_functions.md)
