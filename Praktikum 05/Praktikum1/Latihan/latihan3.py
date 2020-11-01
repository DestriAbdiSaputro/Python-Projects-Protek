#Indo    
indo = float(input("Masukkan nilai Bhs Indonesia  :  "))
#Ipa
ipa = float(input("Masukkan nilai IPA            :  "))
#Mat
mat = float(input("Masukkan nilai Matematika     :  "))
if (indo > 59) and (ipa > 59) and (mat > 70):
    print("Status Kelulusan              : LULUS")
else:
    print("Status Kelulusan              : TIDAK LULUS")
    print("Sebab                         :")
if (indo < 60):
    print("-  Nilai Bhs Indonesia kurang dari 60")
if (ipa < 60):
    print("-  Nilai IPA kurang dari 60")
if (mat == 70):
    print("-  Nilai Matematika tidak lebih dari 70")
elif (mat <= 70):
    print("-  Nilai Matematika kurang dari 70")
