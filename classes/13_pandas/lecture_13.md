# Data Analysis with Pandas and Jupyter Notebooks

Several of the scientists I know and most of the data scientists I know use Pandas paired with Jupyter Notebooks for all their data analysis. Separately they are great tools, but together they create an amazingly expressive, friendly environment for analyzing data extremely quickly. Working soley with these two tools is such a common paradigm we need to least try it for at least one lecture. 

## Installation

Like most of the libraries used in our "special topics" lectures, `pandas` and `Jupyter` do not come standard with Python and will have to be installed separately. Please check the official [SciPy Stack Install Guide](http://www.scipy.org/install.html). For Linux and Mac, the installation is merely a single line of `apt-get`. For Windows, pre-built installers are provided.

#### Anaconda

Consider installing [Anaconda](http://docs.continuum.io/anaconda/install.html) instead. Anaconda is Python packaged with hundreds of libraries that you will want (including `pandas`, `Jupyter notebooks` and almost everything else we will use in this course.)

## Jupyter Notebooks

When working through this lecture and the related homework, I recommend using [Jupyter Notebooks](http://ipython.org/ipython-doc/stable/notebook/index.html). The real topic of the lecture is the `pandas` library. But Pandas and Jupyter together create a wonderfully interactive platform for analyzing data. Jupyter notebooks give you a lot of added functionality:

 * You can go back and edit previous lines, like in a text editor.
 * Tab auto-completion
 * More explicit and colour-highlighted error messages
 * Better history management
 * Basic UNIX/LINUX shell integration
 * Tools for debugging code.
 * Helpful `%` syntax to expedite plotting and timing.

For a quick refresher on installing and using Jupyter Notebooks, look back at the [course introdution](../00_setup_and_intro/lecture_00.md#jupyter-notebooks).

After installation, you can invoke Jupyter on the command line by typing: `jupyter notebook`. Then click "new" in the top-right corner and create a "notebook". This will give you an empty notebook to start working. Valid Python code can be entered in these cells:

![Jupyter: enter code](../../resources/ipython_2_basic_python.png)

Hit shift-and-enter to execute the code in your current cell. You will see a new cell to pop up below to continue your work.

## pandas

Pandas is a powerful library for handling data and performing data analysis. It has a ton of pre-made tools designed to make importing data easier. Once imported, your data will be loaded into a `Series` or `DataFrame` object, which are a lot like a table in a database (or Excel). These objects can be munged, sliced, diced, queried, and joined with other similar objects.

The goal of `pandas` appears to be to expedite the human side of opening datasets and dealing with what you find.

There is an un-official convention when importing `pandas`:

    In [1]: import pandas as pd

## Reading Files

A good place to start is reading pre-existing data with pandas. You may find that this is more common than building a pandas data structure from scratch.

#### Simple Data Formats

The four most common Pandas data import methods are:

 * `read_csv` - comma separated values
 * `read_fwf` - fixed width format
 * `read_table` - general delimited text file
 * `read_pickle` - preserved pandas data structure

Each of these methods takes a file path, and a variety of optional arguments:

  * **header (int)**: The default value is `0` assuming your text file has a single header row. But if your file has a large header or comment block at the top, you can set this value higher. Of set `header=None` if don't have a header at all.
  * **names (list)**: You can use this to manually define the column names as you import.
  * **dtype (dict)**: If not given, pandas will infer the data types when importing data. This option is useful if you want to force certain data types at the import stage, for example: `dtype={'x': np.float64, 'y': np.int32, 'z': np.float64}`. (You can still typecast your data after the import, if you don't know what to expect a priori.
  * **usecols (list)**: Save time and space by only importing the columns you need.
  * **nrows (int)**: Only read the first N rows.
  * **skiprows (list or integer)**: List of line numbers to skip or number of lines to skip at the start of the file.
  
#### Other data formats

For more information on reading in other data formats (Excel spreadsheets, SQL databases, etc.), refer to the [pandas manual](http://pandas.pydata.org/pandas-docs/stable/api.html#input-output).

## Series

Though the focus of this lecture will mainly be on pandas `DataFrame`, knowing a bit about pandas `Series` is useful. A `Series` is a one-dimensional array of labeled data.

There are a lot of ways to create a `Series`.

**From a dictionary**

    In [1]: d = {'a': 'A', 'b': 'B', 'c': 'C'}
    In [2]: pd.Series(d)
    Out[2]: 
    a    A
    b    B
    c    C
    dtype: object
    
**From a list**
    
    In [3]: l = ['A', 'B', 'C']
    In [4]: pd.Series(l)
    Out[4]: 
    0    A
    1    B
    2    C
    dtype: object

**From the constructor**

Pandas also has a constructor to create a `Series` by given the data and the indexes directly:

    In [5]: import numpy as np
    In [6]: x = pd.Series(np.arange(5), index=('a','b','c','d','e'))

**Using the Series**

You can slice a `Series` object, much like you would a list or `np.array`:

    In [7]: x[:3]
    Out [7]:
    a    0
    b    1
    c    2
    dtype: int64

    In [8]: x[2:]
    Out [8]:
    c    2
    d    3
    e    4
    dtype: int64

    In [9]: x[::2]
    Out [9]:
    a    0
    c    2
    e    4
    dtype: int64

But `Series` are also indexed, so unlike NumPy arrays, you can get elements by their index:

    In [10]: x[['b','c']]
    Out [10]:
    b    1
    c    2

What do you think this will return?

    In [11]: x[['a','d','c']][1:]

**Working with NumPy**

A `Series` will also work well with all NumPy functions, returning another `Series`:

    In [12]: np.mean(x)
    Out [12]:
    2.0
    In [13]: np.std(x)
    Out [13]:
    1.4142135623730951

You can even convert a `Series` to an index-less NumPy array using `.values`:

    In [14]: x.values
    Out [14]:
    array([0, 1, 2, 3, 4])


## Data Frames

A `DataFrame` is like a `Series`, but it can be multi-dimensional. Let's convert a `Series` into a `DataFrame` and look at the difference. First, we will ingest data as a `Series`:

    In [4]: one = ['A', 'B', 'C']
    
    In [5]: pd.Series(one)
    Out[5]: 
    0    A
    1    B
    2    C
    dtype: object

And then convert it to a `DataFrame`:

    In [6]: pd.DataFrame(one)

    Out[6]: 
       0
    0  A
    1  B
    2  C

Notice the column header `0` above the column of data? Other than that, creating a one-dimensional data as a dataframe is pretty much the same as creating as a series. Feel free to rename that column of data. However, importing the data as a dataframe opens the door for other options, like appending the data column-wise or row-wise to another dataframe, or using it as a table for performing merges (the `pandas` equivalent to an SQL join).

Let's look at some other ways you might want to create a `DataFrame`.

#### DataFrame from a dictionary of arrays

First, we will fill a dictionary with random numbers. There will be 7 keys (`x1`, `x2`, ...) and the values will be a list of 5 randomly-generated normal numbers. Then, we will convert this dictionary into a `DataFrame`.

    In [6]: d = dict(("x"+str(k+1), np.random.randn(7)) for k in range(5))  # 7 rows by 5 columns
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

#### DataFrame from a NumPy array

We can also convert a `np.array` to a `DataFrame`. In the example below we convert a 7x5 `np.array` to `DataFrame`:

    In [8]: d = np.random.rand(7, 5)  # 7 rows by 5 columns
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
    
#### DataFrame from a dict of series objects

We might also want to create a `DataFrame` from a collection of `Series` objects. Typically, this will be done with a dictionary, so you can label the columns:

    In [1]: r = pd.Series(['a', 'b', 'c'])
    In [2]: s = pd.Series(['X', 'Y', 'Z'])
    In [3]: t = pd.Series([1, 2, 3])
    In [4]: u = pd.Series([6, 5, 4])
    In [5]: d = {'r': r, 's': s, 't': t, 'u': u}
    In [6]: pd.DataFrame(d)
    Out[6]: 
       r  s   t   u
    0  a  X   1   6
    1  b  Y   2   5
    2  c  Z   3   4

## Slicing a DataFrame

#### Column Names in All Caps

It is common in Pandas to convert column headers to all caps. This is because data in the real world is messy and inconsistently labeled columns headers can cost you time.

The easy way to capitalize a string is to use `.upper()`:

    In [1]: 'First_Name'.upper()
    Out[1]: 'FIRST_NAME'

But if your input file has column headers with lots of punctuation or other craziness, you might need to clean them up more thoroughly:

    In [2]: def slugify(s):
                valid = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'
                return ''.join([c for c in s.upper().replace(' ', '_') if c in valid])

    In [3]: slugify('MY Profit!!!')
    Out[3]: 'MY_PROFIT'

The column names are kept in the data frame's `.columns` attribute:

    In [4]: df.columns = [col.upper() for col in df.columns]
    In [5]: df.columns
    Out[5]: 
    ['FIRST_NAME', 'LAST_NAME', 'GENDER', 'AGE', 'HAIR_COLOR', 'EYE_COLOR']

Or, if need be:

    In [6]: df.columns = [slugify(col) for col in df.columns]
    In [7]: df.columns
    Out[7]: 
    ['FIRST_NAME', 'LAST_NAME', 'GENDER', 'AGE', 'HAIR_COLOR', 'EYE_COLOR']

#### Select Data by Column

Now that we know our column names, we can start selecting data from our `DataFrame` object. First, let's select by a single column by name:

    In [3]: df['FIRST_NAME']
    Out[3]: 
       FIRST_NAME
    0    Jennifer
    1       Jaime
    2     Michael
    3        Mary
    4      Robert
    5      Thomas
    6     Natalie
    7      Brenda
    8     Michael
    9    Jennifer
    10    Michael
    11    Jessica
    12      Molly
    13      Jaime

Now let's select multiple columns by name:

    In [4]: cols = ['FIRST_NAME', 'LAST_NAME']
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
    
Alternatively, we could do: `df[['FIRST_NAME','LAST_NAME']]`, which accomplishes the same thing.

We could also do `df.loc[:,cols]`, but we'll go into more detail about this later.
    
#### Select Data by Row

Selecting dataframe data by row looks a lot like slicing a standard Python list:

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

#### Select Data by Row and Column

The `loc` function is my preferred tool for row and column-wise slicing of dataframes. The format for using `loc` is `df.loc[row_indexer, column_indexer]`. Below we slice the `DataFrame` by row and by column to select just the data we want:

    In [6]: df.loc[3:8,['FIRST_NAME','AGE','EYE_COLOR']]
    Out[6]: 
      FIRST_NAME  AGE EYE_COLOR
    3       Mary   42      blue
    4     Robert   37     brown
    5     Thomas   60      blue
    6    Natalie   21     green
    7     Brenda   18     brown
    8    Michael   58     brown

We'll cover more of the `loc` function when we discuss query-like data selecting.


## Returning a View Versus a Copy

The previous `loc` slice can also be accomplished by:

    df[3:8][['FIRST_NAME','AGE','EYE_COLOR']]
    
This is called *chained indexing*: the rows are sliced first, then the columns. This works for data selection, but if you then wanted to set values in this subset, it wouldn't alter the original DataFrame. As such, the `loc` function is typically a better option. For more information about the dangers of chain indexing, see the [pandas manual](http://pandas.pydata.org/pandas-docs/stable/indexing.html#returning-a-view-versus-a-copy).

## Useful Dataframe Tools

#### Dropping columns

There are two ways to drop data from a `DataFrame`. Either you want the remaining data returned separately `(inplace=False)` or you don't `(inplace=True)`:

    df = df.drop(['HAIR_COLOR','EYE_COLOR'], axis=1)           # return new DataFrame
    df.drop(['HAIR_COLOR','EYE_COLOR'], axis=1, inplace=True)  # no return (in place)
    
#### Resetting indices

If you have saved a subset of a `DataFrame` and want to reset the indecies so they are sequential again:

    df = df.reset_index(drop=True)           # return new
    df.reset_index(drop=True, inplace=True)  # no return (in place)
    
#### Dropping duplicate entries

If you want to ensure the entries in your `DataFrame` are unique:

    df = df.drop_duplicates()         # return new
    df.drop_duplicates(inplace=True)  # no return (in place)

Or if you just want to find all the unique combinations in your `DataFrame`:

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

Notice the missing indices? That's how you know some (duplicate) rows were dropped. You may want to reset the indicies.

You can also do all of the above on a single column of a dataframe:

    In [13]: df['HAIR_COLOR'].unique()
    Out[13]: array(['black', 'brown', 'red', 'blonde'], dtype=object)

    In [14]: df['HAIR_COLOR'].unique().tolist()
    Out[14]: ['black', 'brown', 'red', 'blonde']

## Querying Data

Pandas allows you to query a DataFrame, much like you might query a database. Below are some basic queries.

#### Null Data

To look at how to deal with Null data in Pandas, we will start with this example `DataFrame`:

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
    
To find all rows with any null values do:

    In [4]: df[pd.isnull(df).any(axis=1)]
    Out[4]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    3        Mary       NaN      F   42     blonde       NaN
    4         NaN  Phillips      M   37        NaN     brown
    6     Natalie    Potter      F  NaN      brown     green
    7      Brenda     Jones      F  NaN        NaN     brown
    8     Michael     Smith    NaN   58      brown     brown
    11    Jessica       NaN      F   19      black      blue
    
Or you can query for null values in a particular column:

    In [5]: df[df.LAST_NAME.isnull()]
    Out[5]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    3        Mary       NaN      F   42     blonde       NaN
    11    Jessica       NaN      F   19      black      blue

#### Simple Queries

A query starts with creating a mask on your `DataFrame`. The mask sets a True/False value for each row/column, based on some predicate. Here is a simple example predicate:

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

You can use this as a mask in your dataset:

    In [17]: df[df.AGE > 50]
    Out[17]: 
      FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    2    Michael   Johnson      M   55        red     green
    5     Thomas     Moore      M   60      brown      blue
    8    Michael     Smith    NaN   58      brown     brown

Here's another simple query based on a predicate/mask:

    In [18]: df[df.LAST_NAME == "Jones"]
    Out[18]: 
      FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    0   Jennifer     Jones      F   27      black     brown
    7     Brenda     Jones      F  NaN        NaN     brown

#### isin

Sometimes you will want a column to be one of a collection of values. You can use `isin` for this, in much the way you used `in` with Python lists:

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

Alternately, you can get the inverse selection with `~`.

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

To set values in a DataFrame, we will use the `.loc()` method, for the same reasons that it was easy to pull/slice data from a DataFrame using `.loc()`.

As before, we could find all the people with brown hair by doing:

    In [72]: df.loc[df.HAIR_COLOR == 'brown', 'HAIR_COLOR']
    Out[72]: 
    1     brown
    5     brown
    6     brown
    8     brown
    12    brown
    13    brown
    Name: HAIR_COLOR, dtype: object
    
But, we probably want to change "brown" to "brunette":

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
    
#### Complex Queries

If you want more than one predicate in your query, you can string them using the normal boolean operators.

If we want to identify male people over 30:

    In [23]: df[(df.AGE >= 30) and (df.GENDER == 'M')]
    Out[23]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    1       Jaime   Roberts      M   32      brown     hazel
    2     Michael   Johnson      M   55        red     green
    4         NaN  Phillips      M   37        NaN     brown
    5      Thomas     Moore      M   60      brown      blue
    10    Michael     Smith      M   37      black     hazel

Or perhaps we want to identify blondes under the age of 40 or brunettes over the age of 50:

    In [33]: df[((df.HAIR_COLOR == 'blonde') & (df.AGE < 40)) | ((df.HAIR_COLOR == 'brown') & (df.AGE > 50))]
    Out[33]: 
      FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    4     Robert  Phillips      M   37     blonde     brown
    5     Thomas     Moore      M   60      brown      blue
    7     Brenda     Jones      F   18     blonde     brown
    8    Michael     Smith      M   58      brown     brown

Queries can be as complex as you need. But remember that more complicated queries my take more time. If the above logic was hard to follow, consider going back and reviewing [Python's boolean syntax](../../classes/01_basic_syntax/lecture_01.md).
    
#### Apply a Lambda Function to a Query

If your query predicates become sufficiently complicated, you might want to replace them with a function that returns `True`/`False` for each record. To do this, use `.apply()` with a lambda function. For example, let's select all the clients whose first name begins with "M":

    In [8]: df[df.apply(lambda row: row['FIRST_NAME'][0], axis=1) == 'M']
    Out[8]: 
       FIRST_NAME LAST_NAME GENDER  AGE HAIR_COLOR EYE_COLOR
    2     Michael   Johnson      M   55        red     green
    3        Mary     Adams      F   42     blonde      blue
    8     Michael     Smith      M   58      brown     brown
    10    Michael     Smith      M   37      black     hazel
    12      Molly    Bryant      F   21      brown      blue

As your dataframes grow, you may find the amount of data selected by a query is quite large. A handy way to speed up your code could be to reduce the number of columns returned. This can be done by passing `loc` a list of column names. For instance, let's do the same query as above, but with only a few columns:

    In [9]: df.loc[df.apply(lambda row: row['FIRST_NAME'][0], axis=1) == 'M', ['FIRST_NAME', 'GENDER', 'AGE']]
    Out[9]: 
       FIRST_NAME GENDER  AGE
    2     Michael      M   55
    3        Mary      F   42
    8     Michael      M   58
    10    Michael      M   37
    12      Molly      F   21

#### Building Complex Queries With Eval

In some circumstances, you might need to build or pass around a query outside of your current code. In this case, it is typical to see people save the query predicate(s) as a string and use the standard Python `eval` function. Let's look at one of our longer queries again (finding blondes under 40 or brunettes over 50):

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

When the Python interpretter converts the text you write into executable bytecode, it uses the exact same tools that are available to you through `eval`.

## More Dataframe Operations

#### Merge

`merge` is the pandas equivalent to a SQL join. Like SQL joins, a `merge` can be "left", "right", "inner", or "outer".

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
    
When using `merge`, you can create one-to-many relationships:

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

The above one-to-many relationship could be what you want. But this is a common failure mode to watch out for during a `merge`. In the case above, we ended up with 19 final records instead of the original 13. It is not hard to imagine a case where these extra 6 records were not intentional or desired. It's just something to think about when merging.
    
#### Groupby

The `groupby` allows you to aggregate a DataFrame object by field and then, possibly, map the results with some function. Here are some example use cases:

 * A big box company groups it's purchase log by item category (men's clothing, women's clothing, home furnishings, etc.) and region, then applys `sum` to the sale prices. This creates a break down of sales volume by region and category.

 * A forum website groups its members by age and topics of interest. They they apply `min`/`max` to the age for each topic. This gives the website creators some idea of trendy topics for different age groups.

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

Or let's group all of our clients by first name and count how many have the same hair color (yes, some of these examples are a little contrived):
    
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

And just as one final exercise, let's insert a "random integer" field to our data frame:

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

The pandas `DataFrame.sort()` allows you to sort a DataFrame object by one or more columns. In the case of multiple columns, the order you provide them will be the order of priority for sorting. For instance:

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

Notice the order of priority in the sorting. The three Smiths are last alphabetically for last names. But the two Michael Smiths come after Jennifer Smith, because of their first name. And finally, one Michael Smith comes after the other due to their ages.

#### append

You can use `append` to add one DataFrame object onto the end of another:

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

Notice the order is preserved in append, based on which DataFrame object is being appended to.

#### concat

You can use `concat` to append two or more DataFrame objects:

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

#### Common Data Formats

Writing your DataFrame object to a common format file is similar to reading files in Pandas. Instead of using `read_` functions, use `to_` functions (a similar set of optional parameters are available). Two functions you'll likely want are:

 * `to_csv` - comma separated values
 * `to_pickle` - preserved pandas data structure

#### Other Data Formats

For more information on writing to other data formats, consult the [pandas manual](http://pandas.pydata.org/pandas-docs/stable/api.html#serialization-io-conversion).

## Problem Sets

 * [Pandas for Data Analysis](problem_set_1_pandas.md)

## Further Reading

 * [Installing Pandas](http://pandas.pydata.org/pandas-docs/stable/install.html)
 * [Official Panadas Tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html)
 * [Python & Pandas Top 10](http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/)


[Back to Syllabus](../../README.md)
