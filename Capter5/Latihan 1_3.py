# Pengerjaan Rapor

bindo = int(input('Masukkan nilai Bahasa Indonesia: '))
matik = int(input('Masukkan nilai Matematika: '))
ipa = int(input('Masukkan nilai IPA: '))
x = 'LULUS'
y = 'TIDAK LULUS'

    
if (0>=bindo) or (0>=matik) or (0>=ipa):
    print ('Maaf nilai tidak valid')
elif (100<=bindo) or (100<=matik) or (100<=ipa):
    print ('Maaf nilai tidak valid')
elif (bindo>60) and (matik>70) and (ipa>60):
    print ('Status kelulusan:',x)
else:
    print('Status kelulusan:', y)

#Sebab
if (bindo<60) and (matik<70) and (ipa<60):
    print ('Sebabnya : ')
if (bindo<60):
    print ('Nilai Bahasa Indonesia kurang dari 60')
if (matik<70):
    print ('Nilai Matematika kurang dari 70')
if (ipa<60):
    print ('Nilai IPA kurang dari 60')




