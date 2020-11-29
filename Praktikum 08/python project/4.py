print('-----------------------------------------')
print('               Data Sayur                ')
print('-----------------------------------------')
sayur = ['bayam', 'kangkung', 'wortel', 'selada']
print(sayur)
print('Menu:'
      '\n A. Tambah data sayur'
      '\n B. Hapus daya sayur'
      '\n C. Tampilkan data sayur')
while True:
    pil = input('Pilihan Anda: ')
    try:
        if (pil=='A') or (pil=='a') or (pil=='Tambah data sayur'):
            sayur_tambah = input('Nama Sayur: ')
            sayur.append(sayur_tambah)
            print(sayur)
            lagi = input('Lanjut? (y/n) : ')
            if (lagi=='y'):
                continue
            elif (lagi=='n'):
                break
            else:
                print('Hanya Yes(y) or No(n)')
                lagi = input('Lanjut? (y/n) : ')
                if (lagi=='y'):
                    continue
                elif (lagi=='n'):
                    break
        elif (pil=='B') or (pil=='b') or (pil=='Hapus daya sayur'):
            sayur_hapus = input('Nama Sayur: ')
            sayur.remove(sayur_hapus)
            print(sayur)
            lagi = input('Lanjut? (y/n) : ')
            if (lagi=='y'):
                continue
            elif (lagi=='n'):
                break
            else:
                print('Hanya Yes(y) or No(n)')
                lagi = input('Lanjut? (y/n) : ')
                if (lagi=='y'):
                    continue
                elif (lagi=='n'):
                    break
        elif (pil=='C') or (pil=='c') or (pil=='Tampilkan data sayur'):
            print(sayur)
            lagi = input('Lanjut? (y/n) : ')
            if (lagi=='y'):
                continue
            elif (lagi=='n'):
                break
            else:
                print('Hanya Yes(y) or No(n)')
                lagi = input('Lanjut? (y/n) : ')
                if (lagi=='y'):
                    continue
                elif (lagi=='n'):
                    break
        else:
            print('salah menu')
    except ValueError:
        print('Data tidak ditemukan')
    
