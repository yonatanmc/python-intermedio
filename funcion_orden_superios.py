
#función de orden superior
def operacion(x, mifuncion): #función principal
    return mifuncion(x)

def raiz(x):
    return x**0.5

def cuadrado(x):
    return x**2

if __name__ == '__main__':
    resultado = operacion(4, raiz)
    print(resultado)