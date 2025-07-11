print("NUMERO PRIMO")
num = int(input("Escribe un numero mayor que 1:"))
if num<=1:
    print("No es un número mayor que 1")
else:
    divisores=0
    for i in range(2, num//2+1, 1):
        if num%i==0:
           divisores+=1
           
    if divisores>0:
        print(f"{num} no es primo")
    else:
        print(f"{num} es primo")