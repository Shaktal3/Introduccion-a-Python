import csv

fichero = open("chocolate.csv",'r')

contenido = csv.DictReader(fichero, delimiter=',')
anterior=""
for linea in contenido:
    if linea["Rating"]=="Rating" or float(linea["Rating"])>=3.5:
        print(linea["Company"] ,"   ", linea["Rating"], "   ", linea["Country of Origin"])


fichero.close()