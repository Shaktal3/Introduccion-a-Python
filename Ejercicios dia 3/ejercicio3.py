print("MAYORES QUE EL ANTERIOR")

num = int(input("Cuantos valores vas a introducir?"))

if(num <=0):
    print("Imposible!")
else:
    primero = int(input("Escribe un número:"))

    for i in range(0, num-1, 1):
        nuevo = int(input(f"Escribe un número mayor que {primero}:"))
        if nuevo <= primero:
            print(f"{nuevo} no es mayor que {primero}!")
        primero = nuevo
    print("fin.")
