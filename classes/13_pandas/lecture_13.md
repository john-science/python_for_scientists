# Data Analysis with Pandas

## Installation

Like most of the libraries used in our "special topics" lectures, pandas does not come standard with Python and will have to be installed. Please check the official [SciPy Stack Install Guide](http://www.scipy.org/install.html). For Linux and Mac, the installation is merely a single line of `apt-get`. For Windows, pre-built installers are provided.

#### Anaconda

Consider installing [Anaconda](http://docs.continuum.io/anaconda/install.html) instead. Anaconda is Python packaged with hundreds of libraries that you will want (including Pandas and almost everything else we will use in this course.)

## Intro to pandas

#### Why use pandas?

pandas is a powerful tool for handling data and performing data analysis. It can accomplish the same tasks you would typically do in Microsoft Excel (sort, filter, pivot, etc.), but unlike Excel, pandas can be used in Python programs to streamline repetitive tasks and allow reusability of code. Additionally, it can perform the same tasks that you would typically do in a database, like SQL (queries, joins, etc.), but it does so in Python memory (no need to establish and connect to a database!).

Lastly, many pandas functions are based off of other popular Python utilities (numpy, scipy, etc.).

## iPython

When importing pandas into the Python interpreter for on-the-fly programming and debugging, consider using iPython. It has several features not available in the standard Python interpreter:

 * Tab auto-completion (on class names, functions, methods, and variables)
 * More explicit and colour-highlighted error messages
 * Better history management
 * Basic UNIX shell integration (you can run simple shell commands: cp, ls, rm, cp, etc.)

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

There is convention of types to help save you typing when using pandas:

    In [1]: import pandas as pd

## Reading Files

A good place to start is reading pre-existing data with pandas. You may find that this is more common than building a pandas data structure from scratch.

#### Common data formats

There are four methods to read in different types of data:

 * `read_csv` - comma separated values
 * `read_fwf` - fixed width format
 * `read_table` - general delimited text file
 * `read_pickle` - preserved pandas data structure

Each of these methods can be passed a file path (string), and they will run. But the also a variety of optional arguments:

  * **header (int)**: If not given, pandas will use row 0 as the header line and the start of the data. This is useful if your file has a header/comment block and the data starts several lines down. If your file has no header, set `header=None` to avoid having the first line used at the header.
  
  * **names (list)**: Use if you would like to define the column names upon importing the data. This should be used with the explicit option `header=None`.
 
  * **dtype (dict)**: If not given, pandas will infer the data types when importing data. This option is useful if you want to force certain data types at the import stage, for example: `dtype={'x': np.float64, 'y': np.int32, 'z': np.float64}`.  (Note that pandas allows typecasting after importing into pandas as well).

  * **usecols (list)**: Import only certain columns. Saves time and space!
 
  * **nrows (int)**: Number of rows of file to read. Useful for reading pieces of large files.
  
  * **skiprows (list or integer)**: List of line numbers to skip (0-indexed) or number of lines to skip (int) at the start of the file.
  
#### Other data formats

For more information on reading in other data formats (Excel spreadsheets, SQL databases, etc.), refer to the [pandas manual](http://pandas.pydata.org/pandas-docs/stable/api.html#input-output).

## Series

Though the focus of this lecture will mainly be on pandas `DataFrame`, knowing a bit about pandas `Series` is useful. Series are simply one-dimensional arrays of data with axis labels (indices). Series can be created from scratch using a dictionary or a list.

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

DataFrames are like Series, but they can be multi-dimensional version of the pandas Series. Let's convert a Series into a DataFrame and look at the difference:

**Data imported as a series**

    In [4]: one = ['A','B','C']
    
    In [5]: pd.Series(one)
    Out[5]: 
    0    A
    1    B
    2    C
    dtype: object

**Data imported as a dataframe**

    In [6]: pd.DataFrame(one)

    Out[6]: 
       0
    0  A
    1  B
    2  C

Notice the column header `0` above the column of data? Other than that, importing one-dimensional data as a dataframe is pretty much the same as importing it as a series. Feel free to rename that column of data. However, importing the data as a dataframe opens the door for other options, like appending the data column-wise or row-wise to another dataframe, or using it as a table for performing merges (pandas equivalent to an SQL join).

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
    In [5]: d = {'l1':pd.Series(l1), 'l2':pd.Series(l2), 'l3':pd.Series(l3), 'l4':pd.Series(l4)}
    In [6]: pd.DataFrame(d)
    Out[6]: 
      l1 l2  l3  l4
    0  a  X   1   6
    1  b  Y   2   5
    2  c  Z   3   4
    
Of course, the data can be comprised of other data types, not just `float`. I would recommend dusting off your numpy and dictionary/list skills learned in previous lessons and build your own arrays/series of varying data types.

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

Slicing by row looks a lot like list slicing:

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
    
This is called chained indexing. In the example above, the rows are sliced first, then the columns. While it does not pose a problem when selecting subsets of a dataframe, it becomes problematic when you want to set the values of this subset (e.g. replacing erroneous data). That being said, the preferred way of combination indexing is the `loc` function, whether it's actually used to set values in a dataframe subset or used simply to view the subset of data.

More information about the dangers of chained indexing can be found in the [pandas manual](http://pandas.pydata.org/pandas-docs/stable/indexing.html#returning-a-view-versus-a-copy).

## Useful Dataframe Tools

#### Dropping columns

There are two ways to drop data from a dataframe, one if you want the data returned and the other if not:

    df = df.drop(['HAIR_COLOR','EYE_COLOR'], axis=1)
    df.drop(['HAIR_COLOR','EYE_COLOR'], axis=1, inplace=True)  # alternate way
    
#### Resetting indices

This becomes useful when you've saved a subset of a dataframe and wish to sequentially reassign the indices.

    df = df.reset_index(drop=True)
    df.reset_index(drop=True, inplace=True)  # alternate way
    
#### Dropping duplicate entries

This is useful when you're dealing with data that should have unique entries.

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

Alternately, you can do the same with a single column of data (that is, it can only be performed on series).

    In [13]: df['HAIR_COLOR'].unique()
    Out[13]: array(['black', 'brown', 'red', 'blonde'], dtype=object)

    In [14]: df['HAIR_COLOR'].unique().tolist()
    Out[14]: ['black', 'brown', 'red', 'blonde']

## Querying Data

Having the ability to query data and extract subsets of data with ease is one of the many things that makes pandas so powerful. We will cover some basic skills and functions for subsetting pandas dataframes.

#### Null Data

Sometimes you'll need to identify null values in your data.

    In [3]: df
    Out[3]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    0    Jennifer     Jones      F   27      black     brown
    1       Jaime   Roberts      M   32      brown     hazel
    2     Michael   Johnson      M   55        red     green
    3        Mary       NaN      F   42     blonde       NaN
    4         NaN  Phillips      M   37        NaN     brown
    5      Thomas     Moore      M   60      brown      blue
    6     Natalie    Potter      F  NaN      brown     green
    7      Brenda     Jones      F  NaN        NaN     brown
    8     Michael     Smith    NaN   58      brown     brown
    9    Jennifer     Smith      F   36      black     brown
    10    Michael     Smith      M   37      black     hazel
    11    Jessica       NaN      F   19      black      blue
    12      Molly    Bryant      F   21      brown      blue
    13      Jaime  Anderson      F   46      brown     green
    
To find all rows with any null values:

    In [4]: df[pd.isnull(df).any(axis=1)]
    Out[4]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    3        Mary       NaN      F   42     blonde       NaN
    4         NaN  Phillips      M   37        NaN     brown
    6     Natalie    Potter      F  NaN      brown     green
    7      Brenda     Jones      F  NaN        NaN     brown
    8     Michael     Smith    NaN   58      brown     brown
    11    Jessica       NaN      F   19      black      blue
    
It can also be performed by column:

    In [5]: df[df.LAST_NAME.isnull()]
    Out[5]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    3        Mary       NaN      F   42     blonde       NaN
    11    Jessica       NaN      F   19      black      blue

#### Simple Queries

Performing simple queries involves setting a single condition on which to mask the dataframe. This could invovle testing for a single value or a range, so long as only one condition is applied.

    In [16]: df.AGE > 50
    Out[16]: 
    0     False
    1     False
    2      True
    3     False
    4     False
    5      True
    6     False
    7     False
    8      True
    9     False
    10    False
    11    False
    12    False
    13    False
    Name: AGE, dtype: bool
    
    In [17]: df[df.AGE > 50]
    Out[17]: 
      FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    2    Michael   Johnson      M   55        red     green
    5     Thomas     Moore      M   60      brown      blue
    8    Michael     Smith    NaN   58      brown     brown
    
    In [18]: df[df.LAST_NAME == "Jones"]
    Out[18]: 
      FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    0   Jennifer     Jones      F   27      black     brown
    7     Brenda     Jones      F  NaN        NaN     brown

#### isin

Have certain values you want to search for? This is were you'll want `isin` handy.

    In [6]: vals = ['brown', 'blue']
    In [7]: df.loc[df.EYE_COLOR.isin(vals)]
    Out[7]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    0    Jennifer     Jones      F   27      black     brown
    4         NaN  Phillips      M   37        NaN     brown
    5      Thomas     Moore      M   60      brown      blue
    7      Brenda     Jones      F  NaN        NaN     brown
    8     Michael     Smith    NaN   58      brown     brown
    9    Jennifer     Smith      F   36      black     brown
    11    Jessica       NaN      F   19      black      blue
    12      Molly    Bryant      F   21      brown      blue

Alternately, you can get the inverse with `~`.

    In [8]: df.loc[~df.EYE_COLOR.isin(vals)]
    Out[8]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    1       Jaime   Roberts      M   32      brown     hazel
    2     Michael   Johnson      M   55        red     green
    3        Mary       NaN      F   42     blonde       NaN
    6     Natalie    Potter      F  NaN      brown     green
    10    Michael     Smith      M   37      black     hazel
    13      Jaime  Anderson      F   46      brown     green
    
    In [9]: df.loc[~df.EYE_COLOR.isin(vals)].EYE_COLOR.unique().tolist()
    Out[9]: ['hazel', 'green', nan]

#### Setting Values

Setting values in a dataframe, whether it's for a single cell (unique row and column location) or a series of entries, is simple so long as the correct slicing method is used. Remember the difference between returning a view and a copy of a dataframe? For setting any values in a dataframe, it's best to stick to the `loc` method.

**Let's call people with brown hair "brunettes" instead**

    In [72]: df.loc[df.HAIR_COLOR == 'brown', 'HAIR_COLOR']
    Out[72]: 
    1     brown
    5     brown
    6     brown
    8     brown
    12    brown
    13    brown
    Name: HAIR_COLOR, dtype: object
    
    In [73]: df.loc[df.HAIR_COLOR == 'brown', 'HAIR_COLOR'] = "brunette"

    In [74]: df
    Out[74]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    0    Jennifer     Jones      F   27      black     brown
    1       Jaime   Roberts      M   32   brunette     hazel
    2     Michael   Johnson      M   55        red     green
    3        Mary     Adams      F   42     blonde      blue
    4      Robert  Phillips      M   37     blonde     brown
    5      Thomas     Moore      M   60   brunette      blue
    6     Natalie    Potter      F   21   brunette     green
    7      Brenda     Jones      F   18     blonde     brown
    8     Michael     Smith      M   58   brunette     brown
    9    Jennifer     Smith      F   36      black     brown
    10    Michael     Smith      M   37      black     hazel
    11    Jessica    Rabbit      F   19      black      blue
    12      Molly    Bryant      F   21   brunette      blue
    13      Jaime  Anderson      F   46   brunette     green

The same can be done with setting values for null entries, but remember to use the correct slicing method.
    
#### Complex Queries

Sometimes you will want more than one predicate in your query logic. Here it is important to remember your boolean logic.

Find men age 30 and over:

    In [23]: df[(df.AGE >= 30) & (df.GENDER == 'M')]
    Out[23]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    1       Jaime   Roberts      M   32      brown     hazel
    2     Michael   Johnson      M   55        red     green
    4         NaN  Phillips      M   37        NaN     brown
    5      Thomas     Moore      M   60      brown      blue
    10    Michael     Smith      M   37      black     hazel

For blondes under age 40 or brunettes over age 50:

    In [33]: df[((df.HAIR_COLOR == 'blonde') & (df.AGE < 40)) | ((df.HAIR_COLOR == 'brown') & (df.AGE > 50))]
    Out[33]: 
      FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    4     Robert  Phillips      M   37     blonde     brown
    5     Thomas     Moore      M   60      brown      blue
    7     Brenda     Jones      F   18     blonde     brown
    8    Michael     Smith      M   58      brown     brown
    
Subsetting pandas dataframes can be as simple or as complex as you need it to be. More complicated selection queries may take longer on very large data sets. But even complex queries will boil down to understand [Python's basic boolean syntax](../../classes/01_basic_syntax/lecture_01.md).
    
#### Apply a Lambda Function to a Query

If the conditions you want to select data by become sufficiently complicated, you might want to use a function that returns `True`/`False` for each record. To do this, you will typically use `.apply()` with a lambda function. For example, let's find all the clients whose first name begins with "M":

    In [8]: df[df.apply(lambda row: row['FIRST_NAME'][0], axis=1) == 'M']
    Out[8]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    2     Michael   Johnson      M   55        red     green
    3        Mary     Adams      F   42     blonde      blue
    8     Michael     Smith      M   58      brown     brown
    10    Michael     Smith      M   37      black     hazel
    12      Molly    Bryant      F   21      brown      blue

For very large datasets, returning all of the columns might be unnecessarily large amounts of information. To return just certain columns, it will be easier to use `loc`. Let's find those same clients but with fewer columns:

    In [9]: df.loc[df.apply(lambda row: row['FIRST_NAME'][0], axis=1) == 'M', ['FIRST_NAME', 'GENDER', 'AGE']]
    Out[9]: 
       FIRST_NAME GENDER  AGE
    2     Michael      M   55
    3        Mary      F   42
    8     Michael      M   58
    10    Michael      M   37
    12      Molly      F   21

#### Building Complex Queries With Eval

An option when writing very long queries is to save the query to a string and then use the `eval` function. This might be helpful when trying to perform a similar query in many places, so you can pass the query conditions around.

First, let's look at our previous query (finding blondes under age 40 or brunettes over age 50):

    In [33]: df[((df.HAIR_COLOR == 'blonde') & (df.AGE < 40)) | ((df.HAIR_COLOR == 'brown') & (df.AGE > 50))]

Now, we can save that query to a string:

    In [22]: my_query = "((df.HAIR_COLOR == 'blonde') & (df.AGE < 40)) | ((df.HAIR_COLOR == 'brown') & (df.AGE > 50))"

But you can't run this query directly:

    In [23]: df[my_query]
    ---------------------------------------------------------------------------
    KeyError: "((df.HAIR_COLOR == 'blonde') & (df.AGE < 40)) | ((df.HAIR_COLOR == 'brown') & (df.AGE > 50))"    

First you have to use `eval` to convert the text to Python code:

    In [24]: df[eval(my_query)]
    Out[24]: 
      FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    4     Robert  Phillips      M   37     blonde     brown
    5     Thomas     Moore      M   60      brown      blue
    7     Brenda     Jones      F   18     blonde     brown
    8    Michael     Smith      M   58      brown     brown

It is fun to note that `eval` is the same logic that Python uses to convert the text you write into executable Python code.

## More Dataframe Operations

#### Merge

`merge` is the pandas equivalent to a SQL join. Like SQL joins, a `merge` can be 'left', 'right', 'inner', or 'outer'.

Here is a simple example of a `merge`:

    In [108]: genders = pd.DataFrame({'GENDER': ['M', 'F'], 'GENDER_LONG': ['male', 'female']})

    In [109]: genders
    Out[109]: 
      GENDER GENDER_LONG
    0      M        male
    1      F      female

    In [110]: pd.merge(left=df, right=genders, how='left', on=['GENDER'])
    Out[110]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR  RAND_INT GENDER_LONG
    0    Jennifer     Jones      F   27      black     brown         2      female
    1       Jaime   Roberts      M   32   brunette     hazel         9        male
    2     Michael   Johnson      M   55        red     green         3        male
    3        Mary     Adams      F   42     blonde      blue         9      female
    4      Robert  Phillips      M   37     blonde     brown         6        male
    5      Thomas     Moore      M   60   brunette      blue         5        male
    6     Natalie    Potter      F   21   brunette     green         5      female
    7      Brenda     Jones      F   18     blonde     brown         6      female
    8     Michael     Smith      M   58   brunette     brown         1        male
    9    Jennifer     Smith      F   36      black     brown         2      female
    10    Michael     Smith      M   37      black     hazel         4        male
    11    Jessica    Rabbit      F   19      black      blue         7      female
    12      Molly    Bryant      F   21   brunette      blue         2      female
    13      Jaime  Anderson      F   46   brunette     green         9      female
    
Beware of how you use `merge`, paying special attention to unintentional one-to-many relationships.

    In [111]: genders = pd.DataFrame({'GENDER': ['M', 'M', 'F'], 'GENDER_LONG': ['male', 'man', 'female']})
    In [111]: genders
    Out[111]: 
    GENDER GENDER_LONG
    0      M        male
    1      M         man
    2      F      female
    
    In [112]: pd.merge(right=df, left=genders, how='left', on=['GENDER'])
    Out[112]: 
       GENDER GENDER_LONG FIRST_NAME LAST_NAME  AGE HAIR_COLOR EYE_COLOR  RAND_INT
    0       M        male      Jaime   Roberts   32   brunette     hazel         9
    1       M        male    Michael   Johnson   55        red     green         3
    2       M        male     Robert  Phillips   37     blonde     brown         6
    3       M        male     Thomas     Moore   60   brunette      blue         5
    4       M        male    Michael     Smith   58   brunette     brown         1
    5       M        male    Michael     Smith   37      black     hazel         4
    6       M         man      Jaime   Roberts   32   brunette     hazel         9
    7       M         man    Michael   Johnson   55        red     green         3
    8       M         man     Robert  Phillips   37     blonde     brown         6
    9       M         man     Thomas     Moore   60   brunette      blue         5
    10      M         man    Michael     Smith   58   brunette     brown         1
    11      M         man    Michael     Smith   37      black     hazel         4
    12      F      female   Jennifer     Jones   27      black     brown         2
    13      F      female       Mary     Adams   42     blonde      blue         9
    14      F      female    Natalie    Potter   21   brunette     green         5
    15      F      female     Brenda     Jones   18     blonde     brown         6
    16      F      female   Jennifer     Smith   36      black     brown         2
    17      F      female    Jessica    Rabbit   19      black      blue         7
    18      F      female      Molly    Bryant   21   brunette      blue         2
    19      F      female      Jaime  Anderson   46   brunette     green         9
    
Notice that our (accidental) one-to-many relationship during the `merge` lead to 19 final records instead of 13. We have no duplicated all of the male records.
    
#### Groupby

`groupby` is a useful tool for aggregating data by field and then applying a function. Some examples include:

 * Grouping a company purchase log by item category (men's, women's, home furnishings, etc.) and region, then applying `sum` to the sale prices. Could be used to report volume of sales by region and item category.

 * Grouping a client list by clothing size and gender, then applying `min`/`max` to age to get the age range of clients (men and women) for each clothing size. Could be used to illustrate trends in clothing size with varying age, and to compare the trends for men and women.

Let's group our client list by last name and then count the number of people with each eye color:

    In [103]: df.groupby(['LAST_NAME', 'EYE_COLOR'], as_index=False)['EYE_COLOR'].count()
    Out[103]: 
    LAST_NAME  EYE_COLOR
    Adams      blue         1
    Anderson   green        1
    Bryant     blue         1
    Johnson    green        1
    Jones      brown        2
    Moore      blue         1
    Phillips   brown        1
    Potter     green        1
    Rabbit     blue         1
    Roberts    hazel        1
    Smith      brown        2
               hazel        1
    dtype: int64

Or let's group all of our clients by first name and count how many have the same hair color:
    
    In [104]: df.groupby(['FIRST_NAME', 'HAIR_COLOR'], as_index=False)['HAIR_COLOR'].count()
    Out[104]: 
    FIRST_NAME  HAIR_COLOR
    Brenda      blonde        1
    Jaime       brunette      2
    Jennifer    black         2
    Jessica     black         1
    Mary        blonde        1
    Michael     black         1
                brunette      1
                red           1
    Molly       brunette      1
    Natalie     brunette      1
    Robert      blonde        1
    Thomas      brunette      1
    dtype: int64

And just as one final exercise, let's add a "random integer" field to our data frame:

    In [105]: df['RAND_INT'] = np.random.randint(1, 10, size=len(df))
    In [106]: df
    Out[106]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR  RAND_INT
    0    Jennifer     Jones      F   27      black     brown         8
    1       Jaime   Roberts      M   32      brown     hazel         5
    2     Michael   Johnson      M   55        red     green         6
    3        Mary     Adams      F   42     blonde      blue         9
    4      Robert  Phillips      M   37     blonde     brown         6
    5      Thomas     Moore      M   60      brown      blue         2
    6     Natalie    Potter      F   21      brown     green         7
    7      Brenda     Jones      F   18     blonde     brown         6
    8     Michael     Smith      M   58      brown     brown         2
    9    Jennifer     Smith      F   36      black     brown         1
    10    Michael     Smith      M   37      black     hazel         1
    11    Jessica    Rabbit      F   19      black      blue         4
    12      Molly    Bryant      F   21      brown      blue         7
    13      Jaime  Anderson      F   46      brown     green         8

Now we can group our data by last name and gender and sum the random integers in each group:

    In [107]: df.groupby(['LAST_NAME', 'GENDER'], as_index=False)['RAND_INT'].sum()
    Out[107]: 
       LAST_NAME GENDER  RAND_INT
    0      Adams      F         9
    1   Anderson      F         9
    2     Bryant      F         2
    3    Johnson      M         3
    4      Jones      F         8
    5      Moore      M         5
    6   Phillips      M         6
    7     Potter      F         5
    8     Rabbit      F         7
    9    Roberts      M         9
    10     Smith      F         2
    11     Smith      M         5

#### Sort

You can imagine sorting a data frame based on a single column. But the pandas `DataFrame.sort()` method takes a list of columns and will sort your data frame using the list as an order of priority. Sorting is actually very easy to do:

    In [117]: df.sort(['LAST_NAME', 'FIRST_NAME', 'AGE'])
    Out[117]: 
        FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR  RAND_INT
    3        Mary     Adams      F   42     blonde      blue         9
    13      Jaime  Anderson      F   46   brunette     green         9
    12      Molly    Bryant      F   21   brunette      blue         2
    2     Michael   Johnson      M   55        red     green         3
    7      Brenda     Jones      F   18     blonde     brown         6
    0    Jennifer     Jones      F   27      black     brown         2
    5      Thomas     Moore      M   60   brunette      blue         5
    4      Robert  Phillips      M   37     blonde     brown         6
    6     Natalie    Potter      F   21   brunette     green         5
    11    Jessica    Rabbit      F   19      black      blue         7
    1       Jaime   Roberts      M   32   brunette     hazel         9
    9    Jennifer     Smith      F   36      black     brown         2
    10    Michael     Smith      M   37      black     hazel         4
    8     Michael     Smith      M   58   brunette     brown         1

#### append

Use `append` to add one data frame onto the end of another:

    In [12]: df1 = df[:8]
    In [13]: df2 = df[8:]
    In [14]: df_appended = df2.append(df1)
    In [15]: df_appended
    Out[15]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR  RAND_INT
    8     Michael     Smith      M   58   brunette     brown         1
    9    Jennifer     Smith      F   36      black     brown         2
    10    Michael     Smith      M   37      black     hazel         4
    11    Jessica    Rabbit      F   19      black      blue         7
    12      Molly    Bryant      F   21   brunette      blue         2
    13      Jaime  Anderson      F   46   brunette     green         9
    0    Jennifer     Jones      F   27      black     brown         2
    1       Jaime   Roberts      M   32   brunette     hazel         9
    2     Michael   Johnson      M   55        red     green         3
    3        Mary     Adams      F   42     blonde      blue         9
    4      Robert  Phillips      M   37     blonde     brown         6
    5      Thomas     Moore      M   60   brunette      blue         5
    6     Natalie    Potter      F   21   brunette     green         5
    7      Brenda     Jones      F   18     blonde     brown         6

Notice the order is preserved in append, which you can tell by looking at the indices above.

#### concat

Use `concat` to do similar combining as with `append`, but you can do many data frames at the same time:

    In [15]: DFs = []
    In [16]: DFs.append(df[10:])
    In [17]: DFs.append(df[5:10])
    In [18]: DFs.append(df[0:5])
    
    In [19]: len(DFs)
    Out[19]: 3
    
    In [20]: pd.concat(DFs)
    Out[20]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR  RAND_INT
    10    Michael     Smith      M   37      black     hazel         4
    11    Jessica    Rabbit      F   19      black      blue         7
    12      Molly    Bryant      F   21   brunette      blue         2
    13      Jaime  Anderson      F   46   brunette     green         9
    5      Thomas     Moore      M   60   brunette      blue         5
    6     Natalie    Potter      F   21   brunette     green         5
    7      Brenda     Jones      F   18     blonde     brown         6
    8     Michael     Smith      M   58   brunette     brown         1
    9    Jennifer     Smith      F   36      black     brown         2
    0    Jennifer     Jones      F   27      black     brown         2
    1       Jaime   Roberts      M   32   brunette     hazel         9
    2     Michael   Johnson      M   55        red     green         3
    3        Mary     Adams      F   42     blonde      blue         9
    4      Robert  Phillips      M   37     blonde     brown         6
    
## Writing Files

#### Common data formats

Writing data to an output file is as easy as reading a file in Pandas. Instead of using `read_` functions, use `to_` functions. A similar set of optional parameters are available, but the main two functions you'll probably want are:

 * `to_csv` - comma separated values
 * `to_pickle` - preserved pandas data structure

#### Other data formats

For more information on writing to other data formats, consult the [pandas manual](http://pandas.pydata.org/pandas-docs/stable/api.html#serialization-io-conversion).

## Further Reading

 * [Installing Pandas](http://pandas.pydata.org/pandas-docs/stable/install.html)
 * [Official Panadas Tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html)
 * [Python & Pandas Top 10](http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/)


[Back to Syllabus](../../README.md)
