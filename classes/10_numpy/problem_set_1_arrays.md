# Using NumPy Arrays

## Problems

 * Coming Soon
 * Coming Soon: create various arrays, use sum, prod, sqrt, ceil, floor
 * Coming Soon: add, subtract, multiple, divide arrays
 * Coming Soon: [array iteration](http://docs.scipy.org/doc/numpy/reference/arrays.classes.html#array-iterators)
 * Coming Soon: [masked arrays](http://docs.scipy.org/doc/numpy/reference/maskedarray.generic.html)

#### Set 1

1. Create a NumPy array of the integers 1 through 7.
2. Set the first and last elements in the array to zero.
3. Use `.size` to determine the length of the array.
4. Sum all of the integers in the array.
5. Using the results from parts 3 and 4, find the average of the array.

#### Set 2

1. Create a 1D NumPy array of 10,000 elements, all initially set to 0.0.
2. Use a `while` loop and set every 101st element equal to 1.0. (0, 101, 202, 303, ...).
3. Change the shape of the array to be 100 x 100.
4. Use a `for` loop to set the first element of every row equal to the sum of all the values in that row.
5. Create a new array from the first elements in each of your rows. (HINT: You can make an array from a list.)
6. Take the product of all the elements in your new array.

#### Set 3

1. Use `arange` to create an array of decimals from zero to 26. (HINT: dtype=float)
2. Reshape that array to be a 3 x 3 x 3 multi-dimensional array.
3. Print the first and last element in the array, using three indexes.
4. Using three `for` loops, divide every number by the `sum` of all 3 elements in its row.
5. Calculate the `sum` of all the elements in the array.
6. Create a new array, where every element is the square root of the old one.
7. Calculate the product of all the elements in your new array.

## Solutions

* [NumPy Arrays - Solutions](problem_set_1_solutions.md)


[Back to Lecture](lecture_10.md)
