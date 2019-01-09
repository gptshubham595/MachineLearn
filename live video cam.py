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
    name='Live'
    #ret return
    #cap.get shows default
    print ('Width:'+str(cap.get(3)))
    print ('Height:'+str(cap.get(4)))
    
    #cahnging resolution
    cap.set(3,1280)
    cap.set(4,960)
    
    print ('Width:'+str(cap.get(3)))
    print ('Height:'+str(cap.get(4)))
    
    if cap.isOpened():
        ret,frame=cap.read()
        
    else:
        ret =False
    
    while ret:
        ret,frame=cap.read()
        
        out=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('old',frame)
        cv2.imshow(name,out)
        if cv2.waitKey(1)==27:
            break
          
    cv2.destroyWindow(name)
    cv2.destroyWindow('old')
    
    cap.release()
if __name__=='__main__':
    main()