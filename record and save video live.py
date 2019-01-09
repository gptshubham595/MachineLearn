# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:00:37 2019

@author: gptshubham595
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 16:18:21 2019

@author: gptshubham595
"""

import cv2
import matplotlib.pyplot as plot


def main():
    cap =cv2.VideoCapture(0)
    
    out="C:\\opencv learn machin\\output.avi"
    #coding encoding
    
    #fourcc four char code
    
    #WMV2,WMV1,MJPG,DIVX,XVID,H264
    
    #for vission we need atleast framerate of 25
    
    
    codec=cv2.VideoWriter_fourcc('X','V','I','D')
    framerate=30
    resolution =(640,480)
    
    VideoOut =cv2.VideoWriter(out,codec,framerate,resolution)
    
    name='Live'
    
    if cap.isOpened():
        ret,frame=cap.read()
        
    else:
        ret =False
    
    while ret:
        ret,frame=cap.read()
        
        VideoOut.write(frame)
        out=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        cv2.imshow('old',frame)
        cv2.imshow(name,out)
        if cv2.waitKey(1)==27:
            break
          
    cv2.destroyWindow(name)
    cv2.destroyWindow('old')
    VideoOut.release()
    cap.release()
if __name__=='__main__':
    main()