# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:25:14 2019

@author: gptshubham595
"""

import cv2
import numpy as np



def main():
    events=[i for i in dir(cv2) if 'EVENT' in i]
    print(events)
    
if __name__=='__main__':
    main()