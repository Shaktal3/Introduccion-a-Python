print("COMPARADOR DE NUMEROS")
actual = int(input("En qué año estamos?"))
otro = int(input("Introduce un año cualquiera:"))

if actual > otro:
    if actual-otro>1:
        print("Desde el año", otro, "han pasado", actual-otro, "años.")
    else:
        print("Desde el año", otro, "ha pasado", actual-otro, "año.")
elif otro > actual:
    if otro-actual>1:
        print("Para llegar al año", otro, "faltan", otro-actual, "años.")
    else:
        print("Para llegar al año", otro, "falta", otro-actual, "año.")
else:
    print("Es el mismo año.")