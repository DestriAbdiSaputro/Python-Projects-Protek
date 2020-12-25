file  = open('2.txt', 'r')
data  = file.readlines()
hasil = []
for i in data:
    pisah = i.split('|')
    dict  = {'nim' : pisah[0], 'nama' : pisah[1], 'alamat' : pisah[2]}
    hasil += [dict]
print('dataMhs = ',hasil)
