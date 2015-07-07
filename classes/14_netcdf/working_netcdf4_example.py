from netCDF4 import Dataset

# Creating testing NetCDF file
root = Dataset("heat_map.nc", "w", format="NETCDF4")
# Adding a second group
test_grp = root.createGroup("testing_data")
print('\ngroups = ' + str(root.groups.keys()))

# Adding 4 Dimensions
time = root.createDimension("time", None)
layer = root.createDimension("layer", 11)
lat = root.createDimension("lat", 321)
lon = root.createDimension("lon", 291)
print('\ndimensions = ' + str(root.dimensions.keys()))

# Looking at dimension sizes
print('\nnumber of layers = ' + str(len(layer)))
print('Is layer unlimited in dimension? ' + str(layer.isunlimited()))
print('Is time unlimited in dimension? ' + str(time.isunlimited()))

# Add two variables to the file
temp = root.createVariable("temp", "f4", ("time","layer","lat","lon"), least_significant_digit=3)
rh = root.createVariable("rh", "f", ("time","layer","lat","lon"))

# Adding a variable for each dimension in the file
times = root.createVariable("time", "f8", ("time"))
layers = root.createVariable("layer", "i4", ("layer"))
latitudes = root.createVariable("latitude", "f4", ("lat"))
longitudes = root.createVariable("longitude", "f4", ("lon"))

# Adding scalar variable to file
num_fires = root.createVariable("num_fires", 'i')
print('\nvariables = ' + str(root.variables.keys()))

# Adding global attributes
root.description = "Heat map in California during the final days."
root.apocolypse = 'Aliens invade, the oceans boil, Wierd Al breaks the 10 ten list again.'
root.problem = 'Aliens start many wild fires, Smokey the Bear retires.'

# Adding variable attributes
latitudes.units = "degrees north"
longitudes.units = "degrees east"
layers.units = "hPa"
rh.units = 'percent'
temp.units = "F"
times.units = "hours since 0001-01-01 00:00:00.0"
times.calendar = "gregorian"

# Looking at attributes
print('\nAttributes = ' + str(root.ncattrs()))
for name in root.ncattrs():
    print('attribute: ' + name + ', value: ' + str(getattr(root, name)))

# Writing Data
from numpy.random import random
temp[0:1,0:11,:,:] = 100.0 * random(size=(1, 11, 321, 291)) + 70.0
print('temp.shape = ' + str(temp.shape))

# Altering Data
temp[0][0][0][0] = -24.5
from numpy import arange
temp[0][10][34][56:78] = 2.0 * arange(56, 78)

# Reading Data
print('\ntemp[0][0][0][0] = ' + str(temp[0][0][0][0]))
print('temp[0][0][50][50] = ' + str(temp[0][0][50][50]))
print('temp[0][0][79][25:29] = ' + str(temp[0][0][79][25:29]))

# Filling Time Coordinates
from datetime import datetime, timedelta
from netCDF4 import date2num, num2date
dates = [datetime(2015, 6, 21) + n*timedelta(hours=12) for n in range(temp.shape[0])]
times[:] = date2num(dates,units=times.units,calendar=times.calendar)
print('\ntimes = ' + str(times[:]))

# Convert numbers back to datetimes
dates = num2date(times[:],units=times.units,calendar=times.calendar)
print('\ndates = ' + str(dates))

# Showing how to modify time dimensions
print('temp.shape before = ' + str(temp.shape))
temp[0:5,0:11,:,:] = random(size=(5, 11, 321, 291))
print('temp.shape after = ' + str(temp.shape))
print('length of time = ' + str(len(time)))
