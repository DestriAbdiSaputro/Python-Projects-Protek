def bintang(n):
    if (n%2 == 1):
        atas = int((0.5 * n)+1)
        bawah = int(0.5 * n)
        for j in range (atas):
            print(("*" * (1 + 2*j)).center(1 + 2*n))
        for j in range (bawah):
            j+=1
            print(("*" * (1 + 2*(bawah-j))).center(1 + 2*n))
    else:
        print('------------------------------------')
        print('Nilai n Harus Berupa Bilangan Ganjil')
        print('------------------------------------')

bintang(15)
