# NumPy Arrays

> NumPy arrays are the starting point for nearly all hard math and science work in Python.

NumPy is the most popular mathematics library for Python. NumPy takes a big step toward making Python as fast as C for serious mathematical computations. There are hundreds of scientific and mathematical libraries in Python that just could not exist without NumPy. Several of these libraries we will cover in this sourse: SciPy, matplotlib, pandas, and netCDF4.

For sure, NumPy is a big math library with more than just `np.array`. But you have to start somewhere, so this lecture will focus on NumPy arrays.


#### Installation

NumPy is the first third-party library we will use in this class. But it won't be the last. There are a ton of amazing tools written for Python that you as a scientist/engineer/geek/whatever will want to use. But they don't come pre-packaged with Python. You will have to install them separately. 

You will want Python v3.3 (or newer) to use NumPy and all of the other libraries that require it.

You can find instructions for installing NumPy [here](http://docs.scipy.org/doc/numpy/user/install.html).

> **Please Note** The NumPy group [has said](https://github.com/numpy/numpy/blob/master/doc/neps/dropping-python2.7-proposal.rst) they will be dropping support for Python 2.X on Jan 1, 2020.  Since this library is the basis of nearly all science and engineering work in Python it will be very important that you move from Python 2.X to Python 3.X at some point.


#### Anaconda

Consider installing [Anaconda](http://docs.continuum.io/anaconda/install.html) instead. Anaconda is Python packaged with hundreds of tools and libraries that you will want (This includes NumPy and everything else we will use in this course.)


## The NumPy array

### Lists vs Arrays

The `list` is the standard ordered-sequence data structure in Python. The Python `list` is an extremely flexible tool. But, it turns out, that flexibility costs speed. NumPy introduces its own data structure, the  [array](http://wiki.scipy.org/Tentative_NumPy_Tutorial#head-c5f4ceae0ab4b1313de41aba9104d0d7648e35cc):

```python
>>> from numpy import array
```

One of the first differences you will find is that, unlike lists, all of the items in a NumPy `array` have to be of the same type.

```python
>>> lst = [1, 2, 3, 4.5]
>>> lst
[1, 2, 3, 4.5]
>>> from numpy import array
>>> a = array([1, 2, 3, 4.5])
>>> a
array([ 1.,  2.,  3.,  4.5])
```

Do you see what happened? Python automatically typecast all of the elements in the `array` to be of the same type. And since you would lose information going from 4.5 to 4, all of the elements in your `array` had to become decimals.

### NumPy Types

As well as having it's own data structure, NumPy goes one step further and has it's own types:

```python
>>> type(lst[0])
int
>>> type(a[0])
<type 'numpy.float64'>
```

The NumPy library tries to default all of your numbers (integers, decimals, etc) to 64-bit versions. And there are NumPy alternatives to all the normal Python [primative types](https://en.wikipedia.org/wiki/Primitive_data_type):

 * int --> int64 (thought int16 and int32 are available)
 * float --> float64 (thought float16 and float32 are available)

There are, of course, many other data types in NumPy. For a full list, look [here](http://docs.scipy.org/doc/numpy/user/basics.types.html)

### Creating Arrays

One difference between lists and NumPy.arrays is that arrays don't just have to be one-dimensional:

```python
>>> from numpy import array
>>>
>>> array([[1, 2, 3], [7, 8, 9]])
array([[1, 2, 3],
       [7, 8, 9]])
>>> 
>>> array([[1, 2, 3], [7, 8, 9]], dtype=float)
array([[ 1.,  2.,  3.],
       [ 7.,  8.,  9.]])
```

And if you start out with a 1D `array`, you can make a 2D `array` using `reshape`:

```python
>>> a = array([1, 2, 3, 4.5])
>>> b = a.reshape(2, 2)
>>> b
array([[ 1. ,  2. ],
       [ 3. ,  4.5]])
```

The `.reshape()` method is really pretty smart. It doesn't move any of the data around in memory, which would be quite slow. All it does is change how you access data. This is an extremely convenient feature that will almost always make your life easier.

What do you think will happen if you run this code?

```python
>>> a = array([1, 2, 3, 4.5])
>>> c = a.reshape(3, 3)
```

You can use `numpy.arange` to fill a `numpy.array` much like you used `range` to fill a Python-standard `list`:

```python
>>> count = range(5)
>>> count
[0, 1, 2, 3, 4]
>>> 
>>> from numpy import arange
>>> 
>>> c = arange(18)
>>> c
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17])
```

The `numpy.arange` function can work like it does above, or it can take three paramters: `min`, `max`, and `step`:

```python
>>> arange(2, 15, 4)
array([ 2,  6, 10, 14])
```

What do you think the following code will produce?

```python
>>> arange(2, 15)
```

Here's a quick example using `arange` and `reshape` together:

```python
>>> d = arange(18).reshape(3,6)
>>> d
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17]])
```

You can also create a multi-dimensional `array` right from the start:

```python
>>> from numpy import array
>>> e = array([[0, 1, 2, 3], [4, 5, 6, 7]])
>>> e
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
```

And, unlike the standard Python libraries, NumPy will let you define the type of the array:

```python
>>> from numpy import array
>>> f = array([[0, 1, 2, 3], [4, 5, 6, 7]], np.float32)
>>> f
array([[ 0.,  1.,  2.,  3.],
       [ 4.,  5.,  6.,  7.]])
```

Frequently, you will want to initialize an `np.array` with all zero values:

```python
>>> from numpy import zeros
>>>
>>> z = zeros(5, dtype=np.int64)
>>> z
array([0, 0, 0, 0, 0])
>>> 
>>> y = zeros((2, 3), dtype=np.float32)
>>> y
array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])
```

Similarly, you can use `ones` to initialize an array to all 1 values:

```python
>>> from numpy import ones
>>> 
>>> ones(4)
array([ 1.,  1.,  1.,  1.])
>>> 
>>> ones((2, 5), dtype=np.int64)
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
```

### Array Math

One of the great things about numpy is that it makes operating on every element of an array super easy. For instance, if you want to add or subtract two arrays:

```python
>>> from numpy import array
>>> a = array([1, 2, 3])
>>> b = array([-1, 2, 3])
>>> 
>>> a + b
array([0, 4, 6])
>>> 
>>> a - b
array([2, 0, 0])
```

And you can do math an numpy arrays using just regular numbers:

```python
>>> 2 * a
array([2, 4, 6])
>>> 
>>> a + 1
array([2, 3, 4])
```

And you can combine the two:

```python
>>> 2 * (a + b) - 4
array([-4,  4,  8])
```

This functionality saves a lot of tedious code writing. And the resulting operations are usually much faster than they would be written using Python lists.

What would you expect this to produce?

```python
>>> 2 * (1 - a + b)
```

### NumPy array Operations

Another great feature of numpy arrays is the huge variety of helper methods.

#### ndim

Use `.ndim` to determine how many dimensions your multi-dimensional `np.array` has:

```python
>>> r = zeros((3, 2), dtype=np.float64)
>>> r
array([[ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.]])
>>> r.ndim
2
```

And another example:

```python
>>> cube = zeros((2, 2, 2), dtype=np.float64)
>>> cube.ndim
3
```

#### shape

Use `.shape` get more information about the structure of your `np.array`:

```python
>>> r.shape
(3, 2)
>>>
>>> cube.shape
(2, 2, 2)
```

Most frequently, I use `.shape` to get just one of the dimensions of the `np.array`:

```python
>>> r.shape[0]
3
```

#### dtype

Use `.dtype` to get the type of the elements in an `array`:

```python
>>> r.dtype
dtype('float64')
```

#### flatten

Use `flatten` to convert a multi-dimensional `array` to a single dimension:

```python
>>> a = array([[2,3,4],[7,8,9]])
>>> a
array([[2, 3, 4],
       [7, 8, 9]])
>>>
>>> a.flatten()
array([2, 3, 4, 7, 8, 9])
```

Remember, this is quite fast because the data is not being move around, it is only changing out we access it.

#### transpose

Use `transpose` to flip the x and y directions in your `array`:

```python
>>> a = array([[2, 3, 4], [7, 8, 9]])
>>> a
array([[2, 3, 4],
       [7, 8, 9]])
>>>
>>> a.transpose()
array([[2, 7],
       [3, 8],
       [4, 9]])
```

Alternatively, you can just use the shorthand `.T` to do the same thing.

```python
>>> a = array([[2, 3, 4], [7, 8, 9]])
>>> a.T
array([[2, 7],
       [3, 8],
       [4, 9]])
>>>
>>> a
array([[2, 3, 4],
       [7, 8, 9]])
```

Notice that neither of these methods changes what is in the `a` place in memory; they return a totally new array.

#### sqrt

NumPy even has mathematical functions designed to act on entire arrays. A lot of them, like `sqrt`:

```python
>>> from numpy import sqrt
>>> a = array([1, 4, 9, 25, 144, 81])
>>> sqrt(a)
array([  1.,   2.,   3.,   5.,  12.,   9.])
```

#### ceil & floor

Use `ceil` and `floor` to round NumPy `np.float64`s up or down to the nearest integer:

```python
>>> from numpy import ceil, floor
>>> 
>>> a = array([1.001, 2.49, 2.5, 3.5001, 9.9])
>>> 
>>> ceil(a)
array([  2.,   3.,   3.,   4.,  10.])
>>> floor(a)
array([ 1.,  2.,  2.,  3.,  9.])
```

What would you expect this to return?

```python
>>> x = array([3.912, 15.8999, 35.98989])
>>> floor(sqrt(x))
```

#### sum & prod

NumPy also includes the ability to make the sum and product of all the elements in an array:

```python
>>> from numpy import sum, prod
>>> a = array([1, 2, 3, 4, 5, 6])
>>> 
>>> sum(a)
21
>>> prod(a)
720
```

And since they are built into NumPy, `sum` and `prod` can handle multi-dimensional arrays:

```python
>>> m = array([[1, 2, 3], [4, 5, 6]])
>>> m
array([[1, 2, 3],
       [4, 5, 6]])
>>> sum(m)
21
>>> prod(m)
720
```

#### sort

Use `sort` to put the elements of a 1D array in order:

```python
>>> from numpy import sort
>>> a = array([1, 2, 3, 4, 5, 4, 3, 2, 1])
>>> sort(a)
array([1, 1, 2, 2, 3, 3, 4, 4, 5])
```

And if you apply `sort` to a multi-dimensional `array`, it will return each sub-array ordered:

```python
>>> m = array([[9, 4, 2], [1, 0, -3]])
>>> m
array([[ 9,  4,  2],
       [ 1,  0, -3]])
>>> sort(m)
array([[ 2,  4,  9],
       [-3,  0,  1]])
```

A related function is `argsort`, which instead returns the indices of the sorted elements:

```python
>>> x = np.array([2, 1, 4, 3, 5])
>>> np.argsort(x)
[1 0 3 2 4]
```

#### clip

Use `clip` if you want to set the max and min value allowed in your array:

```python
>>> from numpy import clip
>>> 
>>> a = array([1, 2, 3, 0, -32, 99, 999])
>>> 
>>> clip(a, 0, 10000)
array([  1,   2,   3,   0,   0,  99, 999])
>>> clip(a, -999, 1)
array([  1,   1,   1,   0, -32,   1,   1])
```

This simple goes through your array and converts any values below your `MIN` to the `MIN` and converts any values above your `MAX` to `MAX`.

#### tolist

You could convert a `numpy.array` to a standard Python `list` using `list()`:

```python
>>> a = array([1, 4, 1, 5, 9])
>>> a
array([1, 4, 1, 5, 9])
>>> list(a)
[1, 4, 1, 5, 9]
```

But this might not behave like you expect for a multidimensional `array`. It just returns list of arrays:

```python
>>> m = array([[1, 2, 3], [7, 8, 9]])
>>> m
array([[1, 2, 3],
       [7, 8, 9]])
>>> list(m)
[array([1, 2, 3]), array([7, 8, 9])]
```

So, `numpy` provides the `tolist()` method, which will convert deep into the `array` structure:

```python
>>> m.tolist()
[[1, 2, 3], [7, 8, 9]]
```

#### combining arrays

There are two convenient methods for combining arrays in numpy, `concatenate` and `vstack`:

```python
>>> c = array([[1,2,3], [4,5,6]])
>>> d = array([[5,6,7], [8,9,0]])
>>> 
>>> np.concatenate((c, d))
array([[1, 2, 3],
       [4, 5, 6],
       [5, 6, 7],
       [8, 9, 0]])
>>> 
>>> np.vstack((c, d))
array([[1, 2, 3],
       [4, 5, 6],
       [5, 6, 7],
       [8, 9, 0]])
```

The above 2D array example makes these seem very similar. But there is a difference, which is easiest to see in a 1D example:

```python
>>> import numpy as np
>>> from numpy import array
>>> 
>>> a = array([1,2,3,4,5])
>>> b = array([9,8,7,6,5])
>>> 
>>> np.concatenate((a, b))
array([1, 2, 3, 4, 5, 9, 8, 7, 6, 5])
>>> 
>>> np.vstack((a, b))
array([[1, 2, 3, 4, 5],
       [9, 8, 7, 6, 5]])
```

What do you suppose would happen if you tried to `np.concatenate` or `np.vstack` 2D arrays?


## NumPy Random Numbers

Well, now that we've seen the basics of NumPy arrays let's try using them for something. 

NumPy also has a lot of tools built in to help you generate [random numbers](https://en.wikipedia.org/wiki/Pseudorandom_number_generator). We will not cover the topic of random number generation in detail, as it is a whole field onto itself. If this topic interests you, start your research [here](https://en.wikipedia.org/wiki/Random_number_generation). There are many different distributions of random numbers, and though we will only cover two, there are many more supported by NumPy that you can read about in the [documentation](http://docs.scipy.org/doc/numpy/reference/routines.random.html).

### Flat Distribution

When we say a distribution of random numbers is *flat*, we mean that the numbers generated are evenly distributed between the minimum and maximum. In NumPy, the default minimum is 0.0 (inclusive) and the default maximum 1.0 (exclusive), when generating random decimals.

#### rand

Use `random.rand` to fill a NumPy `array` with random `float64` values between 0.0 and 1.0:

```python
>>> from numpy import random
>>> 
>>> random.rand(1)
array([ 0.05895439])
>>> random.rand(3)
array([ 0.3581962, 0.5377904, 0.0094921])
>>> random.rand(2, 3)
array([[ 0.35675058,  0.51579755,  0.03851769],
       [ 0.74684991,  0.55219055,  0.37000399]])
```

#### randint

Use `random.randint` to fill a NumPy `array` with random `int64` values, where you can set the min and max integers, as well as the `array` dimensions.

You can just provide a maximum integer (min defaults to zero, max is exclusive):

```python
>>> from numpy import random
>>> random.randint(5)
0
>>> random.randint(5)
4
>>> random.randint(5)
3
>>> random.randint(5)
2
```

Or you can provide a min and a max (min inclusive, max exclusive):

```python
>>> random.randint(5, 10)
9
>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
7
```

Or you can create an entire array of random integers by providing the dimensions of the array as a third parameter:

```python
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
```

#### choice

You can use `random.choice` to select an element from a 1D `array` (multidimensional arrays won't work):

```python
>>> from numpy import array, random
>>> a = array([1, 2, 3, 4, 5, 6, 7])
>>> random.choice(a)
5
>>> random.choice(a)
7
>>> random.choice(a)
1
```

The `choice` function is part of a flat distribution, because each element in the list is equally likely to be selected.

### Normal Distribution

When random numbers are generated with a [Normal Distribution](https://en.wikipedia.org/wiki/Normal_distribution), the average value is zero but the numbers can be decimals anywhere from infinity to negative infinity. In NumPy, the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of the normal distribution of random numbers is 1:

![Normal Distribution](http://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Normal_Distribution_PDF.svg/350px-Normal_Distribution_PDF.svg.png)

Use `random.randn` to produce an `array` of `float64` values, with a Normal Distribution (centered around zero, with a standard deviation of 1):

```python
>>> from numpy import random
>>> random.randn(1)
array([ 0.82712644])
>>> random.randn(4)
array([-0.0518932 ,  1.02017916, -0.50273024,  0.63187314])
```

And, again, we can create higher-dimensional arrays:

```python
>>> random.randn(2, 4)
array([[-0.1366172 , -0.41921541,  1.98640058, -0.75165991],
       [ 1.69984245,  0.65345415, -1.90558238, -0.41176329]])
>>>
>>> random.randn(2, 2, 2)
array([[[ 0.16383478, -0.03612812],
        [ 0.03078127,  0.54628765]],
       [[ 0.23479626,  1.0837927 ],
        [-0.50655975, -0.6393057 ]]])
```

### Permutations

A common desire is to randomly order an existing sequence of values. NumPy provides two basic ways to do that.

#### Shuffle

Use `random.shuffle` if you want to randomly switch all the elements in a NumPy `array` in place:

```python
>>> a = array([1, 2, 3, 4, 5])
>>> random.shuffle(a)
>>> a
array([4, 1, 5, 3, 2])
>>> random.shuffle(a)
>>> a
array([1, 3, 5, 2, 4])
```

The caveat here is that this shuffling is not deep. For a multi-dimensional `array`, it will only shuffle the outermost arrays:

```python
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
```

#### Permutation

Use `permutation` if you don't want to alter the original `array`, but just create a randomized version of it:

```python
>>> a = array([1, 2, 3, 4, 5])
>>> m = array([[1, 2, 3], [4, 5, 6]])
>>> 
>>> random.permutation(a)
array([3, 4, 1, 2, 5])
>>> random.permutation(a)
array([2, 4, 1, 3, 5])
>>> 
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
```

The difference between `random.shuffle` and `random.permutation` is very similar to the difference we saw between `.sort()` and `sorted()` for lists. The first one alters the sequence "in place", and the second one doesn't alter the sequence, but creates an altered version of it.

## Is that all for NumPy?

Oh no.

This class is meant to give an introduction and foundation to NumPy, not cover all the deep corners of the library. NumPy has a lot more tools that you might find useful: treating 2D arrays as matricies, Fourier transforms, polynomials, linear algebra, and statistics. But as long as you take the time to understand the numpy array and the numpy data types, the rest of the library should be approachable.

We will cover NumPy statistics in the SciPy class. For a full reference on what is available in NumPy, look in the [official documentation](http://docs.scipy.org/doc/numpy/reference/).

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
 * [Matlab to Python Cheatsheet](https://cheatsheets.quantecon.org/)


[Back to Syllabus](../../README.md)
