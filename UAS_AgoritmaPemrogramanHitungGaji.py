"""
UAS ALGORITMA PEMROGRAMAN
REYNALDI JONATHAN HARTONO
20083000010 / 2A
"""

import os
import sys
import datetime
from time import process_time_ns

x = datetime.datetime.now()
    
golongan=[1,2,3]
gajiPokok=[2500000,4500000,6500000]
os.system('cls')
#PROGRAM TRANSAKSI
print("=============================================")
print("    PERHITUNGAN GAJI KARYAWAN CV. LOGOS")
print("    MOHON DATA DIISI DENGAN BENAR!!!")
print("             Tanggal : ",x.strftime("%x"))
print("=============================================")
print("")
print("")
nama =    input("Nama                :" + " "*2)
gol = int(input("Golongan            :" + " "*2))
jk =      input("Jenis Kelamin (L/P) :" + " "*2)
sk =      input("Status Kawin        :" + " "*2)
ja =  int(input("Jumlah Anak         :" + " "*2))
os.system('cls')

if gol== 1:
    i = 0
    tunjangan = 0.01
elif gol== 2:
    i = 1 
    tunjangan = 0.03
elif gol== 3:
    i = 2
    tunjangan = 0.05
if jk.upper() == "L" and sk.lower() == 'kawin':
    tunIstri = gajiPokok[i]*tunjangan 
else: tunIstri = 0
if sk.lower() == 'kawin' and ja > 0:
    tunAnak = gajiPokok[i] * 0.02
else: tunAnak = 0
gajiBrt = gajiPokok[i] + tunAnak + tunIstri
biayaJbtn = gajiBrt * 0.005
iuranP = 15000
iuranO = 3500
gajiNet = gajiBrt - biayaJbtn - iuranO - iuranP
print(" ")

print(" ")
print("=============================================")
print("                  SLIP GAJI")
print("             Tanggal : ",x.strftime("%x"))
print("=============================================")
print("")
print("")
print("Nama                 :"," ",nama)
print("Golongan             :"," ",gol)
print("Jenis Kelamin        :"," ",jk)
print("Status Kawin         :"," ",sk)
print("Gaji Pokok           :"," ",gajiPokok[i])
print("Tunjangan Istri      :"," ",tunIstri)
print("Tunjangan Anak       :"," ",tunAnak)
print(">> Gaji Bruto        :"," ",gajiBrt)
print("_"*22)
print("Biaya Jabatan        :"," ",biayaJbtn)
print("Iuran Pensiun        :"," ",iuranP)
print("Iuran Organisasi     :"," ",iuranO)
print(">>Gaji Netto         :"," ",gajiNet)

    

