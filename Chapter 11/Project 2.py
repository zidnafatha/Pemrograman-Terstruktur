from datetime import*
from dateutil.relativedelta import relativedelta

myfile = open('d:\PinjamBuku.txt', 'w+')
while True:
    a = input('Masukkan Kode Member : ')
    b = input('Masukkan Nama Member : ')
    c = input('Masukkan Judul Buku  : ')
    i = datetime.now()
    j = str(i.year)+'-'+str(i.month)+'-'+str(i.day)
    k = datetime.now() + relativedelta(days=7)
    l = str(k.year)+'-'+str(k.month)+'-'+str(k.day)
    myfile.write(a+'|'+b+'|'+c+'|'+j+'|'+l+'\n')
    x = input('Ulangi Lagi? (y/n) ')
    if x=='y':
        continue
    elif x=='n':
        myfile = open('d:\PinjamBuku.txt', 'r+')
        data = myfile.read()
        print(data)
        break
    else:
        print('INPUT SALAH! RUNNING ULANG')
