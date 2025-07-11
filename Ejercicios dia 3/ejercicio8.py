print("SUMA DE UN RANGO")

inicio = int(input("Escribe el primer número:"))
fin = int(input("Escribe un número mayor:"))
acum=0

if(fin>inicio):
    for i in range(inicio, fin+1, 1):
        acum = acum + i
    
    print(f"La suma de los valores es {acum}")
else:
    print("El segundo número debe ser mayor que el primero.")