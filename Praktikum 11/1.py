import datetime

def diffDate(x): 
    now = datetime.datetime.now()
    dict = x.split('-')
    skrg = datetime.datetime(now.year, now.month, now.day) 
    x = datetime.datetime(int(dict[0]), int(dict[1]), int(dict[2])) 
    selisih = skrg-x  
    if selisih.days < 0:
        selisih = selisih * -1
    return selisih.days

x = '2020-12-26'
print('Selisih tanggal',x,'dengan tanggal hari ini adalah ',diffDate(x))
