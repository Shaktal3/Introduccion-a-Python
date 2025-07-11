def pinta_rectangulo(ancho, alto, caracter):
    for i in range(alto):
        for j in range(ancho):
            print(caracter, end=" ")
        print("")




ancho = int(input("Ancho del rectangulo:"))
alto = int(input("Alto del rectangulo:"))
caracter = input("Caracter:")

pinta_rectangulo(ancho, alto, caracter)

