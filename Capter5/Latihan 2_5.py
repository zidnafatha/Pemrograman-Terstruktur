print('Hallo... Nama saya Mr Robeth, Saya akan Memilih Bilangan Acak dari 1-100')
print('Silahkan Ditebak yaa...')
from random import randint
bil = randint (0,100)

while True:
    tebakan = int(input('Tebakan Anda: '))
    if tebakan < bil:
        print('Bilangan Tebakan Anda Terlalu Kecil')
    elif tebakan > bil:
        print('Bilangan Tebakan Anda Terlalu Besar')
    elif tebakan == bil:
        print('Yeeey... Tebakan Anda Benar')
        break
print ('Terimakasih Telah Bermain')
