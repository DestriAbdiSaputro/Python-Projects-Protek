print(" Total Tarif Yang Harus Dibayar Customer")

jam_sewa = float(input("Jam Sewa : "))
jam_kembali = float(input("Jam Kembali : "))
lama_sewa = jam_kembali - jam_sewa
if lama_sewa <= 12:
    biaya_akhir = 200000
elif lama_sewa > 12:
    waktu_pokok = 12
    waktu_lebih = lama_sewa - waktu_pokok
    biaya_12_jam = 200000
    biaya_perpanjangan = waktu_lebih//1 * 10000
    biaya_akhir = biaya_12_jam + biaya_perpanjangan
print(" Lama Sewa : ",lama_sewa)
print(" Biaya Sewa : Rp",biaya_akhir)
