print("Conversor de segundos a horas, minutos y segundos")
segundos = int(input("Introduce los segundos:"))
horas = segundos//3600
minutos = (segundos%3600) // 60
segundos = (segundos%3600) % 60
print ("Son", horas , "horas," , minutos, "minutos, ", segundos, "segundos.")