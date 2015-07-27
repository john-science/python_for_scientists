# Using NumPy Arrays

## Solutions

#### Set 1

    # 1. Create a NumPy array of the integers 1 through 7.
    >>> from numpy import array
    >>> a = array([1, 2, 3, 4, 5, 6, 7])
    
    # 2. Set the first and last elements in the array to zero.
    >>> a[0] = 0
    >>> a[-1] = 1
    >>> a
    array([0, 2, 3, 4, 5, 6, 0])
    
    # 3. Use `.size` to determine the length of the array.
    >>> a.size
    7

    # 4. Sum all of the integers in the array.
    >>> from numpy import sum
    >>> 
    >>> sum(a)
    20
    
    # 5. Using the results from parts 3 and 4, find the average of the array.
    >>> float(sum(a)) / a.size
    2.857142857142857

#### Set 2

    # 1. Create a 1D NumPy array of 10,000 elements, all initially set to 0.0.
    >>> from numpy import zeros
    >>> 
    >>> a = zeros(10000)

    # 2. Use a `while` loop and set every 101st element equal to 1.0. (indices 0, 101, 202, 303, ...).
    >>> i = 0
    >>> while i <= a.size:
    ...     a[i] = 1.0
    ...     i += 101

    # 3. Change the shape of the array to be 100 x 100.
    >>> b = a.reshape(100, 100)
    
    # 4. Use a `for` loop to set the 1st element of every row equal to the sum of that row.
    >>> from numpy import sum
    >>> for row in range(100):
    ...     b[row][0] = sum(b[row])

    # 5. Create a new array from the first elements in each of your rows.
    >>> lst = []
    >>> for row in b:
    ...     lst.append(row[0])
    ... 
    >>> lst
    >>> c = array(lst)

    # 6. Take the product of all the elements in your new array.
    >>> from numpy import prod
    >>> prod(c)
    1.0

#### Set 3

    # 1. Use `arange` to create an array of decimals from zero to 26. (HINT: dtype=float)
    >>> from numpy import arange
    >>> arange(27, dtype=float)

    # 2. Reshape that array to be a 3 x 3 x 3 multi-dimensional array.
    >>> a = arange(27, dtype=float).reshape(3, 3, 3)
    >>> a
    array([[[  0.,   1.,   2.],
            [  3.,   4.,   5.],
            [  6.,   7.,   8.]],
    
           [[  9.,  10.,  11.],
            [ 12.,  13.,  14.],
            [ 15.,  16.,  17.]],
    
           [[ 18.,  19.,  20.],
            [ 21.,  22.,  23.],
            [ 24.,  25.,  26.]]])
    
    # 3. Print the first and last element in the array, using three indexes.
    >>> a[0][0][0]
    0.0
    >>> a[2][2][2]
    26.0
    
    # 4. Using three `for` loops, divide every number by the `sum` of all 3 elements in its row.
    >>> from numpy import sum
    >>> for i in range(3):
    ...     for j in range(3):
    ...         total = sum(a[i][j])
    ...         for k in range(3):
    ...             a[i][j][k] /= total
    
    # 5. Calculate the `sum` of all the elements in the array.
    >>> sum(sum(sum(a)))
    9.0
    
    # 6. Create a new array, where every element is the square root of the old one.
    >>> from numpy import sqrt
    >>> s = sqrt(a)

    # 7. Calculate the product of all the elements in your new array.
    >>> from numpy import prod
    >>> prod(s)
    0.0
    >>> # Why zero?
    ... # Because a[0][0][0] and s[0][0][0] were both 0.0.

#### Set 4

    # 1. Use `numpy.ones` to create an array, `a`, which is five elements long.
    >>> a = ones(5)
    
    # 2. Use `arange` to create an array, `b`, which is the integers from 2 to 6 (five elements long).
    >>> b = arange(2, 7)
    
    # 3. Use `arange` to create an array, `c`, which is the even integers 2 to 12.
    >>> c = arange(2, 12, 2)
    
    # 4. Use `arange` to create an array, `d`, which is the float values of the integers from 1 to 5.
    >>> d = arange(1, 6, dtype=float)
    
    # 5. Create a new array: x = c + a - b.
    >>> x = c + a - b

    # 6. What is the value of d - x?
    >>> d - x
    array([ 0.,  0.,  0.,  0.,  0.])


[Back to Problem Set](problem_set_1_arrays.md)
