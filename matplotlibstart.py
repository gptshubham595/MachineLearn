# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import matplotlib.pyplot as plot

def main():
   
    #Various Colour spaces
    #HSV-Hue Saturation Value
    #GRAY
    #CMY - Can Marientine Yellow
    #RGB
    #BGR
    
    #print('cv2 version:',format(cv2.__version__))
    imgpath="C:\\opencv learn machin\\misc\\4.1.01.tiff"
    #1-by preserving same colour default
    #0-grayscale
    
    
    #cv2.imread is saved in memory as B G R
    
    
    img=cv2.imread(imgpath,1)
    
    
    #cmap=colormap
    
    
    #plot.imshow saves as R G B
    
    plot.imshow(img,cmap='gray')
    plot.title('Gray image')
    #remove griding numbers in x and y scale
    plot.xticks([])
    plot.yticks([])
    plot.show()
    
    
    plot.imshow(img)
    plot.title('Default')
    plot.show()
    
 
if __name__=="__main__"    :
    main()
    