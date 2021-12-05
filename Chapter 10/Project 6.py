teks = 'SAYA SUKA PYTHON'
print(teks)
i = 0
a = int(input('Masukkan Nilai Pergeseran : '))
for k in range(len(teks)):
    j = teks[i]
    x = ord(j)
    if x==32:
        print(chr(x), end='')
    if x+a>90:
        print(chr(65+((x+a)-91)), end='')
    elif x!=32:
        x+=int(a)
        y = chr(x)
        print(y, end='')
    i+=1

