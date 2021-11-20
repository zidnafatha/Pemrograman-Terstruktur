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

nilaiMhs = [{'nim':'A01','nama':'Amir','mid':50,'uas':80},
            {'nim':'A02','nama':'Budi','mid':40,'uas':90},
            {'nim':'A03','nama':'Cici','mid':50,'uas':50},
            {'nim':'A04','nama':'Dedi','mid':20,'uas':30},
            {'nim':'A05','nama':'Fifi','mid':70,'uas':40}]

i = 0
while True:
    print (nilaiMhs[i])
    i+=1
    if i==5:
        break

def carinilaitertinggi(list):
    nilaiakhir=[]
    nomorindex=[]
    i=0
    for data in list:
        mid= data['mid']
        uas= data['uas']
        x= (mid+2*uas)/3
        nilaiakhir+=[round(x)]
        
    for x in nilaiakhir:
        tertinggi=max(nilaiakhir)
        if x==tertinggi:
            nomorindex+=[i]
            break
        i+=1

    for i in nomorindex:
        print('Mahasiswa dengan nilai tertinggi adalah', list[i]['nama'],'('+list[i]['nim']+')')

i = 0
while True:
    print (nilaiMhs[i])
    i+=1
    if i==5:
        break
carinilaitertinggi(nilaiMhs)
