i = int(input('mau memasukkan berapa bilangan? '))
j = 0
lis = []
while True:
    x = input('masukkan bilangan : ')
    lis.insert(j, x)
    j+=1
    i-=1
    print ('list yang anda punya', lis)
    if i==0:
        lis.reverse()
        print (lis)
        break
