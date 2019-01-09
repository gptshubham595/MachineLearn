# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:33:27 2019

@author: gptshubham595
"""


import cv2
import matplotlib.pyplot as plot
import numpy as np

def main():
    
    cap =cv2.VideoCapture(0)
    
    #ret return
    
    if cap.isOpened():
        ret,frame=cap.read()    
    else:
        ret =False
        
    while ret:
        
        ret,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        #green 
        lowg=np.array([40,50,50])
        highg=np.array([80,255,255])
        
        #red
        lowr=np.array([140,150,0])
        highr=np.array([180,255,255])
        #blue
        low=np.array([100,50,50])
        high=np.array([140,255,255])
        
        #binary image array
        
        imagemask=cv2.inRange(hsv,low,high)
        
        cv2.imshow("Image mask",imagemask)
        
        cv2.imshow("Original",frame)
        if cv2.waitKey(1)==27:
            break
        
        
    cv2.destroyWindow("Original")
    cv2.destroyWindow("Image mask")
    cap.release()
    

    
if __name__=="__main__":
    main()