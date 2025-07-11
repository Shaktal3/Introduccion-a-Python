import csv

fichero = open("chocolate.csv",'r')

contenido = csv.reader(fichero, delimiter=',')
anterior=""
for linea in contenido:
    if linea[0]!=anterior:
        print(linea[0])
    anterior=linea[0]


fichero.close()