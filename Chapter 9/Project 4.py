import random
string = input('Masukkan String yang akan diubah : ')
loop = (int(input('Berapa Kali Perulangan? ')))
def shuffleString(x, n):
    lis = []
    while True:
        i = ''.join(random.sample(x,len(x)))
        if i in lis:
            continue
        else:
            lis.append(i)
            n-=1
            if n==0:
                print(lis)
                break

print('randomString(', string, loop,') -> ', end='')
shuffleString(string, loop)

