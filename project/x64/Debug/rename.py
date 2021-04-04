import os

from skimage import io,transform
import glob

import tensorflow as tf
#tf.compat.v1.disable_eager_execution()
import numpy as np

path_name = "./train_2/"

#path_name='/home/huiyu/PycharmProjects/faceCodeByMe/testdata'
#path_name :表示你需要批量改的文件夹
"""i=0
for item in os.listdir(path_name):#进入到文件夹内，对每个文件进行循环遍历
    #os.rename(os.path.join(path_name,item),os.path.join(path_name,(str(i+1)+'Mango'+'.jpg')))
    #os.path.join(path_name,item)表示找到每个文件的绝对路径并进行拼接操作
    print(item)
    i+=1"""

"""j=0
print(os.listdir(path_name))
for i in os.listdir(path_name):
    
    print(j,':',"'",i,"'",',')
    j += 1
    """

path = "./train_2/"
w = 100
h = 100
c = 3
cate = [path + x for x in os.listdir(path) if os.path.isdir(path+x)]
images = []
labels = []
p = 0
k = 0
i = 0
for index, folder in enumerate(cate):
    
    for item in os.listdir(folder):#进入到文件夹内，对每个文件进行循环遍历
        #os.rename(os.path.join(path_name,item),os.path.join(path_name,(str(i+1)+'image'+'.jpg')))
        #os.path.join(path_name,item)表示找到每个文件的绝对路径并进行拼接操作
        #print(item[len(item)-4:])
        #print(item)
        if item[len(item)-4:] == '.png':
            print(item[len(item)-4:])
            print(item[:len(item)-4])
            os.rename(os.path.join(folder,item),os.path.join(folder,(item[:len(item)-4]+'.jpg')))
            i+=1
print(i)

"""
    p = p + 1
    k=0
    for im in glob.glob(folder + '/*.png'):
        #print(k)
        k=k+1
        #print(im)
        
        img = io.imread(im)
        #print(img)
        img = transform.resize(img, (w, h,c))
        print(np.shape(img))
        a = np.asarray(img, np.float32)
        #print(img)
        images.append(img)
        #labels.append(index)
   #     if k > 1:
    #        break
    #if p > 1:
    #    break
#a = np.asarray(images, np.float32)"""
