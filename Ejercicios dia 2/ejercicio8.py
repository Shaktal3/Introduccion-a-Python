print("COMPARADOR DE NUMEROS")
actual = int(input("En qué año estamos?"))
otro = int(input("Introduce un año cualquiera:"))

if actual > otro:
    print("Desde el año", otro, "han pasado", actual-otro, "años.")
elif otro > actual:
    print("Para llegar al año", otro, "faltan", otro-actual, "años.")
else:
    print("Es el mismo año.")