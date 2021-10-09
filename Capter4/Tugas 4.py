# import library
import time
import datetime
import math

a_b = int(input('Berapa km jarak kota A ke B? '))
rata2kecab = int(input('Berapa km/jam rata rata kecepatan perjalanan kota A ke B? '))
b_c = int(input('Berapa km perjalanan yang dilanjutkan? '))
rata2kecbc = int(input('Berapa km/jam rata rata kecepatan selanjutnya? '))

waktua_b = a_b/rata2kecab*60
waktub_c = b_c/rata2kecbc*60
istirahat = int(input('Berapa menit waktu yang digunakan untuk istirahat? '))
perjalanan = int(waktua_b + waktub_c + istirahat)
wkttempuh = perjalanan/60
jam = math.floor(wkttempuh)
wktmenit = perjalanan%60
berangkat = int(input('Berangkat pada pukul? '))
berangkatmenit = int(input('Lebih berapa menit? '))

# kasih jeda 3 detik
time.sleep(3)
print ('Jadi perjalanan membutuhkan waktu', perjalanan, 'menit')
print ('sama seperti', jam, 'jam', wktmenit, 'menit' )

# kasih jeda 2 detik
time.sleep(2)
jam2 = berangkat + jam
menit = berangkatmenit + wktmenit
print ('sampai minimal pada pukul', jam2, 'lebih', menit, 'menit')
