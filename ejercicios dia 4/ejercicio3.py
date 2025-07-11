def calcula_Total(cantidad, IVA = 21):
    total = cantidad + cantidad * IVA/100
    return total


print(calcula_Total(1350))


print(calcula_Total(1350, 13))