import os 
import shutil

fileslists_path = '/cluster/work/cvl/qimaqi/3dv_gaussian/ShapenetRender_more_variation/filelists/'
for files_list in os.listdir(fileslists_path):
    file_name = files_list.split('.')[0]
    os.makedirs(file_name, exist_ok=True)
    shutil.copy(os.path.join(fileslists_path, files_list), os.path.join(file_name, files_list))
