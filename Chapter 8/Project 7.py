buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print (buah)
def hargamahal():
    i = max(list(buah.values()))
    for key, value in buah.items():
        if value == i:
            print (key)
            
print ('Harga buah Termahal adalah : ', end='')
hargamahal()


