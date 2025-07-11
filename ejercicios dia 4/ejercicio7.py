def es_vocal(caracter : str)->bool:
    lower_caracter = caracter.lower()
    if(lower_caracter in 'aeiou'):
        return True
    else:
        return False
    

vocal = input("introduce una vocal:")
print(es_vocal(vocal))