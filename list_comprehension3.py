def run():
    """ my_dict = {}
    for i in range(1, 101):
        my_dict[i] = i**3 """
    
    #my_dict = {i: i**3 for i in range(1, 101)}
    lista = [1, 2, 3, 4, 5]
    my_dict = [i**2 for i in lista]

    print(my_dict)

if __name__ == '__main__':
    run()
    