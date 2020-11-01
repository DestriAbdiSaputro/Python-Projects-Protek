import random

# komputer memilih angka secara acak dari 1 s.d 100
angka = random.randint(1,100)  
# atur agar 

print('Hai, nama saya Destri, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
teks_petunjuk = 'Tebakan Anda : '

tebakan = False
while not tebakan:
  tebak = input(teks_petunjuk)
  tebak = int(tebak)
  if tebak == angka:
    tebakan = True
  elif tebak > angka:
    print('Hehehe...Bilangan tebakan anda terlalu besar')
  else:
      print('Hehehe...Bilangan tebakan anda terlalu kecil')
  

if tebakan:
  print('Yeeee...Bilangan tebakan anda BENAR :-)')
