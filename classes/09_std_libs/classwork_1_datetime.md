# A Longer datetime Example

## The Birthday Problem

### The Problem Setup

I have a terrible memory. And so I am terrible at remembering everyone's birthdays. There are so many. And if I suddenly remember my Mom's birthday is tomorrow, it's too late to send her a present.

I have solved this little problem in my life using Python

I wrote a script that I run a couple times a week tell me who's birthday is coming up. This script is a very simple little example of the Python `datetime` library.

### Your Goal

Write a script that includes a hard-code dictionary of people's names and birthdates, and:

1. Calculates the age in years of each person
2. Calculates the number of days until their next birthday
3. Prints the results, with upcoming birthdays first

### Things you might need to know:

You can define a `datetime` in Python by writing:

    >>> from datetime import datetime
    >>> d = datetime(2001, 12, 31)  # year, month, day
    >>> print(d)
    2012-12-31
    >>> very_specific = datetime(2012, 12, 31, 5, 26, 17, 1236)
    >>> print(very_specific)
    2012-12-31 05:26:17.001236

You can find the difference between two datetimes by just using the `-` operator, just like they were numbers:

    >>> diff = datetime(2012, 2, 11) - datetime(2001, 12, 31)
    >>> diff
    datetime.timedelta(3694)
    >>> diff.days
    3694
    >>> diff.seconds
    0
    >>> diff_years = (diff.days + diff.seconds / 86400.0) / 365.2425
    >>> diff_years
    10.113828483815547

If you want to deal directly with the difference between two `datetime` objects, you can use a `timedelta` object:

    >>> from datetime import datetime,timedelta
    >>> d = datetime.today()  # This is todays date
    >>> d
    datetime.datetime(2015, 2, 16, 11, 14, 43, 180182)
    >>> diff = timedelta(days=1)
    >>> diff
    datetime.timedelta(1)
    >>> tomorrow = d + diff
    >>> tomorrow
    datetime.datetime(2015, 2, 17, 11, 14, 43, 180182)

You may also want to remember that you can get the keys and values from a dictionary by typing:

    >>> halflives = {'U238': 4.468E9, 'U239': 4.46E-5,
    ...              'Pu239': 2.41E4, 'Fe54': 3.1E22,
    ...              'K40': 1.238E9}
    >>> halflives.keys()
    ['U238', 'U239', 'K40', 'FE54', 'PU239']
    >>> halflives.values()
    [4468000000.0, 4.46e-05, 1238000000.0, 3.1e+22, 24100.0]

And maybe it will be helpful to wrong that you can sort the values of a list by doing:

    >>> lst = [1,3,7,3,5,2,9,0,999]
    >>> sorted(lst)
    [0, 1, 2, 3, 3, 5, 7, 9, 999]
    >>> sorted(lst, reverse=True)
    [999, 9, 7, 5, 3, 3, 2, 1, 0]


### The Solution

    from datetime import datetime

    # Hand-Entered Birthday List (this could also be read from an input file)
    bdays = {'Dad':        datetime(1958, 1, 9),
             'Wife':       datetime(1985, 2, 2),
             'Grandma1':   datetime(1920, 11, 17),
             'Grandpa2':   datetime(1932, 4, 14),
             'Grandma2':   datetime(1940, 6, 4),
             'Sister':     datetime(1974, 6, 6),
             'Neice':      datetime(2012, 8, 8),
             'Mom':        datetime(1960, 7, 17),
             'Friend1':    datetime(1974, 9, 19),
             'Friend2':    datetime(1980, 10, 14),
             'Friend3':    datetime(1965, 8, 8),
             'Aunt1':      datetime(1962, 6, 25),
             'Aunt2':      datetime(1962, 7, 24),
             'SisterNLaw': datetime(1990, 5, 5)}

    # place to save my output results
    out = {}

    # loop through the people in my life
    for bday in bdays:
        # find today's date
        today = datetime.now()
        # calc number of years from birth
        diff = today - bdays[bday]
        diff_years = (diff.days + diff.seconds / 86400.0) / 365.2425
        
        # calc number of days to next bday
        next_bday = datetime(today.year, bdays[bday].month, bdays[bday].day)
        if next_bday >= today:
            days_left = (next_bday - today).days
        else:
            next_bday = datetime(today.year + 1, bdays[bday].month, bdays[bday].day)
            days_left = (next_bday - today).days
        
        # format the output line for printing
        line = bday.ljust(10) + ":\t" + \
               str(bdays[bday].strftime('%Y-%m-%d')) + "\t\t" + \
               str(round(diff_years, 3)) + "\t\t" + \
               str(days_left)
        
        # add output line to output dictionary
        out[days_left] = line

    # sort and print the results dictionary
    people = out.keys()

    # print results to screen
    print("\nPerson    :\tBirthday\t\tYears\t\tDays to Next")
    for key in sorted(people):
        print(out[key])
