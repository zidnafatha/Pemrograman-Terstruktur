teks = input('Masukkan kalimat/kata yang akan diubah : ')
a = input('Huruf yang akan dirubah : ')
b = input('Update perubahan : ')
def ubahHuruf(teks, a, b):
    i = teks.replace(a, b )
    print (i)

ubahHuruf(teks, a, b)
