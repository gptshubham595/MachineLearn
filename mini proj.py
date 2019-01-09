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
    
    img=np.zeros((512,512,3),np.uint8)
    windowName='OpenCv BGR Color Palete'
    cv2.namedWindow(windowName)
    #Text,TitleBox,min and max value,function
    cv2.createTrackbar('Blue:',windowName,0,255,emptyfun)
    cv2.createTrackbar('Green:',windowName,0,255,emptyfun)
    cv2.createTrackbar('Red:',windowName,0,255,emptyfun)
    
    while(True):
        cv2.imshow(windowName,img)
        if cv2.waitKey(1)==27:  
            break
        blue=cv2.getTrackbarPos('Blue:',windowName)
        green=cv2.getTrackbarPos('Green:',windowName)
        red=cv2.getTrackbarPos('Red:',windowName)
        img[:]=[blue,green,red]
        
        
        
   
    
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()