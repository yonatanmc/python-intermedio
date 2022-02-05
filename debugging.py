# ERRORES
# tipos
# 1: SyntaxError
# 2: Exception [KeyboardInterrupt, KeyError, IndexError, FileNotFoundError, ZeroDivisionError, ImportError, ...]

#utiliza este algoritmo para practicar Debugging with Python
#La primera forma de ver errores es utilizar RUN AND DEBUG con visual studio code y verificar linea por linea que ocurre
#DEBUGGING

def division(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = int(input("ingresa un numero: "))
    print(division(num))
    print("... fin del programa ...")

if __name__ == "__main__":
    run()