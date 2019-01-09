# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:33:27 2019

@author: gptshubham595
"""


import cv2
import matplotlib.pyplot as plot
import numpy as np

def main():
    
    imgp1="C:\\opencv learn machin\\misc\\4.2.01.tiff"
    imgp2="C:\\opencv learn machin\\misc\\4.2.05.tiff"
    #1-by preserving same colour default
    #0-grayscale
    
    img1=cv2.imread(imgp1,1)
    img2=cv2.imread(imgp2,1)
    
    
    
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    add=img1 - img2
    
    title=['Hello','Lena','Add']
    image=[img1,img2,add]

    for i in range(3):
        #Row,Col,Order No.
        plot.subplot(1,3,i+1)
        plot.imshow(image[i])
        plot.title(title[i])
        plot.xticks([])
        plot.yticks([])
    plot.show()
    
if __name__=="__main__":
    main()