mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('=========================================================')
print('NIM   NAMA MAHASISWA         TGL LAHIR       TEMPAT LAHIR')
print('---------------------------------------------------------')

for n in range(len(mhs)):
    i = mhs[n].split(':')
    print(i[0].ljust(6), end='')
    print(i[1].ljust(20), end='')
    j = (i[2].split('-'))
    j.reverse()
    k = '/'.join(j)
    print(k.rjust(12), end='')
    print(i[3].rjust(19))

