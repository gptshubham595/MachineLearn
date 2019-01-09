
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 23:45:25 2018

@author: gptshubham595
"""
import cv2
import numpy as np

def main():
    #draing canvas size ,BGR,unsigned int
    img=np.zeros((512,512,3),np.uint8)
    
    
    #circle X,Y Radius BGR filled
    cv2.circle(img,(100,100),(100),(0,255,0),-1)
    #draw line X1,Y1 to X2,Y2 and in BGR Thickness
    cv2.line(img,(0,99),(99,0),(0,0,255),4)
    #x1,y1 and x4,y4
    cv2.rectangle(img,(40,60),(200,200),(10,150,100),1)
    #0Rotation 360angle of ellipse portion
    cv2.ellipse(img,(250,250),(50,20),0,0,360,(127,127,127),-1)
    #making an array for coordinates 
    points=np.array([[80,2],[125,30],[40,62],[53,12],[64,52]],np.int32)
    points=points.reshape((-1,1,2))
    cv2.polylines(img,[points],True,(0,255,255))
    
    text='Testing Values'
    #where to show ,text ,center,font,size,BGR
    cv2.putText(img,text,(200,200),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0))
    
    cv2.imshow('Pic',img)
    if cv2.waitKey(1) ==27:
        cv2.destroyWindow('Pic')

if __name__=="__main__":
        main()
        
