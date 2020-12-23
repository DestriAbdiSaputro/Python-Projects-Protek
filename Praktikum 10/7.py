myfile   = input    ('File Teks Hasil Penyandian : ')
file     = open(myfile, 'r')
n        = int(input('Keyword                    : '))
filebaru = open('7.txt', 'w+')
split    = (file.read()).split('|')
text     = str(split[0])
hasil    = ''

for i in text:
    if i.isupper():
        awal   = ord(i) - ord('A')
        akhir  = (awal - n) % ((ord('Z'))-(ord('@')))
        hasill = akhir + ord('A')
        hasil  = hasil + chr(hasill)
    elif i.islower():
        awal   = ord(i) - ord('a')
        akhir  = (awal - n) % ((ord('z'))-(ord('`')))
        hasill = akhir + ord('a')
        hasil  = hasil + chr(hasill)
    else:
        hasil += i

filebaru.write(hasil)
filebaru.close()
