myfile = open('d:\Chapter10.txt', 'w+')
while True:
    nim = input(str('Masukkan NIM    : '))
    nama = input(str('Masukkan Nama   : '))
    alamat = input(str('Masukkan Alamat : '))
    myfile.write(nim+'|'+nama+'|'+alamat+'\n')
    x = input('Ulangi input lagi(y/n) : ')
    if x=='y':
        continue
    if x=='n':
        myfile.close()
        break
    
myfile1 = open('d:\Chapter10.txt', 'r')
file1 = myfile1.read()
print (file1)
