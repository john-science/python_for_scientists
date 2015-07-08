# Basic netCDF4 Operations

## Print the Totals of All Variables

Create a function called `print_totals` that:

1. Opens a NetCDF file as a `netCDF4.Dataset`.
2. Loops through each variable
3. Checks to see if the variable is the IOAPI `TFLAG` variable and, if so, ignores it.
4. Calculates the total of all grid cells in the current variable using `numpy.sum`.
5. Prints the variable name, variable units, and total nicely to the screen.

## Creating a Simple NetCDF File

Create a function called `create_empty_elevation` that:

1. Takes an input variable `file_path`.
2. Opens a new NetCDF file for writing using `netCDF4.Dataset` at a location defined by `file_path`.
3. Make sure you open the file in `"NETCDF4"` format.
4. Add an unlimited dimension `time`.
5. Add two dimensions `x` and `y`, both with length 100.
6. Add the variable `elevation`, with units of `f4`, all three dimensions, and with only 2 least significant digits.
7. Add the attribute `units` to the `elevation` variable, and give it a value of `km`.
8. Save/close your new NetCDF file.

## Writing to a NetCDF File

Create a function called `fill_valley_elevation` that:

1. Takes an input variable `file_path`.
2. Opens a new NetCDF file for writing using `netCDF4.Dataset` at a location defined by `file_path`.
3. Imports `arange`, `cos`, and `pi` from `numpy`.
4. Uses `arange` to create an array called `steps` from `0.0` to `2 * pi`  in steps of `pi / 50.0`
5. Create an array called `yosemite` that is 1.218 times the cosine of `steps` plus 1.372.
6. Import `float32` and `array` from `numpy`.
7. Create a 3D array called `valley` of size 1 x 100 x 100, where each row is `yosemite`.
8. Set the values of the `elevation` variable equal to `valley`.
9. Add an attribute called `FILEDESC` with a value of `'elevation of an imaginary valley'`.
10. Add an attribute called `HISTORY` with a value of `"The elevation doesn't change much over time."`.
11. Save/close your new NetCDF file.

## Pulling it All Together

Use the functions you've already created:

1. Use `create_empty_elevation` to create a file called "elevation.ncf".
2. Use `fill_vallye_elevation` to add test data to "elevation.ncf".
3. Use `print_totals` to print out the sum of all the elevation values in "elevation.ncf."  (NOTE: Adding elevations doesn't make a lot of sense, but this is just homework.)

## IOAPI Files

 * Coming Soon

## Solutions

 * [Basic netCDF4 - Solutions](problem_set_1_solutions.md)

[Back to Lecture](lecture_14.md)
