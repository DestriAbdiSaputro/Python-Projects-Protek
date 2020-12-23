myfile = input('Masukkan Nama File : ')
file = open(myfile, 'w+')
while True:
    nim    = input('Masukkan NIM       : ')
    nama   = input('Masukkan Nama Mhs  : ')
    alamat = input('Masukkan Alamat    : ')
    hasil = '|'.join([nim,nama,alamat])
    file.write(hasil)
    file.write('\n')
    print()
    lagi = input('Ulangi input lagi (y/n): ')
    print()
    if (lagi == 'y') or (lagi == 'Y'):
        continue
    elif (lagi == 'n') or (lagi == 'N'):
        break
    else:
        print('Harus Y/N')
        break
file.close()
