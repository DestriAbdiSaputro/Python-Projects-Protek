import datetime

def diffDate(x): 
    now = datetime.datetime.now()
    nx = x.split('-')
    skrg = datetime.datetime(now.year, now.month, now.day) 
    x = datetime.datetime(int(nx[0]), int(nx[1]), int(nx[2])) 
    selisih = skrg-x  
    if selisih.days < 0:
        selisih = selisih * -1
    return selisih.days

x = '2020-12-26'
print(diffDate(x))
