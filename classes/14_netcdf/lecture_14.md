# NetCDF Files in Python

The NetCDF file format is more and more common these days. NetCDF files are binary files with a lot of flexibility for describing dimensioned variables.

## The Library

In this class, we will use the [netCDF4](https://github.com/Unidata/netcdf4-python) library to interface with NetCDF files.

#### Installation

The `netCDF4` library does not come standard with Python, so you will have to install it yourself. The standard installation procedure for installing the dependencies from source can be found at:

 * [Linux Install Instructions](https://code.google.com/p/netcdf4-python/wiki/UbuntuInstall)

I found this link better for downloading and installing the Python library itself:

 * [Google Code Instructions](http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html)

## Reading & Writing NetCDF

To read or write NetCDF files, use the `Dataset` constructor.

    >>> from netCDF4 import Dataset
    >>> root = Dataset("write_test.nc", "w", format="NETCDF4")
    >>> root.close()

The netCDF4 library supports four different NetCDF formats: `NETCDF3_CLASSIC`, `NETCDF3_64BIT`, `NETCDF4_CLASSIC`, and the default is `NETCDF4`. When reading a file, netCDF4 will attempt to auto-detect the file type.

    >>> from netCDF4 import Dataset
    >>> data = Dataset("read_test.nc", "r")
    >>> data.close()

Following the usual Python syntax, you can open an existing NetCDF file to write more date to it by using `r+`.

    >>> from netCDF4 import Dataset
    >>> data = Dataset("read_test.nc", "r+")
    >>> # add more data
    >>> data.close()

## Groups

Groups are a powerful new ability in NetCDF version 4. They are much akin to the folder/directory structure in your computer. Each group can contain everything that a NetCDF file can contain (dimensions, variables, and attributes), but also other groups. Every NetCDF version 4 file starts out with one root group that basically contains the entire file.

Use `createGroup` to create a new group:

    >>> from netCDF4 import Dataset
    >>> root = Dataset("heat_map.nc", "w", format="NETCDF4")
    >>> test_grp = root.createGroup("testing_data")
    >>> print(root.groups)
    OrderedDict([('testing_data', <netCDF4.Group object at 0x1588e50>)])

## Dimensions

All variables in NetCDF files are defined in terms of a set of dimensions. For instance, meteorological variables might be defined along four dimensions: latitude, longitude, altitude, and time. But surface elevation data might only have two dimensions: latitude and longitude. Obviously, before we create any variables, we need to define the dimensions in the file. Use `createDimension`:

    >>> time = root.createDimension("time", None)
    >>> layer = root.createDimension("layer", 11)
    >>> lat = root.createDimension("lat", 321)
    >>> lon = root.createDimension("lon", 291)

Here we pass `createDimension` two things: the first is a string name for the dimension and the next is the length of the dimension. By putting `None` for the length of the `"time"` dimension, we are allowing the time dimension to be unlimited.

Much like for groups, to get an ordered dictionary of the dimensions, simply do:

    >>> print(root.dimensions)
    OrderedDict([('time', <netCDF4.Dimension object at 0x15b5910>),
                 ('lat', <netCDF4.Dimension object at 0x15b5960>),
                 ('lon', <netCDF4.Dimension object at 0x15b59b0>),
                 ('layer', <netCDF4.Dimension object at 0x15b5a00>)])

You can also ask for the length of a dimension, or if the dimension is unlimited:

    >>> len(layer)
    11
    >>> layer.isunlimited()
    False
    >>> time.isunlimited()
    True

## Variables

Variables are where we hold the meat of the data in our NetCDF files. Variables have names, data types, and exist along the dimensions we described earlier. As the name suggests, we can keep adding data along an unlimited dimension will just grow the dimension of the file in that direction.

    >>> temp = root.createVariable("temp", "f4", ("time","layer","lat","lon"))
    >>> rh = root.createVariable("rh", "f", ("time","layer","lat","lon"), least_significant_digit=3)

Here we see `createVariable` takes three things: the variable name, its data type, and a tuple describing the dimensions of the variable. There are several data types supported by NetCDF files:

Data Type | Technical Specifier | Shorthand Specifier
:--- | :---: | :---:
32-bit floating point | f4 | f
64-bit floating point | f8 | d
32-bit signed integer | i4 | i
16-bit signed integer | i2 | h
64-bit singed integer | i8 | 
8-bit signed integer | i1 | b
8-bit unsigned integer | u1 | 
16-bit unsigned integer | u2 | 
32-bit unsigned integer | u4 | 
64-bit unsigned integer | u8 | 
single-character string | S1 | c

Also notice the use of the `least_significant_digit` keyword. We frequently don't need all the digits of precision that the 32-bit float `f4` provides. In this case we are saying that we only really need 3 decimal places of precision to be stored.

It is also very common to create a variable for each dimension:

    >>> times = root.createVariable("time", "f8", ("time"))
    >>> layers = root.createVariable("layer", "i4", ("layer"))
    >>> latitudes = root.createVariable("latitude", "f4", ("lat"))
    >>> longitudes = root.createVariable("longitude", "f4", ("lon"))

It is also possible to create "scalar" variables, that have no dimensions and are just simple numbers. But these are not very common. Just leave off the dimensions:

    >>> num_fires = root.createVariable("num_fires", 'i')

**FUN FACT**: Variables and Dimensions can not be deleted from a NetCDF file. This is not a bug in `netCDF4`, but a feature in the underlying C API. Your only option is to copy the file bit-by-bit, and just skip the variable in question.

## Attributes

Attributes are extra information you attach to a group or a variable. They can be strings, numbers, or sequences. Some really common examples are putting attributes on the root group:

    >>> root.description = 'Heat map in California during the final days.'
    >>> root.problem = "It's hot. So hot."

Also, variables frequently need attributes:

    >>> latitudes.units = "degrees north"
    >>> longitudes.units = "degrees east"
    >>> layers.units = "hPa"
    >>> rh.units = 'percent'
    >>> temp.units = "F"
    >>> times.units = "hours since 0001-01-01 00:00:00.0"
    >>> times.calendar = "gregorian"

If you want to see what attributes a group or variable have, use `.ncattrs() :

    >>> root.ncattrs()
    [u'description', u'problem']
    >>> 
    >>> for name in root.ncattrs():
    ...     print(name)
    ...     print(getattr(root, name))
    ... 
    description
    Heat map in California during the final days.
    problem
    It's hot. So hot.

Of course, this also works for variables:

    >>> temp.ncattrs()
    [u'units']
    >>> 
    >>> temp.units
    u'Celcius'

## Dealing with Data

Reading and writing data to/from NetCDF files is pretty easy. 

#### Writing Data

The first thing we know is that `temp` is a 4D variable, where one of the dimensions is time. So we will create a four-dimensional array, and store the values in `temp`:

    >>> from numpy.random import random
    >>> temp[0:1,0:11,:,:] = 100.0 * random(size=(1, 11, 321, 291)) + 70.0

At this point, we could even address an individual data point directly:

    >>> temp[0][0][0][0] = -24.5

Or we could use the `list` slicing syntax to set several locations at once:

    >>> from numpy import arange
    >>> temp[0][10][34][56:78] = 2.0 * arange(56, 78)

It is important to note though that until you initialize all of the values of a variable, you can't set individual values:

    >>> rh[0][0][0][0] = 123.4
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "netCDF4.pyx", line 2778, in netCDF4.Variable.__getitem__ (netCDF4.c:34626)
      File "netCDF4.pyx", line 3319, in netCDF4.Variable._get (netCDF4.c:41263)
    IndexError

#### Reading Data

Similarly, once a variable has values, we can read locations using the standard `list` syntax:

    >>> temp[0][0][0][0]
    -24.5
    >>> temp[0][0][50][50]
    83.317664206502371
    >>> temp[0][0][79][25:29]
    array([ 141.61345365,  129.34104319,  121.31416574,   80.44523185])

Keep in mind that this won't work if the variable is totally unset:

    >>> rh[0][0][0][0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "netCDF4.pyx", line 2778, in netCDF4.Variable.__getitem__ (netCDF4.c:34626)
      File "netCDF4.pyx", line 3319, in netCDF4.Variable._get (netCDF4.c:41263)
    IndexError

While the NumPy data structures used in netCDF4 are significantly faster, they were designed to make use of the syntax we already know from the standard Python lists for reading and writing data points. This makes netCDF4 easier to learn and will speed our our work.

## Dealing with Time Coordinates

Working with the time dimension could be a little unweidly because the units are frequnetly things like: "hours since midnight, January 1st, 1970.". To help with this, `netCDF4` comes with two tools to convert between `datetime` objects, and the integers representing the number of hours since some datetime: `date2num` and `num2date`.

    >>> from datetime import datetime, timedelta
    >>> from netCDF4 import date2num, num2date

First, let's create a list of `datetimes` for our time dimension and use `date2num` to load them into place:

    >>> dates = [datetime(2015, 6, 21) + n*timedelta(hours=12) for n in range(temp.shape[0])]
    >>> times[:] = date2num(dates,units=times.units,calendar=times.calendar)
    >>> print(times[:])
    [ 17658504.  17658516.  17658528.  17658540.  17658552.  17658564.
      17658576.  17658588.  17658600.  17658612.  17658624.  17658636.
      17658648.  17658660.  17658672.  17658684.  17658696.  17658708.]

By contrast, you can use `num2date` to convert these numbers back into something more human-readable:

    >>> dates = num2date(times[:],units=times.units,calendar=times.calendar)
    >>> print(dates)
    [datetime.datetime(2015, 6, 21, 0, 0) datetime.datetime(2015, 6, 21, 12, 0)
     datetime.datetime(2015, 6, 22, 0, 0) datetime.datetime(2015, 6, 22, 12, 0)
     datetime.datetime(2015, 6, 23, 0, 0) datetime.datetime(2015, 6, 23, 12, 0)
     datetime.datetime(2015, 6, 24, 0, 0) datetime.datetime(2015, 6, 24, 12, 0)
     datetime.datetime(2015, 6, 25, 0, 0) datetime.datetime(2015, 6, 25, 12, 0)
     datetime.datetime(2015, 6, 26, 0, 0) datetime.datetime(2015, 6, 26, 12, 0)
     datetime.datetime(2015, 6, 27, 0, 0) datetime.datetime(2015, 6, 27, 12, 0)
     datetime.datetime(2015, 6, 28, 0, 0) datetime.datetime(2015, 6, 28, 12, 0)
     datetime.datetime(2015, 6, 29, 0, 0) datetime.datetime(2015, 6, 29, 12, 0)]

Working with unlimited dimensions is actually pretty easy. For instance, if we printed out the `shape` of `temp` now, we would get:

    >>> temp.shape
    (1, 11, 321, 291)

But the time dimension will automatically add up if we simply add more data:

    >>> from numpy.random import random
    >>> temp[0:5,0:11,:,:] = random(size=(5, 11, 321, 291))
    >>> print('temp.shape after = ' + str(temp.shape))
    (5, 11, 321, 291)

So all we had to do above was add data into one of our variables and the time variable was automatically grown to match:

    >>> print(len(time))
    5

## Data Compression

When creating a variable, you can opt to have it compressed:

    >>> pressure = root.createVariable("pressure",
                                       "f4",
                                       ("time", "layer", "lat", "lon"),
                                       zlib=True,
                                       least_significant_digit=3,
                                       complevel=9)

We did three things to improve the compression of the variable. First and foremost, we set `zlib=True`, this is what defines `pressure` as a compressed variable. Second, we set `least_significant_digit` to our lowest tolerable level, reducing the number of decimal places we have to store and compress. Lastly, we set the optional "compression level" parameter `complevel` to 9. The `complevel` parameter can go from 1 (fastest, but least compression) to 9 (slowest, but most compression), 4 is the default.

## GRIDDED IOAPI Files

Many programs that use NetCDF files will require them to be in the IOAPI format. These IOAPI-formatted NetCDF files will be read/written by `netCDF4` like any other NetCDF files, but will have several restrictions which define them. There are [8 different types](https://www.cmascenter.org/ioapi/documentation/3.1/html/VBLE.html) of IOAPI file currently supported, and for the sake of brevity, we will only discuss the [GRIDDED IOAPI](https://www.cmascenter.org/ioapi/documentation/3.1/html/DATATYPES.html#grdded) format used for representing 2D or 3D time-dependent variables.

#### The GRIDDED IOAPI Format

IOAPI/NetCDF restrictions:

 * must be formatted for NETCDF3_CLASSIC
 * must have six dimensions:
  * TSTEP = Unlimited dimension
  * DATE-TIME = Julian Day and Time (YYYYJJJJ, HHMMSS)
  * LAY = number of vertical layers
  * VAR = number of variables
  * ROW = number of rows
  * COL = number of columns
 * must have a TFLAG variable to map DATE-TIMES to each variable's TSTEP (TSTEP, VAR, DATE-TIME)
 * [variables](https://www.cmascenter.org/ioapi/documentation/3.1/html/VBLE.html)
  * names = 16 characters (with trailing spaces)
  * must have "units" attribute = 16 characters (with trailing spaces)
  * must have "var_desc" description attribute = 80 characters (with trailing spaces)
 * requires a certain set of [global attributes](https://www.cmascenter.org/ioapi/documentation/3.1/html/INCLUDE.html#fdesc):
  * **IOAPI_VERSION** version id string
  * **EXEC_ID** value of environment variable EXECUTION_ID 
  * **FTYPE** data structure type for the variables in this file
  * **UPNAM** name of last program writing to this file
  * **FILEDESC** text describing the file
  * **HISTORY** text history of file and alterations
  * **WDATE** last-update date
  * **WTIME** last-update time
  * **CDATE** file-creation date
  * **CTIME** file-creation time
  * **SDATE** file start date YYYYDDD
  * **STIME** file start time HHMMSS
  * **TSTEP** file time step HHMMSS
  * **GDNAM** grid name
  * **GDTYP** horizontal coordinate system type, defined in [PARMS3.EXT](https://www.cmascenter.org/ioapi/documentation/3.1/html/INCLUDE.html#parms), 2 is LCC projection
  * **P_ALP** first map projection descriptive parameter
  * **P_BET** second map projection descriptive parameter
  * **P_GAM** third map projection descriptive parameter
  * **XCENT** longitude for coordinate system origin (where X = 0)
  * **YCENT** latitude for coordinate system origin (where Y = 0)
  * **XORIG** X-coordinate for lower-left (southwest) corner of the grid
  * **YORIG** Y-coordinate for lower-left (southwest) corner of the grid
  * **XCELL** X-coordinate grid cell size
  * **YCELL** Y-coordinate grid cell size
  * **NCOLS** number of horizontal grid columns
  * **NROWS** number of horizontal grid rows
  * **NTHIK** boundary perimeter thickness (number of cells)
  * **VGTYP** vertical coordinate type
  * **VGTOP** model-top, for sigma coord types
  * **NLAYS** number of vertical grid layers
  * **VGLVLS** array of vertical coordinate grid level values
  * **NVARS** number of variables
  * **VAR-LIST** string representing list of variable names

I find these restrictions are generally enough to worry about. Are you really going to need to worry about the fact that you can't have more than 1024 variables in a file? But there are many more restrictions that define an IOAPI NetCDF file, GRIDDED or otherwise. You can find these in the [official documentation](https://www.cmascenter.org/ioapi/documentation/3.1/html/VBLE.html).

GRIDDED IOAPI restrictions:

 * global attribute `NTHIK` is ignored (`NTHIK = 0`)

The `NETCDF3_CLASSIC` restrictions:

 * can only have one unlimited dimension
 * do not support groups (only the root group is allowed)

#### GRIDDED IOAPI Examples

For the following examples, imagine we are reading a GRIDDED-type IOAPI NetCDF file called "small_test.ncf".

Of course, all GRIDDED IOAPI files have the same dimensions:

    >>> root.dimensions.keys()
    [u'TSTEP', u'DATE-TIME', u'LAY', u'VAR', u'ROW', u'COL']

But what dimensions does this file have?

    >>> root.variables.keys()
    [u'TFLAG', u'PM25']

Well, `'PM25'` may have been a surprise, but we already knew the file had to contain a `TFLAG` variable:

    >>> print(root.variables['TFLAG'])
    <type 'netCDF4.Variable'>
    int32 TFLAG(TSTEP, VAR, DATE-TIME)
        units: <YYYYDDD,HHMMSS>
        long_name: TFLAG           
        var_desc: Timestep-valid flags:  (1) YYYYDDD or (2) HHMMSS                                
    unlimited dimensions: TSTEP
    current shape = (1, 1, 2)
    >>> 
    >>> print(root.variables['TFLAG'][:])
    [[[2007335       0]]]

And all IOAPI-formatted NetCDF files have to contain the same list of attributes:

    >>> sorted(root.ncattrs())
    [u'CDATE', u'CTIME', u'EXEC_ID', u'FILEDESC', u'FTYPE', u'GDNAM', u'GDTYP',
     u'HISTORY', u'IOAPI_VERSION', u'NCOLS', u'NLAYS', u'NROWS', u'NTHIK',
     u'NVARS', u'P_ALP', u'P_BET', u'P_GAM', u'SDATE', u'STIME', u'TSTEP',
     u'UPNAM', u'VAR-LIST', u'VGLVLS', u'VGTOP', u'VGTYP', u'WDATE', u'WTIME',
     u'XCELL', u'XCENT', u'XORIG', u'YCELL', u'YCENT', u'YORIG']

And all of these attributes are easily accessible:

    >>> root.IOAPI_VERSION
    u'$Id: @(#) ioapi library version 3.0 $                                           '
    >>> root.NVARS
    1
    >>> root.NLAYS
    1
    >>> root.NROWS
    291
    >>> root.NCOLS
    321

## Example Scripts

Working with NetCDF files can take some time getting used to. So here are some short scripts to serve as examples of doing various small tasks.

 * [Script](netcdf4_class_examples.py) version of the non-IOAPI portion of this lecture.
 * [Script](average_two_netcdfs.py) that averages two very similar NetCDF files.
 * [Script](make_gridded_ioapi_template.py) that will make a copy of a GRIDDED IOAPI NetCDF file with all empty data.
 * [Script](extract_cell_from_3d_ioapi.py) that will extract the values at a single grid cell for a GRIDDED IOAPI NetCDF.

## Problem Sets

 * [Basic netCDF4 Operations](problem_set_1_netcdf4_operations.md)

## Further Reading

netCDF4 resources:

 * [Official API Docs](http://unidata.github.io/netcdf4-python/)
 * [Quick netCDF4 Intro](http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html)
 * [Great GoogleCode Introduction](https://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html)
 * [Read & Plot a NetCDF File](http://schubert.atmos.colostate.edu/~cslocum/netcdf_example.html) - Useful example, also plots using MatPlotLib
 * [netCDF4 Tutorial Module](https://code.google.com/p/netcdf4-python/source/browse/trunk/examples/tutorial.py) - This is just a Python module that uses all the netCDF4 features.
 * [Official netCDF4 GitHub Repo](https://github.com/Unidata/netcdf4-python)

General NetCDF resources:

 * [NetCDF docs](http://www.unidata.ucar.edu/software/netcdf/docs/)
 * [Official UCAR NetCDF Site](http://www.unidata.ucar.edu/software/netcdf/index.html)

IOAPI resources:

 * [IOAPI-based one-man NetCDF Library](https://github.com/barronh/pseudonetcdf)
 * [IOAPI User Manual](https://www.cmascenter.org/ioapi/documentation/3.1/html/AA.html)
 * [IOAPI requirements](https://www.cmascenter.org/ioapi/documentation/3.1/html/REQUIREMENTS.html)
 * [CF Conventions - Standard Names](http://cfconventions.org/Data/cf-standard-names/28/build/cf-standard-name-table.html)
 * [IOAPI netCDF4 Example](https://dawes.sph.unc.edu/uncaqmlsvn/pyPASS/trunk/Utilities/ModelMetaData.py)


[Back to Syllabus](../../README.md)
