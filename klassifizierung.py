# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:20:44 2022

@author: elnuevo
"""

import os

import numpy as np

import cv2
# from cv2 import cv2.imshow

import matplotlib.pyplot as plt
# import termios
import cv2
from time import sleep
import pandas as pd

def calc_gray_mean(list, path):
    mean = []
    for i in list:
        print(i)
        img_load = cv2.imread(path + i)
        gray_image = cv2.cvtColor(img_load, cv2.COLOR_RGB2GRAY)
        mean.append(cv2.mean(gray_image)[0])
        print(mean)
    print("gray mean done")
    return mean

def calc_colour_mean(list, path):
    mean = []
    for i in list:
        print(i)
        img_load = cv2.imread(path + i)
        mean.append(cv2.mean(img_load)[0:3])
        #print(mean)
    print("colour mean done")
    return mean
def calc_momentum(list, path):



if __name__ == "__main__":
    path = "14.10.2021/"
    path = "test/"
    list = os.listdir(path)
    print(list)
    #mean_c
    data = {'gray_mean': calc_gray_mean(list, path),
            'colour_mean': calc_colour_mean(list, path)
            }

    df = pd.DataFrame(data, index=list)
    print(df)
    sleep(1000)

