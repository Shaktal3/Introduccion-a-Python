print("COMPARADOR DE NUMEROS")
num1 = int(input("Introduce un número:"))
num2 = int(input("Introduce otro número:"))

if num1 > num2:
    print("Menor:", num2, "Mayor:", num1 )
elif num2 > num1:
    print("Menor:", num1, "Mayor:", num2 )
else:
    print("Son iguales.")