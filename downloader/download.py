# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:57:46 2019

@author: JIGAR'S PC
"""
import certifi
import urllib3
import sys
import os
def download(url_supplied=None,log=False):
    if len(sys.argv)== 1 and url_supplied is None:
        print("No Url supplied")
        return None
    
    if url_supplied is None:
        url_supplied = sys.argv[-1]
    
    file_name = url_supplied.split('/')[-1]
    
    poolmanager=urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    
    try:
        u = poolmanager.urlopen(method='GET',url=url_supplied,preload_content=False)
    except urllib3.exceptions.SSLError:
        print("SSL Error")
    try:
        file_size=u.info().getheaders("Content-length")[0]
    except:
        file_size=1
    file_path = os.path.join("Downloads",file_name)
    while os.path.exists(file_path) is True:
        file_path=str(file_path.split('.')[0])+str('0')+str('.')+str(file_path.split('.')[1])
        file_name=str(file_name.split('.')[0])+str('0')+str('.')+str(file_name.split('.')[1])
    chunk_size=8192
    file_size_d=0
    if log:
        print("Downloading file: "+str(file_name)+" [Size: "+str(file_size)+ " ]")
   
    try:
        f=open(file_path,'wb') 
        while True:
                buffer = u.read(chunk_size)
                if not buffer:
                    break
                file_size_d += len(buffer)
                f.write(buffer)
                if log:
                    print("status: {0}%".format(int(file_size_d)/int(file_size) * 100))
                
        f.close()
        return file_path
    except Exception as e:
        print("the following error occured while dowloading the file {0}::{1}".format(file_name,e))
if __name__ == '__main__':
    download()