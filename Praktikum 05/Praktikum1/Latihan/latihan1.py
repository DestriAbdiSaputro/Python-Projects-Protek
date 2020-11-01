#Indo    
indo = float(input("Masukkan nilai Bhs Indonesia  :  "))
#Ipa
ipa = float(input("Masukkan nilai IPA            :  "))
#Mat
mat = float(input("Masukkan nilai Matematika     :  "))
if (indo > 59) and (ipa > 59):
    if (mat > 70):
        print("Status Kelulusan              : LULUS")
    else:
        print("Status Kelulusan              : TIDAK LULUS")
else:
    print("Status Kelulusan              : TIDAK LULUS")
