import sys
import os

import cv2
import json

import retinex

data_path = 'data'
img_list = os.listdir(data_path)
if len(img_list) == 0:
    print 'Data directory is empty.'
    exit()

with open('config.json', 'r') as f:
    config = json.load(f)

for img_name in img_list:
    if img_name == '.gitkeep':
        continue
    
    img = cv2.imread(os.path.join(data_path, img_name))

    img_msrcr = retinex.MSRCR(
        img,
        config['sigma_list'],
        config['G'],
        config['b'],
        config['alpha'],
        config['beta'],
        config['low_clip'],
        config['high_clip']
    )
   
    img_amsrcr = retinex.automatedMSRCR(
        img,
        config['sigma_list']
    )

    img_msrcp = retinex.MSRCP(
        img,
        config['sigma_list'],
        config['low_clip'],
        config['high_clip']        
    )    

    shape = img.shape
    cv2.imshow('Image', img)
    cv2.imshow('retinex', img_msrcr)
    cv2.imshow('Automated retinex', img_amsrcr)
    cv2.imshow('MSRCP', img_msrcp)
    cv2.waitKey()
