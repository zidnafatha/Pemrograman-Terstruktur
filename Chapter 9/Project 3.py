i = int(input('Menghendaki berapa baris? '))

def bintang(n):
    space = i
    for x in range((i//2)+1):
        print(('*'*(2*x+1)).center(space))
    for x in reversed(range(i//2)):
        print(('*'*(2*x+1)).center(space))
        
bintang(i)  

        
