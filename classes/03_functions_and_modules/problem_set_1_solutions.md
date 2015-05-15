# Python Functions - Solutions

## Simple Functions

Write a function named:

#### 1. `product` that takes in two numbers and returns their product.

    def product(num1, num2):
        '''return the product of two numbers'''
        return num1 * num2
        
#### 2. `absolute` that takes in a number and returns its absolute value.

    def absolute(num):
        '''returns the absolute value of a number'''
        if n < 0.0:
            return (-1.0 * num)
        else:
            return num
            
#### 2. cheating, using built-in functions
    def absolute(num):
        '''returns the absolute value of a number'''
        return abs(num)
        
#### 3. `sum_up_to` that takes in an integer and adds all of the positve integers from zero to the input.

    def sum_up_to(number):
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
    
#### 4. `list_average` that takes an input `list` of numbers and uses a `for` loop to return the average.

    def list_average(lst):
        '''averages a list of numbers'''
        sum = 0
        for val in lst:
            sum += val
        
        return sum / len(lst)
    
#### 4. cheating, using built-in functions

    def list_average(lst):
        '''averages a list of numbers'''
        return sum(lst) / len(avg)
        
#### 5. `odd_filter` that takes a `list` of integers and returns a list containing only the odd numbers.

    def odd_filter(lst):
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

#### 6. `make_square_dict` that takes in an integer `n` and returns a dictionary where the keys are the numbers `1` through `n` and the values are the square of the key.

    def make_square_dict(n):
        '''Input: a positive integer n
        Output: a dictionary where keys are 1 through n
                and values are the square of the keys
        '''
        d = {}
        
        for i in range(1, n + 1):
            d[i] = i * i
        
        return d

#### 7. `list_to_set` that takes in a `list` of values and returns a `set` of those values.

    def list_to_set(lst):
        '''Input: a list
        Output: a set version of that list
        '''
        return set(lst)

#### 7. The hard way. Python is doing something like this behind the scenes.

    def list_to_set(lst):
        '''Input: a list
        Output: a set version of that list
        '''
        s = set()
        
        for item in lst:
            if item not in s:  # notice the use of "not in"
                s.add(item)
        
        return s

#### 8. `not_in` that takes in a `list` and returns `True` if the value *isn't* in the list.

    def not_in(lst, value):
        '''Input: a list and any value
        Output: returns True if value ISN'T in the list,
                and False otherwise.
        '''
        if value in lst:
            return False
        else:
            return True

#### 9. `triple_union` that takes in three sets and returns the union of all three.

    def triple_union(set1, set2, set3):
        '''Input: three sets
        Output: the union of all three sets
        '''
        return set1.union(set2).union(set3)

#### 10. `get_sorted_keys` that takes in a dictionary and returns a sorted list of its keys.

    def get_sorted_keys(d):
        '''Input: any dictionary
        Output: a sorted list of the input dicts keys
        '''
        return sorted(d.keys())

#### 11. `hey_you` that prints "Hello, X!" (keywordd default value of X is "World").

    def hey_you(X="World"):
        '''Print "Hello, X!" with a default X of "World"'''
        print("Hello, " + X + "!")
    
#### 12. `print_divisible` that takes aa `list` of integers and prints all that are evenly divided by X (default value 2).

    def print_divisible(lst, X=2):
        '''return the subset of a list that shares a common denominator'''
        new_lst = []
        for val in lst:
            if val % X == 0:
                new_lst.append(val)
        
        return new_lst
    
#### 13. `extend_set` that takes a set and extends it by another set (whose default value is the empty set).

    def extend_set(new_set, old_set=set()):
        '''extend one set by another'''
        for s in new_set:
            old_set.add(s)
        
        return old_set

## Modules

Create a Python module called:

#### 1. `hey_jude.py` that includes the function `hey_you` from problem #11 above, and calls it from a `main` function with the `X` value of `'Jude'`.

This is the entire module:

    def main():
        hey_you("Jude")
    
    
    def hey_you(X="World"):
        '''Print "Hello, X!" with a default X of "World"'''
        print("Hello, " + X + "!")
    
    
    if __name__ == '__main__':
        main()

#### 2. `list_to_set.py` that includes the function `list_to_set` from problem #7. In the `main` function, convert this list into a set, and print the results before and after: `pi = [1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9]`.

    def main():
        pi = [1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9]
        
        print("Before:")
        print(pi)
        
        pi_set = list_to_set(pi)
        print("After:")
        print(pi_set)
    
    
    def list_to_set(lst):
        # fill this in from the answer above
    
    
    if __name__ == '__main__':
        main()

#### 3. `sixty_minutes.py` that includes the function `triple_union` from problem #9 above. Print these three sets and their union: `twos = set([2, 4, 6, 10, 12])`, `threes = set([3, 6, 12])`, and `fours = set([4, 12])`.

    def main():
        twos = set([2, 4, 6, 10, 12])
        threes = set([3, 6, 12])
        fours = set([4, 12])
        
        print("Set 1:")
        print(twos)
        print("Set 2:")
        print(threes)
        print("Set 3:")
        print(fours)
        
        union_set = triple_union(twos, threes, fours)
        
        print("Their Union:")
        print(union_set)
    
    
    def triple_union(set1, set2, set3):
        # fill this in from the answer above
    
    
    if __name__ == '__main__':
        main()

#### 4. `coincidence.py` that includes the function `product` from problem #1 above. In the `main` function set `a` equal to `2` and `b` equal to `497`. Print the value of `product(a, b)`, and also print the value of the sum of `a` and `b`. Notice anything strange?

    def main():
        a = 2
        b = 497
        
        print('a=' + str(a) + ', b=' + str(b))
        
        print('Product:')
        print(product(a, b))
        
        print('Sum:')
        print(a + b)
    
    
    def product(num1, num2):
        # fill this in from the answer above

    
    if __name__ == '__main__':
        main()

#### 5. `sorted_squares.py` that includes the functions `make_square_dict` and `get_sorted_keys` from problems #6 and #10 above. In the `main` function, create a square dictionary from 1 to 20. Print the keys of that dictionary. Then use `get_sorted_keys` to print the keys in order.

    def main():
        square = make_square_dict(20)
        print(square.keys())
        
        print(get_sorted_keys(square))


    def make_square_dict(n):
        # fill this in from the answer above


    def get_sorted_keys(d):
        # fill this in from the answer above

    
    if __name__ == '__main__':
        main()

## Importing

Create a Python module called:

#### 1. `roll_the_dice.py` that uses `from random import randint` to print the result of a random dice roll (print 1 through 6 randomly from the `main` function).

    def main():
        print(roll_the_dice())
        print(roll_the_dice())
        print(roll_the_dice())
        print(roll_the_dice())


    def roll_the_dice():
        '''produces a number 1 through 6,
        just like a dice roll
        '''
        from random import randint
        return randint(1, 6)


    if __name__ == '__main__':
        main()

#### 2. `set_theory.py` that imports `triple_union` from `sixty_minutes.py` and `list_to_set` from `list_to_set.py`. In the `main` function, convert these threee lists into sets and print their union: `six = range(1, 7)`, `evens = range(2, 13, 2)`, and `thirds = range(3, 13, 3)`.

    from sixty_minutes import triple_union
    from list_to_set import list_to_set
    
    
    def main():
        six = range(1, 7)
        evens = range(2, 13, 2)
        thirds = range(3, 13, 3)
        
        six_set = list_to_set(six)
        evens_set = list_to_set(evens)
        thirds_set = list_to_set(thirds)
    
        print(triple_union(six_set, evens_set, thirds_set))
    
    
    if __name__ == '__main__':
        main()


XKCD is always relevant:

![XKCD is always relevant](http://imgs.xkcd.com/comics/random_number.png)



[Back to Problem Set](problem_set_1_functions_modules.md)
