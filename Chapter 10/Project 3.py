myfile = open('d:\Chapter10.txt', 'r')
list = []
file = myfile.readlines()
for i in range(len(file)):
    x = file[i].split('|')
    data = {'nim': x[0], 'nama': x[1], 'alamat': x[2]}
    list.append(data)

print(list)
myfile.close()
