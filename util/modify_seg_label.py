import cv2
from PIL import Image
import os
import numpy as np

root='D:\\2021-2022研究生\segcode\dataset\Woodscape\semantic_annotations\gtLabels'
output='D:\\2021-2022研究生\segcode\dataset\Woodscape\semantic_annotations\LaMkLabels'
fullnames=os.listdir(root)
namelists=[]
for item in fullnames:
    name=item.split()[0]
    namelists.append(name)

for gt in namelists:
    print('processing:'+gt)
    file=root+'\\'+gt
    img=Image.open(file)
    arr=np.array(img)
    road=arr==1
    lamk=2*(arr==2)
    modified_gt=np.maximum(road,lamk)
    newgt=Image.fromarray(modified_gt)
    newgt.save(output+'\\'+gt)
