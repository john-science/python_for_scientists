# Map, Reduce, Filter

## Lambda

### Problems

In order to use `map`, `reduce`, and `filter` you're going to have to get used to `lambda` functions.  Create lambda functions to do the following things:

1. Find the square of a number.
2. Find the cube of a number.
3. Convert a Fahrenheit temperature to Celsius. (Hint: (5/9)(F - 32))
4. Add two numbers.
5. Multiple two numbers.
6. Join a list of strings, by placing the space character between them.

### Solutions

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

## Map

### Problems

Using only a single line `map` statement, create a list of the following items:

1. The cubes of the numbers 1 through 33.
2. All numbers less than 1000 that are evenly divisible by 3.
3. Convert these temps from Fahrenheit to Celsuis: `temps = [-42.0, -10.9, 0.0, 20.7, 32.0, 42.0, 101, 273, 320]`
4. The square of all even, two-digit numbers.

### Solutions

    # 1. The cubes of the numbers 1 through 33.
    map(lambda n: n**3, range(1, 34))
    
    # 2. All positive numbers less than 1000 that are evenly divisible by 3.
    map(lambda i: 3 * i, range(1, 334))
    
    # 3. Convert these temps from Fahrenheit to Celsuis: `temps = [-42.0, -10.9, 0.0, 20.7, 32.0, 42.0, 101, 273, 320]`
    map(lambda f: (float(5) / 9) * (f - 32), temps)
    
    # 4. The square of all even, two-digit numbers.
    map(lambda e: e * e, range(10, 100, 2))

## Reduce

### Problems

Use only a single `reduce` statement to perform the following calculations:

1. Find the product of all the odd, two-digit numbers.
2. Find the sum of all three-digit numbers that are divisible by three.
3. Turn the list `tst = ['This', 'is', 'a', 'test.']` into a single string.

### Solutions

    # 1. Find the product of all the odd, one-digit numbers.
    reduce(lambda a, b: a * b, range(11, 100, 2))
    
    # 2. Find the sum of all three-digit numbers that are divisible by three.
    reduce(lambda a, b: a + b, range(102, 1000, 3))
    
    # 3. Turn the list `tst = ['This', 'is', 'a', 'test.']` into a single string.
    reduce(lambda r, s: r + ' ' + s, tst)

## Filter

### Problems

Using only a single `filter` statement, solve the following puzzles:

1. What positive, odd numbers less than 1000 are evenly divisible by 7 and 13?
2. What integers less than 10,000 are both: the square of another integer and evenly divisible by 2?
3. How many positive, even numbers less than 1,000,000 are evenly divisible by 99?

### Solutions

    # 1. What positive, odd numbers less than 1000 are evenly divisible by 7 and 13?
    filter(lambda n: (n % 2 == 1) and (n % 7 == 0) and (n % 13 == 0), range(1000))
    
    # 2. What numbers less than 10,000 are both: the square of another integer and evenly divisible by 2?
    from math import sqrt
    filter(lambda n: (sqrt(n) % 1 == 0) and (n % 2 == 0), range(10000))
    
    # 3. What numbers less than 1,000 are evenly divisible by 2, 3, 4, and 5?
    filter(lambda n: (n % 2 == 0) and (n % 3 == 0) and (n % 4 == 0) and (n % 5 == 0), range(1000))
    # 3, or...
    filter(lambda n: (n % 3 == 0) and (n % 4 == 0) and (n % 5 == 0), range(1000))


[Back to Lecture](lecture_05.md)
