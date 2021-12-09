from datetime import*
def diffDate(x):
    i = datetime.now()
    j = str(i.year)+'-'+str(i.month)+'-'+str(i.day)
    now = datetime.strptime(j, '%Y-%m-%d')
    inp = datetime.strptime(x, '%Y-%m-%d')
    selisih = inp-now
    return selisih.days


k = input('Masukkan (tahun-bulan-tanggal): ')
print (diffDate(k))
