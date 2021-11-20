i = int(input('mau memasukkan berapa kata? '))
j = 0
lis = []
while True:
    k = input('Masukkan kata : ')
    lis.insert(j, k)
    i-=1
    j+=1
    if i==0:
        len(lis)
        lis.sort()
        for kata in lis:
            print (kata, end='')
            print ('(', len(kata), 'karakter)')
        break
