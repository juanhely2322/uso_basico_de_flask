
def  revisar(func):
    def error(a,b):
        if b==0:
            print("no se puede dividir por 0")
            return
        else:
            return func(a,b)
        
        func(a,b)
    return error

@revisar
def divicion(a,b):
    return a/b

print(divicion(10,0))