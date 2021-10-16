i = 0
jml = 0
jmlbilangan = 0
while i < 100:
    i += 1
    if i%2 == 1:
        print (i)
        jml += 1
        jmlbilangan += i
print ('Banyaknya Bilangan Ganjil: ', str (jml))
print ('Jumlah Semua Bilangan Ganjil: ', int (jmlbilangan))
