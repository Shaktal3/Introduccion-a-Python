def subrutina():
    
    print (a)
    nonlocal a
    a = 32
    return


a=31
subrutina()
print(a)