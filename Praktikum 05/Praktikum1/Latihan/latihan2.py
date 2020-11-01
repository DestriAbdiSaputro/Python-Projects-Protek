#Indo    
indo = float(input("Masukkan nilai Bhs Indonesia  :  "))
#Ipa
ipa = float(input("Masukkan nilai IPA            :  "))
#Mat
mat = float(input("Masukkan nilai Matematika     :  "))
if (indo > 100) or (ipa > 100) or (mat > 100):
    print("Maaf input ada yang tidak valid")
elif (indo >= 60) and (ipa >= 60) and (mat > 70):
    print("Status Kelulusan              : LULUS")
elif (indo < 1) or (ipa < 1) or (mat < 1):
    print("Maaf input ada yang tidak valid")
else:
    print("Status Kelulusan              : TIDAK LULUS")
