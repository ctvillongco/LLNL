# Christopher Villongco
# February 8, 2016

# This script will convert a xi table of element locations of data points to a form for interpolating mesh quantities
# at those element locations using List Stress/Strain

import os
import numpy
import pprint

ID = NUMBER_TO_CHANGE

##################################################
############### Specify Inputs  ##################
##################################################

#cwd = '/data/scratch/cvillong/Projects/LLNL/ComputeXis/0p2mm/'
cwd = '/data/scratch/cvillong/Projects/LLNL/0p2mm/xitables/'

meshname = 'pt68_9478_remesh'

# input file
file_xi_table = 'XiTable_'+meshname+'_%.6d.txt'%ID

# output files
file_ListElemPoints = 'ListXis_'+meshname+'_%.6d.txt'%ID

col_names = ['Xi1','Xi2','Xi3','Distance','Dot Product','Element','Data','Index']
col_formats = [numpy.float, numpy.float, numpy.float, numpy.float, numpy.float, numpy.int, numpy.int, numpy.int]

##################################################
############### Load input file ##################
##################################################

os.chdir(cwd)
print "Working on directory ", cwd

fid_xitable = open(file_xi_table,'rb')

dt = numpy.dtype({
     'names': col_names,
     'formats': col_formats})
           
xitable = numpy.loadtxt(fid_xitable, skiprows=1, dtype=dt)

#####################################################
############### Prepare output file 1 ###############
#####################################################

file = open(file_ListElemPoints, 'wb')
file.write('Element\txi(1)\txi(2)\txi(3)\tPoints\n')
for j in range(len(xitable)):
    cl = xitable[j]
    file.write('%d\t%.6f\t%.6f\t%.6f\t%d\n' %(cl[5],cl[0],cl[1],cl[2],j+1))
file.close()
