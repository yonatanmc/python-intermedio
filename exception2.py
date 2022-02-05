# utiliza palabras claves try, except y raise para evelar un error si el usuario ingresa un numero negativo
# en nuestr programa de divisores (el programa solo debe aceptar numero positivo)

def divisores(num):
    divisores = []
    try:
        if num < 0:
            raise ValueError("No puede ingresar un  número negativo")
        else:
            divisores = [i for i in range(1, num + 1) if num % i == 0]            
        return divisores
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        num = int(input("ingrese un número: "))
        print(divisores(num))
    except ValueError:
        print("ingrese número positivo")


if __name__ == '__main__':
    
    run()