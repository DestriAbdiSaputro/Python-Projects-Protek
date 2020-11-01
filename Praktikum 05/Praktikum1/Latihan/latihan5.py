#kode karyawan
kode = input("Masukkan kode karyawan                      : ")
#nama karyawan
nama = input("Masukkan nama karyawan                      : ")
#golongan
gol =  input("Masukkan golongan                           : ")
if (gol == "A") or (gol == "a"):
 gaji_pokok = 10000000
 potongan = 2.5
 tunjangan = gaji_pokok*10/100
 tunjangan_anak = gaji_pokok*5/100
elif (gol == "B") or (gol == "b"):
    gaji_pokok = 8500000
    potongan = 2.0
    tunjangan = gaji_pokok*10/100
    tunjangan_anak = gaji_pokok*5/100
elif (gol == "C") or (gol == "c"):
    gaji_pokok = 7000000
    potongan = 1.5
    tunjangan = gaji_pokok*10/100
    tunjangan_anak = gaji_pokok*5/100
elif (gol == "D") or (gol == "d"):
    gaji_pokok = 5500000
    potongan = 1.0
    tunjangan = gaji_pokok*10/100
    tunjangan_anak = gaji_pokok*5/100
#status
status = input("Masukkan status(1:Menikah,2:Belum Menikah)  : ")
if (status == "1") or (status == "menikah") or (status =="Menikah"):
    anak = int(input("Masukkan jumlah anak                        : "))
print("============================================")
print("        STRUK RINCIAN GAJI KARYAWAN         ")
print("--------------------------------------------")
#tampilan nama karyawan
print("Nama Karyawan          :",nama, "(Kode:",kode,")")
#tampilan golongan
print("Golongan               :",gol)
#status menikah
print("Status Menikah         :",status)
if (status == "1") or (status == "menikah") or (status =="Menikah"):
    print("Jumlah Anak            :",anak)
else:
    print("Jumlah Anak            : -")
print("--------------------------------------------")
#gaji pokok
print("Gaji Pokok             : Rp ",gaji_pokok)
if (status == "1") or (status == "menikah") or (status =="Menikah"):
    print("Tunjangan Istri/Suami  : Rp ",tunjangan)
    print("Tunjangan Anak         : Rp ",tunjangan_anak*anak)
else:
    print("Tunjangan Istri/Suami  : - ")
    print("Tunjangan Anak         : - ")
print("-------------------------------------------- +")
#gaji kotor
if (status == "1") or (status == "menikah") or (status =="Menikah"):
    gaji_kotor = gaji_pokok+tunjangan+tunjangan_anak*anak
    print("Gaji Kotor             : Rp ",gaji_kotor)
else:
    print("Gaji Kotor             : Rp ",gaji_pokok)
#potongan

if (status == "1") or (status == "menikah") or (status =="Menikah"):
    potong = gaji_kotor*potongan/100
    print("Potongan(",potongan,"%)       : Rp ",potong)
else:
    print("Potongan(",potongan,"%)       : Rp ",gaji_pokok*potongan/100)
print("-------------------------------------------- -")
if (status == "1") or (status == "menikah") or (status =="Menikah"):
    print("Gaji Bersih            : Rp ",gaji_kotor-potong)
else:
    print("Gaji Bersih            : Rp ",gaji_pokok-gaji_pokok*potongan/100)
