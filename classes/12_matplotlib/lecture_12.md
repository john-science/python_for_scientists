# Plotting with matplotlib

Matplotlib is a standard plotting library in Python. That is, people use it all the time to make 2D or 3D informational graphics. This is not a thorough guide to everything you can do with the library. But a quick introduction to the four major kinds of plots you (as a scientist/engineer) will want to make 99% of the time. The plots are easy to make, and easy to customize. Matplotlib also allows for a dizzying amount of customization, so you can create anything from quick-and-easy plots to publication-quality plots.

## Installing matplotlib

Like most of the libraries used in our "special topics" lectures, matplotlib does not come standard with Python and will have to be installed. Please check the official [SciPy Stack Install Guide](http://www.scipy.org/install.html). For Linux and Mac, the installation is merely a single line of `apt-get`. For Windows, pre-built installers are provided.

## Outline

 * [Scatter Plots](https://github.com/theJollySin/python_for_scientists/blob/master/classes/12_matplotlib/lecture_12.md#scatter-plots)
 * [Line Plots](https://github.com/theJollySin/python_for_scientists/blob/master/classes/12_matplotlib/lecture_12.md#line-plots)
 * [Bar Charts](https://github.com/theJollySin/python_for_scientists/blob/master/classes/12_matplotlib/lecture_12.md#bar-charts)
 * [Histograms](https://github.com/theJollySin/python_for_scientists/blob/master/classes/12_matplotlib/lecture_12.md#histograms)
 * [Multiple Plots](https://github.com/theJollySin/python_for_scientists/blob/master/classes/12_matplotlib/lecture_12.md#multiple-plots)
 * [Error Bars](https://github.com/theJollySin/python_for_scientists/blob/master/classes/12_matplotlib/lecture_12.md#error-bars)
 * [Common Customizations](https://github.com/theJollySin/python_for_scientists/blob/master/classes/12_matplotlib/lecture_12.md#common-customizations)

## Scatter Plots

First, let's generate a few random data points:

    from numpy import random
    
    N = 100
    x = random.rand(N)
    y = random.rand(N)

Now, we will use those as X and Y values on a scatter plot:

    import matplotlib.pyplot as plt
    plt.scatter(x, y)
    plt.show()

![Simple Scatter Plot](../../resources/scatter1.png)

That's it! Once you have the data, it's just three lines to create a scatter plot!

#### Customizations

Those three lines are great. But you're going to want the power to control how that plot looks. So for each type of plot in this lecture we will show some customization options.

#### Color

We can change the color of the dots in several ways:

    # all the same
    plt.scatter(x, y, c='red')
    
    # each different
    plt.scatter(x, y, c=np.random.rand(N))

We can use single letters ('r', 'g', 'b', ...), special words ('red', 'green' 'blue', 'none'), or even numbers from 0.0 to 1.0 to represent colors. And we can provide a single color, or a list of them (one for each point). For more information on color options in matplotlib check the [documentation](http://matplotlib.org/api/colors_api.html) or [these examples](http://matplotlib.org/examples/color/named_colors.html).

#### Size

Much like color, we can provide one value for all data points, or one value for each data point:

    # all the same
    plt.scatter(x, y, s=100)
    
    # each different
    plt.scatter(x, y, s=100 * np.random.rand(N))

The `s` values shown are the area of your dot in pixels. So, if you are using circles, your area is: pi * r * r. If you want to get the exact size you want, calculate the area of the dot you want.

#### Alpha

Perhaps you want your dots to be partially transparent, to help see overlapping dots:

    # all the same
    plt.scatter(x, y, alpha=0.5)
    
    # each different
    plt.scatter(x, y, alpha=np.random.rand(N))

Alpha goes from 0.0 (invisible) to 1.0 (not transparent at all).

#### Edge Colors

If you don't want your dot shapes to have those black edges, you can do:

    # all the same
    plt.scatter(x, y, edgecolors='none')

Of course, if you want, you can change the color of your edges using the same terms you used to change the color of the dots:

    # all the same
    plt.scatter(x, y, edgecolors='b')
    
    # each different
    plt.scatter(x, y, edgecolors=np.random.rand(N))

#### Full Example

Here is the simple scatter plot example above, using several customizations:

    # create random data points
    from numpy import random
    N = 100
    x = random.rand(N)
    y = random.rand(N)

    # plot the data
    import matplotlib.pyplot as plt
    plt.scatter(x, y, c=x*y, s=1000*random.rand(N), alpha=0.5, edgecolor='none')
    plt.show()

![Customized Scatter Plot](../../resources/scatter2.png)

## Line Plots

You can use `plot` to take make a line plot out of a series of points:

    # mock up some data
    from numpy import arange, cos
    x = arange(10)
    y = cos(x)
    
    # make a line plot
    import matplotlib.pyplot as plt
    plt.plot(x, y)
    plt.show()

![Simple Line Plot](../../resources/line_plot_1.png)

#### Line Style

Your line can be a solid line, or several kinds of dashed lines:

    # dashed line
    plt.plot(x, y, linestyle='--')
    
    # dashed and dotted line
    plt.plot(x, y, linestyle='-.')
    
    # solid line
    plt.plot(x, y, linestyle='-')
    
    # dotted
    plt.plot(x, y, linestyle=':')

#### Line Width

You can also set the width of your line (in pixels):

    # thin (default) line width
    plt.plot(x, y, linewidth=1)
    
    # very thick line
    plt.plot(x, y, linewidth=5)

#### Line Color

You set line color using the same options you used to set scatter plot color, but now you can only provide one color, not many:

    # red line
    plt.plot(x, y, c='red')
    
    # blue line
    plt.plot(x, y, c='b')
    
    # white line
    plt.plot(x, y, c='white')
    
    # green line
    plt.plot(x, y, c='g')

#### Full Example

And now let's pull it all together. We can make a line plot of chosen color, width, and style:

    # mock up some data
    from numpy import arange, cos
    x = arange(10)
    y = cos(x)
    
    # make a line plot
    import matplotlib.pyplot as plt
    plt.plot(x, y, linestyle='-.', linewidth=10, c='red')
    plt.show()

![Fancish Line Plot](../../resources/line_plot_2.png)

## Bar Charts

You can use `bar` to create vertical bar chart:

    >>> import numpy as np
    >>> N = 20
    >>> x = np.arange(N)
    >>> y = np.random.randint(1, 100, N)
    >>> 
    >>> from matplotlib import pyplot as plt
    >>> plt.bar(x, y)
    >>> plt.show()

![Simple Vertical Bar Chart](../../resources/bar_plot_simple_1.png)

Or `barh` to create a horizontal bar chart:

    >>> plt.bar(x, y)
    >>> plt.show()

![Simple Horizontal Bar Chart](../../resources/barh_plot_simple_1.png)

#### Color and Alpha

As before, you can use `color` and `alpha` keywords to set the color and transparency of your bars.

#### Align

Use the `align` keyword to orient your bars in relation to the values they represent. You have to options:

    # align bars so left edge is on their values (default)
    plt.bar(x, y, align='edge')
    
    # align bars so they are centers on their values
    plt.bar(x, y, align='center')

#### Edgecolor

Use the `edgecolor` keyword to set the outline color of your bars.

    # set no outline
    plt.barh(x, y, edgecolor='none')
    
    # set outline color to blue
    plt.barh(x, y, edgecolor='blue')

#### Width

Use `width` to make the bars wider or thinner. You can set the width of them as you want. But if your width is greater than the spacing of your bars, they will overlap.

    # bars just barely touch
    plt.bar(x, y, width=1.0)
    
    # bars are far apart
    plt.bar(x, y, width=0.5)

#### Log

Use `log=True` if you want your bar chart to be logarithmic along the Y-axis. The default is `log=False`.

#### Bottom: Stacked Bar Charts

Use `bottom` to shift offset a set of bars up above the X-axis. This will allow you to plot multiple bars in a multiple bar chart:

    >>> from numpy import array
    >>> x = array([1, 2, 3, 4, 5])
    >>> y1 = array([2, 3, 4, 6, 4])
    >>> y2 = array([7, 5, 4, 6, 8])
    >>> 
    >>> from matplotlib import pyplot as plt
    >>> plt.bar(x, y1, color='b')
    >>> plt.bar(x, y2, color='r', bottom=y1)
    >>> plt.show()

#### Full Example

Let's put it all together and make a stacked bar chart with custom colors and widths.

    import numpy as np
    N = 10
    x = numpy.arange(N)
    y1 = np.random.randint(1, 30, N)
    y2 = np.random.randint(1, 10, N)
    y3 = np.random.randint(1, 20, N)

    from matplotlib import pyplot as plt
    plt.bar(x, y1, color='r', edgecolor='none', width=0.9)
    plt.bar(x, y2, color='g', edgecolor='none', width=0.9, bottom=y1)
    plt.bar(x, y3, color='b', edgecolor='none', width=0.9, bottom=y1+y2)
    plt.show()

![Stack Bar Chart](../../resources/bar_plot_fancy_1.png)

## Histograms

 * Coming Soon

You can `hist` to create a histogram:

    plt.hist(x, 10)

## Multiple Data Set - One Plot

 * Coming Soon

## Multiple Plots - One Image

 * Coming Soon

## Error Bars

 * Coming Soon

## Common Customizations

 * Coming Soon
 * Coming Soon: Legend
 * Coming Soon: Grid
 * Coming Soon: Axis min, max, and Labels
 * Coming Soon: Title
 * Coming Soon: Save it to a file


## Further Reading

Matplotlib is a powerful tool. But there are so many options for different ways to plot things remembering all of them would be a pain. So I cheat. [Here](http://matplotlib.org/gallery.html) is the cheat sheet: a wonderful collection of matplotlib examples.

 * [matplotlib gallery](http://matplotlib.org/gallery.html)
 * [matplotlib color docs](http://matplotlib.org/api/colors_api.html)
 * [matplotlib color examples](http://matplotlib.org/examples/color/named_colors.html)


[Back to Syllabus](../../README.md)
