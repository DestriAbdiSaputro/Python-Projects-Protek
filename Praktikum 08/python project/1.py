print('---------------------------------------')
print('  Mengurutkan Bilangan Besar ke Kecil')
print('---------------------------------------')
#input bil bulat
data = []
try:
    #input banyak bil bulat
    n = int(input('Banyak Bilangan Bulat : '))
    for i in range (n):
        bil = int(input('Masukkan Bilangan Bulat : '))
        data = data +[bil]
        data.sort(reverse=True)
except ValueError:
    print('Bukan Bilangan Bulat')
print('Bilangan Bulat Dari Besar ke Kecil : ',data)
