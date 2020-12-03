print(' '*20,'Langkah Kerja Nomor 1 s/d 8')
print('='*75)
a = ['1','5','6','3','6','9','11','20','12']
b = ['7','4','5','6','7','1','12','5','9']
a[0:8]
print(a[:2]+ ['3']+ a[2:])
print(b[:1]+ ['15']+ b[1:])
print('='*75)
print(a[:9]+ ['4'])
print(b[:9]+ ['8'])
print('='*75)
a = [ 1 , 5 , 6 , 3 , 6 , 9 , 11 , 20 , 12 ]
b = [ 7 , 4 , 5 , 6 , 7 , 1 , 12 , 5 , 9 ]
a.sort()
b.sort()
print(a)
print(b)
print('='*75)
a = ['1','5','6','3','6','9','11','20','12']
b = ['7','4','5','6','7','1','12','5','9']
c = a[0:7]
d = b[2:9]
print(c)
print(d)
print('='*75)
c = [ 1 , 5 , 6 , 3 , 6 , 9 , 11 ]
d = [ 5 , 6 , 7 , 1 , 12 , 5 , 9 ]
e=[]
for i in range(len(d)):
    e += [c[i]+d[i]]
print('e =',e)
print('='*75)
e=tuple(e)
print('List e dalam tuple =', e)
print('='*75)
e = (6, 8, 10, 12, 13, 14, 18, 22)
print('Nilai Minimal Elemen E:', min(e))
print('Nilai Maksimal Elemen E:', max(e))
print('Jumlah Seluruh Elemen E:', sum(e))
