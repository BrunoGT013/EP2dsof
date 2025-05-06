import random

def rolar_dados(quantidade):
    resultado = []
    for i in range(quantidade):
        resultado.append(random.randint(1, 6))
    return resultado


def guardar_dado(lista_rolados, lista_estoque, indice_dado):
    dado_escolhido = lista_rolados[indice_dado]
    lista_estoque.append(dado_escolhido)
    return [lista_rolados, lista_estoque]
