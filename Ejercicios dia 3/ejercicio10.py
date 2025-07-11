num = int(input("Cuantos valores vas a introducir:"))

acum=0
menor=float('inf')
mayor=float('-inf')


for i in range(1, num+1, 1):
    val = float(input(f"Escribe el numero {i}: 5"))
    acum = acum + val
    if val<menor:
        menor = val
    if val>mayor:
        mayor = val

print(f"El menor es: {menor}")
print(f"El mayor es: {mayor}")
print(f"La media es: {acum/num}")

    
