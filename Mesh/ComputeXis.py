# Name: Christopher Villongco
# Date: September 5, 2012
# This script will compute the Xi coordinates of loaded data points within the volume of a 3D FE mesh


# USER INPUT=============================================================================
# directory where .cont6 model is located
dir = '/home/cvillong/Human Models/BiV2/'
#dir = '/home/cvillong/Human Models/BiV6/'
#dir = '/data/scratch/cvillong/Output/EP/tT/BiV6/8448-3/fitAT/'
dir ='/data/scratch/cvillong/Fibers/HNF2/'
dir ='/data/scratch/cvillong/Models/BiV1/'
dir = '/data/scratch/cvillong/Models/BiV4/'
#dir = '/data/scratch/cvillong/Models/BiV5/'
#dir = '/data/scratch/cvillong/Models/BiV2/8448-2/'
#dir = '/data/scratch/cvillong/Models/BiV6/8448-3/'
#dir = '/data/scratch/cvillong/Models/BiV7/8448-6/'
#dir = '/data/scratch/cvillong/Models/BiV8/'
dir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV1/8448-4/allParams-2/iter1/set180/'
dir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV2/8448-2/allParams-1/iter1/set37/'
dir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV3/8448-7/allParams-2/iter1/set82/'
dir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV4/8448-2/allParams-1/iter1/set461/'
dir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV5/8448-12/allParams-1/iter1/set229/'
dir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV6/8448-3/allParams-1/iter1/set468/'
dir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV7/8448-6/allParams-1/iter1/set213/'
dir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV8/8448-5/allParams-1/iter1/set229/'
dir = '/home/cvillong/Fitting/Dog/'
dir = '/data/scratch/cvillong/Models/ExV1/'
dir = '/data/scratch/cvillong/Models/BiVavg/'
dir = '/data/scratch/cvillong/Models/sham/'
dir = '/data/scratch/cvillong/Models/ExV1/'
dir = '/home/cvillong/For People/MelodyDong/tacheartdtdataandmesh/'
dir = '/home/cvillong/Scripts/NBCR/'
dir = '/data/scratch/cvillong/Fibers/'


# directory where data file is located
datadir = '/data/scratch/cvillong/Output/EP/fk/BiV6/8448-2/CRT-tt-max--5e-3--1/'
datadir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV6/8448-3/batchTest-3/iter1/set49/'
datadir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV2/8448-2/Conds-3/iter1/set225/'
datadir = '/data/scratch/cvillong/Fitting/'
datadir = dir
#datadir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV1/8448-4/allParams-2/iter1/set180/'
#datadir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV4/8448-2/allParams-1/iter1/set91/'
#datadir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiV5/8448-12/allParams-1/iter1/set229/'
#datadir = '/data/scratch/cvillong/Output/EP/tT-epi-HF/BiVavg/8448-1/opt-BiV/iter7/set1/'

# base continuity model
modelFile = 'HNF2_1056_FA2DT_prefit-no-data'
modelFile = 'BiV2_128_EP_fk_tt-max--0p5e-1--3_AT-prefit'
#modelFile = 'BiV6_128_biv-cpu-1_prefit_noData'
#modelFile = 'BiV6_128_AT-prefit'
modelFile = 'BiV2_128_AT_prefit'
modelFile = 'HNF2_1056_FA2DT_prefit-no-data'
modelFile = 'HNF2_1056-2_FA2DT_prefit'
#modelFile = 'HNF2_8448-2_FA2DT_prefit'
modelFile = 'BiV1_Model_Fibers_Deflation'
modelFile = 'BiV1_132-4'
modelFile = 'BiV1_128'
modelFile = 'BiV4_128'
#modelFile = 'BiV5_128'
#modelFile = 'BiV3_128'
#modelFile = 'BiV2_128'
#modelFile = 'BiV6_128'
#modelFile = 'BiV7_128'
#modelFile = 'BiV8_CT_ED_DT'
modelFile = 'BiV1_128_prefitAT'
modelFile = 'BiV2_128_prefitAT'
modelFile = 'BiV3_128_prefitAT'
modelFile = 'BiV4_128_prefitAT'
modelFile = 'BiV5_128_prefitAT'
modelFile = 'BiV6_128_prefitAT'
modelFile = 'BiV7_128_prefitAT'
modelFile = 'BiV8_128_prefitAT'
modelFile = 'D0912_DS'
modelFile = 'BiVavg_128_prefitAT'
modelFile = 'sham_model_DT'
modelFile = 'sham_model_DT_prefit'
modelFile = 'sham_model_512_DT_prefit'
modelFile = 'ExV1_24576Linear_cm'
modelFile = 'TAC_20140617_2corrected_Transrot'
modelFile = 'Sham_20140605_6corrected_Transrot'
modelFile = '3D_unfitted_mirror_fitted'
modelFile = 'BiV5-LV_784e_hole_final_labeled_fibers_prefit'

#data_file = 'data_DT_HNF2_576_FA2DT_9-9-9'
# data_file = 'data_BiV6_1056_biv-cpu-1_444-grid-out.csv'
# data_file = 'data_BiV2_8448_EP_fk_tt-max--0p5e-1--3_40_333-grid-out.txt'
# data_file = 'data_BiV6_1056_optEP-40-gpu-1_444-grid-out.txt'
data_file = 'data_BiV2_8448-2_CRT-tt-max--5e-3--1.txt'
data_file = 'data_optEP_AT_240_BiV6_8448-3_EP_tT_333.txt'
data_file = 'data_BiV6_8448-3_EP_tT-CRT_CRT-1_nodal_AT_out_333.txt'
data_file = 'data_optEP_AT_49_BiV6_8448-3_EP_tT-epi-HF_333-grid-out.txt'
data_file = 'data_optEP_AT_225_BiV2_8448-2_EP_tT-epi-HF_333-grid-out.txt'
data_file = 'data_DT_HNF2_576_FA2DT_9-9-9.txt'
data_file = 'data_DT_HNF2_1152_FA2DT_5-5-9.csv'
data_file = 'data_HNF2_1056_FA2DT_postfit_cubicGeom_linearField_12-4-4-4.txt'
data_file = 'data_ListXis_8448-4_EP_tT-epi-HF_gaussPoints-grid-out.txt'
data_file = 'data_optEP_AT_180_BiV1_8448-4_EP_tT-epi-HF_gaussPoints-grid-out.txt'
data_file = 'data_optEP_AT_91_BiV4_8448-2_EP_tT-epi-HF_gaussPoints-grid-out.txt'
#data_file = 'data_optEP_AT_229_BiV5_8448-12_EP_tT-epi-HF_gaussPoints-grid-out.txt'
#data_file = 'data_BiV3_8448-7_EP_tT-epi-HF_gaussPoints-grid-out.txt'
#data_file = 'data_BiV2_8448-2_EP_tT-epi-HF_gaussPoints-grid-out.txt'
#data_file = 'data_BiV6_8448-3_EP_tT-epi-HF_gaussPoints-grid-out.txt'
#data_file = 'data_BiV7_8448-6_EP_tT-epi-HF_gaussPoints-grid-out.txt'
#data_file = 'data_BiV8_8448-5_EP_tT-epi-HF_gaussPoints-grid-out.txt'
data_file = 'data_BiV1_8448-4_EP_tT-epi-HF_allParams-2_iter1_set180-nodal-ATs.txt'
data_file = 'data_BiV2_8448-2_EP_tT-epi-HF_allParams-1_iter1_set37-nodal-ATs.txt'
data_file = 'data_BiV3_8448-7_EP_tT-epi-HF_allParams-2_iter1_set82-nodal-ATs.txt'
data_file = 'data_BiV4_8448-2_EP_tT-epi-HF_allParams-1_iter1_set461-nodal-ATs.txt'
data_file = 'data_BiV5_8448-12_EP_tT-epi-HF_allParams-1_iter1_set229-nodal-ATs.txt'
data_file = 'data_BiV6_8448-3_EP_tT-epi-HF_allParams-1_iter1_set468-nodal-ATs.txt'
data_file = 'data_BiV7_8448-6_EP_tT-epi-HF_allParams-1_iter1_set213-nodal-ATs.txt'
data_file = 'data_BiV8_8448-5_EP_tT-epi-HF_allParams-1_iter1_set229-nodal-ATs.txt'
data_file = 'data_logDT.txt'
data_file = 'data_optEP_AT_1_BiVavg_8448-1_EP_tT-epi-HF_gaussPoints-grid-out.txt'
data_file = 'data_BiVavg_8448-1_EP_tT-epi-HF_gaussPoints-grid-out.txt'
data_file = 'sham_DTform2.txt'
data_file = 'DT_data_fit2_cm.txt'
data_file = 'TAC_20140617_DTform.txt'
data_file = 'Sham_20140605_DTform.txt'
data_file = 'DTFitting_DTform_d_roty90.txt'
data_file = 'data_ListSS-3_LV_biv5_rcc128e_BM_gaussPoints_xi_clean.txt'

case = 'fibers'
#case = 'nAT'

load_files = 0
load_calcmesh = 0

case = 'fibers'
#case = 'nAT'

load_files = 0
load_calcmesh = 0
# if load_files = 1
# specify continuity model to compute Xi locations in if loading files and calcmesh
# modelFile2 = 'BiV2_1056_prefit'
# modelFile2 = 'D6_DT_prefit'

output = datadir + 'XiTable_' + modelFile + case + '.txt'

# xi calculation subdivision
subdiv = '8'
subdiv = '10'
subdiv = '5'
#subdiv = '6'
#subdiv = '8'
#subdiv = '2'

# USER INPUT=============================================================================

print 'Loading model %s'%(dir + modelFile + '.cont6')
self.Load_File(dir + modelFile + '.cont6', log=0)

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
