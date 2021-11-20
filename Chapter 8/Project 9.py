buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
i = input('Buah yang dibeli : ')
j = int(input('Jumlah yang dibeli(kg) : '))
k = buah[i]*j
print ('Buah yang dibeli  :', i)
print ('Jumlah            :', j,'kg')
print ('--------------------------')
print ('Total Pembayaran  : Rp', k)

