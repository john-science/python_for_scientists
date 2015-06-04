# Comprehensions

#### List Comprehensions

Use a single-line list comprehension to create the following list:

    # 1. A list of all the odd numbers from 17 to 34.
    >>> [i for i in range(17, 35) if i % 2 == 1]
    [17, 19, 21, 23, 25, 27, 29, 31, 33]

    # 2. A list of all the odd numbers in: `years = [1492, 1776, 1812, 1945, 1969, 1984, 1985, 2001, 2015]`
    >>> [yr for yr in years if yr % 2 == 1]
    [1945, 1969, 1985, 2001, 2015]
    
    # 3. The square of all numbers from 4 to 14.
    >>> [i * i for i in range(4, 15)]
    [16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
    
    # 4. The number of times each digit occurs in the sequence: `pi = "141592653589793238462643383279502881"`. (Hint: str.count('0'). Hint: your answer should be a list 10 items long, one for each digit 0 through 9.)
    >>> [pi.count(str(i)) for i in range(10)]
    [1, 3, 5, 6, 3, 4, 3, 2, 5, 4]
    

#### Dictionary Comprehensions

Use a single-line dictionary comprehension to create a dictionary of the following terms.

    # 1. Using `zip`, where the keys are `keys = ["a", "b", "c"]` and the values are `values = [1, 2, 3]`.
    >>> dict(zip(keys, values))
    {'a': 1, 'c': 3, 'b': 2}
    
    # 2. A dictionary where the keys are 1 through 10 and the values are the cube of the keys.
    >>> keys = range(1, 11)
    >>> values = [i * i * i for i in keys]
    >>> dict(zip(keys, values))
    {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}

    # 3. A dictionary where the keys are 1 through 10 and the values are True if the key is odd and False if even.
    >>> keys = range(1, 11)
    >>> values = [k % 2 == 1 for k in keys]
    >>> dict(zip(keys, values))
    {1: True, 2: False, 3: True, 4: False, 5: True, 6: False, 7: True, 8: False, 9: True, 10: False}


[Back to Problem Set](problem_set_2_comprehensions.md)
