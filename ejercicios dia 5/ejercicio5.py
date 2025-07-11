fichero= open('test.txt', 'r')

lineas = fichero.readlines()

for i in lineas:
    print(i)


fichero.close()