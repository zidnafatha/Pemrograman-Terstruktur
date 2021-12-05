myfile = open('d:\Chapter10.txt', 'r')
x = 0
ganjil = 0
genap = 0
file = myfile.readlines()
i = len(file)
while True:
    y = int(file[x])
    x+=1
    i-=1
    if y%2==0:
        genap+=1
    if y%2==1:
        ganjil+=1
    if i==0:
        break
print ('Banyak bilangan ganjil :', ganjil)    
print ('Banyak bilangan genap :', genap)
