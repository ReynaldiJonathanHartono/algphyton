# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:39:53 2021

@author: Reynaldi Jonathan Hartono
"""

#menampilkan nilai huruf
import os
Clear = lambda : os.system('cls')

jwb = "y"
while jwb=="y" or jwb=="Y": 
    Clear()
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(      "Cek Nilai Huruf")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("by Jonathan")
    n = int(input("Masukkan Nilai = "))
    #cek nilai
    if int(n)>0 and int(n)<=100:
        if n>80:
            sts = "Baik Sekali"
        elif n>=65: sts="Baik"
        elif n>=55: sts="Cukup"
        elif n>=40: sts="Kurang"
        else:
            sts = "Kurang Sekali"
        print(sts)
    else:
        pesan="Masukkan 0-100 saja"
        print(pesan)
        
    jwb = input("Apakah mau menghitung ulang (Y/T) ? ")
    if jwb=="t" or jwb=="T":
        break
