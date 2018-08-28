# -*- coding: UTF-8 -*-
from __future__ import print_function
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
import cv2
import random, sys
import getopt
import argparse
import errno
import os
import random
import shutil
import re
import numpy as np

debug = False
enhance_flag = "_enhance"
extra_enhance = True
endless = False

enhance_resize = True
enhance_rotate = True
enhance_flip = False
enhance_lambda = False
enhance_color = False
enhance_brightness = False
enhance_contrast = False
enhance_sharpness = False
enhance_hsvfactor = False  # unrecommend

resize_hight = 300
resize_weight = 300

rotate_step = 90

flip_x = True
flip_y = True
flip_xy = True
flip_yx = True

# range(istart, istop, istep)


lambda_start = 0.7
lambda_step = 4
lambda_range = 4.0

color_start = 0.7
color_step = 4
color_range = 4.0

brightness_start = 0.7
brightness_step = 4
brightness_range = 4.0

contrast_start = 0.7
contrast_step = 4
contrast_range = 4.0

sharpness_start = 0.7
sharpness_step = 4
sharpness_range = 4.0

hsvfactor_times = 3


# 颜色
def image_enhance_color(img, prename, istart=color_start, istep=color_step, irange=color_range):
    img_list = []
    imgenhancer = ImageEnhance.Color(img)
    for i in range(1, istep):
        factor = i / irange
        if (factor < istart): continue
        newimg = imgenhancer.enhance(factor)
        newname = prename + "_color_%.2f" % factor
        # newimg.show(newname)
        # newimg.save(newname+'.jpg')
        img_list.append((newimg, newname))
    return (img_list)


# 亮度
def image_enhance_brightness(img, prename, istart=brightness_start, istep=brightness_step, irange=brightness_range):
    img_list = []
    imgenhancer = ImageEnhance.Brightness(img)
    for i in range(1, istep):
        factor = i / irange
        if (factor < istart): continue
        newimg = imgenhancer.enhance(factor)
        newname = prename + "_brightness_%.2f" % factor
        # newimg.show(newname)
        # newimg.save(newname+'.jpg')
        img_list.append((newimg, newname))
    return (img_list)


# 对比度
def image_enhance_contrast(img, prename,istart=contrast_start, istep=contrast_step, irange=contrast_range):
    img_list = []
    imgenhancer = ImageEnhance.Contrast(img)
    for i in range(1, istep):
        factor = i / irange
        if (factor < istart): continue
        newimg = imgenhancer.enhance(factor)
        newname = prename + "_contrast_%.2f" % factor
        # newimg.show(newname)
        # newimg.save(newname+'.jpg')
        img_list.append((newimg, newname))
    return (img_list)


# 锐化
def image_enhance_sharpness(img, prename,istart=sharpness_start, istep=sharpness_step, irange=sharpness_range):
    img_list = []
    imgenhancer = ImageEnhance.Sharpness(img)
    for i in range(1, istep):
        factor = i / irange
        if (factor < istart): continue
        newimg = imgenhancer.enhance(factor)
        newname = prename + "_sharpness_%.2f" % factor
        # newimg.show(newname)
        # newimg.save(newname+'.jpg')
        img_list.append((newimg, newname))
    return (img_list)


# 像素点
def image_enhance_lambda(img, prename,istart=lambda_start, istep=lambda_step, irange=lambda_range):
    img_list = []
    for i in range(1, istep):
        factor = i / irange
        if (factor < istart): continue
        newimg = img.point(lambda i: i * (factor))  # 对每一个像素点进行增强
        newname = prename + "_lambda_%.2f" % factor
        # newimg.show(newname)
        # newimg.save(newname+'.jpg')
        img_list.append((newimg, newname))
    return (img_list)


# HSV色域变换
def image_enhance_hsvfactor(img, prename, itimes=hsvfactor_times):
    img_list = []
    cvimg = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    for i in range(itimes):
        hsv = cv2.cvtColor(cvimg, cv2.COLOR_BGR2HSV)
        seed = []
        seed.append(np.random.random())
        seed.append(np.random.random())
        seed.append(np.random.random())
        hsv[:, :, 0] = hsv[:, :, 0] * (0.8 + seed[0] * 0.2)
        hsv[:, :, 1] = hsv[:, :, 1] * (0.3 + seed[1] * 0.7)
        hsv[:, :, 2] = hsv[:, :, 2] * (0.2 + seed[2] * 0.8)
        cvimg = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        newimg = Image.fromarray(cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB))
        newname = prename + "_hsv_%.2f_%.2f_%.2f" % (seed[0], seed[1], seed[2])
        img_list.append((newimg, newname))
    return (img_list)


# 旋转
def image_enhance_rotate(img, prename, istep=rotate_step):
    img_list = []
    for i in range(istep, 360, istep):
        newimg = img.rotate(i)
        newname = prename + "_rotate_%d" % i
        # newimg.show(newname)
        # newimg.save(newname+'.jpg')
        img_list.append((newimg, newname))
    return (img_list)


# 翻转
def image_enhance_flip(img, prename):
    img_list = []
    if (flip_x):
        newimg = img.transpose(Image.FLIP_LEFT_RIGHT)
        newname = prename + "_flip_x"
        # newimg.show(newname)
        # newimg.save(newname+'.jpg')
        img_list.append((newimg, newname))
    if (flip_y):
        newimg = img.transpose(Image.FLIP_TOP_BOTTOM)
        newname = prename + "_flip_y"
        # newimg.show(newname)
        # newimg.save(newname+'.jpg')
        img_list.append((newimg, newname))
    if (flip_xy):
        newimg = img.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.ROTATE_90)
        newname = prename + "_flip_xy"
        # newimg.show(newname)
        # newimg.save(newname+'.jpg')
        img_list.append((newimg, newname))
    if (flip_yx):
        newimg = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
        newname = prename + "_flip_yx"
        # newimg.show(newname)
        # newimg.save(newname+'.jpg')
        img_list.append((newimg, newname))
    return (img_list)


# def main(argv):
#     try:
#         opts, args = getopt.getopt(argv, "hi:o:", ["inputdir=", "outputdir="])
#     except getopt.GetoptError:
#         print('usage: image_enhance_tool.py -i <inputdir> -o <outputdir>')
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt == '-h':
#             print('image_enhance_tool.py -i <inputdir> -o <outputdir>')
#             sys.exit()
#         elif opt in ("-i", "--inputdir"):
#             print('read '+arg)
#             specfile = arg
#         elif opt in ("-p", "--outputdir"):
#             pictfile = arg
#             # file_open_pict = open(pictfile, 'w');
#         else:
#             print('unknow option')
#
#
#
#
#     img = Image.open("sample.jpg")
#     # trans img to rgb
#     img = img.convert("RGB")
#
#     # PIL lambda
#     # imgbri = img.point(lambda i: i * 1.4)  # 对每一个像素点进行增强
#     # imgbri.save("1bri.jpg")
#     # imgbri.show()
#
#     # PIL ImageEnhance
#     img_enhance_color(img, color_step, color_range)
#     img_enhance_brightness(img, brightness_step, brightness_range)
#     img_enhance_contrast(img, contrast_step, contrast_range)
#     img_enhance_sharpness(img, sharpness_step, sharpness_range)

def getImgs(imageDir):
    exts = ["jpg", "png", "bmp"]

    # All images with one image from each class put into the validation set.
    allImgsM = []
    enhImgsM = []
    for subdir, dirs, files in os.walk(imageDir):
        for fName in files:
            (imageClass, imageName) = (os.path.basename(subdir), fName)
            if any(imageName.lower().endswith("." + ext) for ext in exts):
                if (endless or enhance_flag not in imageName):
                    allImgsM.append((imageClass, imageName))
                else:
                    enhImgsM.append((imageClass, imageName))
    print("+ Number of Images: '{}'.".format(len(allImgsM)))
    # print(allImgsM)
    return (allImgsM, enhImgsM)


def enhanceMgr(img, prename):
    res_list = []
    flip_list = []
    if (enhance_rotate):
        img_list = image_enhance_rotate(img, prename)
        res_list += img_list
        flip_list += img_list
    if (enhance_flip):
        img_list = image_enhance_flip(img, prename)
        res_list += img_list
        flip_list += img_list
    if (enhance_lambda):
        img_list = image_enhance_lambda(img, prename)
        res_list += img_list
        if (extra_enhance):
            _img_list = []
            for (_img, _name) in flip_list:
                _img_list += image_enhance_lambda(_img, _name)
            res_list += _img_list
    if (enhance_color):
        img_list = image_enhance_color(img, prename)
        res_list += img_list
        if (extra_enhance):
            _img_list = []
            for (_img, _name) in flip_list:
                _img_list += image_enhance_color(_img, _name)
            res_list += _img_list

    if (enhance_brightness):
        img_list = image_enhance_brightness(img, prename)
        res_list += img_list
        if (extra_enhance):
            _img_list = []
            for (_img, _name) in flip_list:
                _img_list += image_enhance_brightness(_img, _name)
            res_list += _img_list

    if (enhance_contrast):
        img_list = image_enhance_contrast(img, prename)
        res_list += img_list
        if (extra_enhance):
            _img_list = []
            for (_img, _name) in flip_list:
                _img_list += image_enhance_contrast(_img, _name)
            res_list += _img_list

    if (enhance_sharpness):
        img_list = image_enhance_sharpness(img, prename)
        res_list += img_list
        if (extra_enhance):
            _img_list = []
            for (_img, _name) in flip_list:
                _img_list += image_enhance_sharpness(_img, _name)
            res_list += _img_list
    if (enhance_hsvfactor):
        img_list = image_enhance_hsvfactor(img, prename)
        res_list += img_list
        if (extra_enhance):
            _img_list = []
            for (_img, _name) in flip_list:
                _img_list += image_enhance_hsvfactor(_img, _name)
            res_list += _img_list

    return res_list


def get_prename(imagename):
    (filepath, basename) = os.path.split(imagename)
    (filename, extension) = os.path.splitext(basename)
    return (filepath + "/" + filename)


# def env(img):
#     a = np.asarray(img.convert('L')).astype('float')
#
#     depth = 10.  # (0-100)
#     grad = np.gradient(a)  # 取图像灰度的梯度值
#     grad_x, grad_y = grad  # 分别取横纵图像梯度值
#     grad_x = grad_x * depth / 100.
#     grad_y = grad_y * depth / 100.
#     A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
#     uni_x = grad_x / A
#     uni_y = grad_y / A
#     uni_z = 1. / A
#
#     vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
#     vec_az = np.pi / 4.  # 光源的方位角度，弧度值
#     dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
#     dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
#     dz = np.sin(vec_el)  # 光源对z 轴的影响
#
#     b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
#     b = b.clip(0, 255)
#
#     im = Image.fromarray(b.astype('uint8'))  # 重构图像
#     im.save('Ronaldo2.jpg')

def enhance_images(imageDir):
    print("run enhance_image on " + imageDir)
    (allImgsM, enhImgs) = getImgs(imageDir)
    cnt = 1
    for person, imagename in allImgsM:
        origPath = os.path.join(imageDir, person, imagename)
        # print(imageDir)
        # print(person)
        # print(imagename)
        # print(origPath)
        # print(imageDir+person+ imagename)
        print(cnt, ": work on '%s' " % origPath, end='')
        img = Image.open(origPath)
        # img = cv2.imread(origPath)
        # tfactor(img)
        if (enhance_resize):
            img = img.resize((resize_hight, resize_weight))
        # trans img to rgb
        img = img.convert("RGB")
        # get prename
        prename = get_prename(os.path.join(imageDir, person, imagename))
        # format orig img
        os.remove(origPath)
        img.save(prename + ".jpg")
        # add enhance flag
        prename = prename + enhance_flag
        # ehance img
        img_list = enhanceMgr(img, prename)
        print("get %d copy" % len(img_list), end='')
        for (_img, _name) in img_list:
            _img.save(_name + '.jpg')

        print("[--100%--]")
        cnt += 1
    return


def main():
    # if (debug == True):
    #     enhance_images('./data/')
    #     exit(0)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'imageDir', type=str, help="Dir of image to enhance.")
    # parser.add_argument('--valRatio', type=float, default=0.10,
    #                     help="Validation to training ratio.")
    args = parser.parse_args()

    enhance_images(args.imageDir)
    # main(sys.argv[1:])


if __name__ == '__main__':
    main()
