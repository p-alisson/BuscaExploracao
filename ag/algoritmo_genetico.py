import random, operator, numpy as np, pandas as pd

from ag.fitness import Fitness


def gera_rota(list_cidade):
    rota = random.sample(list_cidade, len(list_cidade))
    return rota

def populacao_inicial(tam_pop, list_cidade):
    populacao = []
    for i in range(0, tam_pop):
        populacao.append(gera_rota(list_cidade))
    return populacao

def rank_rotas(populacao):
    result_fitness = {}
    for i in range(0, len(populacao)):
        result_fitness[i] = Fitness(populacao[i]).rota_fitness()
    return sorted(result_fitness.items(), key=operator.itemgetter(1), reverse=True)

def selecao(pop_ranked, tam_elite):
    result_selecao = []
    df = pd.DataFrame(np.array(pop_ranked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    for i in range(0, tam_elite):
        result_selecao.append(pop_ranked[i][0])
    for i in range(0, len(pop_ranked) - tam_elite):
        pick = 100 * random.random()
        for i in range(0, len(pop_ranked)):
            if pick <= df.iat[i, 3]:
                result_selecao.append(pop_ranked[i][0])
                break
    return result_selecao

def reprodutores(populacao, result_selecao):
    reprodutores = []
    for i in range(0, len(result_selecao)):
        index = result_selecao[i]
        reprodutores = populacao[index]

    return reprodutores

def reproducao(rep1, rep2):
    filho = []
    filho_r1 = []
    filho_r2 = []

    gene_a = int(random.random()*len(rep1))
    gene_b = int(random.random()*len(rep1))

    gene_inicial = min(gene_a, gene_b)
    gene_final = max(gene_a, gene_b)

    for i in range(gene_inicial, gene_final):
        filho_r1.append(rep1[i])

    filho_r2 = [item for item in rep2 if item not in filho_r1]
    filho = filho_r1 + filho_r2

    return filho

def cria_geracao(reprodutores, tam_elite):
    filhos = []
    quantidade = len(reprodutores)-tam_elite
    pool = random.sample(reprodutores, len(reprodutores))

    for i in range(0, tam_elite):
        filhos.append(reprodutores[i])

    for i in range(0, quantidade):
        filho = reproducao(pool[i], pool[len(reprodutores)-i-1])
        filhos.append(filho)

    return filhos

def mutacao(indiviuo, taxa_mutacao):
    for trocado in range(len(indiviuo)):
        if(random.random()<taxa_mutacao):
            troca_com =int(random.random()*len(indiviuo))
            cidade1 = indiviuo[trocado]
            cidade2 = indiviuo[troca_com]

            indiviuo[trocado] = cidade2
            indiviuo[troca_com] = cidade1

    return indiviuo

def transmuta_pop(populacao, taxa_mutacao):
    pop_transmutada = []

    for i in range(0, len(populacao)):
        ind_transmutado = mutacao(populacao[i], taxa_mutacao)
        pop_transmutada.append(ind_transmutado)

    return pop_transmutada

def prox_geracao(geracao_atual, tam_elite, taxa_mutacao):
    pop_ranked = rank_rotas(geracao_atual)
    result_selecao = selecao(pop_ranked, tam_elite)
    reprodutores = reproducao(geracao_atual, result_selecao)
    filhos = cria_geracao(reprodutores, tam_elite)
    prox_geracao = transmuta_pop(filhos, taxa_mutacao)

    return prox_geracao

def algoritmo_genetico(populacao, tam_pop, tam_elite, taxa_mutacao, geracoes):
    pop = cria_geracao(tam_pop, populacao)
    print("Distancia Inicial" + str(1/rank_rotas(pop)[0][1]))

    for i in range(0, geracoes):
        pop = prox_geracao(pop, tam_elite, taxa_mutacao)

    print("Distancia Final: " + str(1 / rank_rotas(pop)[0][1]))
    ind_melhor_rota = rank_rotas(pop)[0][0]
    melhor_rota = pop[ind_melhor_rota]
    return melhor_rota