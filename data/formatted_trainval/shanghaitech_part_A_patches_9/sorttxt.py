import os
import sys
# usage: python delete_some_word.py *.txt word_to_delete
#temp_file=sys[1]
#word=sys[2]
with open('/home/timing/Git_Repos_Summer/CSRNet-pytorch/data/formatted_trainval/shanghaitech_part_A_patches_9/partA_namelist.txt','r') as fpr:
    content=fpr.read()
content = content.replace('\n','","')
print(content)
with open('/home/timing/Git_Repos_Summer/CSRNet-pytorch/data/formatted_trainval/shanghaitech_part_A_patches_9/partA_namelist_after.txt','r+') as fpw:
    fpw.write(content)

