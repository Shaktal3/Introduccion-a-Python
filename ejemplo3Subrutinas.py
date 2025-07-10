def subrutina():
    def sub_subrutina():
        def sub_sub_subrutina():
            #sub_sub_subrutina
            nonlocal a
            a = 5
            print(a)
            return
        #sub_subrutina
        a = 5
        sub_sub_subrutina()
        print(a)
        return
    #subrutina
    a=4
    sub_subrutina()
    print(a)
    return

#principal
a = 3
subrutina()
print(a)