
ID = NUMBER_TO_CHANGE

 # USER INPUT=============================================================================
# directory where .cont6 model is located
dir = '/data/scratch/cvillong/Projects/LLNL/'
#dir = '/data/scratch/cvillong/Fitting/ForPeople/KevinVincent/'

# directory where data file is located
datadir = dir + '0p2mm/'
#datadir = dir

# base continuity model
modelFile = 'pt68_9478'
#modelFile = 'pt68_9478-gp3'
#modelFile = 'swine_lesion1'

#data_file = 'pt68_9478_fk_verts_0p2mm_chunk_%.6d.txt'%ID
data_file = 'pt68_9478_fk_verts_0p2mm_NoHeader_reduced_chunk-_%.6d.txt'%ID
#data_file = 'data_01mm.txt'

case = 'remesh_%.6d'%ID
#case = 'remesh_reduced_unfilt_%.6d'%ID
#case = 'swine'

load_files = 0
load_calcmesh = 0

load_files = 0
load_calcmesh = 0

output = datadir + 'XiTable_' + modelFile + '_' + case + '.txt'

# xi calculation subdivision
#subdiv = '5'
subdiv = '4'
#subdiv = '5'

# USER INPUT=============================================================================

print 'Loading model %s'%(dir + modelFile + '.cont6')
self.Load_File(dir + modelFile + '.cont6', log=0)
print 'Will calculate xi coordinates at a resolution of %s subdivisions per element direction!\n'%subdiv
self.LoadContModule(('fitting',));
print 'Loading fitting data file %s'%(datadir+data_file)
self.LoadFittingData(datadir + data_file, log=0)

self.auto_update_dimensions()
self.Send(None, log=0)


if load_files:
    # load nodes form from file
    print 'Importing nodes from %s'%(dir+'nodes_'+modelFile2+'.txt')
    print 'Importing elements from %s'%(dir+'elems_'+modelFile2+'.txt')
    nodes = self.stored_data.nodes.obj
    nodes.loadTableFromFile(dir+'nodes_'+modelFile2+'.txt')
    #nodes.loadTableFromFile(folder + NodesFileStr, preserveLabels = False)
    self.stored_data.store(nodes)

    # load elements form from file
    elems = self.stored_data.elem.obj
    elems.loadTableFromFile(dir+'elems_'+modelFile2+'.txt')
    #nodes.loadTableFromFile(folder + NodesFileStr, preserveLabels = False)
    self.stored_data.store(elems)

if load_calcmesh:
    # text files with precalculated lines and faces for CalculateMesh
    file_lines = dir + 'lines_' + modelFile2 + '.txt'
    file_faces= dir + 'faces_'+modelFile2+'.txt'
    print 'Importing calculated lines from %s'%(file_lines)
    print 'Importing calculated faces from %s'%(file_faces)

    self.CalcMeshFast([('Import from table...', file_lines), \
    ('Do not Calculate', None), ('Import from table...', file_faces),  \
    ('Angle change scale factors (for nodal derivs wrt angle change)', None)], log=0)
    
else:
    self.CalcMeshFast([('Calculate', None), ('Do not Calculate', None), ('Calculate', None), \
    ('Angle change scale factors (for nodal derivs wrt angle change)', None)], log=1)

# 2D surface fit
# self.FitData({'preapplyConstraints':0,'calcErrorStr':'error = (data-x)*weight\n','geomDataIsCart':1,'err':'1.00e-006','selections':{'Coordinate 2': 'coord_2', 'Coordinate 3': 'coord_3', 'Coordinate 1': 'coord_1'},'initializeFields':0,'iterationLimit':'10','fit_selections':(),'xi_options':{'dpError': '50.0', 'errorType': 'sd', 'datalist': 'all', 'sdError': '50.0', 'optimizeVars': 0, 'filterData': True, 'calcType': 'on 2D surface', 'showTable': True, 'subdivisions': subdiv, 'itmax': '50', 'vmax': '1.5', 'elemlist': 'all', 'ignorePoints': 1, 'tolerance': '1e-006', 'dpErrorType': 'sd', 'newtonUpdate': 1, 'outputPath':output},'output_type':'Update nodal variable'}, log=0)

# 3D volume fit
self.FitData({'preapplyConstraints':0,'calcErrorStr':'error = (data-x)*weight\n','geomDataIsCart':1,'err':'1.00e-006','selections':{'Coordinate 2': 'coord_2', 'Coordinate 3': 'coord_3', 'Coordinate 1': 'coord_1'},'initializeFields':0,'iterationLimit':'10','fit_selections':(),'xi_options':{'dpError': '50.0', 'errorType': 'sd', 'datalist': 'all', 'sdError': '50.0', 'optimizeVars': 1, 'filterData': True, 'calcType': 'in 3D volume', 'showTable': True, 'subdivisions': subdiv, 'itmax': '50', 'vmax': '1.5', 'elemlist': 'all', 'ignorePoints': 1, 'tolerance': '1e-006', 'dpErrorType': 'sd', 'newtonUpdate': 1, 'outputPath':output},'output_type':'Update nodal variable'}, log=0)

# 3D volume fit with labels
#~ self.FitData({'preapplyConstraints':0,'calcErrorStr':'error = (data-x)*weight\n','geomDataIsCart':1,'err':'1.00e-006','selections':{'Coordinate 2': 'coord_2', 'Coordinate 3': 'coord_3', 'Coordinate 1': 'coord_1'},'initializeFields':0,'iterationLimit':'10','fit_selections':(),'xi_options':{'dpError': '50.0', 'errorType': 'sd', 'datalist': 'LV;default;ST', 'sdError': '50.0', 'optimizeVars': 1, 'filterData': True, 'calcType': 'in 3D volume', 'showTable': True, 'subdivisions': subdiv, 'itmax': '50', 'vmax': '1.5', 'elemlist': 'LV;default;ST', 'ignorePoints': 1, 'tolerance': '1e-006', 'dpErrorType': 'sd', 'newtonUpdate': 1, 'outputPath':output},'output_type':'Update nodal variable'}, log=0)

print 'Saved xi table to %s!'%(output)
