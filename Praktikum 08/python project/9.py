print('----------------------------------')
print('            Toko Buah             ')
print('----------------------------------')
print('apel : 5000',
      '\njeruk : 8500',
      '\nmangga : 7800',
      '\nduku : 6500')
hargabuah = {'apel' : 5000, 'jeruk' : 8500,
             'mangga' : 7800, 'duku' : 6500}

namabuah = input('Nama buah yang dibeli : ')
harga = hargabuah.get(namabuah)
kg = int(input('Berapa Kg             : '))
total = harga*kg
print('----------------------------')
print('Total harga           : Rp.',total)
