import csv

fichero = open("chocolate.csv",'r')

contenido = csv.reader(fichero, delimiter=',')

for linea in contenido: 
    print(linea)


fichero.close()