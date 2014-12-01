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



#### Sets



#### Dictionaries

