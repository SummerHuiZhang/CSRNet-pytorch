import os
import random
import torch
import numpy as np
from torch.utils.data import Dataset
from PIL import Image
from image_256 import *
import torchvision.transforms.functional as F
class listDataset(Dataset):
    def __init__(self, root1, root2, shape=None, shuffle=True, transform=None, train=False, seen=0, batch_size=4, num_workers=4,epoch=0,mae_list=[],epoch_period2=50):
#        if train:
#            root = root *4
#        random.shuffle(root)
        
        self.nSamples = len(root)
        self.lines1 = root1
        self.lines2 = root2
        self.transform = transform
        self.train = train
        self.shape = shape
        self.seen = seen
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.epoch = epoch
        self.mae_list = mae_list
        self.epoch_period2 = epoch_period2
    def __len__(self):
        return self.nSamples
    def __getitem__(self, index):
        assert index <= len(self), 'index range error' 
        if self.train == True and self.epoch >  (self.epoch_period2-1):
#            index_1 = random.randint(0,250)  #big mae, target
#            print('root.size=',len(self.lines),'mae_list_size=',len(self.mae_list))
##            target_imgpath_list = np.random.choice(self.lines,size=len(self.lines),replace=True,p=self.mae_list)
            img_path_1 = self.lines1[index] 
##            img_path_1 = target_imgpath_list[index]
#            index_2 = random.randint(250,699) #small mae, source
#            print('Line 36, source_mae_list sum=',np.sum(self.mae_list))
##            mae_list_temp = 1-np.array(self.mae_list)
##            source_mae_list=[]
#            print('Line 38, source_mae_list=',mae_list)
##            for m in range(len(self.mae_list)):
#                print('mae_list[m]=',mae_list[m])
##                source_mae_list.append(abs(mae_list_temp[m])/699)
#                print('m=',m,'sourec_mae_list=',source_mae_list)
#            source_mae_list=(np.array(source_mae_list)).reshape(1,len(source_mae_list))
##            source_imgpath_list = np.random.choice(self.lines,size=len(self.lines),replace=True,p=source_mae_list)
            img_path_2 = self.lines2[index_2]
            img1,target1 = load_data(img_path_1,self.train)
            img2,target2 = load_data(img_path_2,self.train)
#            print('epoch=',self.epoch,'img_path_1=',img_path_1,'img_path_2=',img_path_2,'mae_list=',mae_list)

            if self.transform is not None:
                img1 = self.transform(img1)
                img2 = self.transform(img2)
            return img1,target1,img2,target2,img_path_1,img_path_2
        else:
            img_path = self.lines1[index]
#            print('Line 43 in model_VGG,img_path is',img_path)
            img,target = load_data(img_path,self.train)

            if self.transform is not None:
                img = self.transform(img)
            return img,target,img_path
