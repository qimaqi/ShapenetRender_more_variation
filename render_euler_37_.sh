#!/bin/bash
#SBATCH --output=./joblogs/shapenet_37_%j.log      # Redirect stdout to a log file
#SBATCH --error=./joblogs/shapenet_37_%j.error     # Redirect stderr to a separate 


module load eth_proxy
module load stack/2024-06
module load python_cuda/3.11.6
# export PYTHONPATH=$HOME/.local/lib64/python3.11/site-packages:$PYTHONPATH
#  export PYTHONPATH=$HOME/.local/lib64/python3.11/site-packages:$PYTHONPATH


python3 render_batch.py --filelist_dir=filelists_037_  --debug=True
# sbatch --output=sbatch_log/37_.out  --ntasks=16 --mem-per-cpu=4g --time=4-0 --gpus=rtx_4090:1 filelists_037_.sh
# 874537