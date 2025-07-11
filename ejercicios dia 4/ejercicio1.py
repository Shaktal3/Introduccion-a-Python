def pinta_rectangulo(ancho: int, alto: int):
    for i in range(alto):
        for j in range(ancho):
            print("*", end=" ")
        print("")




ancho = int(input("Ancho del rectangulo:"))
alto = int(input("Alto del rectangulo:"))

pinta_rectangulo(ancho, alto)


