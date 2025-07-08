print("Conversor de horas, minutos y segundos a segundos")
horas = int(input("Introduce las horas:"))
minutos = int(input("Introduce los minutos:"))
segundos = int(input("Introduce los segundos:"))

resultado = horas*60*60 + minutos*60 + segundos
print ("Son", resultado , "segundos.")