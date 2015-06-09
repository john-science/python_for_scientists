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

We already saw that we can use `scipy` to create a [arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean):

    >>> scipy.mean(a)
    2.4321250000000001
    >>> scipy.mean(m)
    2.4321250000000001

But we can also use `scipy.stats` to calculate a [geometric mean](https://en.wikipedia.org/wiki/Geometric_mean):

    >>> stats.gmean(a)
    2.3001417284768615

And if we ask for the geometric mean of a multi-dimensional array, we will get an array in return (with the geometeric mean of each column:

    >>> stats.gmean(m)
    array([ 1.76635217,  1.94422221,  2.67790963,  3.04368198])

If we want, we can collapse this further by finding the geometric mean of that array:

    >>> stats.gmean(stats.gmean(m))
    2.3001417284768615

Similarly, you can use `stats.hmean` to calculte the [harmonic mean](https://en.wikipedia.org/wiki/Harmonic_mean):

    >>> stats.hmean(a)
    2.1679023922542315
    >>> stats.hmean(m)
    array([ 1.64210526,  1.93846154,  2.63598603,  2.93350222])
    >>> stats.hmean(stats.hmean(m))
    2.1679023922542311

Lastly, we can use `stats.sem` to calculate the [standard error of the mean](https://en.wikipedia.org/wiki/Standard_error) (referring to the arithmetic mean):

    >>> stats.sem(a)
    0.30337626552211178

#### Histograms

Whether for analysis or plotting, we frequently want to make a [histogram](https://en.wikipedia.org/wiki/Histogram) out of our data.

Use `stats.histogram` to produce a histogram, by simply providing an array of data and the number of bins:

    >>> stats.histogram(a, 3)
    (array([ 2.,  5.,  1.]), 0.5, 1.4, 0)

What has been returned is a tuple of four items:

    (values in the 3 bins you asked for, start value, bin size, # of items not binned)

That is, the `histogram` return has bins from: 0.5 -> 1.9 -> 4.3 -> 5.7

And inside these bins we have the values: 2, 5, 1.

Alternatively, you can use `stats.histogram2` to calculate how many items are in each bin, if you provide both the data *and* the location of the bins:

    >>> stats.histogram2(a, range(10))
    array([0, 2, 4, 1, 1, 0, 0, 0, 0, 0])

#### Percentiles

If you want to know [percentile](https://en.wikipedia.org/wiki/Percentile) of a dataset a certain value would be at, you could use `stats.percentileofscore`:

    >>> from numpy import array
    >>> from scipy import stats
    >>> 
    >>> grades = array([50, 81, 55, 100, 64, 72, 68, 73])
    >>> 
    >>> stats.percentileofscore(grades, 60)
    25.0
    >>> stats.percentileofscore(grades, 70)
    50.0
    >>> stats.percentileofscore(grades, 80)
    75.0
    >>> stats.percentileofscore(grades, 90)

Or you can go the opposite direction and ask what percentile a certain score would fit into with `stats.scoreatpercentile`:

    >>> stats.scoreatpercentile(grades, 55)
    71.400000000000006
    >>> stats.scoreatpercentile(grades, 64)
    72.480000000000004
    >>> stats.scoreatpercentile(grades, 72)
    73.319999999999993

#### Bayesian Statistics

Use `stats.bayes_mvs` to calculate the [Bayesian confidence intervals](http://en.wikipedia.org/wiki/Credible_interval) for the important values in your data set:

    >>> stats.bayes_mvs(grades)
    ((70.375, (59.942906473297676, 80.807093526702317)),
     (339.57500000000005, (120.69794896230246, 783.38757978857814)),
     (17.534429743228785, (10.986261828406533, 27.98906178828755)))

Each line above represents:

    (center of the interval, (lower bound on the interval, upper bound of the interval))

The three lines in order represent: the mean, variance, and standard deviation of your data set.

#### One-Way ANOVA

The simple one-way [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance) is a basic hypothesis-testing tool, used throughout all the sciences.

The Analysis of Variance (ANOVA) is a way to compare the similarity of data sets. In particular, an ANOVA tests the similarity of two or more data sets.

Use `stats.f_oneway` on two or more data sets:

    >>> x = scipy.mean(grades)
    >>> stats.f_oneway(grades, array([x, x]))
    (0.0, 1.0)

Here we compare the `grades` data set with another data set that is made of up two elements: each of which is mean of `grades`. So, of course, these two data sets have the same mean, and we reject the [null hypothesis](https://en.wikipedia.org/wiki/Null_hypothesis) that there is no relation between the data sets. But what do those two number we returned mean?

This is the best case result: `(0.0, 1.0)`. The first number is the [F-value](http://en.wikipedia.org/wiki/Analysis_of_variance#The_F-test) and the second number is the [p-value](http://en.wikipedia.org/wiki/Analysis_of_variance#The_F-test). The thing to remember is that you want your p-value to be 1.0. Worse case scenario, it will be 0.0. In fact, let's show what an example where the two data sets don't compare well at all:

    >>> stats.f_oneway(grades, array([-99 * x, -99 * x]))
    (373371.4201575499, 5.7626233819586514e-20)

In this case, the null hypothesis is strongly supported since the p-value is almost zero and F-value is very large.

## Interpolation

Use `stats.interp1d` if you have a 1D series of data points and you want to build an interpolating function:

    >>> from numpy import sin, pi
    >>> x = [float(i) for i in range(10)]
    >>> y = [sin(i) for i in range(10)]
    >>> 
    >>> from scipy.interpolate import interp1d
    >>> 
    >>> f = interp1d(x, y)
    >>> f2 = interp1d(x, y, kind='cubic')

These `f` and `f2` that we created is a Python function that we can now use, like any other function:

    >>> f([pi/2, pi, 2*pi])
    array([ 0.88018607,  0.01398078, -0.01424018])
    >>> f2([pi/2, pi, 2*pi])
    array([  9.92889428e-01,   5.22304460e-04,   4.39283521e-05])

You might remember from trignometry, `sin(pi/2) = 1.0` and `sin(pi) = 0.0`. So what we see is that adding `kind=cubic` to our `interp1d` made the interpolated function more accurate. There are several other `kind` option for how we might want to build the interpolated line:

 * linear
 * nearest
 * zero
 * slinear
 * quadratic
 * cubic

Similar to `interp1d`, you can use `stats.grid_data` to fit a multi-dimensional data. For more on that look [here](http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html#multivariate-data-interpolation-griddata).

Another feature of the `interpolate` module you might find interesting is the ability to take fine-tune control of a [splite fit](http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html#spline-interpolation) to your data.

## Optimizations

The `optimize` module is too big to cover here, but if you want more information, take a look at the official [tutorial](http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html).

#### Least-Square Fitting

In particular, there is a module for tutorial for least-square fitting on the [tutorial](http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html#least-square-fitting-leastsq).


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
