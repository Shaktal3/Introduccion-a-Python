print("circulo o triangulo")

opcion = input("Qué área quieres calcular? \na)Triángulo \nb)Círculo\n")
if opcion =='a':
    base = int(input("Introduce la base:"))
    altura = int(input("Introduce la altura:"))
    print("El área del triángulo es:", base*altura/2)
elif opcion =='b':
    radio = int(input("Introduce el radio:"))
    print("El área del círculo es:", 3.14 * radio * radio)
else:
    print("esa opcion no es valida")