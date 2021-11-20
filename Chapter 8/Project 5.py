def kuadrat(bil):
    hasil = bil * bil
    return hasil

print('Menghitung nilai kuadrat dari suatu list')
bilangan = []
bilangan2 = []
brp = int(input('Membuat list berapa bilangan? '))
while True:
    bil = int(input('Sebutkan Bilangan : '))
    bilangan.append(bil)
    brp-=1
    bilangan2.append(kuadrat(bil))
    if brp==0:
        print('List Data Yang Dimiliki : ', bilangan)
        print('List Operasional Kuadrat :', bilangan2)
        break
