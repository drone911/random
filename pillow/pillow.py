# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:16:01 2019

@author: JIGAR'S PC
"""
import os
import PIL


file_name=os.getcwd()+"\pillow.png"

orig_img=PIL.Image.open(file_name)


def create_contact(imgs):
    width=imgs[0].width
    height=imgs[0].height
    
    contact_img=PIL.Image.new(imgs[0].mode,(width * 3,height * 3))
    
    for i in range(3):
        for j in range(3):
            contact_img.paste(imgs[i + j*3],(width * i,height * j))
            
    return contact_img

def change_intensity(img,channel,intensity):
    new_img=PIL.Image.new(img.mode,(img.width,img.height))
    for i in range(img.width):
        for j in range(img.height):
            pixel=list(img.getpixel((i,j)))
            pixel[channel]=int(pixel[channel]*intensity)
            new_img.putpixel((i,j),tuple(pixel))
    return new_img
def show(img,name):
    img.save(os.getcwd()+"\{}.png".format(name),"PNG")
    os.startfile(os.getcwd()+"\{}".format(name)+".png")

imgs=[]
intensities=[0.1,0.5,0.9]
channels=[0,1,2]
for channel in channels:
    for intensity in intensities:
        imgs.append(change_intensity(orig_img,channel,intensity))

contact=create_contact(imgs)
show(contact,"something")