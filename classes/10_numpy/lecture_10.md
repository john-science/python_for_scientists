# NumPy

NumPy is a really popular mathematics library for Python. Why do you care? Because many of the other libraries scientists and engineers care about are based on NumPy. In fact, several of the libraries we will cover in this class require NumPy to run: SciPy, matplotlib, pandas, and netCDF4.

#### Installation

NumPy is the first third-party library we have seen in this class. But it won't be the last. There are a ton of amazing tools written for Python that you as a scientist/engineer/geek/whatever will want to use. But they don't come pre-packaged with Python. You will have to install them yourself. 

You will need Python v2.4, v2.5, v2.6, v2.7 or v3.2 and newer to use NumPy and all of the other libraries that require it.

You can find instructions for installing NumPy [here](http://docs.scipy.org/doc/numpy/user/install.html).

## The NumPy array

So far in this class we have considered lists to be the data structure of choice in Python. Lists are amazingly flexible tools that allow us to do a lot of things. But that flexibility costs us some speed. Instead, we will use the NumPy [array](http://wiki.scipy.org/Tentative_NumPy_Tutorial#head-c5f4ceae0ab4b1313de41aba9104d0d7648e35cc):

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

## NumPy Types

 * Coming Soon

## NumPy array Operations

 * Coming Soon

## NumPy Random Numbers

 * Coming Soon

## Further Reading

 * [Why NumPy arrays instead of lists?](http://stackoverflow.com/questions/993984/why-numpy-instead-of-python-lists)
 * [Official NumPy Tutorial](http://wiki.scipy.org/Tentative_NumPy_Tutorial)
 * [Intro PDF to NumPy and Scipy from UC SB](http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf)


[Back to Syllabus](../../README.md)
