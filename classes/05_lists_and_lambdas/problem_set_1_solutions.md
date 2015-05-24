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
    
    # 6. Join a list of strings, by placing the space character between them.
    make_sentence = lambda r, s: r + ' ' + s

#### Map - Solutions

    # 1. The cubes of the numbers 1 through 33.
    map(lambda n: n**3, range(1, 34))
    
    # 2. All positive numbers less than 1000 that are evenly divisible by 3.
    map(lambda i: 3 * i, range(1, 334))
    
    # 3. Convert these temps from Fahrenheit to Celsuis: `temps = [-42.0, -10.9, 0.0, 20.7, 32.0, 42.0, 101, 273, 320]`
    map(lambda f: (float(5) / 9) * (f - 32), temps)
    
    # 4. The square of all even, two-digit numbers.
    map(lambda e: e * e, range(10, 100, 2))

#### Reduce - Solutions

    # 1. Find the product of all the odd, one-digit numbers.
    reduce(lambda a, b: a * b, range(11, 100, 2))
    
    # 2. Find the sum of all three-digit numbers that are divisible by three.
    reduce(lambda a, b: a + b, range(102, 1000, 3))
    
    # 3. Turn the list `tst = ['This', 'is', 'a', 'test.']` into a single string.
    reduce(lambda r, s: r + ' ' + s, tst)

#### Filter - Solutions

    # 1. What positive, odd numbers less than 1000 are evenly divisible by 7 and 13?
    filter(lambda n: (n % 2 == 1) and (n % 7 == 0) and (n % 13 == 0), range(1000))
    
    # 2. What numbers less than 10,000 are both: the square of another integer and evenly divisible by 2?
    from math import sqrt
    filter(lambda n: (sqrt(n) % 1 == 0) and (n % 2 == 0), range(10000))
    
    # 3. What numbers less than 1,000 are evenly divisible by 2, 3, 4, and 5?
    filter(lambda n: (n % 2 == 0) and (n % 3 == 0) and (n % 4 == 0) and (n % 5 == 0), range(1000))
    # 3, or...
    filter(lambda n: (n % 3 == 0) and (n % 4 == 0) and (n % 5 == 0), range(1000))


[Back to Problem Set](problem_set_1_map_reduce_filter.md)
