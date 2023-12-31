# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:02:29 2023

@author: Pauline
"""


import elikopy 
import elikopy.utils
from elikopy.individual_subject_processing import report_solo



f_path = "/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/alcoholic_study/"
dic_path="/home/users/q/d/qdessain/Script_python/fixed_rad_dist.mat"

#ALCOHOLIC PATIENTS
#patient_list = ["sub41_E1", "sub27_E1", "sub32_E1", "sub09_E1", "sub45_E1", "sub48_E1", "sub21_E1", "sub05_E1", "sub15_E1", "sub11_E1", "sub46_E1", "sub31_E1", "sub16_E1", "sub26_E1", "sub50_E1", "sub22_E1", "sub47_E1", "sub44_E1", "sub02_E1", "sub53_E1", "sub18_E1", "sub01_E1", "sub34_E1", "sub35_E1", "sub51_E1", "sub23_E1", "sub04_E1", "sub38_E1", "sub19_E1", "sub28_E1", "sub24_E1", "sub33_E1", "sub37_E1", "sub29_E1", "sub14_E1", "sub13_E1", "sub36_E1", "sub12_E1", "sub06_E1", "sub43_E1", "sub40_E1", "sub45_E3", "sub20_E1", "sub39_E1", "sub17_E1", "sub52_E1", "sub42_E1", "sub08_E1", "sub10_E1", "sub30_E1", "sub32_E2", "sub29_E2", "sub53_E2", "sub31_E2", "sub39_E2", "sub07_E2", "sub45_E2", "sub13_E2", "sub24_E2", "sub42_E2", "sub11_E2", "sub25_E2", "sub21_E2", "sub08_E2", "sub01_E2", "sub09_E2", "sub50_E2", "sub22_E2", "sub34_E2", "sub30_E2", "sub37_E2", "sub12_E2", "sub20_E2", "sub17_E2", "sub14_E2", "sub04_E2", "sub05_E2", "sub06_E2", "sub33_E2", "sub35_E2", "sub43_E2", "sub27_E2", "sub28_E2", "sub19_E2", "sub15_E2", "sub26_E2", "sub02_E2", "sub40_E2", "sub18_E2", "sub52_E2", "sub51_E2", "sub36_E2", "sub48_E2", "sub46_E2", "sub03_E2", "sub41_E2", "sub27_E3", "sub34_E3", "sub09_E3", "sub02_E3", "sub30_E3", "sub17_E3", "sub36_E3", "sub22_E3", "sub20_E3", "sub39_E3", "sub03_E3"]


#CONTROLS
#patient_list = ['sub67_E1', 'sub61_E1', 'sub63_E1', 'sub58_E1', 'sub64_E1', 'sub56_E1', 'sub54_E1', 'sub59_E1', 'sub73_E1', 'sub68_E1', 'sub72_E1', 'sub57_E1', 'sub62_E1', 'sub65_E1', 'sub70_E1', 'sub55_E1', 'sub71_E1', 'sub69_E1', 'sub66_E1', 'sub60_E1', 'sub60_E2', 'sub61_E2', 'sub54_E2', 'sub71_E2', 'sub66_E2', 'sub67_E2', 'sub63_E2', 'sub57_E2', 'sub68_E2', 'sub65_E2', 'sub69_E2', 'sub73_E2', 'sub58_E2', 'sub59_E2', 'sub55_E2', 'sub62_E2', 'sub72_E2', 'sub64_E2', 'sub70_E2']

#All patients

patient_list = ["sub41_E1", "sub27_E1", "sub32_E1", "sub09_E1", "sub45_E1", "sub48_E1", "sub21_E1", "sub05_E1", "sub15_E1", "sub11_E1", "sub46_E1", "sub31_E1", "sub16_E1", "sub26_E1", "sub50_E1", "sub22_E1", "sub47_E1", "sub44_E1", "sub02_E1", "sub53_E1", "sub18_E1", "sub01_E1", "sub34_E1", "sub35_E1", "sub51_E1", "sub23_E1", "sub04_E1", "sub38_E1", "sub19_E1", "sub28_E1", "sub24_E1", "sub33_E1", "sub37_E1", "sub29_E1", "sub14_E1", "sub13_E1", "sub36_E1", "sub12_E1", "sub06_E1", "sub43_E1", "sub40_E1", "sub45_E3", "sub20_E1", "sub39_E1", "sub17_E1", "sub52_E1", "sub42_E1", "sub08_E1", "sub10_E1", "sub30_E1", "sub32_E2", "sub29_E2", "sub53_E2", "sub31_E2", "sub39_E2", "sub07_E2", "sub45_E2", "sub13_E2", "sub24_E2", "sub42_E2", "sub11_E2", "sub25_E2", "sub21_E2", "sub08_E2", "sub01_E2", "sub09_E2", "sub50_E2", "sub22_E2", "sub34_E2", "sub30_E2", "sub37_E2", "sub12_E2", "sub20_E2", "sub17_E2", "sub14_E2", "sub04_E2", "sub05_E2", "sub06_E2", "sub33_E2", "sub35_E2", "sub43_E2", "sub27_E2", "sub28_E2", "sub19_E2", "sub15_E2", "sub26_E2", "sub02_E2", "sub40_E2", "sub18_E2", "sub52_E2", "sub51_E2", "sub36_E2", "sub48_E2", "sub46_E2", "sub03_E2", "sub41_E2", "sub27_E3", "sub34_E3", "sub09_E3", "sub02_E3", "sub30_E3", "sub17_E3", "sub36_E3", "sub22_E3", "sub20_E3", "sub39_E3", "sub03_E3",'sub67_E1', 'sub61_E1', 'sub63_E1', 'sub58_E1', 'sub64_E1', 'sub56_E1', 'sub54_E1', 'sub59_E1', 'sub73_E1', 'sub68_E1', 'sub72_E1', 'sub57_E1', 'sub62_E1', 'sub65_E1', 'sub70_E1', 'sub55_E1', 'sub71_E1', 'sub69_E1', 'sub66_E1', 'sub60_E1', 'sub60_E2', 'sub61_E2', 'sub54_E2', 'sub71_E2', 'sub66_E2', 'sub67_E2', 'sub63_E2', 'sub57_E2', 'sub68_E2', 'sub65_E2', 'sub69_E2', 'sub73_E2', 'sub58_E2', 'sub59_E2', 'sub55_E2', 'sub62_E2', 'sub72_E2', 'sub64_E2', 'sub70_E2']

#patient_list = ['sub67_E1', 'sub67_E2']
 
#patient_list = ["sub55_E2", "sub59_E2", "sub62_E2", "sub72_E2"]
 
#patient_list = ["sub09_E1", "sub09_E2", "sub19_E1", "sub19_E2", "sub54_E2", "sub55_E1"]
                                  
study = elikopy.core.Elikopy(f_path, slurm=True, slurm_email='pauline.hermans@student.uclouvain.be', cuda=False)

# =============================================================================
# Patient list
# =============================================================================
#study.patient_list()

# =============================================================================
# Tractography
# =============================================================================
study.tracking(folder_path = f_path, patient_list_m=patient_list, max_angle = 25, streamline_number = 100000, cutoff =0.09, output_filename = "tracto_25_100000_09")



study.export(tractography=True, raw=True, preprocessing=True, dti=True, noddi=True, diamond=True, mf=True, wm_mask=True, report=False, preprocessed_first_b0=True, patient_list_m=None)
elikopy.utils.merge_all_reports(f_path)