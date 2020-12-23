myfile = input('Masukkan nama file : ')
try:
    file = open(myfile,'r')
    bil = file.readlines()
    genap = 0
    ganjil = 0
    for i in bil:
        j = int(i)
        if j % 2 == 0:
            genap += 1
        if j % 2 == 1:
            ganjil += 1
    print('Banyaknya bilangan genap  : ',genap)
    print('Banyaknya bilangan ganjil : ',ganjil)
except FileNotFoundError:
    print('File Tidak Ada atau Salah Penulisan')
except ValueError:
    print('File Tidak Sesuai Format')
