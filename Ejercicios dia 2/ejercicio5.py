print("DIVISOR DE NUMEROS")
dividendo = int(input("Introduce el dividendo:"))
divisor = int(input("Introduce el divisor:"))

if dividendo % divisor == 0:
    print("La division es exacta. Cociente:", dividendo//divisor)
else:
    print("La division no es exacta. Cociente:", dividendo//divisor, "Resto:", dividendo % divisor)