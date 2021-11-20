buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
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



