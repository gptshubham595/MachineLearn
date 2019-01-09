# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 16:18:21 2019

@author: gptshubham595
"""

import cv2
import matplotlib.pyplot as plot


def main():
    cap =cv2.VideoCapture(0)
    
    #ret return
    
    if cap.isOpened():
        ret,frame=cap.read()
        print(ret)
        print(frame)
    else:
        ret =False
    
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    plot.imshow(img)
    plot.title('Image')
    plot.show()
    
    cap.release()
    
if __name__=='__main__':
    main()