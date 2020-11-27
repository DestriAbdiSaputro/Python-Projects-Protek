nama = input("Masukkan nama file: ")
try:
    file = open(nama, "a")
    file.write(input("Data yang mau ditambahkan: "))
    lagi = input("Mau lagi (y/n) : ")
    while (lagi == 'y'):
        file.write(input("Data yang mau ditambahkan: "))
        lagi = input("Mau lagi (y/n) : ")
    if (lagi == 'n'):
        file.close()
except FileNotFoundError:
    print("File Tidak Ada")
