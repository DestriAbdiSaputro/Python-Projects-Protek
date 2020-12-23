myfile   = input('Masukkan Nama File : ')
file     = open (myfile, 'r')
filebaru = input('File Output(.txt)  : ')
output= open(filebaru, 'w+')
for i in file:
    list = i.split('|')
    hasil = int(list[0]) + int(list[1])
    output.write(str(hasil))
    output.write('\n')
    
output.close()
