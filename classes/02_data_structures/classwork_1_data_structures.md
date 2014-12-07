# Python Data Structures

#### Lists

There are several ways to initalize a list:

    lst = []
    odds = [1, 3, 5, 7]
    evens = ['two', 'four', 'six', 'eight']
    wibbly_wobbly = [0.0, 1, 'two', 3L]

And several ways to access elements in a list:

    evens[2]
    odds[-1]
    evens[:2]
    odds[1:33]

But we also have several ways to loop over the elements of a list:

    for element in odds:
        print(element)
    
    for index,value in enumerate(evens):
        print(index, value)
    
    # This is very common, but not very Pythonic:
    for i in range(len(evens)):
        print(evens[i])

There are also several major ways to modify a list:

    evens.append('ten')
    print(evens)
    
    evens.extend(['12', '14', '16'])
    print(evens)
    
    evens.insert(18, -1)
    print(evens)
    
    del evens[4:]
    print(evens)
    
    item = evens.pop()
    print(evens)
    
    evens.reverse()
    print(evens)

There are also several ways to search for items in a list:

    evens.index('two')
    evens.count('two')

In general, sorting a list of items can be a complex task. Because if the list is very long, it could take a *very* long time. But for the case of short lists, or list of things that are easy to sort, like numbers, Python has some sorting functionality included:

    lst = [7, 4, 3, 1, 8, 4, 333, -1234]
    lst.sort()
    print(lst)
    
    lst = [7, 4, 3, 1, 8, 4, 333, -1234]
    sorted(lst)

So, what is the difference between `sort` and `sorted` above?

#### Tuples

Because Tuples are immutable, you need to give ALL the elements when you initially define it:

    tup = ('Rock', "Lobster", 1, '!')

Once you have defined a tuple, you can't alter the elements. Try it:

    tup[0] = 'Red'

But you can append multiple tuples together to create new tuples:

    new_tup = tup + ('big', 'as', 'a', whale)

Because creating a new tuple does not alter an old one.

You can also find the length of a tuple:

    >>>> len(new_tup)
    8

We tend to use tuples for things that won't need to change, like the names of things: days of the week, months of the year, counties, vehicle types, etc.

#### Sets

You can declare a new set in one of three ways:

    >>> primes = {2,3,5,7,11,13,17}
    >>> primes = set([2,3,5,7,11,13,17])
    >>> primes = set()
    >>> primes.add(2)
    >>> primes.add(3)
    >>> primes.add(5)

Let's say you have information about the location of wildfires in California. And, among other things, you want a complete list of all the counties that had fires. You could loop through each fire and add that fire's county to a set:

    >>> counties = set()
    >>> counties.add('Yolo')
    >>> counties.add('Napa')
    >>> counties.add('Napa')
    >>> counties.add('Yolo')
    >>> counties.add('Mendicino')
    >>> counties.add('Humboldt')

Because sets only include unique values, you won't have two copies of 'Yolo' and 'Napa' in you final set. You will only have the unique values you want:

    >>> counties
    set(['Humboldt', 'Mendicino', 'Napa', 'Yolo'])

And, if what you really wanted was a list, you could just convert the set to a list:

    >>> cnty_list = list(counties)
    ['Humboldt', 'Mendicino', 'Napa', 'Yolo']

To remove an item from a set:

    counties.remove('Yolo')

#### Dictionaries

There are four ways to create a list:

Number 1, the standard way:

    d = {"favorite cat": None, "favorite spam": "all"}

Number 2, method declaration:

    d = dict(one=1, two=2, cat='dog')

Number 3, filling in items as you go:

    d = {}  # empty dictionary
    d['cat'] = 'dog'
    d['one'] = 1
    d['two'] = 2

Number 4, start with a list of tuples:

    mylist = [("cat", "dog"), ("one", 1), ("two", 2)]

You can also use dictionaries to format print statements. The `%` operator works conveniently to substitute values from a dict into a string by name:

    >>> hash = {}
    >>> hash['word'] = 'garfield'
    >>> hash['count'] = 42
    >>> s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
    'I want 42 copies of garfield'

The `del` operator does deletions. In the simplest case, it can remove the definition of a variable, as if that variable had not been defined. `del` can also be used on list elements or slices to delete that part of the list and to delete entries from a dictionary.

    var = 6
    del var  # var no more!
    
    list = ['a', 'b', 'c', 'd']
    del list[0]     ## Delete first element
    del list[-2:]   ## Delete last two elements
    print list      ## result is ['b']
    
    dict = {'a':1, 'b':2, 'c':3}
    del dict['b']   ## Delete 'b' entry
    print dict      ## result is {'a':1, 'c':3}

Of course, you can also make dictionaries where the values are themselves dictionaries. This for a nearly arbitarily complex collection of data:

    >>> books = {}
    >>> dune = {'title': 'Dune', 'author': 'Herbert', 'genre': 'sci-fi'}
    >>> enders = {'title': 'Ender\'s Game', 'author': 'Card', 'genre': 'sci-fi'}
    >>> hobbit = {'title': 'The Hobbit', 'author': 'Tolkein', 'genre': 'fantasy'}
    >>> books['Dune'] = dune
    >>> books['Enders'] = enders
    >>> books['Hobbit'] = hobbit
    >>> books['Guide'] = {'title': "Hitchhiker's Guide to the Galaxy", 'author': 'Adams', 'genre': 'sci-fi'}
    >>> books
    {'Enders': {'genre': 'sci-fi', 'author': 'Card', 'title': "Ender's Game"}, 'Hobbit': {'genre': 'fantasy', 'author': 'Tolkein', 'title': 'The Hobbit'}, 'Dune': {'genre': 'sci-fi', 'author': 'Herbert', 'title': 'Dune'}, 'Guide': {'genre': 'sci-fi', 'author': 'Adams', 'title': "Hitchhiker's Guide to the Galaxy"}}

Notice that in the `books` dictionary above, we can catalog a great amount of information about our books: the title, author, genre, ISBN, copies sold, pages, language, you name it. But if we forgot to list the `title` for one book, no error would be thrown. It is up to us to validate our data entry or write code to look through the dictionary and make sure all the correct fields exist. `With great flexibility comes great error checking.`
