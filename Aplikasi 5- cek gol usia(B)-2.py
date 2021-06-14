# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:38:58 2021

@author: Reynaldi Jonathan Hartono
"""
#cek golongan usia
import os
Clear = lambda : os.system('cls')

jwb = "y"
while jwb=="y" or jwb=="Y": 
    Clear()
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(     "Cek Golongan Usia")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("by Jonathan")
    
    u = int(input("Masukkan Umur = "))
    #cek nilai
    if int(u)>0 and int(u)<=100:
        if u>60:
            sts = "Lansia"
        elif u>=35: sts="Dewasa"
        elif u>=18: sts="Pemuda"
        elif u>=15: sts="remaja"
        else:
            sts = "Anak"
        print(sts)
    else:
        pesan="Masukkan 0-100 saja"
        print(pesan)
        
    jwb = input("Apakah mau menghitung ulang (Y/T) ? ")
    if jwb=="t" or jwb=="T":
        break
