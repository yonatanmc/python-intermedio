# Assert statements

# Es una manera poco usual de manejar los errores en python
# Evalúa una condicional, si esta se cumple continuamos con el flujo normal del python, si no se cumple eleva un error del tipo AssertionError y nos muestra un mensaje.
# Su sintaxis es:
# assert <condicion>, <"mensaje">
# <código>

def division(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():

    num = input("ingresa un numero: ")
    assert num.isnumeric(), "debes ingresar un número"
    print(division(int(num)))
    print("... fin del programa ...")


if __name__ == "__main__":
    run()
