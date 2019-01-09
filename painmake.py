# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:25:14 2019

@author: gptshubham595
"""

import cv2
import numpy as np

windowName='Drawing'
img=np.zeros((512,512,3),np.uint8);
img.fill(255)
cv2.namedWindow(windowName)

drawing=False
mode=True
(ix,iy)=(-1,-1)
    

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    
    if (event == cv2.EVENT_LBUTTONDOWN):
        drawing=True
        (ix,iy)=x,y
    elif (event == cv2.EVENT_MOUSEMOVE):
        if drawing==True:
            if mode==True:
                cv2.circle(img,(x,y),3,(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),10,(255,255,255),-1)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.circle(img,(x,y),3,(0,255,0),-1)
        else:
                cv2.circle(img,(x,y),10,(255,255,255),-1)
                
#bind callback to window
cv2.setMouseCallback(windowName,draw_circle)

def main():
    global mode
    
    while(True):    
        cv2.imshow(windowName,img)
        k=cv2.waitKey(1)
        if k==ord('m') or k==ord('M'):
            mode=not mode
        elif k==27:
            break
    cv2.destroyWindow(windowName)
if __name__=='__main__':
    main()