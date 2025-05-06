import random

def rolar_dados(quantidade):
    resultado = []
    for i in range(quantidade):
        resultado.append(random.randint(1, 6))
    return resultado


def guardar_dado(lista_rolados, lista_estoque, indice_dado):
    dado_escolhido = lista_rolados.pop(indice_dado)
    lista_estoque.append(dado_escolhido)
    return [lista_rolados, lista_estoque]


def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado_removido = dados_no_estoque.pop(dado_para_remover)
    dados_rolados.append(dado_removido)
    final = [dados_rolados, dados_no_estoque]
    return final

def calcula_pontos_regra_simples(dados):
    pontos = {i: 0 for i in range(1, 7)}
    for dado in dados:
        if 1 <= dado <= 6:
            pontos[dado] += dado
    return pontos


def calcula_pontos_soma(dados):
    return sum(dados)



