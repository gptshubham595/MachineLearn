# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:25:14 2019

@author: gptshubham595
"""

import cv2
import numpy as np

windowName='Drawing'
img=np.zeros((512,512,3),np.uint8);
cv2.namedWindow(windowName)

def draw_circle(event,x,y,flags,param):
    if (event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img,(x,y),40,(0,255,0),-1)
        cv2.circle(img,(x-10,y-10),5,(0,0,255),-1)
        cv2.circle(img,(x+10,y-10),5,(0,0,255),-1)
    if (event == cv2.EVENT_RBUTTONDOWN):
        cv2.circle(img,(x,y),10,(0,0,255),-1)
#bind callback to window
cv2.setMouseCallback(windowName,draw_circle)

def main():
    while(True):    
        cv2.imshow(windowName,img)
        if cv2.waitKey(1)==27:
            cv2.destroyWindow(windowName)
            break
if __name__=='__main__':
    main()