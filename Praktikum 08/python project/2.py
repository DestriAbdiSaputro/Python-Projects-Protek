def dataStat(x):
    if(isinstance(x, list)):
        tupleX  = tuple(x)
        a  = sum(tupleX) / len(tupleX)
        b  = max(tupleX) 
        c  = min(tupleX)
        return [a, b, c]
    else:
        print('Data tidak valid')
        return False

def DataInput():
    try:
        count = int(input('Berapa data yang akan diinput? '))
        loop = 0
        data = []
        while loop < count:
            number = int(input('Masukkan bil bulat ke-{0} : '.format(loop+1)))
            data.append(number)
            loop += 1

        return data
    except ValueError:
        print('data yang anda masukan bukan angka / salah')
        return False

DataList = DataInput()
print('='*10,'Hasil','='*10)
if(DataList):
    result   = dataStat(DataList)
    print('Rata-rata  {0}        : {1}'.format(DataList,result[0]))
    print('Nilai tertinggi {0}  : {1}'.format(DataList,result[1]))
    print('Nilai terendah {0}   : {1}'.format(DataList,result[2]))
