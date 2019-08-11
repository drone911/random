# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:23:26 2019

@author: JIGAR'S PC
"""

import cv2
from  skimage.segmentation import slic,mark_boundaries
import os
import argparse


def main(args):
    
    file_name=os.getcwd()+"\\"+args["image"]
    
    img=cv2.imread(file_name, cv2.IMREAD_COLOR)
    segments=slic(img,n_segments=args["segments"])
    
    cv2.imshow('superPixeled', mark_boundaries(img,segments))
    cv2.imwrite(os.getcwd()+'\\superPixeled-{}'.format(args["image"]), segments)
    cv2.waitKey(0)
if __name__=="__main__":
    
    args=argparse.ArgumentParser(description="finds superpixels in an image")
    args.add_argument("-i", "--image", required=True, help="path to the image")
    args.add_argument("-s", "--segments", type=int, default=100, help="number of segments")
    args=vars(args.parse_args())
    main(args)
    