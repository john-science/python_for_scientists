# Python Functions

Don't scroll down too far, or you'll see the solutions.

## Simple Functions

### Classwork

Write simple functions that does the following that:

1. return the product of two numbers
2. returns the absolute value of a number
3. takes in a number and adds all of the positve number from zero to the input
4. uses `from random import randint` to return the result of a random dice roll
5. takes an input list of numbers and returns the average
6. takes in a lits of integers and returns a list containing only the odd numbers

### Solutions

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
    
## Nested Functions

    > Homework not Complete Yet
