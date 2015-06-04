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

You can use `ndim` to determine how many dimensions your multi-dimensional `array` has:

    >>> r = zeros((3, 2), dtype=float)
    >>> r
    array([[ 0.,  0.],
           [ 0.,  0.],
           [ 0.,  0.]])
    >>> r.ndim
    2

#### shape

You can use `shape` get more information about the structure of your `array`:

    >>> r.shape
    (3, 2)

#### dtype

You can also get the type of the elements in the array using `.dtype`:

    >>> r.dtype
    dtype('float64')

#### flatten

You can use `flatten` to convert a multi-dimensional `array` to a single dimension:

    >>> a = array([[2,3,4],[7,8,9]])
    >>> a
    array([[2, 3, 4],
           [7, 8, 9]])
    >>> a.flatten()
    array([2, 3, 4, 7, 8, 9])

#### transpose

You can use `transpose` to flip the x and y directions in your `array`:

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

You can use `ceil` and `floor` to round NumPy `float64`s up or down to the nearest integer:

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

You can use `sort` to put the elements of a 1D array in order:

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

You can use `clip` if you want to set the max and min value allowed in your array:

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

If you want to convert a `numpy.array` to a standard Python `list`, you could try just using `list()`:

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

 * Coming Soon

#### randint

 * Coming Soon

#### choice

 * Coming Soon

### Normal Distribution

When random numbers are generated with a [Normal Distribution](https://en.wikipedia.org/wiki/Normal_distribution), the average value is zero but the numbers can be decimals anywhere from infinity to negative infinity. In NumPy, the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of the normal distribution of random numbers is 1:

![Normal Distribution](http://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Normal_Distribution_PDF.svg/350px-Normal_Distribution_PDF.svg.png)

 * Coming Soon

### Permutations

 * Coming Soon

#### Shuffle

 * Coming Soon

#### Permutation

 * Coming Soon

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
