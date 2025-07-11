print("FACTORIAL")

num = int(input("Escribe un número entero: "))

if(num>0):
    acum=num
    for i in range(num-1, 0, -1):
        acum = acum * i
else:
    acum=1

print(f"El factorial es {acum}")