from datetime import*
from dateutil.relativedelta import relativedelta

myfile = open('d:\PinjamBuku.txt', 'r+')
file = myfile.readlines()

list = []
nm = 0
for i in range(len(file)):
    x = file[i].replace('\n', '')
    y = x.split('|')
    data = {'Kode' : y[0],
            'Nama' : y[1],
            'Buku' : y[2],
            'Mulai' : y[3],
            'Maks' : y[4],}
    list.append(data)
    print(list[nm])
    nm+=1
nim = input('Masukkan nim yang dicari : ')

index = 0
for c in list:
    k = c['Kode']
    if k==nim:
            print('Kode Member          :', list[index]['Kode'])
            print('Nama Member          :', list[index]['Nama'])
            print('Judul Buku           :', list[index]['Buku'])
            print('Tanggal Mulai Pinjam :', list[index]['Mulai'])
            print('Tanggal Maks Pinjam  :', list[index]['Maks'])
            dt = list[index]['Maks']
            break
    index+=1

def diffDate(x):
    global j
    i = dt
    j = str(x.year)+'-'+str(x.month)+'-'+str(x.day)
    now = datetime.strptime(j, '%Y-%m-%d')
    inp = datetime.strptime(i, '%Y-%m-%d')
    selisih = now-inp
    return selisih.days
myfile.close()

skr = datetime.now()
hari = diffDate(skr)
denda = diffDate(skr)*2000
print('Tanggal Pengembalian :', j)
if hari==0 or hari<=0:
    print('Terlambat            : - ')
    print('Denda                : -')
else:
    print('Terlambat            :', hari, 'Hari')
    print('Denda                :', denda)
