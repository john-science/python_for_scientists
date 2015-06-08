# Statistics with SciPy

SciPy is an amazingly useful library for scientists and engineers of all kinds. In this class we will just be using the portions of SciPy that deal with statistics and data analysis.

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

    >>> scipy.mean(a)
    2.9947833333333338

#### median

    >>> scipy.median(a)
    2.92835

#### standard deviation

If we pretend this very large array is a set of random variables that is distributed by a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution), we can use a few standard scipy functions to calculate:

#### The standard deviation

If our array were a large set of random numbers, we might think think to apply the [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution), and calculate the standard deviation from the mean:

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

The `scipy.stats` module has a great collection of different statistical functions and tools. However, this class can't really cover the topic of statistics in great detail. So instead of fully explaining all of the statistical terms presented, we will simply explain how to use the Python library and provide a basic link to a further explanation of the mathematical concept.

 * Coming Soon: http://docs.scipy.org/doc/scipy/reference/tutorial/stats.html

#### Trimmed Stats

 * Coming Soon: tmean, tvar, tstd, tmax, tmin, tsem

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

 * Coming Soon: f_oneawy
 * [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance)

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
