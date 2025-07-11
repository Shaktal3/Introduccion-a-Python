print("SUMA DE VALORES")

num = int(input("Cúantos valores va a introducir?"))
acum = 0
for i in range(1, num+1, 1):
    valor = float(input(f"Escriba el número {i}:"))
    acum = acum + valor

print(f"La suma de los valores es {acum}")