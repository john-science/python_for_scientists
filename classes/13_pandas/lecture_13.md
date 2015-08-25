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

After installing iPython, invoke it using the command `ipython`.

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

#### Common data formats

 * read_csv (comma separated values)
 * read_fwf (fixed width format)
 * read_table (general delimited text file)
 * read_pickle (preserved pandas data structure)

In most cases, all you need to provide as an argument is the filepath. Each type has its own variety of optional arguments, and we'll touch briefly on a few useful ones.

  * header (int): If not given, pandas will use row 0 as the header line and the start of the data. This is useful if your file has a header/comment block and the data starts several lines down. If your file has no header, set `header=None` to avoid having the first line used at the header.
  
  * names (list): Use if you would like to define the column names upon importing the data. This should be used with the explicit option `header=None`.
 
  * dtype (dict): If not given, pandas will infer the data types when importing data. This option is useful if you want to force certain data types at the import stage (note that typecasting can be done after the data has been imported into pandas as well). Ex. `dtype={'x':np.float64, 'y':np.int32, 'z':np.float64}`

  * usecols (list): Import only certain columns. Saves time and space!
 
  * nrows (int): Number of rows of file to read. Useful for reading pieces of large files.
  
  * skiprows (list or integer): List of line numbers to skip (0-indexed) or number of lines to skip (int) at the start of the file.
  
#### Other data formats

For more information on reading in other data formats (Excel spreadsheets, SQL databases, etc.), you can refer to the pandas manual:

http://pandas.pydata.org/pandas-docs/stable/api.html#input-output

## Series

Though the focus of this course will mainly be on pandas dataframes, knowing a bit about pandas series is useful. Series are simply one-dimensional arrays of data with axis labels (indices). Series can be created from scratch using a dictionary or a list.

**From a dictionary**

    In [1]: d = {'a':'A','b':'B','c':'C'}
    In [2]: pd.Series(d)
    Out[2]: 
    a    A
    b    B
    c    C
    dtype: object
    
**From a list**
    
    In [3]: l = ['A','B','C']
    In [4]: pd.Series(l)
    Out[4]: 
    0    A
    1    B
    2    C
    dtype: object
    
Series can also be extracted from multi-dimensional data structures like dataframes.

    In [5]: df.LAST_NAME
    Out[5]: 
    0        Jones
    1      Roberts
    2      Johnson
    3        Adams
    4     Phillips
    5        Moore
    6       Potter
    7        Jones
    8        Smith
    9        Smith
    10       Smith
    11      Rabbit
    12      Bryant
    13    Anderson
    Name: LAST_NAME, dtype: object

    In [6]: type(df.LAST_NAME)
    Out[6]: pandas.core.series.Series

## Data Frames and Data Sets

Dataframes are the multi-dimensional version of the pandas series. However, a dataframe can be one-dimension (one row, one column, or both) so long as the data is imported as a dataframe.

**Data imported as a series**

    In [4]: l = ['A','B','C']
    
    In [5]: pd.Series(l)
    Out[5]: 
    0    A
    1    B
    2    C
    dtype: object

**Data imported as a dataframe**

    In [6]: pd.DataFrame(l)

    Out[6]: 
       0
    0  A
    1  B
    2  C

Notice the column header `0` above the column of data? Other than that, importing one-dimensional data as a dataframe is pretty much the same as importing it as a series. Feel free to rename that column of data. However, importing the data as a dataframe opens the door for other practices, like appending the data column-wise or row-wise to another dataframe, or using it as a table for performing merges (pandas equivalent to an SQL join).

Again, you're less likely to build pandas dataframes from scratch and will more likely import existing data using one of the `read_` functions. But for those itching to build their own dataframes, there are a few ways to do so.

#### From a dictionary of arrays

    In [6]: d = dict( ("x"+str(k+1), np.random.randn(7)) for k in range(5) )  # 7 rows by 5 columns
    In [7]: df = pd.DataFrame(d)
    Out[7]: 
             x1        x2        x3        x4        x5
    0 -1.517961  1.275236 -0.186226 -0.331491  2.396869
    1  3.468361 -1.397977 -0.883015 -0.078715  0.743549
    2  1.286010 -1.446566 -0.643641  0.717790  0.747485
    3  0.252657 -0.247126  0.090866  1.435567 -0.495681
    4  0.903237 -0.413400 -0.754602  0.597491 -0.198482
    5 -0.274422 -0.315801  1.312623  3.297479  1.335182
    6 -0.875649  2.542598  0.051351  0.252638  1.541355

#### From a numpy ndarray

    In [8]: d = np.random.rand(7,5)  # 7 rows by 5 columns
    In [9]: df = pd.DataFrame(d)
    Out[9]: 
              0         1         2         3         4
    0  0.966545  0.387958  0.175133  0.194291  0.224350
    1  0.571877  0.382613  0.646535  0.836982  0.643568
    2  0.941696  0.806954  0.006444  0.267016  0.545472
    3  0.378179  0.105150  0.194698  0.052711  0.025345
    4  0.259918  0.765968  0.012413  0.107861  0.369962
    5  0.794492  0.524574  0.800396  0.918925  0.047937
    6  0.115055  0.458574  0.847663  0.442791  0.537918
    
#### From a dict of series

    In [1]: l1 = ['a','b','c']  # list 1
    In [2]: l2 = ['X','Y','Z']  # list 2
    In [3]: l3 = [1,2,3]        # list 3
    In [4]: l4 = [6,5,4]        # list 4
    In [5]: d = {'l1':pd.Series(l1), 'l2':pd.Series(l2), 'l3':pd.Series(l3), 'l4':pd.Series(l4)}  # dictionary of series
    In [6]: pd.DataFrame(d)
    Out[6]: 
      l1 l2  l3  l4
    0  a  X   1   6
    1  b  Y   2   5
    2  c  Z   3   4
    
**Of course the data can be comprised of other data types, not just random floats. I would recommend dusting off your numpy and dictionary/list skills learned in previous lessons and build your own arrays/series of varying data types.**

## Slicing a Data Set

#### First, why we want column names in all caps

If a column header is read in from a file rather than defined explicitly by the user, there's no telling what kind of case is used.

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
    
Now that we've gotten the columns taken care of, we can go into how to select data in a dataframe.

#### By column only

    In [4]: cols = ['FIRST_NAME','LAST_NAME']
    In [5]: df[col]
    Out[5]: 
    FIRST_NAME LAST_NAME
    0    Jennifer     Jones
    1       Jaime   Roberts
    2     Michael   Johnson
    3        Mary     Adams
    4      Robert  Phillips
    5      Thomas     Moore
    6     Natalie    Potter
    7      Brenda     Jones
    8     Michael     Smith
    9    Jennifer     Smith
    10    Michael     Smith
    11    Jessica    Rabbit
    12      Molly    Bryant
    13      Jaime  Anderson
    
Using `df[['FIRST_NAME','LAST_NAME']]` accomplishes the same thing.

So does `df.loc[:,cols]` --> we'll go into more detail about this method later.
    
#### By row only

**Like list slicing**

    In [10]: df[:5]
    Out[10]: 
    FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    0   Jennifer     Jones      F   27      black     brown
    1      Jaime   Roberts      M   32      brown     hazel
    2    Michael   Johnson      M   55        red     green
    3       Mary     Adams      F   42     blonde      blue
    4     Robert  Phillips      M   37     blonde     brown 
    
    In [11]: df[5:]
    Out[11]: 
    FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    5      Thomas     Moore      M   60      brown      blue
    6     Natalie    Potter      F   21      brown     green
    7      Brenda     Jones      F   18     blonde     brown
    8     Michael     Smith      M   58      brown     brown
    9    Jennifer     Smith      F   36      black     brown
    10    Michael     Smith      M   37      black     hazel
    11    Jessica    Rabbit      F   19      black      blue
    12      Molly    Bryant      F   21      brown      blue
    13      Jaime  Anderson      F   46      brown     green

Other alternate methods are `df.loc[:5,:]` and `df.loc[5:,:]`
    
#### By row and column

The `loc` function is my preferred tool for row and column-wise slicing of dataframes. The format for using `loc` is `df.loc[row_indexer, column_indexer]`. Below is a simple example for combining row and column slicing.

    In [6]: df.loc[3:8,['FIRST_NAME','AGE','EYE_COLOR']]
    Out[6]: 
    FIRST_NAME  AGE EYE_COLOR
    3       Mary   42      blue
    4     Robert   37     brown
    5     Thomas   60      blue
    6    Natalie   21     green
    7     Brenda   18     brown
    8    Michael   58     brown

We'll cover more of the `loc` function when we discuss query-like selection of data.

## Returning a view versus a copy

The previous slice can be accomplished the following way:

    df[3:8][['FIRST_NAME','AGE','EYE_COLOR']]
    
This is called chained indexing. In the example above, the rows are sliced first, then the columns. While it does not pose a problem when selecting subsets of a dataframe, it becomes problematic when you want to set the values of this subset (e.g. replacing erroneous data). This has something to do with how pandas performs operations and the order in which they are performed. That being said, the preferred way of combination indexing is the `loc` function, whether it's actually used to set values in a dataframe subset or used simply to view the subset of data.

More information about the dangers of chained indexing can be found in the pandas manual:
http://pandas.pydata.org/pandas-docs/stable/indexing.html#returning-a-view-versus-a-copy

## Useful Dataframe Tools

#### Dropping columns

    df = df.drop(['HAIR_COLOR','EYE_COLOR'], axis=1)
    df.drop(['HAIR_COLOR','EYE_COLOR'], axis=1, inplace=True)  # alternate way
    
#### Resetting indices

This becomes useful when you've saved a subset of a dataframe and wish to sequentially reassign the indices.

    df = df.reset_index(drop=True)
    df.reset_index(drop=True, inplace=True)  # alternate way
    
#### Dropping duplicate entries

This becomes useful when you're dealing with data that you know should have unique entries.

    df = df.drop_duplicates()
    df.drop_duplicates(inplace=True)

It's also good for getting unique combinations of a subset of data.

    In [12]: df[['EYE_COLOR','HAIR_COLOR']].drop_duplicates()
    Out[12]: 
    EYE_COLOR HAIR_COLOR
    0      brown      black
    1      hazel      brown
    2      green        red
    3       blue     blonde
    4      brown     blonde
    5       blue      brown
    6      green      brown
    8      brown      brown
    10     hazel      black
    11      blue      black

Notice the missing indices? That's how you know some rows were dropped, which were duplicates. If the subset is to be saved for later use, it would be a good idea to reset the indices again.






## Querying Data

## Handling Missing Data

## More Dataframe Operations

## Writing Files

#### Common data formats

 * to_csv (comma separated values)
 * to_pickle (preserved pandas data structure)

#### Other data formats

Again, for more information on writing to other data formats, consult the pandas manual:

http://pandas.pydata.org/pandas-docs/stable/api.html#serialization-io-conversion

## Further Reading

 * [Installing Pandas](http://pandas.pydata.org/pandas-docs/stable/install.html)
 * [Official Panadas Tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html)
 * [Python & Pandas Top 10](http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/)


[Back to Syllabus](../../README.md)
