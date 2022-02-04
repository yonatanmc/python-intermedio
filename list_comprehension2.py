def run():
    """ list_multi = []

    for i in range(1, 100001):
        if i % 4 == 0 and i % 6 == 0 and i % 9 == 0:
            list_multi.append(i) """

    #LIST COMPRENHESION donde muestra la lista de numeros múltiplos de 4, 6 y 9 del 1 hasta 100000
    list_multi = [i  for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(list_multi)

if __name__ == '__main__':
    run()