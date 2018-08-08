# -*- coding:utf-8 -*-

import os
import cv2

path = '../data/'
#Rename the picture
def rename():
    j = 0
    for image_class in os.listdir(path):
        i = 0
        image_path = path + image_class + "/"
        for imgname in os.listdir(image_path):
            Olddir = os.path.join(image_path, imgname)
            if os.path.isdir(Olddir):
                continue
            #imagename = os.path.splitext(imgname)[0]
            imgtype = os.path.splitext(imgname)[1]
            Newdir = os.path.join(path + image_class, imgname[0:3] +"tmp"+ format(str(j), '0>2s') + format(str(i), '0>2s') + imgtype)
            i = i + 1
            os.rename(Olddir, Newdir)
        j = j + 1
rename()

#Resize and save the image
def convertjpg(jpgfile,outdir,width=300,height=300):
    img=cv2.imread(jpgfile)
    try:
        new_img=cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(os.path.join(outdir,os.path.basename(jpgfile)),new_img)
    except Exception as e:
        print(e)
 
for image_class in os.listdir(path):
    image_path = path + image_class + "/"
    for imgname in os.listdir(image_path):
        convertjpg(image_path + imgname, image_path)
 
#Execute the .sh file to create lmdb
#cmd = '/home/xn/caffe/examples/facetestquestions/create_imagenet.sh'
#import subprocess
#p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#while p.poll() == None:
#     line = p.stdout.readline()
#     print line
#     result = result + line
