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
    total = 0
    for valor in dados:
        total += valor
    return total


def calcula_pontos_sequencia_baixa(lista):
    v = []
    for x in lista:
        if x not in v:
            v.append(x)
    v = sorted(v)
    if len(v) < 4:
        return 0
    for i in range(len(v) - 3):
        if v[i] == v[i+1] - 1 and v[i+1] == v[i+2] - 1 and v[i+2] == v[i+3] - 1:
            return 15

    return 0


def calcula_pontos_sequencia_alta(lista):
    v = []
    for x in lista:
        if x not in v:
            v.append(x)
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if v[i] > v[j]:
                temp = v[i]
                v[i] = v[j]
                v[j] = temp
    if len(v) < 5:
        return 0
    for i in range(len(v) - 4):
        if v[i] == v[i+1] - 1 and v[i+1] == v[i+2] - 1 and v[i+2] == v[i+3] - 1 and v[i+3] == v[i+4] - 1:
            return 30

    return 0

def calcula_pontos_full_house(lista):
    valores = []
    contagens = []

    for x in lista:
        if x not in valores:
            valores.append(x)
            contagens.append(1)
        else:
            for i in range(len(valores)):
                if valores[i] == x:
                    contagens[i] += 1

    if len(contagens) == 2:
        if (contagens[0] == 3 and contagens[1] == 2) or (contagens[0] == 2 and contagens[1] == 3):
            soma = 0
            for x in lista:
                soma += x
            return soma

    return 0

def calcula_pontos_quadra(lista):
    for x in lista:
        contador = 0
        for y in lista:
            if x == y:
                contador += 1
        if contador >= 4:
            soma = 0
            for z in lista:
                soma += z
            return soma
    return 0

def calcula_pontos_quina(lista):
    for x in lista:
        contador = 0

        for y in lista:
            if x == y:  
                contador = contador + 1

        if contador >= 5:  
            return 50

    return 0

def calcula_pontos_regra_avancada(lista):
    return {
        'cinco_iguais': calcula_pontos_quina(lista),
        'full_house': calcula_pontos_full_house(lista),
        'quadra': calcula_pontos_quadra(lista),
        'sem_combinacao': calcula_pontos_soma(lista),
        'sequencia_alta': calcula_pontos_sequencia_alta(lista),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(lista)
    }

def faz_jogada(dados, categoria, cartela_de_pontos):
    categorias_simples = [1, 2, 3, 4, 5, 6]

    if categoria in ['1', '2', '3', '4', '5', '6']:
        pontos = calcula_pontos_regra_simples(dados)
        for i in categorias_simples:
            if str(i) == categoria:
                cartela_de_pontos['regra_simples'][i] = pontos[i]

    elif categoria in cartela_de_pontos['regra_avancada']:
        pontos = calcula_pontos_regra_avancada(dados)
        cartela_de_pontos['regra_avancada'][categoria] = pontos[categoria]

    return cartela_de_pontos
