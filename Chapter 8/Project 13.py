nilaiMhs = [{'nim':'A01','nama':'Amir','mid':50,'uas':80},
            {'nim':'A02','nama':'Budi','mid':40,'uas':90},
            {'nim':'A03','nama':'Cici','mid':50,'uas':50},
            {'nim':'A04','nama':'Dedi','mid':20,'uas':30},
            {'nim':'A05','nama':'Fifi','mid':70,'uas':40}]

def nilaiakhir(nilaiMhs):
    nilaiakhir = 0
    akhir = {}
    for x in nilaiMhs:
        nilai = (x['mid']+(2*x['uas']))/3
        if(nilaiakhir == 0) or (nilai > nilaiakhir):
            nilaiakhir = nilai
            akhir['nim'] = x['nim']
            akhir['nama'] = x['nama']
            print (akhir['nama'],',', end='')
            print ('(', (akhir['nim']), ')')
            break
    return akhir

i = 0
while True:
    print (nilaiMhs[i])
    i+=1
    if i==5:
        break

print('Mahasiswa dengan nilai tertinggi adalah ', end='')
nilaiakhir(nilaiMhs)
