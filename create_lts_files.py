import os 
import glob 
import numpy as np 
import json 
from tqdm import tqdm 

shapenet_files_path = '/cluster/work/cvl/qimaqi/ws_dataset/shapenet/ShapeNetCore.v1'
cat_ids = os.listdir(shapenet_files_path)
# only use folder start with 0
cat_ids = [x for x in cat_ids if x.startswith('0')]
cat_ids =  [x for x in cat_ids if not x.endswith('.csv')]

no_texture_objs = {}
for cat_id in tqdm(cat_ids):
    obj_list = []
    no_texture_objs[cat_id] = []
    obj_ids = os.listdir(os.path.join(shapenet_files_path, cat_id))
    for obj_id in obj_ids:
        obj_path = os.path.join(shapenet_files_path, cat_id, obj_id)
        if os.path.isdir(obj_path):
            obj_files = os.listdir(obj_path)
            model_files = [x for x in obj_files if x.endswith('.obj')]
            if len(model_files) > 0:
                obj_list.append(obj_id)
                if 'images' not in obj_files:
                    no_texture_objs[cat_id].append(obj_id)

    # save to filelists as .lst 
    np.savetxt(os.path.join('./filelists/', cat_id + '.lst'), obj_list, fmt='%s')

json.dump(no_texture_objs, open('no_texture_objs.json', 'w'), indent=4)
    