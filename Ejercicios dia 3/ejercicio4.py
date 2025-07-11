print("CUANTOS NEGATIVOS?")

num = int(input("Cuantos valores vas a introducir?"))

if(num <=0):
    print("Imposible!")
else:
    contador=0
    for i in range(0, num, 1):
        valor= int(input(f"Escriba el número {i+1}:"))
        if valor<0:
            contador+=1
    print(f"Ha escrito {contador} números negativos.")
    print("fin.")
