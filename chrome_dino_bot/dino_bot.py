# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 21:40:34 2019

@author: JIGAR'S PC
"""

import cv2
import numpy as np
from grab_screen import grab_screen
from pynput.keyboard import Controller,Key
import time
import win32api as wapi


    
THRESH=230
FACTOR=0.04

def mouse_callback(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        
if __name__=="__main__":
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',mouse_callback)
    controller=Controller()   
    for i in range(5)[: :-1]:
        print(i)
        time.sleep(1)
    
    paused=False
    
    while True:
        if not paused:
            screen=grab_screen(region=(50,200,700,500))
            if cv2.waitKey(25) == ord('q'):
                break
            coordinates=((241,200),(250,230))                                                                                                                                   
            width=coordinates[1][0]-coordinates[0][0]
            heigth=coordinates[1][1]-coordinates[0][1]                               
            
            gray=cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
            cv2.rectangle(screen,coordinates[0],coordinates[1],(255,255,0),2,2)
            roi=gray[coordinates[0][0]:coordinates[1][0],coordinates[0][1]:coordinates[1][1]]
            if np.mean(np.reshape(roi,(width*heigth)))<THRESH:
                #print("jump")
                controller.press(Key.up)
                controller.release(Key.up)
            print(np.mean(np.reshape(roi,(width*heigth))))
            cv2.imshow('image', screen)
        if wapi.GetAsyncKeyState(ord('P')):
            if paused:
                paused=False
                time.sleep(1)
            else:
                paused=True
                time.sleep(1)
    cv2.destroyAllWindows()
            