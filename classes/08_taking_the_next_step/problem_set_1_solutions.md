# PEP8 & Style

## Reformat the Code

### One Statement Per Line - Solution (Reformatted Code)

    print('one')
    print('two')
    
    if x == 1:
        print('one')
    
    x_is_big = x >= 200
    slope_is_negative = derivative(f(x)) < 0;
    
    if x_is_big and slope_is_negative:
        print('something')

### Crazy Conditionals -  Solution (Reformatted Code)

What if the value of `thing` is `False`? And while we're at it, why would you ever write `if thing == True`? Isn't that just the same as `if thing`? And let's connect all of these `if` statements in the standard way:

    if thing:
        print('thing is truthy!')
    elif not thing:
        print('thing is falsey!')
    elif thing is None:
        print('thing is None!')

### Searching in a Dictionary - Solution (Reformatted Code)

The major problem with the above example code is that the `has_key` function has been deprecated. It is now preferable to use `in` for Python 2.x and 3.x.

Also, that `dict()` there is technically find. But don't be fancy.

    tardis = {}
    tardis['doctor'] = 'who'

    if 'master' in tardis:
        print('Run!')

### Finding Elements in a Dictionary - Solution (Reformatted Code)

Again, we see the old `has_key` function used. Ick. But also this is a prime example of using the dictionary method `get`. This will allow you to return a default value if the key you are looking for in the dictionary does not exist.

    d = {'XKCD': 'stick'}
    
    # These are examples of how to safely retrieve values from dictionaries
    print(d.get('XKCD', 'default_value'))       # prints 'stick'
    print(d.get('Garfield', 'default_value')')  # prints 'default_value'

    # Or you can do an explicit test first
    if 'Garfield' in d:
        print('fat_cat')
    else:
        print('default_value')


### Importing - Solution (Reformatted Code)

Keep each `import` on a separate line. And most people keep them in alphabetical order, because things easier to find when you start to get a lot of imports.

    import os
    import sys

### Naming Things - Solution (Reformatted Code)

Class names should be `CamelCase`.
Function and Method names should be `snake_case`.
Variable and Attribute names should be `snake_case`.

    class ParallelUniverse:
    
        def __init__(self):
            self.evil_spock = True
        
        def mirror_mirror(self):
            # do something
        
    universe_one = ParallelUniverse()

### Save Your Indents - Solution (Reformatted Code)

First off, fix those variable names. But the big problem with the code above is that `if littleList[0]:` causes everything below it to be indented one more time. This is fine once, but with all the loops and `if`s below it, suddenly the code can become so indented it's hard to read. The solution is to use a `continue`:

    for little_list in some_big_list:
        if not little_list[0]:
            continue  # notice how using a 'continue' improves the indents below?
        if little_list[1] == 'Spock':
            if little_list[2] == 'fire':
                print('Spock! Fire the torpedos!')
            else:
                print('Runaway!')
        else:
            if little_list[2] == 'fire':
                print('Sulu! Fire the torpedos!')
            else:
                print('Runaway!')

But, you know what, the rest of those `if` statements could be combined to be shorter too:

    for little_list in some_big_list:
        if not little_list[0]:
            continue
        
        if little_list[2] != 'fire':
            print('Runaway!')
        else:
            if little_list[1] == 'Spock':
                crew_member = 'Spock'
            else:
                crew_member = 'Sulu'
            
            print(crew_member + ' Fire the torpedos!')

Lastly, we *could* make that whole `crew_member` definition shorter. This one is a lot more optional, but a good use of Python's [ternary operator](http://www.blog.pythonlibrary.org/2012/08/29/python-101-the-ternary-operator/):

    for little_list in some_big_list:
        if not little_list[0]:
            continue
        
        if little_list[2] != 'fire':
            print('Runaway!')
        else:
            crew_member = 'Spock' if little_list[1] == 'Spock' else 'Sulu'
            print(f"{crew_member} Fire the torpedos!")

### Mystery Example 1 - Solution (Reformatted Code)

    def fibonacci_list(n):
        """Returns all of the Fibonacci Numbers below n"""
        result_list = []
        a = 0
        b = 1
        while b < n:
            result_list.append(b)
            temp = a
            a = b
            b += temp
        return result_list
    
    first_100 = fibonacci_list(100)
    print(first_100)

### Mystery Example 2 - Solution (Reformatted Code)

In this case, for both the list `a` and the dictionary `d`, we want to iterate over the indexes and values at the same time. This is where `enumerate` comes in handy. Not only will it be faster than the two procedures in the code above, but it makes for much cleaner, easier to read code.

    # d is some big dictionary of craziness
    # a is some big list of string
    
    for i, value in enumerate(d):
        some_function(i, value)
    
    for j, value in enumerate(a):
        print(f"Value number {j} is: {value}")

### Mystery Example 3 - Solution (Reformatted Code)

There are a few things that could be improved about that messy plotting loop:

    import matplotlib
    import numpy
    
    file_path = "/path/to/some_file.txt"
    
    try:
        f = open(file_path, 'r')
    except IOError:
        print(f"Failed to open file: {file_path}")
        exit()
    
    for line in f.readlines():
        plot_things_using_matplotlib(line)
    
    f.close()

### Mystery Example 4 - Solution (Reformatted Code)

Don't fight Python on this whitespace thing. You won't come out looking good.

    squares = {}
    cubes = {}
    
    for i in range(1e7):
        if i %% 3 == 0:
            squares[i] = i * i
        if i %% 7 == 0:
            cubes[i] = i * i * i

[Back to Problem Set](problem_set_1_pep8.md)
