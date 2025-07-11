password = input("Introduce una contraseña: ")
intentos=0
repetido=''

while intentos < 3 and repetido!=password:
    repetido = input("Repite la contraseña: ")
    intentos+=1