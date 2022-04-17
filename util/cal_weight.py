import torch
from PIL import Image
from train.dataset import woodscapes
import numpy as np


root='D:\\2021-2022研究生\segcode\dataset\Woodscape'
dataset=woodscapes(root)
leng=len(dataset)
road=0
lm=0
for i in range(0,leng):
    print('processing:'+dataset.filenames[i])
    label=np.array(dataset.get_label(i))
    road=road+np.sum(label==1)
    lm=lm+np.sum(label==2)
p_rd=road/(leng*1280*966)
p_lm=lm/(leng*1280*966)
p_void=1-p_lm-p_rd
p=np.array([p_void,p_rd,p_lm])
wt=1/np.log(1.1+p)
print(wt)



