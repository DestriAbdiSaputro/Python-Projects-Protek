print('----------------------------------')
print('            Toko Buah             ')
print('----------------------------------')
print('apel : 5000',
      '\njeruk : 8500',
      '\nmangga : 7800',
      '\nduku : 6500')
hargabuah = {'apel' : 5000, 'jeruk' : 8500,
             'mangga' : 7800, 'duku' : 6500}
totalbel = 0
data = []
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
