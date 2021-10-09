# import library
import time
import datetime
import math

#menghitung dana sewa
tarifsewa1 = 200000
tarifsewa2 = 10000

# kasih jeda 2 detik
time.sleep(2)
print('Tulis Berdasarkan Jam bulatnya saja')
print('ex = pukul 06.30 tulis 6')
mulai = int(input('Pukul berapa customer mulai menyewa? '))
mulai1 = int(input('Lebih berapa menit? '))
kembali = int(input('Pukul berapa customer mengembalikan? '))
kembali1 = int(input('Lebih berapa menit? '))

lamapinjam = kembali - mulai
lamapinjam1 = (kembali1 - mulai1)
sisa = lamapinjam-12

# kasih jeda 2 detik
time.sleep(2)
print ('Lama pinjam', lamapinjam,'jam', lamapinjam1,'menit')
jam = lamapinjam1/60

# kasih jeda 2 detik
time.sleep(2)             
tarif = tarifsewa1 + (tarifsewa2*jam) + (sisa*tarifsewa2)
trf = math.ceil(tarif)                      
print ('jadi, tarif penyewaan Rp', trf)
