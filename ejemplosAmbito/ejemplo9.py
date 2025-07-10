def subrutina():
    def sub_subrutina():
        a=3
        print(a)
        a=5
        return
    
    global a
    a=3
    sub_subrutina()
    print(a)
    return


a = 4
subrutina()
print(a)