import os
import sys
# usage: python delete_some_word.py *.txt word_to_delete
#temp_file=sys[1]
#word=sys[2]
with open('/home/timing/Git_Repos_Summer/CSRNet-pytorch/data/original/shanghaitech/merge_part_AB/val/ground_truth/merge_AB_GT_with_val.json','r+') as fpr:
    content=fpr.read()
content = content.replace('\n','","')
print(content)
with open('/home/timing/Git_Repos_Summer/CSRNet-pytorch/data/original/shanghaitech/merge_part_AB/val/ground_truth/merge_AB_GT_with_val.json','w') as fpw:
    fpw.write(content)


