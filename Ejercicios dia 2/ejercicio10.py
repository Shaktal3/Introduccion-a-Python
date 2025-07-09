print("COMPARADOR DE 3 NUMEROS")
num1 = int(input("Introduce un número:"))
num2 = int(input("Introduce otro número:"))
num3 = int(input("Introduce otro número más:"))

if num1==num2==num3:
    print ("Los 3 números son iguales")
elif num1==num2 or num2==num3 or num1==num3:
    print ("Ha escrito 2 numeros iguales.")
else:
    print("Todos los numeros son distintos.")

        