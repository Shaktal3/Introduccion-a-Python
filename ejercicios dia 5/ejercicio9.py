import csv

fichero = open("chocolate.csv",'r')

contenido = csv.reader(fichero, delimiter=',')
anterior=""
for linea in contenido:
    if linea[6]=="Rating" or float(linea[6])>=3.5:
        print(linea)


fichero.close()