#coding=utf-8
import os
rootdir="./data/val"
#存在train的图片目录
file=open('./data/val.txt','w')
#保存在train.txt中
x=-1
for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in filenames:
# list=os.path.split(dirname)
        list=os.path.split(parent)[-1]#split把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
        file.write(list + "/"+  dirname)
        file.write(' '+"%d"%x)
        file.write('\n')
    x=x+1;
file.close()
print "Done"