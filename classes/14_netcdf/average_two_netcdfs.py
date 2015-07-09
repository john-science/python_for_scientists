'''
The purpose of this script is to take in two similar NetCDF files,
and average all of the variables across each grid cell.

Most of this code is just checking to make sure the files are
similar enough for this to work. But there are still some outlying
cases that are not checked: the units of all the variables, the
NETCDF format of the files, etc.
'''


import sys
from netCDF4 import Dataset

def main():
    average_two_similar_netcdfs(sys.argv[1], sys.argv[2], sys.argv[3])


def average_two_similar_netcdfs(file1, file2, outfile):
    '''Take two input files and average every grid cell
    of every variable. This requires that both files have
    the exact same dimensions and variables.'''
    # copy file1 to the end file location
    copyfile(file1, outfile)

    # open your new output file in read/write mode
    root = Dataset(outfile, 'r+')

    # open the second input file in read mode
    root2 = Dataset(file2, 'r')

    # verify that your two files have the same dimensions
    if sorted(root.dimensions.keys()) != sorted(root2.dimensions.keys()):
        raise Exception('These two input files have different dimensions.')

    # verify that your dimensions all have the same length
    for dim in root.dimensions.keys():
        if len(root.dimensions[key]) != len(root2.dimensions[key]):
            raise Exception('The dimension ' + dim + ' is not the same length in both files.')

    # verify that your two files have the same variables
    if sorted(root.variables.keys()) != sorted(root2.variables.keys()):
        raise Exception('These two input files have different dimensions.')

    # verify that your variables all have the same shape
    for var in root.variables.keys():
        if root.variables[var].shape != root2.variables[var].shape:
            raise Exception('The variable ' + var + ' is not the same shape in both files.')

    # loop through all the variables in the outfile and perform the average
    for var in root.variables.keys():
        root.variables[var][:] = (root.variables[var][:] + root2.variables[var][:]) / 2.0

    root.close()


if __name__ == "__main__":
    main()
