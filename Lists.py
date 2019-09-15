def chop(list):
    ultimo = len(list) - 1
    contador = 0
    for word in list:
        if contador == 0 or contador == ultimo:
            list[contador] = None
        contador += 1
    return list

def chop2(list):
    ultimo = len(list) - 1
    contador = 0
    for word in list:
        if contador == 0 or contador == ultimo:
            list[contador] = ''
        contador += 1
    return list


lista = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4, 5, 6, 7]


lista3 = chop(lista)
lista4 = chop2(lista2)
print(lista3)