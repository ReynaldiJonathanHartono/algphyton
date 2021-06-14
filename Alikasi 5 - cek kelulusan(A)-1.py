# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:31:47 2021

@author: Reynaldi Jonathan Hartono
"""
#cek kelulusan
import os
Clear = lambda : os.system('cls')

jwb = "y"
while jwb=="y" or jwb=="Y":  
    Clear()
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("       Cek Kelulusan")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("by Jonathan")
    
    n = int(input("Masukkan Nilai = "))
    #cek nilai
    if int(n)>0 and int(n)<=100:
        if n>60:
            sts = "LULUS"
        else:
            sts = "ULANG"
        print(sts)
    else:
        pesan="Masukkan 0-100 saja"
        print(pesan)
        
    jwb = input("Apakah mau menghitung ulang (Y/T) ? ")
    if jwb=="t" or jwb=="T":
        break


