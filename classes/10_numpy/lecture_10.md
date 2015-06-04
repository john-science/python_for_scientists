# NumPy

NumPy is a really popular mathematics library for Python. Why do you care? Because many of the other libraries scientists and engineers care about are based on NumPy. In fact, several of the libraries we will cover in this class require NumPy to run: SciPy, matplotlib, pandas, and netCDF4.

#### Installation

NumPy is the first third-party library we have seen in this class. But it won't be the last. There are a ton of amazing tools written for Python that you as a scientist/engineer/geek/whatever will want to use. But they don't come pre-packaged with Python. You will have to install them yourself. 

You will need Python v2.4, v2.5, v2.6, v2.7 or v3.2 and newer to use NumPy and all of the other libraries that require it.

You can find instructions for installing NumPy [here](http://docs.scipy.org/doc/numpy/user/install.html).

## The NumPy array

### Lists vs Arrays

The `list` is the standard ordered-sequence data structure in Python. The Python `list` is an extremely flexible tool. But it turns out, that flexibility costs us some speed. NumPy introduces its own data structure, the  [array](http://wiki.scipy.org/Tentative_NumPy_Tutorial#head-c5f4ceae0ab4b1313de41aba9104d0d7648e35cc):

    >>> from numpy import array

One of the first differences you will find is that, unlike lists, all of the items in a NumPy `array` have to be of the same type.

    >>> lst = [1, 2, 3, 4.5]
    >>> lst
    [1, 2, 3, 4.5]
    >>> from numpy import array
    >>> a = array([1, 2, 3, 4.5])
    >>> a
    array([ 1.,  2.,  3.,  4.5])

Do you see what happened? Python automatically typecast all of the elements in the `array` to be of the same type. And since you would lose information going from 4.5 to 4, all of the elements in your `array` had to become decimals.

### NumPy Types

As well as having it's own data structure, NumPy goes one step further and has it's own types:

    >>> type(lst[0])
    int
    >>> type(a[0])
    <type 'numpy.float64'>

The NumPy library tries to default all of your numbers (integers, decimals, etc) to 64-bit versions. And there are NumPy alternatives to all the normal Python [primative types](https://en.wikipedia.org/wiki/Primitive_data_type):

 * int --> int64 (thought int16 and int32 are available)
 * float --> float64 (thought float16 and float32 are available)

There are, of course, many other data types in NumPy. For a full list, look [here](http://docs.scipy.org/doc/numpy/user/basics.types.html)

### Creating Arrays

One major difference between lists and NumPy.arrays is that arrays don't just have to be one-dimensional like lists:

    >>> from numpy import array
    >>>
    >>> array([[1, 2, 3], [7, 8, 9]])
    array([[1, 2, 3],
           [7, 8, 9]])
    >>> 
    >>> array([[1, 2, 3], [7, 8, 9]], dtype=float)
    array([[ 1.,  2.,  3.],
           [ 7.,  8.,  9.]])

And if you start out with a 1D `array`, you can make a 2D `array` by using `reshape`:

    >>> a = array([1, 2, 3, 4.5])
    >>> b = a.reshape(2, 2)
    >>> b
    array([[ 1. ,  2. ],
           [ 3. ,  4.4]])

And you can use `numpy.arange` to fill a `numpy.array` much like you used `range` to fill a list:

    >>> count = range(5)
    >>> count
    [0, 1, 2, 3, 4]
    >>> 
    >>> from numpy import arange
    >>> 
    >>> c = arange(18)
    >>> c
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17])

And, of course, you can use `arange` and `reshape` together:

    >>> d = arange(18).reshape(3,6)
    >>> d
    array([[ 0,  1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10, 11],
           [12, 13, 14, 15, 16, 17]])

Of course, you can also create a multi-dimensional `array` right from the start:

    >>> from numpy import array
    >>> e = array([[0, 1, 2, 3], [4, 5, 6, 7]])
    >>> e
    array([[0, 1, 2, 3],
           [4, 5, 6, 7]])

And, unlike the standard Python libraries, NumPy will let you define the type of the array:

    >>> from numpy import array
    >>> f = array([[0, 1, 2, 3], [4, 5, 6, 7]], float)
    >>> f
    array([[ 0.,  1.,  2.,  3.],
           [ 4.,  5.,  6.,  7.]])

Frequently, you will want to initialize an `array` with all zero values to start:

    >>> from numpy import zeros
    >>>
    >>> z = zeros(5, dtype=int)
    >>> z
    array([0, 0, 0, 0, 0])
    >>> 
    >>> y = zeros((2, 3), dtype=float)
    >>> y
    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])

Similarly, you can use `ones` to initialize an array to all 1 values:

    >>> from numpy import ones
    >>> 
    >>> ones(4)
    array([ 1.,  1.,  1.,  1.])
    >>> 
    >>> ones((2, 5), dtype=int)
    array([[1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1]])

### NumPy array Operations

Another difference you will see between Python lists and NumPy arrays is the helper methods.

#### ndim

Use `.ndim` to determine how many dimensions your multi-dimensional `array` has:

    >>> r = zeros((3, 2), dtype=float)
    >>> r
    array([[ 0.,  0.],
           [ 0.,  0.],
           [ 0.,  0.]])
    >>> r.ndim
    2

Of course, an `array` can have a lot of dimensions:

    >>> threed = zeros((2, 2, 2), dtype=int)
    >>> threed.ndim
    3

#### shape

Use `.shape` get more information about the structure of your `array`:

    >>> r.shape
    (3, 2)

#### dtype

Use `.dtype` to get the type of the elements in an `array`:

    >>> r.dtype
    dtype('float64')

#### flatten

Use `flatten` to convert a multi-dimensional `array` to a single dimension:

    >>> a = array([[2,3,4],[7,8,9]])
    >>> a
    array([[2, 3, 4],
           [7, 8, 9]])
    >>> a.flatten()
    array([2, 3, 4, 7, 8, 9])

#### transpose

Use `transpose` to flip the x and y directions in your `array`:

    >>> a = array([[2, 3, 4], [7, 8, 9]])
    >>> a
    array([[2, 3, 4],
           [7, 8, 9]])
    >>> a.transpose()
    array([[2, 7],
           [3, 8],
           [4, 9]])

#### sqrt

There are even mathematical functions built into NumPy that will apply to all of the elements of an array, like `sqrt`:

    >>> from numpy import sqrt
    >>> a = array([1, 4, 9, 25, 144, 81])
    >>> sqrt(a)
    array([  1.,   2.,   3.,   5.,  12.,   9.])

#### ceil & floor

Use `ceil` and `floor` to round NumPy `float64`s up or down to the nearest integer:

    >>> from numpy import ceil, floor
    >>> 
    >>> a = array([1.001, 2.49, 2.5, 3.5001, 9.9])
    >>> a
    array([ 1.001 ,  2.49  ,  2.5   ,  3.5001,  9.9   ])
    >>> ceil(a)
    array([  2.,   3.,   3.,   4.,  10.])
    >>> floor(a)
    array([ 1.,  2.,  2.,  3.,  9.])

#### sum & prod

NumPy also includes the ability to make the sum and product of all the elements in an array:

    >>> from numpy import sum, prod
    >>> a = array([1, 2, 3, 4, 5, 6])
    >>> sum(a)
    21
    >>> prod(a)
    720

And since they are built into NumPy, `sum` and `prod` can handle multi-dimensional arrays:

    >>> m = array([[1, 2, 3], [4, 5, 6]])
    >>> m
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> sum(m)
    21
    >>> prod(m)
    720

#### sort

Use `sort` to put the elements of a 1D array in order:

    >>> from numpy import sort
    >>> a = array([1, 2, 3, 4, 5, 4, 3, 2, 1])
    >>> sort(a)
    array([1, 1, 2, 2, 3, 3, 4, 4, 5])

And if you apply `sort` to a multi-dimensional `array`, it will return each sub-array ordered:

    >>> m = array([[9, 4, 2], [1, 0, -3]])
    >>> m
    array([[ 9,  4,  2],
           [ 1,  0, -3]])
    >>> sort(m)
    array([[ 2,  4,  9],
           [-3,  0,  1]])

#### clip

Use `clip` if you want to set the max and min value allowed in your array:

    >>> from numpy import clip
    >>> 
    >>> a = array([1, 2, 3, 0, -32, 99, 999])
    >>> 
    >>> clip(a, 0, 10000)
    array([  1,   2,   3,   0,   0,  99, 999])
    >>> clip(a, -999, 1)
    array([  1,   1,   1,   0, -32,   1,   1])

You can see that any values above the max or below the min are converted to the `MAX` and `MIN` values you set in your clip statement:

    >>> clip(lst, MIN, MAX)

#### tolist

Convert a `numpy.array` to a standard Python `list` using `list()`:

    >>> a = array([1, 4, 1, 5, 9])
    >>> a
    array([1, 4, 1, 5, 9])
    >>> list(a)
    [1, 4, 1, 5, 9]

But you would find this would fail on a multidimensional `array`, and you will just get a list of arrays:

    >>> m = array([[1, 2, 3], [7, 8, 9]])
    >>> m
    array([[1, 2, 3],
           [7, 8, 9]])
    >>> list(m)
    [array([1, 2, 3]), array([7, 8, 9])]

So, `numpy` provides the `tolist()` method, which will convert deep into the `array` structure:

    >>> m.tolist()
    [[1, 2, 3], [7, 8, 9]]

## NumPy Random Numbers

NumPy also has a lot of tools built in to help you generate [random numbers](https://en.wikipedia.org/wiki/Pseudorandom_number_generator). We will not cover the topic of random number generation in detail, as it is a whole field onto itself. If this topic interests you, start your research [here](https://en.wikipedia.org/wiki/Random_number_generation).  There are many different distributions of random numbers, and though we will only cover two, there are many more supported by NumPy that you can read about in the [documentation](http://docs.scipy.org/doc/numpy/reference/routines.random.html).

### Flat Distribution

When we say a distribution of random numbers is *flat*, we mean that the numbers generated are evenly distributed between the minimum and maximum. In NumPy, the default minimum is 0.0 and the default maximum is just less than 1.0, when generating random decimal values.

#### rand

Use `random.rand` to fill a NumPy `array` with random `float64` values between 0.0 and 1.0:

    >>> from numpy import random
    >>> 
    >>> random.rand(1)
    array([ 0.05895439])
    >>> random.rand(1)
    array([ 0.3581962])
    >>> random.rand(2, 3)
    array([[ 0.35675058,  0.51579755,  0.03851769],
           [ 0.74684991,  0.55219055,  0.37000399]])

#### randint

Use `random.randint` to fill a NumPy `array` with random `int64` values, where you can set the min and max integers, as well as the `array` dimensions.

You can just provide a maximum integer (min defaults to zero, max is exclusive):

    >>> from numpy import random
    >>> random.randint(5)
    0
    >>> random.randint(5)
    4
    >>> random.randint(5)
    3
    >>> random.randint(5)
    2

Or you can provide a min and a max (min inclusive, max exclusive):

    >>> random.randint(5, 10)
    9
    >>> random.randint(5, 10)
    5
    >>> random.randint(5, 10)
    5
    >>> random.randint(5, 10)
    7

Or you can create an entire array of random integers by providing the dimensions of the array as a third parameter:

    >>> random.randint(1, 10, 3)
    array([5, 2, 9])
    >>> 
    >>> random.randint(5, 10, (2, 3))
    array([[5, 6, 9],
           [8, 9, 6]])
    >>> 
    >>> random.randint(1, 10, (3, 5))
    array([[5, 4, 7, 1, 4],
           [6, 5, 5, 5, 4],
           [6, 9, 8, 7, 1]])

#### choice

You can use `random.choice` to select an element from a 1D `array`:

    >>> from numpy import array, random
    >>> a = array([1, 2, 3, 4, 5, 6, 7])
    >>> random.choice(a)
    5
    >>> random.choice(a)
    7
    >>> random.choice(a)
    1

The `choice` function is part of a flat distribution, because each element in the list is equally likely to be selected.

### Normal Distribution

When random numbers are generated with a [Normal Distribution](https://en.wikipedia.org/wiki/Normal_distribution), the average value is zero but the numbers can be decimals anywhere from infinity to negative infinity. In NumPy, the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of the normal distribution of random numbers is 1:

![Normal Distribution](http://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Normal_Distribution_PDF.svg/350px-Normal_Distribution_PDF.svg.png)

Use `random.randn` to produce an `array` of `float64` values, with a Normal Distribution (centered around zero, with a standard deviation of 1):

    >>> from numpy import random
    >>> random.randn(4)
    array([ 0.82712644, -1.15210992,  0.96319519, -0.16316335])
    >>> random.randn(4)
    array([-1.39618701, -1.01253218, -0.05627893, -0.78845925])

And, of course, we can create higher-dimensional arrays:

    >>> random.randn(2, 4)
    array([[-0.1366172 , -0.41921541,  1.98640058, -0.75165991],
           [ 1.69984245,  0.65345415, -1.90558238, -0.41176329]])
    >>>
    >>> random.randn(2, 2, 2)
    array([[[ 0.16383478, -0.03612812],
            [ 0.03078127,  0.54628765]],
    
           [[ 0.23479626,  1.0837927 ],
            [-0.50655975, -0.6393057 ]]])


### Permutations

A common desire is to randomly order an existing sequence of values. NumPy provides two basic ways to do just that.

#### Shuffle

Use `random.shuffle` if you want to randomly switch all the elements in a NumPy `array` in place:

    >>> a = array([1, 2, 3, 4, 5])
    >>> random.shuffle(a)
    >>> a
    array([4, 1, 5, 3, 2])
    >>> random.shuffle(a)
    >>> a
    array([1, 3, 5, 2, 4])

The caveat here is that this shuffling is not deep. For a multi-dimensional `array`, it will only shuffle the outermost arrays:

    >>> m = array([[1, 2, 3], [4, 5, 6]])
    >>> m
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> random.shuffle(m)
    >>> m
    array([[4, 5, 6],
           [1, 2, 3]])
    >>> m
    array([[1, 2, 3],
           [4, 5, 6]])

#### Permutation

Use `permutation` if you don't want to alter the original `array`, but just create a randomized version of it:

    >>> m = array([[1, 2, 3], [4, 5, 6]])
    >>> a = array([1, 2, 3, 4, 5])
    >>> 
    >>> random.permutation(a)
    array([3, 4, 1, 2, 5])
    >>> random.permutation(a)
    array([2, 4, 1, 3, 5])
    >>> random.permutation(m)
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> random.permutation(m)
    array([[4, 5, 6],
           [1, 2, 3]])
    >>> 
    >>> a
    array([1, 2, 3, 4, 5])
    >>> m
    array([[1, 2, 3],
           [4, 5, 6]])

The difference between `random.shuffle` and `random.permutation` is very similar to the difference we saw between `.sort()` and `sorted()` for lists. The first one alters the sequence "in place", and the second one doesn't alter the sequence, but creates an altered version of it.

## That's It?

Oh no. There is a lot more functionality available in NumPy. But we will go into more detail about dealing with arrays in the problem sets. And we will talk more about NumPy statistics in the SciPy class. For a full reference on what is available in Python, look at the [official documentation](http://docs.scipy.org/doc/numpy/reference/).

## Problem Sets

 * [Using NumPy Arrays](problem_set_1_arrays.md)
 * [Generating Random Generators in NumPy](problem_set_2_random.md)

## Further Reading

 * [Why NumPy arrays instead of lists?](http://stackoverflow.com/questions/993984/why-numpy-instead-of-python-lists)
 * [Official NumPy Tutorial](http://wiki.scipy.org/Tentative_NumPy_Tutorial)
 * [Intro PDF to NumPy and Scipy from UC SB](http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf)
 * [Docs of Random Numbers in NumPy](http://docs.scipy.org/doc/numpy/reference/routines.random.html)
 * [Random Number Generation](https://en.wikipedia.org/wiki/Random_number_generation)
 * [What is a pseudo-random number?](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
 * [What is a Normal Distribution?](https://en.wikipedia.org/wiki/Normal_distribution)
 * [What is a Standard Deviation?](https://en.wikipedia.org/wiki/Standard_deviation)


[Back to Syllabus](../../README.md)
