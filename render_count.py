import os
import sys
import time
from joblib import Parallel, delayed
import argparse
import trimesh 
from plyfile import PlyData, PlyElement


#
parser = argparse.ArgumentParser()
parser.add_argument('--model_root_dir', type=str, default="/cluster/work/cvl/qimaqi/ws_dataset/shapenet/ShapeNetCore.v1")
parser.add_argument('--render_root_dir', type=str, default="/cluster/work/cvl/qimaqi/ws_dataset/shapenet/ShapeNetCore.v1/render")
parser.add_argument('--filelist_dir', type=str, default="./filelists")
parser.add_argument('--blender_location', type=str, default="/cluster/work/cvl/qimaqi/3dv_gaussian/blender_install/blender-3.6.13-linux-x64/blender")
parser.add_argument('--num_thread', type=int, default=10, help='1/3 of the CPU number')
parser.add_argument('--shapenetversion', type=str, default="v1", help='v1 or v2')
parser.add_argument('--debug', type=bool, default=False)
FLAGS = parser.parse_args()

model_root_dir = FLAGS.model_root_dir
render_root_dir = FLAGS.render_root_dir
filelist_dir = FLAGS.filelist_dir

# cat_ids = {
#         "watercraft": "04530566",
#         "rifle": "04090263",
#         "display": "03211117",
#         "lamp": "03636649",
#         "speaker": "03691459",
#         "cabinet": "02933112",
#         "chair": "03001627",
#         "bench": "02828884",
#         "car": "02958343",
#         "airplane": "02691156",
#         "sofa": "04256520",
#         "table": "04379243",
#         "phone": "04401088"
#     }

def count_obj(model_root_dir, cat_id, obj_id):
	print("Start %s %s" % (cat_id, obj_id))
	if FLAGS.shapenetversion == "v2":
		objpath = os.path.join(model_root_dir, cat_id, obj_id, "models", "model_normalized")
	else:
		objpath = os.path.join(model_root_dir, cat_id, obj_id, "model.obj") #for v1

	obj_save_dir = os.path.join(render_root_dir, cat_id, obj_id)
	os.makedirs(obj_save_dir, exist_ok=True)

	if os.path.exists(os.path.join(obj_save_dir, 'image.zip')):
		print("Exist!!!, skip %s %s" % (cat_id, obj_id))
		return 1
	else:
		return 0 

count=0
for filename in sorted(os.listdir(filelist_dir)):
	if filename.endswith(".lst"):
		cat_id = filename.split(".")[0]
		file = os.path.join(filelist_dir, filename)
		lst = []
		with open(file) as f:
			content = f.read().splitlines()
			for line in content:
				if line != "":
					lst.append(line)

		model_root_dir_lst = [model_root_dir for i in range(len(lst))]
		cat_id_lst = [cat_id for i in range(len(lst))]
		
		for model_root_dir, cat_id, obj_id in zip(model_root_dir_lst, cat_id_lst, lst):
			count+=count_obj(model_root_dir, cat_id, obj_id)
	
print("Finished ", count)

