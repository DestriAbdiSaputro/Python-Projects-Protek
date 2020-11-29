print('----------------------------------')
print('            Toko Buah             ')
print('----------------------------------')
print('apel : 5000',
      '\njeruk : 8500',
      '\nmangga : 7800',
      '\nduku : 6500')
print('Menu:'
      '\n A. Tambah data buah'
      '\n B. Beli buah'
      '\n C. Hapus data buah')
hargabuah = {'apel' : 5000, 'jeruk' : 8500,
             'mangga' : 7800, 'duku' : 6500}
totalbel = 0
data = []
pil = input('Pilihan Anda: ')
if (pil=='A') or (pil=='a') or (pil=='Tambah data buah'):
    namabaru = input('Masukkan nama buah : ')
    if namabaru in hargabuah.keys():
        print('Nama buah sudah ada dalam dictionary')
    else:
        hargabaru = int(input('Masukkan harga satuan : '))
        hargabuah[namabaru] = hargabaru
        print('Data buah :',hargabuah)
elif (pil=='B') or (pil=='b') or (pil=='Beli buah'):
    while True:
        namabuah = input('Nama buah yang dibeli : ')
        harga = hargabuah.get(namabuah)
        kg = int(input('Berapa Kg             : '))
        total = harga*kg
        data = data +[total]
        lagi = input('Beli buah yang lain(y/n)? : ')
        if (lagi == 'y'):
            continue
        elif (lagi == 'n'):
            break
    for i in data:
        totalbel = totalbel + i
    total1 = totalbel
    print('----------------------------')
    print('Total harga           : Rp.',total1)
elif (pil=='C') or (pil=='c') or (pil=='Hapus data buah'):
    hapusdata = input('Nama buah yang dihapus : ')
    del hargabuah[hapusdata]
    print(hargabuah)
