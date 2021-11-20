print('Program memengurutkan list kata dari yang terbanyak karakter')
x = []
while True:
    i = input('Buat isian list : ')
    x.append(i)
    lagi = input('Lagi? (y/n)')
    if lagi=='n':
        print ('List data : ', x)
        break
    
def sortStringByChar(x):
    data = sorted(x, reverse=True, key = len)
    return data

print('Data : ', sortStringByChar(x))
