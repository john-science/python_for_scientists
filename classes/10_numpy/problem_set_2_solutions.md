# Generating Random Numbers in NumPy


## Set 1 - Testing Flatness randint

    # 1. Use `zeros` to create an array with 10 elements, name it `counts`.
    >>> from numpy import zeros
    >>> counts = zeros(10)
    >>> counts
    array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])

    # 2. Use a `for` loop to create 100,000 `random.randint` numbers less than 10. Add 1.0 to each element of `counts` that your random integer matches.
    >>> from numpy import random
    >>> for i in range(100000):
    ...     counts[random.randint(10)] += 1.0
    ... 
    >>> counts
    array([  9960.,  10165.,  10037.,   9810.,  10044.,   9943.,   9953.,
            10068.,   9866.,  10154.])

    # 3. Create a new array `bins` where you divide each element in `counts` by 100,000.
    >>> bins = counts / 100000.0
    >>> bins
    array([ 0.0996 ,  0.10165,  0.10037,  0.0981 ,  0.10044,  0.09943,
            0.09953,  0.10068,  0.09866,  0.10154])

    # 4. Are all 10 spots in `bins` the same?
    # They are REALLY close to the same. It looks *pretty* flat.
    # Maybe we should write a function to make running these tests easier:
    >>> from numpy import zeros, random
    >>> def test_randint_10_bins(num_trials):
    ...     '''test the numpy.random.randint function
    ...     for a set number of trials. Return a list
    ...     of 10 values; the more equal they are, the
    ...     more "flat" the randint distribution is.'''
    ...     counts = zeros(10)
    ...     for i in range(num_trials):
    ...         counts[random.randint(10)] += 1.0
    ...     return counts / num_trials
    ... 
    >>> 
    >>> test_randint_10_bins(1000000)
    array([ 0.099579,  0.100271,  0.100321,  0.100081,  0.099942,  0.099509,
            0.100288,  0.099957,  0.099668,  0.100384])
    >>> 
    >>> test_randint_10_bins(10000000)
    array([ 0.1001418,  0.1000986,  0.0999191,  0.1000831,  0.1000061,
            0.1000549,  0.0998571,  0.09987  ,  0.099856 ,  0.1001133])
    >>> 
    >>> test_randint_10_bins(100000000)
    array([ 0.09998835,  0.1000021 ,  0.10000281,  0.09998915,  0.09995632,
            0.10000618,  0.09998974,  0.09997884,  0.10001397,  0.10007254])
    # That looks *pretty* flat to me!
    
## Set 2 - Testing Flatness rand

    # 1. Use `zeros` to create an array with 10 elements, name it `counts`.
    >>> counts = zeros(10)

    # 2. Use a `for` loop to create 100,000 random decimals between zero and one (use `rand`). For each number you generate, multiple it by 10 and convert it to an integer using `int()`. Then add your number to the `counts` bin, as we did in part 2 of set 2.
    >>> counts = zeros(10)
    >>> for i in range(100000):
    ...     counts[int(10.0 * random.rand())] += 1.0
    ... 
    >>> counts
    array([  9941.,  10051.,  10039.,   9981.,   9712.,  10193.,   9988.,
            10116.,   9771.,  10208.])

    # 3. Create a new array `bins` where you divide each element in `counts` by 100,000.
    >>> bins = counts / 100000
    >>> bins
    array([ 0.09941,  0.10051,  0.10039,  0.09981,  0.09712,  0.10193,
            0.09988,  0.10116,  0.09771,  0.10208])

    # 4. Are all 10 spots in `bins` the same?
    # They're pretty close!  But let's write another function to test them more!
    >>> from numpy import zeros, random
    >>> def test_rand_10_bins(num_trials):
    ...     counts = zeros(10)
    ...     for i in range(num_trials):
    ...         counts[int(10.0 * random.rand())] += 1.0
    ...     return counts / num_trials
    ... 
    >>> 
    >>> test_rand_10_bins(1000000)
    array([ 0.099898,  0.099831,  0.09974 ,  0.100598,  0.100044,  0.100126,
            0.100119,  0.100046,  0.100424,  0.099174])
    >>> test_rand_10_bins(10000000)
    array([ 0.1001109,  0.1000013,  0.099908 ,  0.1001106,  0.0999376,
            0.0999534,  0.1000642,  0.0999279,  0.1000559,  0.0999302])

## Set 3 - Testing Flatness randn

    # 1. Use `zeros` to create an array with 10 elements, name it `counts`.
    >>> counts = zeros(10)

    # 2. Use a `for` loop to create 100,000 random decimals using `randn`. Take the absolute value (`abs`) of each of your numbers, then convert it to an integer using `int`. If your number is less than 10, add 1.0 to the appropriate element in your `counts` array, as in Sets 1 and 2 above.
    >>> for i in range(100000):
    ...     n = abs(random.randn())
    ...     if n < 10:
    ...         counts[int(n)] += 1.0
    ... 
    >>> counts
    array([  6.84240000e+04,   2.71860000e+04,   4.14500000e+03,
             2.42000000e+02,   3.00000000e+00,   0.00000000e+00,
             0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
             0.00000000e+00])

    # 3. Create a new array `bins` where you divide each element in `counts` by 100,000.
    >>> bins = counts / 100000
    >>> bins
    array([  6.84240000e-01,   2.71860000e-01,   4.14500000e-02,
             2.42000000e-03,   3.00000000e-05,   0.00000000e+00,
             0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
             0.00000000e+00])
    >>> 

    # 4. Take a look at `bins`, does it match a Normal Distribution?
    # It looks Really Good, so far. We expected ~68% of values should be within
    # one standard deviation (1.0) of the mean (0.0), and they are!

## Set 4 - Shuffle & Choice

    # 1. Use `arange` to create an array `a` with values 0 to 99.
    >>> from numpy import arange
    >>> a = arange(100)

    # 2. Use `numpy.random.shuffle` to randomly re-order `a`.
    >>> from numpy import random
    >>> random.shuffle(a)

    # 3. Randomly select an element from `a` using `numpy.random.choice`.
    >>> number = random.choice(a)
    >>> number
    34

    # 4. Find the type of your selected element using `.dtype`.
    >>> number.dtype
    dtype('int64')


[Back to Problem Set](problem_set_2_random.md)
