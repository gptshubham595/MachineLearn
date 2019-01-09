# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
def main():
    print('cv2 version:',format(cv2.__version__))
    imgpath="C:\\opencv learn machin\\misc\\4.1.01.tiff"
    #1-by preserving same colour default
    #0-grayscale
    
    img=cv2.imread(imgpath)
    #in opencv it is in BGR not RGB
    print(img)
    print(type(img))
    print(img.dtype)
    #cv2.namedWindow('Pic',cv2.WINDOW_AUTOSIZE)
    #showing image
    cv2.imshow('Pic',img)
 
    #waiting for any key
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__"    :
    main()
    