i = int(input('Menghendaki berapa baris? '))
def bintang(n):
    space = 2*n-1
    for x in range(i):
        print(('*'*(2*x+1)).center(space))

bintang(i)
        
