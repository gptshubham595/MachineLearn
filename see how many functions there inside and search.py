# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:25:14 2019

@author: gptshubham595
"""

import cv2
import numpy as np

def seeall():
    events=[i for i in dir(np)]
    print(events)
def seeall2():
    j=0
    for i in dir(cv2):
        print(i)
        j=j+1

def search2():
    j=0
    for file in dir(cv2):
        if file.startswith('COLOR_'):
            print(file)
            j=j+1
    #int converting to string tyoecast
    print(str(j) +' No. of items')

def main():
   #seeall()
   #search()
   #seeall2()
    search2()
if __name__=='__main__':
    main()