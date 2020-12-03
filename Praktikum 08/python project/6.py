print('----------------------------------')
print('               Buah              ')
print('----------------------------------')
#data buah
def sortStringByChar(data):
    data.sort(key = len,reverse=True)
    print(data)
    
myData = ['apel', 'rambutan', 'jeruk']
sortStringByChar(myData)
