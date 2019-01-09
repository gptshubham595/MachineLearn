# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import matplotlib.pyplot as plot

def main():
    print('cv2 version:',format(cv2.__version__))
    
    imgpath="C:\\opencv learn machin\\misc\\4.1.01.tiff"
    #1-by preserving same colour default
    #0-grayscale
    
    img=cv2.imread(imgpath,0)
    #cv2.namedWindow('Pic',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Pic',img)
 
    outpath="C:\\opencv learn machin\\4.1.01.jpg"
    cv2.imwrite(outpath,img)
    #waiting for any key
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__"    :
    main()
    