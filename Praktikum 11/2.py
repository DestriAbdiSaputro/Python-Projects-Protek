from datetime import *
print('-----------------------------------')
print('          Peminjaman Buku          ')
print('-----------------------------------')
simpan = input('Data Tersimpan Dalam File(.txt) : ')
file   = open(simpan,'a')
while True:
    pinjam = datetime.now().date()
    kembali = pinjam + timedelta(days=7)
    kode = input('Masukkan Kode Member    : ')
    nama = input('Masukkan Nama Member    : ')
    judul = input('Masukkan Judul Buku     : ')
    hasil = '|'.join([kode, nama, judul, str(pinjam), str(kembali)])
    file.write(hasil)
    file.write('\n')
    print()
    lagi        = input('Ulangi lagi (y/n)      : ')
    print()
    if lagi == 'y':
        continue
    elif lagi == 'n':
        print('Data peminjaman sudah tersimpan dalam file',simpan)
        break
    else :
        print('y/n')
        break   
file.close()
