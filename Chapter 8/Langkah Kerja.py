#Nomor 1 - 8
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
a.insert(3, 10)
b.insert(2, 15)
a.insert(11, 4)
b.insert(11, 8)
c = [a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]]
d = [b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9]]
e = [c[0]+d[0], c[1]+d[1], c[2]+d[2], c[3]+d[3], c[4]+d[4], c[5]+d[5], c[6]+d[6], c[7]+d[7]]
datatuple = tuple(e)
print (a)
print (b)
print (datatuple)
print ('nilai maksimalnya', max(datatuple))
print ('nilai minimalnya', min(datatuple))
print ('nilai jumlah dari seluruh data', sum(datatuple))

#Nomor 9 - 11
myString = 'python adalah bahasa pemograman yang menyenangkan'
print('Kata : ', myString)
penyusun = set(myString)
print ('Huruf huruf penyusunnya : ', penyusun)
datahuruf = list(penyusun)
datahuruf.sort()
print('Urutan huruf huruf penyusunnya : ', datahuruf)
