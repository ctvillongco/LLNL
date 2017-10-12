# Name: Christopher Villongco
# Date: February 1, 2016
# This script lists biomechanics quantities from a model to a text file
# It will mainly be used to output dY_dMatl for fiber angle to DT conversion

import sys
import os
from numpy import *
import numpy
import time
from time import localtime, strftime
import shutil

ID = NUMBER_TO_CHANGE

########################################################################################
################################## BEGIN USER INPUT ####################################
########################################################################################

###############################
###### OUTPUT DIRECTORY #######
###############################
# Directory of input and output files
#workingDir = '/data/scratch/cvillong/Projects/LLNL/ComputeXis/0p2mm/'
workingDir = '/data/scratch/cvillong/Projects/LLNL/0p2mm/xitables/'

###############################
######  CONTINUITY MODEL ######
###############################
modelDir = '/data/scratch/cvillong/Projects/LLNL/'
modelFile = 'pt68_9478_BM'

infilename  = 'ListXis_pt68_9478_remesh_%.6d'%ID
outfilename = 'ListdYdMatl_pt68_9478_remesh_%.6d'%ID

# or set gaussPoints flag to 1 if not a regular grid
# Note: there is currently a bug with list stress/strain in outputting dY_dMatl;
# the values are incorrect at grid points, but correct at gauss points
gaussPoints = 0
ReadfromLocations = 1

###############################
######   SELECT XI GRID  ######
###############################
xi1 = 5
xi2 = 5
xi3 = 5

###############################
######  SELECT ELEMENTS  ######
###############################
# elemlist = range(1,238)
elemlist = None

###############################
######  SELECT VARIABLES ######
###############################
varsWanted = ['xi', 'Y', 'dY_dMatl']

########################################################################################
#################################### END USER INPUT ####################################
########################################################################################


########################################################################################
####################################      START     ####################################
########################################################################################

print "\nBegin script (%s)"%(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
time_start = time.clock()
self.Load_File(modelDir + modelFile + '.cont6', log=0)
self.auto_update_dimensions()
self.Send(None, log=0)
self.CalcMesh([('Calculate', None), ('Do not Calculate', None), ('Calculate', None), ('Global arc length scale factors (for nodal derivs wrt arc lengths)', None)], log=0)
self.CompileBM()

if gaussPoints:
    xilist = None
    filename = outfilename + '_gaussPoints' + '.txt'
    print "Outputting list stress/strain at gauss points! :)\n"

    self.LstressAndStrain({'outputPath':workingDir + filename,\
                       'elemlist':elemlist,'inputPath':None,\
                       'varsWanted':varsWanted,\
                       'xilist':xilist}, log=0)

elif ReadfromLocations:
    print "Reading locations from file"
    elemlist = None
    xilist = None
    #filename = outfilename + '_xi' + '.txt'
    self.LstressAndStrain({'outputPath':workingDir + outfilename + '.txt',\
                           'elemlist':elemlist,'inputPath':workingDir + infilename + '.txt',\
                           'varsWanted':varsWanted,\
                           'xilist':xilist}, log=0)

#self.LstressAndStrain({'outputPath':None,'elemlist':None,'inputPath':'/Users/ctvillongco/Dropbox/Research/InSilicoMed/Projects/Thoratek/Meshes/Fibers/ListXi_LV_biv5_rcc128e_BM.txt','varsWanted':['xi', 'Y', 'dY_dMatl'],'xilist':None}, log=0)

else:
    # generate list of xi points 
    start = 0.0
    end = 1.0
    xilist = []
    xi1list = numpy.linspace(start,end,xi1,endpoint=True)
    xi2list = numpy.linspace(start,end,xi2,endpoint=True)
    xi3list = numpy.linspace(start,end,xi3,endpoint=True)

    for j in range(len(xi1list)):
        for k in range(len(xi2list)):
            for m in range(len(xi3list)):
                xilist.append([xi1list[j], xi2list[k], xi3list[m]])
    
    filename = outfilename + '_%s-%s-%s'%(xi1,xi2,xi3) + '.txt'

    self.LstressAndStrain({'outputPath':workingDir + filename,\
                           'elemlist':elemlist,'inputPath':None,\
                           'varsWanted':varsWanted,\
                           'xilist':xilist}, log=0)

print "\nSaved %s to %s"%(outfilename, workingDir)
print "Completed in %s seconds!\n"%(time.clock()-time_start)
print "\nDone (%s)"%(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
