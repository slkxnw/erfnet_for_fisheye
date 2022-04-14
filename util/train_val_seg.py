import os
import random

path='D:\\2021-2022研究生\segcode\dataset\Woodscape'
fullnames=os.listdir(path+'\semantic_annotations\\gtlabels\\')
namelists=[]
for item in fullnames:
    name=item.split()[0].split('.',1)[0]
    namelists.append(name)
random.shuffle(namelists)
trainlist=open(path+'\\train.txt','w')
for i in range(0,int(0.8*len(namelists))):
    trainlist.write(namelists[i]+'\n')
trainlist.close()
vallist=open(path+'\\val.txt','w')
for i in range(int(0.8*len(namelists)),len(namelists)):
    vallist.write(namelists[i]+'\n')
vallist.close()
