sudo nvidia-docker  run      --shm-size 60G --workdir=`pwd` -e CUDA_VISIBLE_DEVICES=2,3 -v /home/timing/:/home/timing/ zhanghui/pytorch:cu80 sh /home/timing/Git_Repos_Summer/CSRNet-pytorch/train.sh
