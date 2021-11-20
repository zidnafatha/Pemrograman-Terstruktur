sayur = ['bayam', 'kangkung', 'wortel', 'selada']
print ('Jenis sayuran: ', sayur)
print('-----------------------')
print ('Menu')
print('A. Tambah Data Sayur')
print('B. Kurangi Data Sayur')
print('C. Print Data Sayur')
print('---------------------')
while True:
    try:
        i = input('Pilihan Menu : ')
        if i=='A':
            j = input('Masukkan : ')
            sayur.append(j)
            continue
        elif i=='B':
            print(sayur)
            j = input('Data apa yang dihapus : ')
            sayur.remove(j)
            continue
        elif i=='C':
            print (sayur)
            break
    except:
        print('Data Sayur Tidak Ditemukan')

