import random
acierto = True

while acierto:
    a= random.randrange(2,11)
    b= random.randrange(2,11)

    respuesta = float(input(f"Cuanto es {a} * {b}?  "))
    if respuesta == a*b:
        acierto=True
    else:
        acierto=False