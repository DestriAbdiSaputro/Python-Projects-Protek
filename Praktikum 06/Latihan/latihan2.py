def starFormation1(n):
    for n in range (n):
        for j in range (n+1):
            print('*',end='')
        print()
def starFormation2(n):
    for n in reversed(range (n)):
        for j in range (n+1):
            print('*',end='')
        print()
def starFormation3(n):
    if n%2==0:
        starFormation1(n//2)
    else:
        starFormation1(n//2+1)
    starFormation2(n//2)
starFormation3(7)
