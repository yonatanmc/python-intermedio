def division(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]    
    return divisors
def run():

    num = input("ingresa un numero: ")
    #utilizando assert
    # condición 1: num.isnumeric() and int(num) > 0 ==> TRUE
    # caso contrario: "debes ingresar solo números positivos" ==> FALSE
    assert num.isnumeric() and int(num) > 0, "debes ingresar solo números positivos"
    print(division(int(num)))
    print("... fin del programa ...")


if __name__ == "__main__":
    run()