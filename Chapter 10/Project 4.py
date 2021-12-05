myfile = open('d:\Chapter10.txt', 'r')
list = []
file = myfile.readlines()
for i in range(len(file)):
    x = file[i].split('|')
    data = {'nim': x[0], 'nama': x[1], 'alamat': x[2]}
    list.append(data)
    
print(list)
nim = input('Masukkan nim yang dicari : ')
index = 0
for j in list:
    k = j['nim']
    if k==nim:
        l = list[index]
        for x, y in l.items():
            print(x+' : '+y)
    else:
        print('Data tidak ditemukan')
        break
    index+=1
myfile.close()
