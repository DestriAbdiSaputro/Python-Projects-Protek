print('----------------------------------')
print('            Harga Buah            ')
print('----------------------------------')
#data buah
def hargabuah():
    hargabuah = {'apel' : 5000, 'jeruk' : 8500,
                 'mangga' : 7800, 'duku' : 6500}
    buah = input('Harga Buah Paling Mahal : ')
    print(hargabuah.get(buah, 0))
hargabuah()
