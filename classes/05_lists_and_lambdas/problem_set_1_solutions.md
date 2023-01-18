# Map, Reduce, Filter - Solutions

#### Lambda - Solutions

    # 1. Find the square of a number.
    square = lambda n: n *n
    
    # 2. Find the cube of a number.
    cube = lambda m: m**3
    
    # 3. Convert a Fahrenheit temperature to Celsius. (Hint: (5/9)(F - 32))
    ftoc = lambda f: (float(5) / 9) * (f - 32)
    
    # 4. Add two numbers.
    add = lambda a, b: a + b
    
    # 5. Multiple two numbers.
    mult = lambda a, b: a * b
    
    # 6. Join two strings, by placing the space character between them.
    make_sentence = lambda r, s: r + ' ' + s

#### Map - Solutions

    # 1. The cubes of the numbers 1 through 33.
    map(lambda n: n**3, range(1, 34))
    
    # 2. All positive numbers less than 1000 that are evenly divisible by 3.
    map(lambda i: 3 * i, range(1, 334))
    
    # 3. Convert these temps from Fahrenheit to Celsuis:
    # `temps = [-42.0, -10.9, 0.0, 20.7, 32.0, 42.0, 101, 273, 320]`
    map(lambda f: (float(5) / 9) * (f - 32), temps)
    
    # 4. The square of all even, two-digit numbers.
    map(lambda e: e * e, range(10, 100, 2))

#### Filter - Solutions

    # 1. What positive, odd numbers less than 1000 are evenly divisible by 7 and 13?
    filter(lambda n: (n % 2 == 1) and (n % 7 == 0) and (n % 13 == 0), range(1000))
    
    # 2. What numbers less than 10,000 are both: the square of another integer and evenly divisible by 2?
    from math import sqrt
    filter(lambda n: (sqrt(n) % 1 == 0) and (n % 2 == 0), range(10000))
    
    # 3. How many positive numbers less than 1,000,000 are evenly divisible by 99?
    len(list(filter(lambda i: i % 99 == 0, range(1000000))))  # answer: 10102

#### Choose Your Own Adventure

    # 1. Find all the numbers evenly divisible by 3, below 100.
    filter(lambda n: n % 3 == 0, range(100))
    
    # 2. Calculate the sum of all the even numbers from 2 to 222.
    >>> sum(lambda a, b: a + b, range(2, 223, 2))
    12432
    
    # 3. Calculate the sum of the first five powers of seven.
    >>> powers = map(lambda i: 7 ** i, range(1, 6))
    >>> sum(lambda a, b: a + b, powers)
    19607


[Back to Problem Set](problem_set_1_map_reduce_filter.md)
