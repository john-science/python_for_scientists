# Data Analysis with Pandas

## Installation

Like most of the libraries used in our "special topics" lectures, pandas does not come standard with Python and will have to be installed. Please check the official [SciPy Stack Install Guide](http://www.scipy.org/install.html). For Linux and Mac, the installation is merely a single line of `apt-get`. For Windows, pre-built installers are provided.

#### Anaconda

Consider installing [Anaconda](http://docs.continuum.io/anaconda/install.html) instead. Anaconda is Python packaged with over 100 tools and libraries that you will want (This includes Pandas and everything else we will use in this course.)

## Intro to pandas

#### Why use pandas?

pandas is a powerful tool for handling data structures and performing data analysis. It can accomplish the same tasks you would typically do in Microsoft Excel (sort, filter, pivot, etc.), but unlike Excel, pandas can be used in Python programs to streamline repetitive tasks and allow reusability of code.

Additionally, it can perform the same tasks that you would typically do in a database, like SQL (queries, joins, etc.), but it does so in Python memory (no need to establish and connect to a database!).

Lastly, many pandas functions are based off of other popular Python utilities (numpy, scipy, etc.).

## iPython

When importing pandas into the Python interpreter for on-the-fly programming and debugging, I would recommend using iPython over the standard Python interpreter. It is basically a more advanced version with additional features.
 * Tab auto-completion (on class names, functions, methods, variables)
 * More explicit and colour-highlighted error messages
 * Better history management
 * Basic UNIX shell integration (you can run simple shell commands such as cp, ls, rm, cp, etc. directly from the iPython command line)

After installing iPython, invoke it using the command "ipython"

    >>>> ipython
    Python 2.6.6 (r266:84292, Jan 22 2014, 09:42:36)
    Type "copyright", "credits" or "license" for more information.
    
    IPython 0.13.2 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

## Importing pandas

Like importing other Python libraries, importing pandas is quite simple.

    In [1]: import pandas as pd

## Reading Files

Before getting into how to build dataframes and other data structures in pandas, let's cover reading in pre-existing data. This will likely be the most common way of getting data into the pandas data structure for manipulation using pandas. In other words, you're less likely to build pandas data structues from scratch, as there are other more useful Python tools to accomplish that.

Common types:
 * read_csv (comma separated values)
 * read_fwf (fixed width format)
 * read_table (general delimited text file)
 * read_pickle (preserved pandas data structure)

#### Other data formats

For more information on reading in other data formats (Excel spreadsheets, SQL databases, etc.), you can refer to the pandas manual:

http://pandas.pydata.org/pandas-docs/stable/api.html#flat-file

## Data Frames and Data Sets

 * Coming Soon

## Reshaping a Data Set

 * Coming Soon

## Slicing a Data Set

**Tip: access columns identified by column names in all caps.**

**Why? If a column header is read in from a file rather than defined explicitly by the user, there's no telling what kind of case is used.**

Trying this should fail if the cases don't match perfectly:

    In [4]: df['FIRST_NAME']
    KeyError: u'no item named FIRST_NAME'
    
Or trying this as well:

    In [5]: df.loc[:,'FIRST_NAME']
    KeyError: 'the label [FIRST_NAME] is not in the [columns]'
 
So we look at what the column headers do look like and find some craziness:

    In [6]: df.columns
    Out[6]:
    Index([u'first_name', u'LAST_NAME', u'gender', u'Age', u'Hair_COLOR', u'eye_Color'], dtype='object')
    
Luckily, there's an easy fix:

    In [7]: df.columns = [x.upper() for x in df.columns]
    In [8]: df.columns
    Out[8]: 
    ['FIRST_NAME', 'LAST_NAME', 'GENDER', 'AGE', 'HAIR_COLOR', 'EYE_COLOR']
    
Now when we try to look up the first names:

    In [9]: df['FIRST_NAME']
    Out[9]: 
    0     Jennifer
    1        Jaime
    2      Michael
    3         Mary
    4       Robert
    5       Thomas
    6      Natalie
    7       Brenda
    8      Michael
    9     Jennifer
    10     Michael
    11     Jessica
    12       Molly
    13       Jaime
    Name: FIRST_NAME, dtype: object
    
Or the second way:
    
    In [10]: df.loc[:,'FIRST_NAME']
    Out[10]: 
    0     Jennifer
    1        Jaime
    2      Michael
    3         Mary
    4       Robert
    5       Thomas
    6      Natalie
    7       Brenda
    8      Michael
    9     Jennifer
    10     Michael
    11     Jessica
    12       Molly
    13       Jaime
    Name: FIRST_NAME, dtype: object

## Handling Missing Data

 * Coming Soon

## Time-Series Data

 * Coming Soon

## Writing Files

 * Coming Soon


## Further Reading

 * [Installing Pandas](http://pandas.pydata.org/pandas-docs/stable/install.html)
 * [Official Panadas Tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html)
 * [Python & Pandas Top 10](http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/)


[Back to Syllabus](../../README.md)
