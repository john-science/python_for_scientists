
import sys
from netCDF4 import Dataset


def main():
    print(extract_cell_from_3d_ioapi(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), layer=0, var=None))


def extract_cell_from_3d_ioapi(file_path, row, col, layer=0, var=None):
    '''Extract a single grid cell from a GRIDDED IOAPI NetCDF file.
    If you don't provide a layer, we'll assume you want the ground layer.
    If you don't provide a variable name, we'll assume you want all of them.
    This will return a dictionary of each variable's values across the time dimension.
    '''
    # opening file as read-only
    root = Dataset(file_path, 'r', format='NETCDF3_CLASSIC')

    # find the variable names (remove TFLAG)
    keys = root.variables.keys()
    keys.remove('TFLAG')

    if var is not None:
        # if variable name is provided, and exists in the file
        if var not in keys:
            raise Exception('The variable ' + str(variable) + ' does not exist.')
        else:
            return {var: root.variables[var][:, layer, row, col]}
    else:
        # if variable name is not provided, return a dictionary of all variables
        results = {}
        for key in keys:
            results[key] = root.variables[key][:, layer, row, col]

        return results


if __name__ == "__main__":
    main()
