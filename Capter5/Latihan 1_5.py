# import library
import time
import datetime
import math

#Data Perusahaan
#Gaji Pokok
a = 10000000
b = 8500000
c = 7000000
d = 5500000
#Potongan
pa = 2.5
pb = 2
pc = 1.5
pd = 1
ppa = int(a*(pa/100))
ppb = int(b*(pb/100))
ppc = int(c*(pc/100))
ppd = int(d*(pd/100))

print ('Tulis Golongan dengan Huruf Kapital (A, B, C, atau D)')
print ('Tulis 1 jika sudah menikah, 2 jika belum')

# kasih jeda 1 detik
time.sleep(1)
nama = input('Nama Karyawan: ')
kode = input('Kode Karyawan: ')
gl = str(input('Golongan Karyawan: '))
stt = str(input('Status Karyawan: '))
if(stt=='1'):
    ank = int(input('Jumlah Anak : '))
else:
    ank=0
#Status dan Tunjangan
nikah = 1
blmnikah = 2
ta = int(a*(10/100))
tb = int(b*(10/100))
tc = int(c*(10/100))
td = int(d*(10/100))
tta = int(ank*(a*(5/100)))
ttb = int(ank*(b*(5/100)))
ttc = int(ank*(c*(5/100)))
ttd = int(ank*(d*(5/100)))

# kasih jeda 3 detik
time.sleep(3)
print ('----------------------------------')
print ('----------------------------------')
print ('STRUK RINCIAN GAJI KARYAWAN')
print ('Nama Karyawan    : ', nama)
print ('Kode Karyawan    : ', kode)
print ('----------------------------------')

# kasi/h jeda 1 detik
time.sleep(1)

#Gaji Pokok
if (gl == 'A'):
    print ('Gaji Pokok            : Rp',a)
elif ( gl == 'B' ):
    print ('Gaji Pokok            : Rp',b)
elif ( gl == 'C' ):
    print ('Gaji Pokok            : Rp',c)
elif ( gl == 'D' ):
    print ('Gaji Pokok            : Rp',d)

# Tunjangan Menikah
if (gl=='A')and(stt=='1'):
    print ('Tunjangan Istri/Suami : Rp',ta)
    print ('Tunjangan Anak        : Rp',tta)
elif (gl=='A')and(stt=='2'):
    print ('Tunjangan Istri/Suami : Rp',ta)
if (gl=='B')and(stt=='1'):
    print ('Tunjangan Istri/Suami : Rp',tb)
    print ('Tunjangan Anak        : Rp',ttb)
elif (gl=='B')and(stt=='2'):
    print ('Tunjangan Istri/Suami : Rp',tb)
if (gl=='C')and(stt=='1'):
    print ('Tunjangan Istri/Suami : Rp',tc)
    print ('Tunjangan Anak        : Rp',ttc)
elif (gl=='C')and(stt=='2'):
    print ('Tunjangan Istri/Suami : Rp',tc)
if (gl=='D')and(stt=='1'):
    print ('Tunjangan Istri/Suami : Rp',td)
    print ('Tunjangan Anak        : Rp',ttd)
elif (gl=='D')and(stt=='2'):
    print ('Tunjangan Istri/Suami : Rp',td)

# kasih jeda 1 detik
time.sleep(1)

print ('----------------------------------- -')
#Potongan
if (gl == 'A'):
    print ('Potongan(', pa,'%)     : Rp',ppa)
elif ( gl == 'B' ):
    print ('Potongan(', pb,'%)     : Rp',ppb)
elif ( gl == 'C' ):
    print ('Potongan(', pc,'%)     : Rp',ppc)
elif ( gl == 'D' ):
    print ('Potongan(', pd,'%)     : Rp',ppd)

# Gaji Bersih
print ('----------------------------------- +')
if (gl == 'A'):
    print ('Gaji Bersih          : Rp',a+ta+tta-ppa)
elif ( gl == 'B' ):
    print ('Gaji Bersih          : Rp',b+tb+ttb-ppb)
elif ( gl == 'C' ):
    print ('Gaji Bersih          : Rp',c+tc+ttc-ppc)
elif ( gl == 'D' ):
    print ('Gaji Bersih          : Rp',d+td+ttd-ppd)
