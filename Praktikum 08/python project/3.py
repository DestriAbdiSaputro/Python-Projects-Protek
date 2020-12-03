print('----------------------------------')
print('         Nama Mahasiswa            ')
print('----------------------------------')
data = []
ulang = 0
n = int(input('Jumlah Mahasiswa : '))
while ulang < n:
    nama = str(input('Nama Mahasiswa : '))
    data.append(nama)
    ulang += 1
data.sort()
print('='*30)
for nama in data:
    print(nama,'(',len(nama),') karakter')
    
