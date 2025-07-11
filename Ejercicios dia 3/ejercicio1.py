print("Divisores")
num = int(input("Escribe un numero mayor que 0:"))
if num<=0:
    print("No es un número mayor que 0")
else:
    divisores = []
    for i in range(1, num//2+1, 1):
        if num%i==0:
            divisores.append(i)
    divisores.append(num)
    print("Los divisores de", num, "son", divisores)