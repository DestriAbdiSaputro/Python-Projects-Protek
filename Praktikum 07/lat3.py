print('-------------------------------')
print('   PROGRAM HITUNG RATA-RATA    ')
print('-------------------------------')
data =[]
sum = 0
while True:
    try:
        nilai = int(input('Masukkan bilangan bulat: '))
        data = data + [nilai]
        lagi = input("Lagi (y/n)? : ")
        if (lagi == 'y'):
            continue
        elif (lagi == 'n') :
            break
    except ValueError:
        print('Bukan Bilangan Bulat')

for angka in data:
    sum = sum + angka
rata2 = sum/len(data)
print('Rata-ratanya adalah : ', rata2)
