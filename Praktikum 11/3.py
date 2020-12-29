import datetime
def diffDate(x): 
    now = datetime.datetime.now()
    nx = x.split('-')
    skrg = datetime.datetime(now.year,now.month,now.day) 
    x = datetime.datetime(int(nx[0]), int(nx[1]), int(nx[2])) 
    selisih = skrg-x
    return selisih.days
print('-----------------------------------')
print('          Peminjaman Buku          ')
print('-----------------------------------')
try:
    simpan = input('Nama File Data Peminjaman : ')
    file = open(simpan,'r')
    kode = input('Masukkan Kode Member : ')
    isi = False
    for i in file.readlines():
        x = i.split('|')
        x[4] = x[4].rstrip('\n')
        dict = {'kode':x[0],'nama':x[1],'judul':x[2],'pinjam':x[3],'maks':x[4]}
        if dict['kode'] == kode:
            isi = True
            kembali = datetime.datetime.today().date()
            terlambat = diffDate(dict['maks'])
            if terlambat < 0:
                terlambat = 0
            denda = 2000 * terlambat
            print()
            print('Data Peminjaman Buku')
            print('Kode Member              :',dict['kode']    )
            print('Nama Member              :',dict['nama']    )
            print('Judul Buku               :',dict['judul']   )
            print('Tanggal Mulai Peminjaman :',dict['pinjam']  )
            print('Tanggal Maks Peminjaman  :',dict['maks']    )
            print('Tanggal Pengembalian     :',kembali         )
            print('Terlambat                :',terlambat,'hari')
            print('Denda                    : Rp',denda        )
    if isi == False:
        print('Kode member',kode,'tidak ada dalam data peminjaman.')
except FileNotFoundError:
    print('File Data Peminjaman Tidak Ada')
