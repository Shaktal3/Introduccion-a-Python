fichero= open('test.txt', 'r')

lineas = fichero.readlines()

for i in lineas:
    print(f"{lineas.index(i)+1} {i.replace("\n", "")} {len(i)}")


fichero.close()