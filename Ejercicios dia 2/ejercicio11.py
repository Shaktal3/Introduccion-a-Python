print("Bisiestos")
anho = int(input("Introduce un año:"))

if anho%4==0:
    if anho%100==0: 
        if anho%400==0:
            print("Es bisiesto")
        else:
            print("No es bisiesto.")
    else:
        print("Es bisiesto.")
else:
    print("No es bisiesto")