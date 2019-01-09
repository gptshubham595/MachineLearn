# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 16:02:44 2019

@author: gptshubham595
"""

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
    
    img1=cv2.imread(imgpath,1)
    
    #changed image colour from BGR to RGB
    
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    #cmap=colormap
    
    
    #plot.imshow saves as R G B
    
    plot.imshow(img)
    plot.title('RGB')
    #remove griding numbers in x and y scale
    plot.xticks([])
    plot.yticks([])
    plot.show()
    
    
    plot.imshow(img1)
    plot.title('BGR')
    plot.show()
    
 
if __name__=="__main__"    :
    main()
    