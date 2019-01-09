# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 00:57:30 2018

@author: gptshubham595
"""


import cv2
import numpy as np

def emptyfun():
    pass

def main():
    
    imgp1="C:\\opencv learn machin\\misc\\4.2.01.tiff"
    imgp2="C:\\opencv learn machin\\misc\\4.2.05.tiff"
    #1-by preserving same colour default
    #0-grayscale
    
    img1=cv2.imread(imgp1,1)
    img2=cv2.imread(imgp2,1)
    
    out=cv2.addWeighted(img1,0.5,img2,0.5,0)
    
    
    windowName='OpenCv BGR Color Palete'
    cv2.namedWindow(windowName)
    #Text,TitleBox,min and max value,function
    cv2.createTrackbar('Alpha:',windowName,0,10,emptyfun)
    
    while(True):
        cv2.imshow(windowName,out)
        if cv2.waitKey(1)==27:  
            break
        x=cv2.getTrackbarPos('Alpha:',windowName)/10
        y=1-x
        out=cv2.addWeighted(img1,x,img2,y,0)
        
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()