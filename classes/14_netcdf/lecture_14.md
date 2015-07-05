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
    >>> root = Dataset("test1.nc", "w", format="NETCDF4")
    >>> print(root.data_model)
    NETCDF4
    >>> root.close()

The netCDF4 library supports four different NetCDF formats: `NETCDF3_CLASSIC`, `NETCDF3_64BIT`, `NETCDF4_CLASSIC`, and the default is `NETCDF4`. When reading a file, netCDF4 will attempt to auto-detect the file type.

    >>> from netCDF4 import Dataset
    >>> data = Dataset("test2.nc", "r")
    >>> print(data.data_model)
    NETCDF3_CLASSIC
    >>> data.close()

## Groups

Groups are a powerful new ability in NetCDF version 4. They are much akin to the folder/directory structure in your computer. Each group can contain everything that a NetCDF file can contain (dimensions, variables, and attributes), but also other groups. Every NetCDF version 4 file starts out with one root group that basically contains the entire file.

Use `createGroup` to create a new group:

    >>> from netCDF4 import Dataset
    >>> root = Dataset("test3.nc", "w", format="NETCDF4")
    >>> test_grp = root.createGroup("testing_data")
    >>> print(root.groups)
    OrderedDict([('testing_data', <netCDF4.Group object at 0x1588e50>)])
    >>> root.close()

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

    >>> temp = root.createVariable("temp", "f4", ("time","level","lat","lon"))
    >>> rh = root.createVariable("rh", "f", ("time","level","lat","lon"))

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
    >>> longitudes = root.createVariable("longitude", "f4", ("lon"))

It is also possible to create "scalar" variables, that have no dimensions and are just simple numbers. But these are not very common. Just leave off the dimensions:

    >>> energy = root.createVariable("energy", 'f4')

## Attributes

Attributes are extra information you attach to a group or a variable. They can be strings, numbers, or sequences. Some really common examples are putting attributes on the root group:

    >>> from netCDF4 import Dataset
    >>> root = Dataset("test4.nc", "w", format="NETCDF4")
    >>> root.description = "Called to work on the Moon"
    >>> root.date_created = "June 21, 2001"
    >>> root.author = "Dave Bowman"

Also, variables frequently need attributes:

    >>> h = root.createVariable("height", f4)
    >>> h.units = "meters"
    >>> h.whos = "It's your height."

If you want to see what attributes a group or variable have, use `.ncattrs() :

    >>> root.ncattrs()
    [u'description', u'date_created', u'author']
    >>>
    >>> for attr_name in root.ncattrs():
    ...     print(attr_name)
    ...     print(getattr(root, attr_name))
    ... 
    description
    Called to work on the Moon
    date_created
    June 21, 2001
    author
    Dave Bowman

Of course, this also works for variables:

    >>> h.ncattrs()
    [u'units', u'whos']
    >>> for attr_name in root.ncattrs():
    ...     print(attr_name, getattr(root, attr_name))
    ... 
    (u'description', u'Called to work on the Moon')
    (u'date_created', u'June 21, 2001')
    (u'author', u'Dave Bowman')

## Dealing with Data

 * Coming Soon

## Dealing with Time Coordinates

 * Coming Soon

## Data Compression

 * Coming Soon

## IOAPI

 * Coming Soon

## Problem Sets

 * Coming Soon

## Further Reading

 * [Official API Docs](http://unidata.github.io/netcdf4-python/)
 * [Great GoogleCode Introduction](https://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html)
 * [Read & Plot a NetCDF File](http://schubert.atmos.colostate.edu/~cslocum/netcdf_example.html) - Useful example, also plots using MatPlotLib
 * [Tutorial Module](https://code.google.com/p/netcdf4-python/source/browse/trunk/examples/tutorial.py) - This is just a Python module that uses all the netCDF4 features.
 * [IOAPI-based one-man NetCDF Library](https://github.com/barronh/pseudonetcdf)
 * [NetCDF docs](http://www.unidata.ucar.edu/software/netcdf/docs/)
 * [IOAPI requirements](https://www.cmascenter.org/ioapi/documentation/3.1/html/REQUIREMENTS.html)
 * [Official GitHub Repo](https://github.com/Unidata/netcdf4-python)
 * [Official UCAR NetCDF Site](http://www.unidata.ucar.edu/software/netcdf/index.html)


[Back to Syllabus](../../README.md)
