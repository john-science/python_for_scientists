# Batteries Included, Part 1

![Python](https://imgs.xkcd.com/comics/python.png)

Batteries Included. That's the Python motto. Python comes with a huge collection of [standard libraries](http://en.wikipedia.org/wiki/Standard_library). Standard libraries are packages of code that come with Python to help you solve common tasks. Why reinvent the wheel every time?

What follows is a selection of handy tools from Python's standard libraries. For a full list of the Python standard libraries check here: [Python 2](https://docs.python.org/2/library/) / [Python 3](https://docs.python.org/3/library/).

## datetime

#### datetime.datetime

Frequently, we will need to deal with dates. First, let's just define a date for June 17, 2015:

    >>> import datetime
    >>> start = datetime.datetime(2015, 6, 17)
    >>> print(start)
    2015-06-17 00:00:00

Now let's define a datetime object for a date and time 6:30 PM on July 17, 2015:

    >>> from datetime import datetime
    >>> end = datetime(2015, 7, 17, 18, 30)
    >>> print(end)
    2015-07-17 18:30:00

If you have a pre-existing `datetime` object, you can pull the individual pieces of information out of it pretty easily:

    >>> end = datetime(2015, 7, 17, 18, 30)
    >>> end.year
    2015
    >>> end.month
    7
    >>> end.day
    17
    >>> end.hour
    18
    >>> end.minute
    30
    >>> end.second
    0

We can even use the standard comparison operators compare the two dates:

    >>> start < end
    True
    >>> start > end
    False
    >>> start <= end
    True
    >>> start >= end
    False
    >>> start == end
    False
    >>> start != end
    True

#### datetime.timedelta

Now let's use a `for` loop and a `timedelta` to print out ever day of Ramadan (2015):

    >>> day = start
    >>> while day < end:
    ...     print(day)
    ...     day += datetime.timedelta(days=1)
    2015-06-17 00:00:00
    2015-06-18 00:00:00
    2015-06-19 00:00:00
    ...
    2015-07-17 00:00:00

If you do a `help(datetime.timedelta)`, you will find out that we can set up a `timedelta` in units of: days, seconds, or microseconds.

#### datetime.strftime

Now, that loop above is a pretty good start, but those print outs are a little ugly. I'd like it if they were formatted more like `June 17, 2015`. To do this, we use the `strftime` function:

    >>> start.strftime('%b %d, %Y')
    'Jun 17, 2015'

OR we could format the dates in the a more computer-friendly format:

    >>> end.strftime('%Y-%m-%d')
    '2015-07-17'

This is the ISO 8601 format and it is ideal for working with computers. Notice that if you alphabetize a list of these strings, the dates will be in chronological order.

![ISO 8601 date formatting](https://imgs.xkcd.com/comics/iso_8601.png)

That `strftime` looks really useful. You can find a complete listing of all of the datetime formatting codes [here](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior).

#### datetime.strptime

There's actually one more Really useful thing we can do with these date formmating strings. Imagine we are reading in a text file and we hit a bunch of text that is meant to represent dates and times. We can use `strptime` to create a `datetime` object from a string:

    >>> from datetime import datetime
    >>> some_text = '2015-03-14'
    >>> d = datetime.strptime(some_text, '%Y-%m-%d')
    >>> print(d)
    datetime.datetime(2015, 3, 14, 0, 0)

## Math

The `math` library has all kinds of things built in.

## Random

![random](http://imgs.xkcd.com/comics/random_number.png)

 * Coming Soon

## itertools

 * Coming Soon

## Copy

 * Coming Soon

## Problem Sets

 * Coming Soon

## Further Reading

 * Official Docs - datetime: ([Python 2](https://docs.python.org/2/library/datetime.html) / [Python 3](https://docs.python.org/3/library/datetime.html))
 * Official Docs - strftime: ([Python 2](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior) / [Python 3](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior))
 * [effbot - datetime](http://www.effbot.org/librarybook/datetime.htm)
 * Official Docs - os: ([Python 2](https://docs.python.org/2/library/os.html) / [Python 3](https://docs.python.org/3/library/os.html))
 * [effbot - os](http://www.effbot.org/librarybook/os.htm)
 * Official Docs - os.path: ([Python 2](https://docs.python.org/2/library/os.path.html#module-os.path) / [Python 3](https://docs.python.org/3/library/os.path.html#module-os.path))
 * [effbot - os.path](http://www.effbot.org/librarybook/os-path.htm)
 * Official Docs - sys: ([Python 2](https://docs.python.org/2/library/sys.html) / [Python 3](https://docs.python.org/3/library/sys.html))
 * [effbot - sys](http://www.effbot.org/librarybook/sys.htm)


[Back to Syllabus](../../README.md)
