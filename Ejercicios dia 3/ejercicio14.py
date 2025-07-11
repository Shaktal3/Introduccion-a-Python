import random
print ("Simulacion de tiradas de dados")


num=(int(input("Cuantos dados quieres tirar? ")))
caras=(int(input("Cuantas caras tienen esos dados? ")))
tirada=[]
for i in range (0, num, 1):
    tirada.append(random.randrange(1,caras+1))

print(*tirada)
