# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:20:44 2022

@author: elnuevo
"""

import os
import cv2
from time import sleep
import pandas as pd
from tkinter import *
import easygui
import tkinter as tk


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
        # print(mean)
    print("colour mean done")
    return mean


def calc_momentum(list, path):
    pass
    return


def manual_klassifizierung(list, path):
    scale = 1.5
    klasse = []
    klasse_typen = ['l', '1', '2', '3', 'h', 'd']
    # l für leer, # Eier, h für huhn, d für dunkel

    for i in list:
        if ".jpg" in i:
            print(i)
            img_load = cv2.imread(path + i)
            gray_image = cv2.cvtColor(img_load, cv2.COLOR_RGB2GRAY)
            if cv2.mean(gray_image)[0] <= 10:
                print(cv2.mean(gray_image)[0])
                klasse.append('d')
            else:
                cv2.imshow("window_name",
                           cv2.resize(img_load, (int(img_load.shape[1] / scale), int(img_load.shape[0] / scale)),
                                      interpolation=cv2.INTER_AREA))
                eingabe = easygui.enterbox("possible vars: 'l', '1', '2', '3', 'h', 'd'")
                rootWindowPosition = "0+1900"
                easygui.rootWindowPosition = rootWindowPosition
                while eingabe not in klasse_typen:
                    eingabe = easygui.enterbox("NUR: 'l', '1', '2', '3', 'h', 'd'", )
                cv2.destroyAllWindows()
                klasse.append(eingabe)

    return klasse


def filterforindex(liste, dfindex):
    indexliste = []
    try:
        dfindex[0]
    except:
        defindex[0] = "test"
    for i in liste:
        if ".jpg" in i and i != dfindex[0][0]:
            indexliste.append(i)
    return indexliste


if __name__ == "__main__":
    path = "14.10.2021/"
    path = "test/"
    liste = os.listdir(path)
    ###########
    indexliste = []
    i_max = "0"
    for i in liste:
        if ".csv" in i:
            if int(i_max[0]) < int(i[0]):
                i_max = i[0]
                try:  # load dataframe
                    print("lade alten df", i)
                    alterdf = pd.read_csv(path + i)
                # alterdf_list = alterdf.values.tolist()
                except:
                    print("Dataframe konnte nicht geladen werden. Oder so")
    try:
        for i in liste:
            if i not in alterdf.values and ".jpg" in i:
                indexliste.append(i)
    except:
        for i in liste:
            if ".jpg" in i:
                indexliste.append(i)
    # mean_c
    # data = {'huhn,dunkel, ei': manual_klassifizierung(list, path),
    #    'gray_mean': calc_gray_mean(list, path),
    #       'colour_mean': calc_colour_mean(list, path)
    #      }

    data = {'index': indexliste,
        'Bildinhalt': manual_klassifizierung(indexliste, path)
            }

    df = pd.DataFrame(data)

    try:
        df = pd.concat([alterdf, df], ignore_index=True, join='inner')
        pass

    except:
        print("concat failed")

    filename = int(i_max)
    while (str(filename) + "lauf.csv") in os.listdir(path):
        filename += 1
        print(filename)
    try:
        os.remove(path + str(filename - 2) + "lauf.csv")
        print("habe gelöscht:", filename-2, "lauf.csv")
    except:
        print("keien alte File zu deleten")
    df.to_csv(path + str(filename) + 'lauf.csv', index=True)
    print(df)
