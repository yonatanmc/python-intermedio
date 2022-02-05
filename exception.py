# TRY: En el try se coloca código que esperamos que pueda lanzar algún error.
# EXCEPT: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.
# ELSE: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try
# FINALLY: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.


def division(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("ingresa un numero: "))
        print(division(num))
        print("... fin del programa ...")
    except ValueError: # 2: Exception [KeyboardInterrupt, KeyError, IndexError, FileNotFoundError, ZeroDivisionError, ImportError, ...]
        print("debe ingresar un número")

if __name__ == "__main__":
    run()