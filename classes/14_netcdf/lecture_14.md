# NetCDF Files in Python

The NetCDF file format is more and more common these days. NetCDF files are binary files with a lot of flexibility for describing dimensioned variables.

## The Library

In this class, we will use the [netCDF4](https://github.com/Unidata/netcdf4-python) library to interface with NetCDF files.

#### Installation

The `netCDF4` library does not come standard with Python, so you will have to install it yourself. The standard installation procedure for installing the prerequisits from source can be found at:

 * [Linux Install Instructions](https://code.google.com/p/netcdf4-python/wiki/UbuntuInstall)

And the links and download instructions for installing the Python library itself can be found at:

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
    >>> lat = root.createDimension("lat", 321)
    >>> lon = root.createDimension("lon", 290)
    >>> layer = root.createDimension("layer", 18)

Here we pass `createDimension` two things: the first is a string name for the dimension and the next is the length of the dimension. By putting `None` for the length of the `"time"` dimension, we are allowing the time dimension to be unlimited.

Much like for groups, to get an ordered dictionary of the dimensions, simply do:

    >>> print(root.dimensions)
    OrderedDict([('time', <netCDF4.Dimension object at 0x15b5910>),
                 ('lat', <netCDF4.Dimension object at 0x15b5960>),
                 ('lon', <netCDF4.Dimension object at 0x15b59b0>),
                 ('layer', <netCDF4.Dimension object at 0x15b5a00>)])

You can also ask for the length of a dimension, or if the dimension is unlimited:

    >>> len(layer)
    18
    >>> layer.isunlimited()
    False
    >>> time.isunlimited()
    True

## Variables

Variables are where we hold the meat of the data in our NetCDF files. Variables have names, data types, and exist along the dimensions we described earlier. As the name suggests, we can keep adding data along an unlimited dimension will just grow the dimension of the file in that direction.

    >>> temp = root.createVariable("temp", "f4", ("time","layer","lat","lon"))
    >>> rh = root.createVariable("rh", "f", ("time","layer","lat","lon"))

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

It is also very common to create a variable for each dimension:

    >>> times = root.createVariable("time", "f8", ("time"))
    >>> layers = root.createVariable("layer", "i4", ("layer"))
    >>> latitudes = root.createVariable("latitude", "f4", ("lat"))
    >>> longitudes = root.createVariable("longitude", "f4", ("lon"), least_significant_digit=3)

Notice the use of the `least_significant_digit` keyword. We frequently don't need all the digits of precision that the 32-bit float `f4` provides. In this case we are saying that we only really need 3 decimal places of precision to be stored.

It is also possible to create "scalar" variables, that have no dimensions and are just simple numbers. But these are not very common. Just leave off the dimensions:

    >>> num_fires = root.createVariable("num_fires", 'i')

## Attributes

Attributes are extra information you attach to a group or a variable. They can be strings, numbers, or sequences. Some really common examples are putting attributes on the root group:

    >>> root.description = "Heat map in California during the final days."
    >>> root.apocolypse = 'Aliens invade, the oceans boil, Wierd Al breaks the 10 ten list again.'
    >>> root.problem = 'Aliens start many wild fires, Smokey the Bear retires.'

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
    [u'description', u'apocolypes', u'problem']
    >>> 
    >>> for name in root.ncattrs():
    ...     print(name)
    ...     print(getattr(root, name))
    ... 
    description
    Heat map in California during the final days.
    apocolypes
    Aliens invade, the oceans boil, Wierd Al breaks the 10 ten list again.
    problem
    Aliens start many wild fires, Smokey the Bear retires.

Of course, this also works for variables:

    >>> temp.ncattrs()
    [u'units']
    >>> 
    >>> temp.units
    u'Celcius'

## Dealing with Data

Reading and writing data from/to NetCDF files is pretty easy. We will assume the `heat_map.nc` example above.

#### Writing Data

The first thing we know is that `temp` is a 4D variable, where one of the dimensions is time. We will get to time in a moment. But first, let's create a 3D dataset to fill in the first time step:

    >>> temps = 100.0 * random(18 * 321 * 290) + 70.0
    >>> temps = temps.reshape(18, 321, 290)

Now we can set the temperature values:

    >>> temp = temps

At this point, we could even address an individual data point directly:

    >>> temp[0][0][0] = -24.5

Or we could use the `list` slicing syntax to set several locations at once:

    >>> from numpy import arange
    >>> temp[12][34][56:78] = 2.0 * arange(56, 78)

It is important to note though that until you initialize all of the values of a variable, you can't set individual values:

    >>> rh[0][0][0] = 123.4
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "netCDF4.pyx", line 2778, in netCDF4.Variable.__getitem__ (netCDF4.c:34626)
      File "netCDF4.pyx", line 3319, in netCDF4.Variable._get (netCDF4.c:41263)
    IndexError

#### Reading Data

Similarly, once a variable has values, we can read locations using the standard `list` syntax:

    >>> temp[0][0][0]
    -24.5
    >>> temp[0][50][50]
    83.317664206502371
    >>> temp[0][79][25:29]
    array([ 141.61345365,  129.34104319,  121.31416574,   80.44523185])

Keep in mind that this won't work if the variable is totally unset:

    >>> rh[0][0][0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "netCDF4.pyx", line 2778, in netCDF4.Variable.__getitem__ (netCDF4.c:34626)
      File "netCDF4.pyx", line 3319, in netCDF4.Variable._get (netCDF4.c:41263)
    IndexError

While the NumPy data structures used in netCDF4 are significantly faster, they were designed to make use of the syntax we already know from the standard Python lists for reading and writing data points. This makes netCDF4 easier to learn and will speed our our work.

## Dealing with Time Coordinates

Working with the time dimension could be a little unweidly because the units are frequnetly things like: "hours since midnight, January 1st, 1970.". To help with this, `netCDF4` comes with two tools to convert between `datetime` objects, and the integers representing the number of hours since some datetime: `date2num` and `num2date`.

    from datetime import datetime, timedelta
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

 * Coming Soon: using unlimited dimensions

## Data Compression

 * Coming Soon: compression inside NetCDF files.

## IOAPI

 * Coming Soon: examples of creating and reading IOAPI-formatted files

IOAPI-formatted NetCDF files have a few restrictions:

 * must have a TFLAG variable
 * must be formatted for NETCDF3_CLASSIC
 * requires a certain set of global attributes

IOAPI required attributes, found on [IOAPI Docs](https://www.cmascenter.org/ioapi/documentation/3.1/html/INCLUDE.html#fdesc):

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
 * **GDTYP** horizontal coordinate system type, using token values LATGRD3, etc., defined in [PARMS3.EXT](https://www.cmascenter.org/ioapi/documentation/3.1/html/INCLUDE.html#parms)
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

Since IOAPI requries NETCDF3_CLASSIC formatting, we also need to know about the NETCDF3_CLASSIC restrictions:

 * can only have one unlimited dimension
 * do not support groups (only the root group is allowed)

## Problem Sets

 * Coming Soon

## Further Reading

 * [Official API Docs](http://unidata.github.io/netcdf4-python/)
 * [Great GoogleCode Introduction](https://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html)
 * [Read & Plot a NetCDF File](http://schubert.atmos.colostate.edu/~cslocum/netcdf_example.html) - Useful example, also plots using MatPlotLib
 * [Tutorial Module](https://code.google.com/p/netcdf4-python/source/browse/trunk/examples/tutorial.py) - This is just a Python module that uses all the netCDF4 features.
 * [CF Conventions - Standard Names](http://cfconventions.org/Data/cf-standard-names/28/build/cf-standard-name-table.html)
 * [IOAPI-based one-man NetCDF Library](https://github.com/barronh/pseudonetcdf)
 * [NetCDF docs](http://www.unidata.ucar.edu/software/netcdf/docs/)
 * [IOAPI requirements](https://www.cmascenter.org/ioapi/documentation/3.1/html/REQUIREMENTS.html)
 * [Official GitHub Repo](https://github.com/Unidata/netcdf4-python)
 * [Official UCAR NetCDF Site](http://www.unidata.ucar.edu/software/netcdf/index.html)
 * [IOAPI netCDF4 Example](https://dawes.sph.unc.edu/uncaqmlsvn/pyPASS/trunk/Utilities/ModelMetaData.py)


[Back to Syllabus](../../README.md)
