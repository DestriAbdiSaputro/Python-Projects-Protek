import random

# komputer memilih angka secara acak dari 1 s.d 100
angka = random.randint(1,100)

print('Hai, nama saya Destri, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
teks_petunjuk = 'Tebakan Anda : '
score = 100
score_min = 0
tebakan = False
nomor_tebakan = 0
while not tebakan:
  tebak = input(teks_petunjuk)
  tebak = int(tebak)
  nomor_tebakan = nomor_tebakan + 1
  score = 100-nomor_tebakan*2
  if tebak == angka:
    tebakan = True
  elif tebak > angka:
    print('Hehehe...Bilangan tebakan anda terlalu besar')
  else:
      print('Hehehe...Bilangan tebakan anda terlalu kecil')
  

if tebakan:
  print('Yeeee...Bilangan tebakan anda BENAR :-)')
if score < score_min:
    print('Score Anda: ',score_min)
else:
    print('Score Anda: ',score)
