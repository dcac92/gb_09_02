secin = input("Введите количество секунд")
secin = int(secin)

sec = secin % 60
min = secin // 60 % 60
hours = (secin // 60) // 60 % 24
days = (secin // 60) // 60 // 24

print("sec = ", sec,"\nmin = ", min, "\nhours = ",hours,
      "\n days = ",days)