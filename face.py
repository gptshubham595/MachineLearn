# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:33:27 2019

@author: gptshubham595
"""


import cv2
import matplotlib.pyplot as plot
import numpy as np

def main():
    cap =cv2.VideoCapture(0)    
    face=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_alt2.xml')
    #smile=cv2.CascadeClassifier(cv2.data.haarcascades+'closed_frontal_palm.xml')
	
    eye=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
    
	
    
    if cap.isOpened():
        ret,img=cap.read()    
        
        
    else:
        ret =False
        
    while ret:
        ret,img=cap.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face.detectMultiScale(gray,1.1,5)
        eyes=eye.detectMultiScale(gray,1.1,5)
        #smiles=smile.detectMultiScale(gray,1.1,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,10),2)
        
        for (x,y,w,h) in eyes:
            cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,10),2)
        
        #for (x,y,w,h) in smiles:
         #   cv2.rectangle(img,(x,y),(x+w,y+h),(0,5,250),2)
        
        
        cv2.imshow('img',img)
        k=cv2.waitKey(1)
        if k==27:
            break
		
    cv2.destroyAllWindows()
    
    cap.release()
    

    
if __name__=="__main__":
    main()