DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Tuinsti',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Hector',
        'age': 19,
        'organization': 'Tuinsti',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Tuinsti',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Tuinsti',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
    {
        'name': 'Yonatan',
        'age': 31,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
    {
        'name': 'Kevin',
        'age': 28,
        'organization': 'Python Organization',
        'position': 'Language Master',
        'language': 'python',
    },
]


def run():
    #list with omprenhesion
    #recupera los nombres de trabajadores que utilizan lenguaje Python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    #recupera lista nombres de trabajadores que son de la organizaci??n Tuinsti
    all_jobtuinsti = [jobs["name"] for jobs in DATA if jobs["organization"] == "Tuinsti"]

    for worker in all_python_devs:
        print(worker)
    for jobs in all_jobtuinsti:
        print(jobs)

def runfiltro():
    
    #UTILIZANDO "FILTER" y "MAP"
    #recupera los nombres de trabajadores que utilizan lenguaje Python
    trabajador_languaje = list(filter(lambda personas: personas["language"] == "python", DATA))
    trabajador_languaje = list(map(lambda personas: personas["name"], trabajador_languaje)) 

    for i in trabajador_languaje:
        print(i)
    print(*trabajador_languaje)    
    print(trabajador_languaje)

# using filter: funci??n de orden superios
def filtro():
    adultos = list(filter(lambda persona: persona["age"] > 18, DATA))
    adultos = list(map(lambda persona: persona["name"], adultos))
    #print(adultos)
    
    edad_persona = list(map(lambda persona: persona | {"old": persona["age"]>70}, DATA))

    for personas in edad_persona:
        print(personas)

def comprehension2():
    adults = [worker ['name'] for worker in DATA if worker ['age'] > 18]
    old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    old_people_lc = [worker| {"old":worker["age"]>70} for worker in DATA] #python 3.9
    print(old_people_lc)


if __name__ == '__main__':
    #run()
    #filtro()
    #runfiltro()
    comprehension2()

# Filter: Recorre toda la lista para devolver uno varios elementos de esta. sirve para filtrar (devolver) elementos espec??ficos en una lista.

# Map: Recorre toda la lista, la modifica y devuelve la misma lista, pero modificada. Sirve parar realizar una operaci??n a todos los elementos de la lista uno a uno y devolver la lista con sus valores modificados.

# Reduce: no devuelve una lista, devuelve un valor haciendo una operaci??n con todos los elementos. Sirve para hacer acumulaciones de los elementos de una lista.