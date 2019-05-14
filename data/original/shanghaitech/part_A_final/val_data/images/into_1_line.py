import os
import sys
# usage: python change \n into ,
#temp_file=sys[1]
#word=sys[2]
with open('/Users/zhanghui/Documents/Git_Repos_Summer/crowdcount-mcnn/data/original/shanghaitech/part_A_final/val_data/partA_val_images/partA_val_namelist.json','r+') as fpr:
	content=fpr.read()
content = content.replace('\n',',')
print(content)
with open('/Users/zhanghui/Documents/Git_Repos_Summer/crowdcount-mcnn/data/original/shanghaitech/part_A_final/val_data/partA_val_images/partA_val_namelist.json','w') as fpw:
	fpw.write(content)