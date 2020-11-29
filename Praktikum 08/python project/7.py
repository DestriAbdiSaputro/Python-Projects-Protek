print('----------------------------------')
print('            Harga Buah            ')
print('----------------------------------')
print({'apel' : 5000, 'jeruk' : 8500,
      'mangga' : 7800, 'duku' : 6500})
hargabuah = {'apel' : 5000, 'jeruk' : 8500,
             'mangga' : 7800, 'duku' : 6500}
maks = max(hargabuah['apel'], hargabuah['jeruk'],
           hargabuah['mangga'],hargabuah['duku'])
def hargamax():
    for i in hargabuah:
        if maks == hargabuah[i]:
            print('Harga Paling Mahal : ', i)

hargamax()
