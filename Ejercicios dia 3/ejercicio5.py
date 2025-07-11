print("CUANTOS PARES E IMPARES?")

num = int(input("Cuantos valores vas a introducir?"))

if(num <=0):
    print("Imposible!")
else:
    pares=0
    impares=0
    for i in range(0, num, 1):
        valor= int(input(f"Escriba el número {i+1}:"))
        if valor%2==0:
            pares+=1
        else:
            impares+=1
    print(f"Ha escrito {pares} números pares y {impares} números impares.")
    print("fin.")
