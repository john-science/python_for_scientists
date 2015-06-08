# Statistics with SciPy

SciPy is an amazingly useful library for scientists and engineers of all kinds. In this class, we will only cover the most popular topics that relate to statistics and data analysis.

We do not intend to cover the topics of statistics or data analysis here. Such discussions will be very brief, but external links will be provided for explanation of the mathematical concepts.

## Installing SciPy

Like most of the libraries used in our "special topics" lectures, SciPy does not come standard with Python and will have to be installed. Please check the official [SciPy Stack Install Guide](http://www.scipy.org/install.html). For Linux and Mac, the installation is merely a single line of `apt-get`. For Windows, pre-built installers are provided.

## Basics

Interestingly, most of the functions found in this sub-section can also be found in NumPy. But that won't be true for the next sub-sections.

Let us start with a 2D array of numbers:

    >>> import scipy
    >>> from numpy import array
    >>> a = array([3.19, 2.222, 2.629, 2.6667, 3.451, 3.81])
    >>> a = a.reshape(3,2)
    array([[ 3.19  ,  2.222 ],
           [ 2.629 ,  2.6667],
           [ 3.451 ,  3.81  ]])

And let's pretend this is a very large `array`.

#### mean

The [arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean) is the simple average of a collection of numbers:

    >>> scipy.mean(a)
    2.9947833333333338

#### median

The [median](https://en.wikipedia.org/wiki/Median) of a collection of numbers is simply the middle number if the collection is ordered:

    >>> scipy.median(a)
    2.92835

#### The standard deviation

If we pretend this very large array is a set of random variables, we might think think to apply the [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution), and calculate the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) from the mean:

    >>> scipy.std(a)
    0.53997709956585715

#### variance

The [variance](https://en.wikipedia.org/wiki/Variance) is a measure of how spread out a set of numbers are:
    
    >>> scipy.var(a)
    0.29157526805555556

#### The covariance

The [covariance](https://en.wikipedia.org/wiki/Covariance) is a measure of how two random variables change together:

    >>> scipy.cov(a)
    array([[ 0.468512  , -0.0182468 , -0.173756  ],
           [-0.0182468 ,  0.00071065,  0.00676715],
           [-0.173756  ,  0.00676715,  0.0644405 ]])

## Stats

The `scipy.stats` module has a great collection of different statistical functions and tools. For a complete listing of what is in this module, check the [documentation](http://docs.scipy.org/doc/scipy/reference/tutorial/stats.html).

#### Trimmed Stats

The trimmed statistics functions below are the same as the basic functions above, but they allow you 

The "trimmed" stastical functions are a covenience, meant to help you find basic stastical values with a slightly modified dataset. These functions are handy if you want to exclude obvious bad data points from a quick analysis.

We calculate the trimmed mean by providing the array of data points, and a pair of min/max values to trim from:

    >>> from numpy import array
    >>> from scipy import stats
    >>> 
    >>> a = array([1.2, 2.1, 3.2, 4.0, 2.6, 1.8, 2.241, 2.316])
    >>> 
    >>> stats.tmean(a, (2, 5))
    2.7428333333333335

By default, if a value is actually *at* one of your limits, it is still included in the average. But you can manually set if your min/max limits are inclusive:

    >>> stats.tmean(a, (1.2, 3))
    2.0428333333333337
    >>> stats.tmean(a, (1.2, 3), (False, False))
    2.2114000000000003

This will also work with multi-dimensional arrays:

    >>> m = array([[1.2, 2.1, 3.2, 4.0], [2.6, 1.8, 2.241, 2.316]])
    >>> m
    array([[ 1.2  ,  2.1  ,  3.2  ,  4.   ],
           [ 2.6  ,  1.8  ,  2.241,  2.316]])
    >>> 
    >>> stats.tmean(m, (1.2, 3))
    2.0428333333333337
    >>> stats.tmean(m, (1.2, 3), (False, False))
    2.2114000000000003

You can also find the [standard error of the mean](https://en.wikipedia.org/wiki/Standard_error) of a trimmed dataset:

    >>> stats.tsem(a, (1, 2))
    0.29999999999999999
    >>> stats.tsem(a, (1, 3))
    0.19974390548344095
    >>> stats.tsem(a, (-99, 3))
    0.19974390548344095

You can also find the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of a trimmed dataset:

    >>> stats.tstd(a, (1, 3))
    0.48927064766514117
    >>> stats.tstd(a, (1, 6))
    0.85807765840694339

And finally, the [variance](https://en.wikipedia.org/wiki/Variance) of the trimmed dataset:

    >>> stats.tvar(a, (-9000, 2))
    0.18000000000000005
    >>> stats.tvar(a, (2, 9000))
    0.53142576666666663

#### Various Means

 * Coming Soon: gmean, hmean, sem
 * [geometric mean](https://en.wikipedia.org/wiki/Geometric_mean)
 * [harmonic mean](https://en.wikipedia.org/wiki/Harmonic_mean)
 * [standard error of the mean](https://en.wikipedia.org/wiki/Standard_error)

#### Histograms

 * Coming Soon: histogram, histogram2, binnedstats

#### Percentiles

 * Coming Soon: scoreatpercentile, percentileatscore

#### Bayesian Statistics

 * Coming Soon: bayes_mvs

#### One-Way ANOVA

The simple one-way [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance) is a basic hypothesis-testing tool, used throughout all the sciences.

 * Coming Soon: f_oneawy

## Interpolation

 * Coming Soon: http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html

## Optimizations

 * Coming Soon: http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html#least-square-fitting-leastsq

#### Least-Square Fitting

 * Coming Soon: pg31 example http://math.jacobs-university.de/oliver/teaching/scipy-intro/scipy-intro.pdf


## Further Reading

 * [Official Tutorial](http://docs.scipy.org/doc/scipy/reference/tutorial/)
 * [Official Tutorial - Stats](http://docs.scipy.org/doc/scipy/reference/tutorial/stats.html)
 * [Official Docs - Stats](http://docs.scipy.org/doc/scipy/reference/stats.html#module-scipy.stats)
 * [Official Tutorial - Interpolation](http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html)
 * [Official Tutorial - Optimizations](http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html#least-square-fitting-leastsq)
 * [SciPy Statistics - Official Tutorial](http://docs.scipy.org/doc/scipy/reference/tutorial/stats.html)
 * [Least Squares Fitting](http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html#least-square-fitting-leastsq)
 * [Interpollation](http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html)
 * [PDF Intro to NumPy and SciPy](http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf)
 * [Sam's SciPy Intro](http://www.sam.math.ethz.ch/~raoulb/teaching/PythonTutorial/intro_scipy.html)

[Back to Syllabus](../../README.md)
