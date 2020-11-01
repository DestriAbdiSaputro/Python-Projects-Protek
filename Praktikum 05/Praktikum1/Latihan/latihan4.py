#kode karyawan
kode = input("Masukkan kode karyawan    : ")
#nama karyawan
nama = input("Masukkan nama karyawan    : ")
#golongan
gol = input("Masukkan golongan         : ")
if (gol == "A") or (gol == "a"):
 gaji_pokok = 10000000
 potongan = 2.5 
elif (gol == "B") or (gol == "b"):
    gaji_pokok = 8500000
    potongan = 2.0 
elif (gol == "C") or (gol == "c"):
    gaji_pokok = 7000000
    potongan = 1.5 
elif (gol == "D") or (gol == "d"):
    gaji_pokok = 5500000
    
    potongan = 1.0 
print("=====================================")
print("     STRUK RINCIAN GAJI KARYAWAN     ")
print("-------------------------------------")
#tampilan nama karyawan
print("Nama Karyawan          :",nama, "(Kode:",kode,")")
#tampilan golongan
print("Golongan               :",gol)
print("-------------------------------------")
#gaji pokok
print("Gaji Pokok             : Rp ",gaji_pokok)
#potongan
potong = gaji_pokok*potongan/100
print("Potongan (",potongan,"%)      : Rp ",potong)
print("------------------------------------- -")
print("Gaji Bersih            : Rp ",gaji_pokok-potong)
