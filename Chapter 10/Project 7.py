myfile1 = open('d:\Chapter10.txt', 'r')
file1 = myfile1.read()
print(file1)
i = 0
a = int(input('Masukkan Nilai Pergeseran : '))
for k in range(len(file1)):
    j = file1[i]
    x = ord(j)
    if x==32:
        print(chr(x), end='')
    elif x-a<65:
        d = (91-((65-(x-a))))
        print(chr(d), end='')
    elif x>65:
        x-=int(a)
        y = chr(x)
        print(y, end='')
    i+=1   


