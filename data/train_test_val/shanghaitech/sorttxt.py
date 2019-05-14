import os
import sys
# usage: python delete_some_word.py *.txt word_to_delete
#temp_file=sys[1]
#word=sys[2]
with open('/home/timing/Git_Repos_Summer/CSRNet-pytorch/data/original/shanghaitech/part_A_final/test_data/images/original_partA_test_namelist.txt','r') as fpr:
    content=fpr.read()
content = content.replace('\n','","')
print(content)
with open('/home/timing/Git_Repos_Summer/CSRNet-pytorch/data/original/shanghaitech/part_A_final/test_data/images/original_partA_test_namelist.txt','r+') as fpw:
    fpw.write(content)

