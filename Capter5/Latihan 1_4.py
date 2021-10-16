# import library
import time
import datetime
import math

#Data Perusahaan
a = 10000000
b = 8500000
c = 7000000
d = 5500000
pa = 2.5
pb = 2
pc = 1.5
pd = 1
ppa = int(a*(pa/100))
ppb = int(b*(pb/100))
ppc = int(c*(pc/100))
ppd = int(d*(pd/100))
print ('Tulis Golongan dengan Huruf Kapital (A, B, C, atau D)')
# kasih jeda 1 detik
time.sleep(1)

nama = input('Nama Karyawan: ')
kode = input('Kode Karyawan: ')
gl = str(input('Golongan Karyawan: '))

# kasih jeda 3 detik
time.sleep(3)
print ('---------------------------')
print ('---------------------------')
print ('STRUK RINCIAN GAJI KARYAWAN')
print ('Nama Karyawan    : ', nama)
print ('Kode Karyawan    : ', kode)
print ('---------------------------')

# kasih jeda 1 detik
time.sleep(1)
if (gl == 'A'):
    print ('Gaji Pokok    : Rp',a)
elif ( gl == 'B' ):
    print ('Gaji Pokok   : Rp',b)
elif ( gl == 'C' ):
    print ('Gaji Pokok    : Rp',c)
elif ( gl == 'D' ):
    print ('Gaji Pokok    : Rp',d)

# kasih jeda 1 detik
time.sleep(1)

print ('--------------------------- -')
#Potongan
if (gl == 'A'):
    print ('Potongan(', pa,'%) : Rp',ppa)
elif ( gl == 'B' ):
    print ('Potongan(', pb,'%) : Rp',ppb)
elif ( gl == 'C' ):
    print ('Potongan(', pc,'%) : Rp',ppc)
elif ( gl == 'D' ):
    print ('Potongan(', pd,'%) : Rp',ppd)

# Gaji Bersih
print ('----------------------------')
if (gl == 'A'):
    print ('Gaji Bersih     : Rp',a-ppa)
elif ( gl == 'B' ):
    print ('Gaji Bersih     : Rp',b-ppb)
elif ( gl == 'C' ):
    print ('Gaji Bersih     : Rp',c-ppc)
elif ( gl == 'D' ):
    print ('Gaji Bersih     : Rp',d-ppd)
