buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('------- Menu -------')
print('A. Tambah Data Buah')
print('B. Beli Buah')
print('C. Hapus Data Buah')
menu = input('Pilihan Menu : ')
if menu=='A':
    while True:
        nama = input('Masukkan nama buah : ')
        if nama in buah:
            print('Nama buah sudah terdaftar')
            break
        else:
            brp = int(input('Berapa harganya : '))
            buah[nama] = brp
            print ('Data buah :')
            for daftar in buah.items():
                print (daftar)
            break
elif menu=='B':
    harga = 0
    i = input('Buah yang dibeli : ')
    j = int(input('Jumlah yang dibeli(kg) : '))
    lg = input('Beli buah lain(y/x)? ')
    while True:
        if lg == 'y':
            i = input('Buah yang dibeli : ')
            x = int(input('Jumlah yang dibeli(kg) : '))
            k = buah[i]*j
            lg = input('Beli buah lain(y/x)? ')
            harga+=k
        else:
            print ('Total Pembayaran  : Rp', harga)
            break
elif menu=='C':
    hapus = input('Nama buah yang dihapus : ')
    if hapus in buah:
        del buah[hapus]
        print ('Data buah :')
        for draft in buah.items():
            print (draft)      
    else:
        print('Nama buah tidak terdaftar')


