print("SUMA DE UN RANGO Y OPERACIÓN")

inicio = int(input("Escribe el primer número:"))
fin = int(input("Escribe un número mayor:"))
acum=0
lista=[]

if(fin>inicio):
    for i in range(inicio, fin+1, 1):
        acum = acum + i
        lista.append(i)
    print(f"La suma de los valores es {acum}")

    for i in lista:
        if(lista.index(i)+1 == len(lista)):
            print(i, end=" = ")
        else:
            print(i, end=" + ")
    print (acum)
else:
    print("El segundo número debe ser mayor que el primero.")