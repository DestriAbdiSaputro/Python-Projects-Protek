def sum(*myData):
    # init values
    sum = 0
    i = 0
    # menjumlahkan semua data dalam myData
    for data in myData:
        sum += data
        i +=1
    # hitung jumlah
    jumlah = sum
    print('Jumlah: ',jumlah)
def average(*myData):
    # init values
    sum = 0
    i = 0
    # menjumlahkan semua data dalam myData
    for data in myData:
        sum += data
        i +=1
    # hitung rata-rata
    average = sum/i
    print('Rata-rata: ',average)
def maks(*mydata):
    # init values
    maksimal = 0
    # data terbesar dalam myData
    for data in mydata:
        if data > maksimal:
            maksimal = data
    maks = maksimal
    print('Nilai Maksimum: ',maksimal)
def min(*myData):
    # init values
    minimum = 100
    # data terbesar dalam myData
    for data in myData:
        if data < minimum:
            minimum = data
    min = minimum
    print('Nilai Minimum: ',minimum)
