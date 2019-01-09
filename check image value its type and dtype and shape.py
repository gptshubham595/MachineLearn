# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
def main():
    print('cv2 version:',format(cv2.__version__))
    imgpath="C:\\opencv learn machin\\4.1.01.jpg"
    #1-by preserving same colour default
    #0-grayscale
    
    img=cv2.imread(imgpath)
    
    #in opencv it is in BGR not RGB
    print(img)
    
    #ndarray is N dimensional array - composite data type and part of numpy numerical python
    print(type(img))
    
    #uint8 unsigned integer of 8 bits 
    #bin 00000000 to 11111111 in hexa 0x00 to 0xFF in decimal 0 to 255 
    #total colours 256*256*256
    print(img.dtype)
    
    #shape-resolution 256-Height 256-W 3-clour channels
    print(img.shape)
    
    #shows N dimensions 
    print(img.ndim)
    
    #show size 256*256*3
    print(img.size)    
    #cv2.namedWindow('Pic',cv2.WINDOW_AUTOSIZE)
    #showing image
   # cv2.imshow('Pic',img)
 
    #waiting for any key
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

if __name__=="__main__"    :
    main()
    