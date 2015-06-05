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

    # 2. Use a `while` loop and set every 101st element equal to 1.0. (0, 101, 202, 303, ...).
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



[Back to Problem Set](problem_set_1_arrays.md)
