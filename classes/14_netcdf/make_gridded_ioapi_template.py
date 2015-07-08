
import sys
from netCDF4 import Dataset


def main():
    copy_gridded_ioapi_to_empty(sys.argv[1], sys.argv[2])


def copy_gridded_ioapi_to_empty(input_path, output_path):
    '''Copy a GRIDDED IOAPI NetCDF file (NETCDF3_CLASSIC)
    to an empty NetCDF file that has the same structure,
    but the variables are empty of data.'''
    # open input NetCDF file
    fin = Dataset(input_path, 'r', format='NETCDF3_CLASSIC')

    # read variables
    fin_var = {}
    for var in fin.variables:
        fin_var[var] = [var, fin.variables[var].units, fin.variables[var].var_desc]
    # read attributes
    fin_attr = {}
    for attr in fin.ncattrs():
        fin_attr[attr] = getattr(fin, attr)

    # open output NetCDF file
    fout = Dataset(output_path, 'w', format='NETCDF3_CLASSIC')
    
    # create the 6 GRIDDED IOAPI dimensions
    TSTEP = fout.createDimension('TSTEP', None)
    DATE_TIME = fout.createDimension('DATE-TIME', 2)
    LAY = fout.createDimension('LAY', fin.NLAYS)
    VAR = fout.createDimension('VAR', fin.NVARS)
    ROW = fout.createDimension('ROW', fin.NROWS)
    COL = fout.createDimension('COL', fin.NCOLS)

    # close input file
    fin.close()

    # variable and attribute definitions
    TFLAG = fout.createVariable('TFLAG', 'i4', ('TSTEP', 'VAR', 'DATE-TIME'))
    TFLAG.units = '<YYYYDDD,HHMMSS>'
    TFLAG.long_name = 'TFLAG'
    TFLAG.var_desc = 'Timestep-valid flags:  (1) YYYYDDD or (2) HHMMSS'

    # remaining variables and attribute definitions
    for key in fin_var:
        species = key
        if species == 'TFLAG':
            continue
        fout.createVariable(species, 'f4', ('TSTEP', 'LAY', 'ROW', 'COL'))
        fout.variables[species].long_name = species
        fout.variables[species].units = fin_var[species][1]
        fout.variables[species].var_desc = fin_var[species][2]

    # global attributes
    for name in fin_attr:
        setattr(fout, name, fin_attr[name])


if __name__ == '__main__':
    main()
