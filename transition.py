# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:33:27 2019

@author: gptshubham595
"""


import cv2
import matplotlib.pyplot as plot
import numpy as np
import time

def main():
    
    imgp1="C:\\opencv learn machin\\misc\\4.2.01.tiff"
    imgp2="C:\\opencv learn machin\\misc\\4.2.05.tiff"
    #1-by preserving same colour default
    #0-grayscale
    
    img1=cv2.imread(imgp1,1)
    img2=cv2.imread(imgp2,1)
    
    
    
    #img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    #img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    
    add=img1 + img2
    z=0
    #50->Intervals
    for i in np.linspace(0,1,50):
        x=i
        y=1-x
        output=cv2.addWeighted(img1,x,img2,y,z)
        cv2.imshow('Transition',output)
        time.sleep(0.1)
        if cv2.waitKey(1)==27:
            break
        
    #x+y+z=1 for good 
    #(img1*x +img2*y+z}/(x+y+z)

    cv2.destroyAllWindows()
if __name__=="__main__":
    main()