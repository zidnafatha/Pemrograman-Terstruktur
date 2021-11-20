i = int(input('mau memasukkan berapa bilangan? '))
z = i
j = 0
h = 0
lis = []
while True:
    x = int(input('masukkan bilangan : '))
    lis.insert(j, x)
    j+=1
    i-=1
    h+=x 
    x = lis
    if i==0:
        print('list yang anda punya', lis)
        break
def dataStat():
    a = h/z
    b = max(lis)
    c = min(lis)
    list = [h/z, max(lis), min(lis)]
    print('Statistika nilai rata rata, max, dan min')
    print(list)

dataStat()
