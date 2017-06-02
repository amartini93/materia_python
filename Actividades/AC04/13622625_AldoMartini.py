# coding=utf-8


# Completen los métodos
# Les estamos dando un empujoncito con la lectura del input
# Al usar la clausula: "with open('sonda.txt', 'r') as f", el archivo se cierra automáticamente al salir de la función.


def sonda():
    list_minerals = []
    dict_minerals = {}
    with open('sonda.txt', 'r') as f:
        for line in f:
            list_minerals.append(line.replace('\n', '').split(','))
        key = ''
        for i in list_minerals[:][]:
            if i != '[' and i != ']':
                key += str(i)
                key += ','
        print(key)
    # for mineral in list_minerals:
    #     dict_minerals[mineral[0:-1]] = mineral[-1]
    # print(dict_minerals)
    # n_questions = int(input('Cuantas veces consultara coordenadas?'))
    # for question in range(n_questions):
    #     coordenates = input('Ingrese las coordenadas separadas por comas: ')
    #     coordenates = coordenates.split(',')
    #     for key, value in dict_minerals.items():
    #         print(key, value, coordenates)
    #         if key == coordenates:
    #             print(value)
                ## no me esta funcionando porque reemplazo el value, etnoces pierdo algunos minerales, pero aveces coincide y corre.
                ## voy a seguir con lo otro

def traidores():
    with open('bufalos.txt', 'r') as f:
        b_list = set()
        for line in f:
            line = line.replace('\n', '')
            b_list.add(line)

    with open('rivales.txt', 'r') as f:
         t_list = set()
         for line in f:
            line = line.replace('\n', '')
            t_list.add(line)
    print(t_list.intersection(b_list), 'Son unos traidores, asesinenlos!!')


def pizzas():
    with open('pizza.txt', 'r') as f:
        for line in f.read().splitlines():
            pass


if __name__ == '__main__':
    exit_loop = False

    functions = {"1": sonda, "2": traidores, "3": pizzas}

    while not exit_loop:
        print(""" Elegir problema:
            1. Sonda
            2. Traidores
            3. Pizzas
            Cualquier otra cosa para salir
            Respuesta: """)

        user_entry = input()

        if user_entry in functions:
            functions[user_entry]()
        else:
            exit_loop = True
