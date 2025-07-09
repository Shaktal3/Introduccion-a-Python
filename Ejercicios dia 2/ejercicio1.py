print ("PAR E IMPAR")
num1 = int(input("Introduce un número par:"))
num2 = int(input("Introduce un número impar:"))
if num1%2 == 0 and num2%2 == 1:
    print("Ambos números son correctos.")
else:
    print("Uno o más de los números no son correctos.\nEjecute de nuevo el programa para volver a intentarlo.")