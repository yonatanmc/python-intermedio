#funcion clasica
def suma(a, b):
    return a + b

#funcion lambda
funcion_lambda = lambda a, b: a + b

#función lambda 2 f(x, a, b, c) = a*x^2 + b*x + c
# indentificador   argumentos:   expresión
poly = lambda x, a, b, c: a*x**2 + b*x + c

##recibir temperatura F° y retorne valor C°

if __name__ == '__main__':
    print("funcion clasica ",suma(2,2))
    print("funcion lambda ", funcion_lambda(2, 4))
    print("funcion lambda poly ", poly(5, 1, 2, 1))