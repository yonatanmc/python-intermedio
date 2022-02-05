# Modos de Apertura de archivos

# r -> Solo lectura
# r+ -> Lectura y escritura
# w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# a -> Añadido (agregar contenido). Crea el archivo si éste no existe
# a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

# with :manejador contextual, controla el flujo del archivo

# open("ruta del archivo","modo de apertura")

# as : asigna un nombre hipotetico para trabajar dentro del algoritmo "nombre alias"

# with open("","") as miarchivo:


def read():
    numeros = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as miarchivo:
        for linea in miarchivo:
            numeros.append(int(linea))
        print(numeros)


def write():
    nombres = ["Coqui", "Yonatan", "Yomaco", "Jesús"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as miarchivo:
        for nombre in nombres:
            miarchivo.write(nombre)
            miarchivo.write("\n")

def run():
    read()
    write()

if __name__ == '__main__':
    run()