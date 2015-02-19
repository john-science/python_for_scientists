# Comprehensions

## List Comprehensions

### Problems

Use a single-line list comprehension to create the following list:

1. A list of all the odd numbers from 17 to 34.
2. A list of all the odd numbers in: `years = [1492, 1776, 1812, 1945, 1969, 1984, 1985, 2001, 2015]`
3. The square of all numbers from 4 to 14.
4. The number of times each digit occurs in the sequence: `pi = "141592653589793238462643383279502881"`. (Hint: str.count('0'). Hint: your answer should be a list 10 items long, one for each digit 0 through 9.)

### Solutions

    # 1. A list of all the odd numbers from 17 to 34.
    [i for i in xrange(17, 34, 2)]
    
    # 2. A list of all the odd numbers in: `years = [1492, 1776, 1812, 1945, 1969, 1984, 1985, 2001, 2015]`
    [y for y in years if y % 2 == 1]
    
    # 3. The square of all numbers from 4 to 14.
    [n**2 for n in xrange(4, 15)]
    
    # 4. The number of times each digit occurs in the sequence:
    # `pi = "141592653589793238462643383279502881"`.
    # (Hint: str.count('0').
    #  Hint: your answer should be a list 10 items long, one for each digit 0 through 9.)
    [pi.count(str(i)) for i in xrange(10)]

## Dictionary Comprehensions

### Problems

Use a single-line dictionary comprehension to create a dictionary of the following terms.

1. Using `zip`, where the keys are `keys = ["a", "b", "c"]` and the values are `values = [1, 2, 3]`.
2. A dictionary where the keys are 1 through 10 and the values are the cube of the keys.
3. A dictionary where the keys are 1 through 10 and the values are True if the key is odd and False if even.

### Solutions

    # 1. Using `zip`, where the keys are `keys = ["a", "b", "c"]`
    #    and the values are `values = [1, 2, 3]`.
    dict(zip(keys, values))
    
    # 2. A dictionary where the keys are 1 through 10
    #    and the values are the cube of the keys.
    {i: i**3 for i in xrange(1, 11)}
    
    # 3. A dictionary where the keys are 1 through 10
    #    and the values are True if the key is odd and False if even.
    {a: False if a % 2 == 0 else True for a in xrange(1, 11)}


[Back to Lecture](lecture_05.md)
