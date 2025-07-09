print ("PAR E IMPAR")
num1 = int(input("Introduce un número par:"))

if num1%2 != 0:
    print("No es un número par.\nEjecute de nuevo el programa para volver a intentarlo.")
else:
    num2 = int(input("Introduce un número impar:"))
    if num2%2 == 0:
        print("No es un número impar.\nEjecute de nuevo el programa para volver a intentarlo.")
    else:
        print("Los valores son correctos.")