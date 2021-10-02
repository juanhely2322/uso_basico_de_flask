
def revisar(operacion,a,b):
        if b==0:
            print("no se puede dividir por 0")
            return
        else:
            return operacion(a,b)
        

def divicion(a,b):
    return a/b

aux=divicion

print(revisar(aux,10,2))



