def bintang(n) :
    for i in range(0,n) :
        bin = "*" * (1 + 2*i)
        center = bin.center(1+2*n)
        print(center)

bintang(15)
