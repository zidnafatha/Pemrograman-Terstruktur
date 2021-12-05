myfile = open('d:\Chapter10.txt', 'w+')
while True:
    bil1 = input(str('Masukkan angka pertama : '))
    bil2 = input(str('Masukkan angka kedua   : '))
    myfile.write(bil1+'|'+bil2+'\n')
    x = input('Ulangi input lagi(y/n) : ')
    if x=='y':
        continue
    if x=='n':
        myfile.close()
        break

myfile1 = open('d:\Chapter10.txt', 'r')
file = myfile1.readlines()
myfile1 = open('d:\Chapter10.txt', 'r')
file1 = myfile1.read()
print (file1)
list = []
for i in range(len(file)):
    x = file[i].split('|')
    data = int(x[0])+int(x[1])
    list.append(data)
for j in list:
    print (j)
myfile.close()
