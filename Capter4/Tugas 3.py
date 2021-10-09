# import library
import time
import datetime

#Judul
print ('Kita akan menghitung keperluan bbm pada jarak tertentu')

# kasih jeda 2 detik
time.sleep(2)

# jarak kota
akec = int(input('Jarak Kota A ke C berapa km? '))
perbandingan = int(input('Tiap lt bbm bisa untuk berapa km? '))

# kasih jeda 3 detik
time.sleep(3)
keperluanbbm = (akec/perbandingan)
print ('ohh... jadi jarak', akec, 'km dapat ditempuh dengan bbm minimal ', keperluanbbm, 'lt')

# kasih jeda 2 detik
time.sleep(2)
print ('Sekarang akan menghitung berapa kali pengisian bbm kendaraan')

# kasih jeda 2 detik
time.sleep(2)

# hitung minimal pengisian air
kapasitas = int(input('Berapa lt kapasitas tangki kendaraan? '))

# kasih jeda 2 detik
time.sleep(2)
minimal = keperluanbbm//kapasitas + 1
print ('jadi pengisian bbm dari kota A ke C hanya perlu', minimal, 'kali saja')
