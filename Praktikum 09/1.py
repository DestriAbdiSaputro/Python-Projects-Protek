def ubahHuruf(teks, a, b):
    listteks = list(teks)
    hasil = ''
    for x in listteks:
        if (x == a):
            x = b
        hasil = ''.join([hasil,x])
    print(hasil)
ubahHuruf('matematika','t','s')

#alternatif dengan replace()
def ubahHuruf(teks, a, b):
    hasil = teks.replace(a,b)
    print(hasil)

ubahHuruf('MATEMATIKA', 'T', 'S')
