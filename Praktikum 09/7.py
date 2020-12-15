mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
#header
print("=" * 62)
print("NIM".ljust(10), "NAMA MAHASISWA".ljust(21), "TGL LAHIR".ljust(15), "TEMPAT LAHIR")
print("-" * 62)
#isi
for data in mhs :
    data       = data.split(":")
    nim        = data[0]
    nama       = data[1]
    tgll       = data[2].split('-')
    formattgll = (tgll[2])+"/"+(tgll[1])+"/"+(tgll[0])
    tempat     = data[3]
    print(nim.ljust(10), nama.ljust(21), formattgll.ljust(15), tempat)
#tutup
print("-" * 62)

