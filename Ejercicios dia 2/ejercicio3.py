print ("PAR E IMPAR")
num1 = int(input("Introduce un número par:"))
num2 = int(input("Introduce un número impar:"))
errores = 0
if num1%2 != 0:
    print("No es un número par.")
    errores+=1
if num2%2 == 0:
    print("No es un número impar.")
    errores+=1

if errores == 0:
    print("Ambos valores son correctos.")
else:
    print("Ejecute de nuevo el programa para volver a intentarlo.")


