def faktorial(x):
    hasil = 1
    for i in range(2,x + 1):
        hasil *= i
    return hasil
def comb(n, r):
    hasil = faktorial(n)/(faktorial(r)*faktorial(n-r))
    return hasil
def permutasi(n, r):
    hasil = faktorial(n)/faktorial(n-r)
    return hasil
print(comb(5,3))
print(permutasi(10,7))
