file = open("d:/data.txt", "r")
sum = 0
try:
    for data in file:
        sum = sum +int(data)
    print(sum)
except ValueError:
    print('Input data tidak valid')
