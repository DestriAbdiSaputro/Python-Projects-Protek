def dataStat(x) :
    a = sum(x) / len(x)
    b = max(x)
    c = min(x)
    return [a,b,c]

while True :
    try :
        n = int(input('Berapa data yang akan input ? : '))
        break
    except ValueError :
        print('Input tidak valid')
        continue
data = []
i = 0
while (i < n) :
    try :
        bil = int(input('Masukkan bil bulat ke-{0} : '.format(i+1)))
        data.append(bil)
        i += 1
    except ValueError :
        print('Input tidak valid')

printData = dataStat(data)        
print(printData)

