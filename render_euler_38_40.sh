#!/bin/bash
#SBATCH --output=./joblogs/shapenet_38_40%j.log      # Redirect stdout to a log file
#SBATCH --error=./joblogs/shapenet_38_40%j.error     # Redirect stderr to a separate 


module load eth_proxy
module load stack/2024-06
module load python_cuda/3.11.6
# export PYTHONPATH=$HOME/.local/lib64/python3.11/site-packages:$PYTHONPATH
#  export PYTHONPATH=$HOME/.local/lib64/python3.11/site-packages:$PYTHONPATH


python3 render_batch.py --filelist_dir=filelists_038_040  # --debug=True
# sbatch --output=sbatch_log/38_40.out  --ntasks=16 --mem-per-cpu=4g --time=4-0 --gpus=rtx_2080:1 render_euler_38_40.sh
# 949815