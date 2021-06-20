'''
Reynaldi Jonathan Hartono
Kelas 2A
'''

import os
clear = lambda : os.system('cls')
jwb = 'y'
while jwb== 'y' or jwb=='Y' :
    kota = ['Surabaya','Bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]
    d = 't'
    while d == 't' or d == 'T' :
        clear()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Transaksi Biaya Ekspedisi')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Pilihan Kota')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('>> 1 = ',kota[0],'Jarak = ',jarak[0],'Ongkir PerKm = ',ongkirperkm[0])
        print('>> 2 = ',kota[1],'Jarak = ',jarak[1],'Ongkir PerKm = ',ongkirperkm[1])
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        pil = int(input('Masukkan Pilihan Kota = '))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        d = input('Ingin Lakukan Transaksi ? (Y/T) : ')
        if d == 'y' or d == 'Y' :
            break
        idx = 0
        while idx >=0 and idx < 2 :
            idx = idx + 1 
            if idx == 0 :
                pil = 1
                break
            else:
                idx = pil - 1
                break
        ongkir = jarak[idx]*ongkirperkm[idx]
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('=> Kota              = ',kota[idx])
        print('=> Jarak             = ',jarak[idx], 'Km')
        print('=> Ongkir PerKm      = ',format(ongkirperkm[idx],',.2f'))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('=> Total Harga = ',format(ongkir,',.2f'))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        jwb = input('Beli Lagi ? (Y/T) : ')
        if jwb == 't' or jwb == 'T':
            break

