# Problem Set 1 - Solutions

## Writing

 * Coming Soon

## Reading

    from netCDF4 import Dataset
    import numpy as np
    
    def print_totals(ncffile):
        """print emissions totaled by major groups"""
        # open NetCDF file
        root = Dataset(ncffile, 'r')
    
        # print individual species totals
        for spec in root.variables:
            if spec == 'TFLAG':
                continue
            try:
                total = np.sum(root.variables[spec][:])
                print(spec + ' = ' + str(total) + ' (' + root.variables[spec].units.strip() + ')')
            except Exception as e:
                print("Error with %s: %s" % (spec, e))
    
        root.close()

## IOAPI

 * Coming Soon

[Back to Problem Set]()
