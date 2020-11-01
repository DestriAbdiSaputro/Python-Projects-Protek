from random import randint
jumlah = 0
while True:
    bil = randint(0,10)
    print(bil)
    jumlah += 1
    if bil == 5:
        break
print("Jumlah Perulangan : " , jumlah)
