o
# -*- coding: utf-8 -*-

"""
Created on Thu Jan  3 16:18:21 2019

@author: gptshubham595
"""

import cv2
import matplotlib.pyplot as plot


def main():
    name='Media player'
    cv2.namedWindow(name)
    file="C:\\opencv learn machin\\output.avi"
    cap =cv2.VideoCapture(file)
    
    ret=True
    
    while (cap.isOpened()):
        ret,frame=cap.read()
            
        print(ret)
        
        if ret:
            cv2.imshow(name,frame)
            if cv2.waitKey(30)==27:
                break
        else:
            break
        
    cv2.destroyWindow(name)
    cap.release()
    
if __name__=='__main__':
    main()