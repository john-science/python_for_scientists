# Geoprocessing in Python

We are actually going to introduce three different libraries in this class. Because most geoprocessing work in Python will require some combination of these libraries. There is also a great [ArcPy](http://help.arcgis.com/en/arcgisdesktop/10.0/help/index.html#//000v00000001000000) library, but this is not free and requires paying for an ArcGIS license. Please be warned: Much knowledge about geographic data formats and geoprocessing is assumed in this lecture.

## Installing All Three Libraries

This lecture uses three libraries that do not come standard with Python. To find instructions for installing these three links, try the following links:

 * [Installing PyProj](https://github.com/jswhit/pyproj)
 * [Installing PyShp](https://code.google.com/p/pyshp/)
 * [Installing osgeo/GDAL](https://pypi.python.org/pypi/GDAL/)

Please Note: Unlike other libraries we have installed thus far, these three geospatial libraries are not included in Anaconda.

## PyProj

PyProj is the Python interface to PROJ.4 library. This library has a small, easy-to-learn API. While the pyproj.Geod class is useful for performing Geodetic and Great Circle computations, we are going to focus entirely on the pyproj.Proj class. This is a must-have tool for doing all calculations between projections.

The first step to working with projections is getting a complete description of your projection. The standard way to do that is to search around on [SpatialReference.org](http://spatialreference.org/) for your projection.

Now let's import `Proj` from `pyproj` and use it to create two projections:.

    >>> from pyproj import Proj
    >>>
    >>> cal = Proj('+proj=aea +lat_1=34 +lat_2=40.5 +lat_0=0 +lon_0=-120 ' +
    >>> '+x_0=0 +y_0=-4000000 +ellps=GRS80 +datum=NAD83 +units=m +no_defs')
    >>>
    >>> pnw = Proj('+proj=aea +lat_1=41 +lat_2=47 +lat_0=44 +lon_0=-120 ' +
    >>> '+x_0=0 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m +no_defs')

The first projection you see is a [NAD83](https://en.wikipedia.org/wiki/North_American_Datum#North_American_Datum_of_1983)-[Albers](https://en.wikipedia.org/wiki/Albers_projection), California projection found [here](http://spatialreference.org/ref/sr-org/10/) on [SpatialReference.org](http://spatialreference.org/). The funny string `'+proj=aea +lat_1=41 ...` is a special format used to define projections called the "Proj4 format". The SpatialReference.org website gives this format of the projection description, along with several other projection formats. The second projection is also a NAD83-Albers Pacific Northwest projection found [here](http://spatialreference.org/ref/sr-org/7260/).

The easiest thing we might want to do is convert lon/lat coordinates into our projection:

    >>> lon1, lat1 = cal(122.4786, 37.8197)
    >>> (lon1, lat1)
    (-7881518.3767960835, 5602240.87313246)

We can also tranform our coordinates from one projection to another:

    >>> from pyproj import transform
    >>>
    >>> lon2, lat2 = transform(cal, pnw, lon1, lat1)
    >>> (lon2, lat2)
    (-7221695.417565364, 5539510.56076528)

And most of the functions in this API can be used on multiple coordinates at one time:

    >>> lats_in = (37.1, 37.5, 37.8)
    >>> lons_in = (122.4, 122.5, 122.6)
    >>> lons_cal, lats_cal = cal(lons_in, lats_in)
    >>>
    >>> lons_cal
    (-7959439.682108858, -7914511.693411917, -7880111.27346794)
    >>> lats_cal
    (5582820.697573803, 5588896.573758813, 5591436.156294066)

## shapefile

Shapefile is the Python interface for shapefiles. There is a great tutorial [here](https://github.com/GeospatialPython/pyshp).

#### Reading Shapefiles

A [shapefile](https://en.wikipedia.org/wiki/Shapefile) is actually a combination of three or more files that work together. To load a shapefile:

    >>> import shapefile
    >>> sf = shapefile.Reader("shapefiles/blockgroups.shp")

Shapefiles are filled with geometric shapes (points, lines, polygons, etc) that have geographic references attached. Use `.shapes()` to return a list of all shapes:

    >>> shapes = sf.shapes()

Or, if you know the file is large and you don't want to load all of the shapes into memory at once, use an iterator:

    >>> for shape in sf.iterShapes():
    ...     print shape

You can also get the coordinate bound box of any shape in the file (lower-left and upper-right):

    >>> bbox = shapes[3].bbox
    >>> ['%.3f' % coord for coord in bbox]
    ['-122.486', '37.787', '-122.446', '37.811']

The `points` attribute contains a list of (x, y) tuples for each point in the shape:

    >>> len(shapes[3].points)
    173
    >>> # Get the 8th point of the fourth shape
    >>> shapes[3].points[7]
    ['-122.471', '37.787']

There are fields of data associated with each geometric object in a shapefile. To get a general listing of what fields this shapefile possesses, use `.fields`:

    >>> fields = sf.fields
    >>> fields
    [["POP90_SQMI", "N", 10, 1], ["MALES", "N", 9, 0], ["FEMALES", "N", 9, 0]]

Where here each field is defined by four quantities:

 1. Field Name
 2. Field Type
 3. Field Length
 4. Decimal Length

And much like calling all of the geometric objects in a shapefile, you can call just the data records:

    >>> records = sf.records()
    >>> records[0]
    [1000, 499, 501]

#### Writing Shapefiles

To create a shapefile, use the `Writer` class:

    >>> w = shapefile.Writer()

When you add a geometric object to a shapefile, it can have one of several types:

 * shapefile.POINT = 1
 * shapefile.POLYLINE = 3
 * shapefile.POLYGON = 5
 * shapefile.MULTIPOINT = 8
 * shapefile.POINTZ = 11
 * shapefile.POLYLINEZ = 13
 * shapefile.POLYGONZ = 15
 * shapefile.MULTIPOINTZ = 18
 * shapefile.POINTM = 21
 * shapefile.POLYLINEM = 23
 * shapefile.POLYGONM = 25
 * shapefile.MULTIPOINTM = 28
 * shapefile.MULTIPATCH = 31

Adding data..

 * Coming Soon

## osgeo

osgeo is the Open Source GIS library.

 * Coming Soon

## osgeo.ogr

 * Coming Soon

## osgeo.osr

 * Coming Soon

## osgeo.gdal

 * Coming Soon

## References

 * [SpatialReference.org](http://spatialreference.org/) - Standard names for most projections
 * [PyProj - Quick Tutorial](http://jswhit.github.io/pyproj/)
 * [Shapefile - Official Guide](https://github.com/GeospatialPython/pyshp)
 * [Shapefile - Definition on Wikipedia](https://en.wikipedia.org/wiki/Shapefile)
 * [OGR - Cookbook](https://pcjericks.github.io/py-gdalogr-cookbook/)
 * [OGR - Free Geoprocessing Mini Course](http://www.gis.usu.edu/~chrisg/python/2009/)
 * [ArcPy - Great List of References](http://gis.stackexchange.com/questions/53816/what-are-some-resources-for-learning-arcpy)
 * [ArcPy - Official Docs](http://help.arcgis.com/en/arcgisdesktop/10.0/help/index.html#/A_quick_tour_of_ArcPy/000v00000001000000/)

[Back to Syllabus](../../README.md)
