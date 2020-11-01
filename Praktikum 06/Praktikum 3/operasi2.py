from operation import*

a = 2
b = 4
c = 6
d = 4
k= kali(b,c)
l= jumlah(a,k)
hasil= kurang(l,d)
print('a. ',a, '+' ,b, '*', c, '-', d ,'=',hasil )
a = 4
b = 7
c = 6
d = 9
k = jumlah(a,b)
l = kurang(c,d)
hasil = kali(k,l)
print('b. (',a, '+' ,b, ')*(', c, '-', d ,') =',hasil )
a = 10
b = 2
c = 7
d = 5
e = 12
f = 34
k = jumlah(a,b)
l = jumlah(c,d)
m = kurang(e,f)
n = bagi(k,l)
hasil = bagi(n,m)
print('c. (',a, '+' ,b, ')/(', c, '+', d ,') /(',e,'-',f,') =',hasil )

