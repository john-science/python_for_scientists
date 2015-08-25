# Data Analysis with Pandas

 * Coming Soon

## Installation

Like most of the libraries used in our "special topics" lectures, Pandas does not come standard with Python and will have to be installed. Please check the official [SciPy Stack Install Guide](http://www.scipy.org/install.html). For Linux and Mac, the installation is merely a single line of `apt-get`. For Windows, pre-built installers are provided.

#### Anaconda

Consider installing [Anaconda](http://docs.continuum.io/anaconda/install.html) instead. Anaconda is Python packaged with over 100 tools and libraries that you will want (This includes Pandas and everything else we will use in this course.)

## Intro to pandas

#### Why use pandas?

pandas is a powerful tool for handling data structures and performing data analysis. It can accomplish the same tasks you would typically do in Microsoft Excel (sort, filter, pivot, etc.), but unlike Excel, pandas can be used in Python programs to streamline repeitive tasks and allow reusability of code. Additionally, it can perform the same tasks that you would typically do in a database (like SQL), but it does so in Python memory (no need to establish and connect to a database!).

## Reading Files

Before getting into how to build databases and other data structures in pandas, let's cover reading in pre-existing data. This will likely be the most common way of getting data into the pandas data structure for manipulation using pandas. In other words, you're less likely to build pandas data structues from scratch, as there are other more useful Python tools to accomplish that.

#### read_csv (comma separated values)

#### read_fwf (fixed width format)

#### read_table (general delimited text file)

#### read_pickle (preserved pandas data structure)

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

    >>> df['FIRST_NAME']
    KeyError: u'no item named FIRST_NAME'
    
Or trying this as well:
    
    >>> df.loc[:,'FIRST_NAME']
    KeyError: 'the label [FIRST_NAME] is not in the [columns]'
 
So we look at what the column headers do look like and find some craziness:

    >>> df.columns
    Index([u'first_name', u'LAST_NAME', u'gender', u'Age', u'Hair_COLOR', u'eye_Color'], dtype='object')
    
Luckily, there's an easy fix:

    >>> df.columns = [x.upper() for x in df.columns]
    >>> df.columns
    ['FIRST_NAME', 'LAST_NAME', 'GENDER', 'AGE', 'HAIR_COLOR', 'EYE_COLOR']
    
    >>> df['FIRST_NAME']
    * PUT RESULT OF PRINTED DATAFRAME
    
    >>> df.loc[:,'FIRST_NAME']
    * PUT RESULT OF PRINTED DATAFRAME

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
