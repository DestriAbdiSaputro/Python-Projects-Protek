import math

print(" Menghitung Waktu Tempuh Pak Amir dari Kota A ke Kota C")
jA = 125
rA = 62
waktuA = jA/rA
print(" Waktu Tempuh kota A ke B ",waktuA)
istirahat = 45
jB = 256
rB = 70
waktuB = jB/rB
jam = waktuA+waktuB
print(" Waktu Tempuh kota B ke C ",waktuB)
print(" Waktu Tempuh A ke C ", jam)
akhir = jam*60 + istirahat
jam = int(akhir //60 + 6)
menit = int(akhir % 60)
print(" Pak Amir sampai di Kota C pada pukul ",jam,".",menit)
