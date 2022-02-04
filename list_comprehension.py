from numpy import square


def run():
    """ squares = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2) """
    #LIST COMPRENHESION mostrando la lista de numeros del 1 al 100 que no sean múltiplos de 3
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]        
    print(squares)


if __name__ == '__main__':
    run()

