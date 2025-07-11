import random

print("MULTIPLICAR ALEATORIOS")

num = int(input(f"Cuantas multiplicaciones quieres resolver? "))
correctas = 0
incorrectas=0

for i in range(0, num, 1):

    a= random.randrange(2,11)
    b= random.randrange(2,11)

    respuesta = int(input(f"Cuanto es {a} * {b}?  "))
    if respuesta == a*b:
        print("Correcto!")
        correctas+=1
    else:
        print("Incorrecto!")
        incorrectas+=1

print(f"Has acertado {correctas} veces!")
print(f"Tu nota es un {correctas*10/num}!")
