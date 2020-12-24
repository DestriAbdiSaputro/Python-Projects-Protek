file = open('2.txt', 'r')
data = file.readlines()
nim  = input('Masukkan NIM yang mau dicari: ')
print()
dict = {}
isi = False
for i in data:
    pisah = i.split('|')
    dict = {'nim': pisah[0],'nama': pisah[1],'alamat': pisah[2]}
    if nim == dict['nim'] :
        isi = True
        print('Data Mahasiswa')
        print('NIM      : ',dict['nim'])
        print('Nama     : ',dict['nama'])
        print('Alamat   : ',dict['alamat'])
if isi == False:
    print('"Data mahasiswa tidak ditemukan"')
