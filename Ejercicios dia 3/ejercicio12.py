import random

print("MULTIPLICAR ALEATORIOS")


a= random.randrange(2,11)
b= random.randrange(2,11)

respuesta = int(input(f"Cuanto es {a} * {b}?  "))
if respuesta == a*b:
    print("Correcto!")
else:
    print("Incorrecto!")