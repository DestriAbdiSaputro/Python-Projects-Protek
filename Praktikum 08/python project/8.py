
print('----------------------------------')
print(' Menghitung Rata- Rata Harga Buah')
print('----------------------------------')
hargabuah = {'apel' : 5000, 'jeruk' : 8500,
             'mangga' : 7800, 'duku' : 6500}
print(hargabuah)
def hargarata():
    jumlah = sum(hargabuah.values())
    rata2 = jumlah/4
    print('Rata-Rata Harga Satuan per Kg : ',rata2,'/kg')
    
hargarata()
