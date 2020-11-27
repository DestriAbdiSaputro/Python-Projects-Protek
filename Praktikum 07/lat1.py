nama = input('Masukkan nama file: ')
try:
    file = open(nama)
    mode = file.read()
    print('Isi file',nama, 'adalah:\n')
    print(mode)
except FileNotFoundError:
    print('File Tidak Ada atau Salah Penulisan')
