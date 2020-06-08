# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:12:45 2020

@author: AustinMain
"""

import site
import os
import shutil

packagepath = site.getsitepackages()[1]

def run():
    targetfolder = os.path.join(packagepath,'ExtEND')
    try:
        os.mkdir(targetfolder)
    except:
        print (packagepath, 'does not exist!')
        
    for root, dirs, files in os.walk('EXTEND'):
        for f in files:
            shutil.copy(os.path.join(root,f), os.path.join(targetfolder,f))
            
if __name__ == '__main__':
    run()