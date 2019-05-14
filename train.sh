
#export PYTHONPATH=~/caffe/python:$PYTHONPATH
python3 -m pip install  h5py
cd /home/timing/Git_Repos_Summer/CSRNet-pytorch 
python3 train.py train.json val.json 0 0
